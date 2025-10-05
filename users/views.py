import csv
import io

from django.db import IntegrityError
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CSVUploadResponseSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(user_type=CustomUser.UserType.USER)

    @action(detail=False, methods=["post"], url_path="upload-csv")
    def upload_csv(self, request):
        """
        Upload a CSV file containing users.
        Expected columns: name,email,age

        Note:
        For large CSV files or bulk uploads, this task can be offloaded to a
        background worker using Celery to prevent blocking the request-response cycle
        and improve performance.
        """
        file = request.FILES.get("file")
        if not file:
            return Response(
                {"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST
            )

        if not file.name.lower().endswith(".csv"):
            return Response(
                {"error": "Only CSV files are allowed."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        decoded_file = file.read().decode("utf-8")
        reader = csv.DictReader(io.StringIO(decoded_file))

        saved_count, rejected_count, errors = 0, 0, []

        for idx, row in enumerate(reader, start=1):
            serializer = self.get_serializer(data=row)
            if serializer.is_valid():
                try:
                    serializer.save()
                    saved_count += 1
                except IntegrityError:
                    errors.append(
                        {
                            "row": idx,
                            "email": row.get("email"),
                            "error": "Duplicate email",
                        }
                    )
                    rejected_count += 1
            else:
                errors.append(
                    {"row": idx, "email": row.get("email"), "errors": serializer.errors}
                )
                rejected_count += 1

        response_data = {
            "saved_records": saved_count,
            "rejected_records": rejected_count,
            "errors": errors,
        }

        response_serializer = CSVUploadResponseSerializer(response_data)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
