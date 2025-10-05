
# CSV Upload API

A Django REST Framework (DRF) project that provides an API for uploading CSV files containing user data, validating the data, and storing it in a custom user model. This project also includes API endpoints to manage users via CRUD operations.

---

## Technology Stack

- Python 3.12+  
- Django 5.x
- Django REST Framework  
- SQLite  
---

## Features

- Upload CSV files with user data (`name`, `email`, `age`).  
- Validate data before saving:
  - Name cannot be empty.  
  - Age must be between 0 and 120.  
  - Email must be unique and valid.  
- Returns detailed response for:
  - Successfully saved records.  
  - Rejected records with error details.  
- ModelViewSet for CRUD operations on users.  


## 🚀 Getting Started

Follow the steps below to set up and run the CSV Upload API on your local machine.

---

### 1. Clone the Repository

Start by cloning the project from GitHub:

```bash
git clone https://github.com/Ananthu303/Csv-api.git
cd csv_api
```

### 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage dependencies for this project. Here’s how to create and activate it:

For **Windows**:
```bash
python -m venv venv

venv\Scripts\activate
```

For **macOS/Linux**:
```bash
python3 -m venv venv

source venv/bin/activate
```

Once activated, your terminal should show something like `(venv)` indicating that the virtual environment is active.

### 3. Install Dependencies

Once the virtual environment is activated, install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Apply the database migrations to set up the necessary database schema:

```bash
python manage.py migrate
```

### 5. Create Superuser (Super Admin)

You need to create a superuser.
Run the following command to create the superuser:

```bash
python manage.py createsuperuser
```

You will be prompted to enter the following information:

- Username
- Email
- Password

This superuser is the SUPERADMIN having full control over the django admin panel

### 6. Run the Development Server

Once everything is set up, run the Django development server:

```bash
python manage.py runserver
```

Now, you can access the API's at `http://127.0.0.1:8000/`.

---

### 7. Usage

1. **Import Postman Collection:**  
   - Open the Postman collection provided in the repository (`CSV API.postman_collection.json`).  

2. **Upload a CSV file:**  
   - Navigate to the endpoint:  
     ```
     POST http://127.0.0.1:8000/api/v1/users/upload-csv/
     ```  
   - Use the `sample_input.csv` file provided in the GitHub repository.  
   - Ensure the request is sent as **form-data** with the key `file`.  

3. **Response:**  

   The API will return a JSON object with:  
   - `saved_records`: Number of successfully added users  
   - `rejected_records`: Number of rejected rows  
   - `errors`: Detailed information for each rejected row  

   **Example response (from `sample-output.json`):**

```json
{
  "saved_records": 2,
  "rejected_records": 1,
  "errors": [
    {
      "row": 3,
      "email": "jane@example.com",
      "errors": {
        "age": ["Age must be between 0 and 120."]
      }
    }
  ]
}

