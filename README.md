# Hospital Management System (HMS)

A comprehensive Hospital Management System built with Django REST Framework and PostgreSQL. This system manages user authentication, patient records, doctor information, and appointments.

## 🚀 Features

- **User Authentication**: JWT-based authentication with login and registration
- **Patient Management**: Create, read, update, and delete patient records
- **Doctor Management**: Manage doctor profiles and specializations
- **Appointment System**: Schedule and manage appointments between patients and doctors
- **RESTful API**: Well-structured API endpoints for all operations
- **CORS Enabled**: Frontend integration ready

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Git

## 🛠️ Tech Stack

- **Backend Framework**: Django 6.0.2
- **API**: Django REST Framework
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: PostgreSQL
- **CORS**: django-cors-headers

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Nithin98765/whatbytes_HMS_task.git
cd whatbytes_HMS_task
```

### Step 2: Set Up Python Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies

Create a `requirements.txt` file if not present:

```txt
Django==6.0.2
djangorestframework
djangorestframework-simplejwt
psycopg2-binary
django-cors-headers
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up PostgreSQL Database

1. **Open PostgreSQL** (pgAdmin or command line)

2. **Create a new database:**
   ```sql
   CREATE DATABASE HMS;
   ```

3. **Create a PostgreSQL user** (if needed):
   ```sql
   CREATE USER postgres WITH PASSWORD '246810@HMS';
   GRANT ALL PRIVILEGES ON DATABASE HMS TO postgres;
   ```

4. **Update database credentials** in `HMS/settings.py` if different:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'HMS',
           'USER': 'postgres',
           'PASSWORD': '246810@HMS',  # Change this to your password
           'HOST': 'localhost',
           'PORT': '5432'
       }
   }
   ```

### Step 5: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to enter:
- Email address
- Name
- Password

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

The server will start at: **http://127.0.0.1:8000/**

## 🌐 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and get JWT tokens |

### Patients

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/patients/` | List all patients |
| POST | `/api/patients/` | Create a new patient |
| GET | `/api/patients/{id}/` | Get patient details |
| PUT | `/api/patients/{id}/` | Update patient |
| DELETE | `/api/patients/{id}/` | Delete patient |

### Doctors

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/doctors/` | List all doctors |
| POST | `/api/doctors/` | Create a new doctor |
| GET | `/api/doctors/{id}/` | Get doctor details |
| PUT | `/api/doctors/{id}/` | Update doctor |
| DELETE | `/api/doctors/{id}/` | Delete doctor |

### Appointments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/appointment/` | List all appointments |
| POST | `/api/appointment/` | Create a new appointment |
| GET | `/api/appointment/{id}/` | Get appointment details |
| PUT | `/api/appointment/{id}/` | Update appointment |
| DELETE | `/api/appointment/{id}/` | Delete appointment |

## 🔑 API Authentication

### Register a New User

**Request:**
```bash
POST http://127.0.0.1:8000/api/auth/register/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "message": "Users registered Successfully"
}
```

### Login

**Request:**
```bash
POST http://127.0.0.1:8000/api/auth/login/
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Using JWT Token

For protected endpoints, include the access token in the Authorization header:

```bash
Authorization: Bearer <your_access_token>
```

## 🧪 Testing the API

### Using cURL

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","password":"test123"}'

# Login
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

### Using Postman

1. Import the endpoints listed above
2. For authentication endpoints, use POST method
3. For protected endpoints, add Bearer token in Authorization tab

### Using Browser

Access the Django REST Framework browsable API:
- Navigate to `http://127.0.0.1:8000/api/auth/register/`
- You'll see a user-friendly interface to test endpoints

## 🗂️ Project Structure

```
whatbytes_HMS_task/
│
├── HMS/                      # Main project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI config
│   └── asgi.py              # ASGI config
│
├── accounts/                 # User authentication app
│   ├── models.py            # Custom User model
│   ├── serializers.py       # User serializers
│   ├── views.py             # Auth views (Register, Login)
│   └── urls.py              # Auth URL patterns
│
├── patients/                 # Patient management app
│   ├── models.py            # Patient model
│   ├── serializers.py       # Patient serializers
│   ├── views.py             # Patient views
│   └── urls.py              # Patient URL patterns
│
├── doctors/                  # Doctor management app
│   ├── models.py            # Doctor model
│   ├── serializers.py       # Doctor serializers
│   ├── views.py             # Doctor views
│   └── urls.py              # Doctor URL patterns
│
├── appointment/              # Appointment management app
│   ├── models.py            # Appointment model
│   ├── serializers.py       # Appointment serializers
│   ├── views.py             # Appointment views
│   └── urls.py              # Appointment URL patterns
│
├── manage.py                 # Django management script
└── requirements.txt          # Python dependencies

```

## ⚙️ Configuration

### Environment Variables (Optional)

For production, it's recommended to use environment variables:

Create a `.env` file:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_NAME=HMS
DATABASE_USER=postgres
DATABASE_PASSWORD=246810@HMS
DATABASE_HOST=localhost
DATABASE_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
```

Install `python-decouple`:
```bash
pip install python-decouple
```

Update `settings.py` to use environment variables.

### CORS Settings

CORS is currently set to allow all origins (development only). For production, update in `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

## 🔧 Troubleshooting

### Common Issues

**1. PostgreSQL Connection Error**
```
django.db.utils.OperationalError: could not connect to server
```
**Solution:** 
- Ensure PostgreSQL is running
- Verify database credentials in `settings.py`
- Check if the database 'HMS' exists

**2. Migration Errors**
```
No changes detected
```
**Solution:**
```bash
python manage.py makemigrations accounts patients doctors appointment
python manage.py migrate
```

**3. CORS Errors in Browser**
```
Access to fetch has been blocked by CORS policy
```
**Solution:**
- Ensure `corsheaders` is in `INSTALLED_APPS`
- Verify `CorsMiddleware` is first in `MIDDLEWARE`
- Check `CORS_ALLOW_ALL_ORIGINS = True` in settings

**4. Cache/304 Errors**
```
304 Not Modified
```
**Solution:**
- Clear browser cache (Ctrl + Shift + Del)
- Use hard reload (Ctrl + Shift + R)
- Or use Incognito/Private mode

**5. JWT Token Expired**
```
Token is invalid or expired
```
**Solution:**
- Use the refresh token to get a new access token
- Re-login to get new tokens
- Access tokens expire in 15 minutes by default

## 📊 Admin Panel

Access the Django admin panel at: **http://127.0.0.1:8000/admin/**

Login with your superuser credentials to:
- Manage users
- View/edit patients
- View/edit doctors
- View/edit appointments
- Access admin-only features

## 🧹 Database Management Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Open Django shell
python manage.py shell

# Run tests
python manage.py test

# Collect static files (production)
python manage.py collectstatic
```

## 📝 Development Workflow

1. **Activate virtual environment**
   ```bash
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

2. **Make your changes** to models, views, serializers, etc.

3. **Create and apply migrations** if models changed
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Test your endpoints** using Postman, cURL, or the browsable API

## 🔒 Security Notes

- Change the `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Implement rate limiting for APIs
- Use HTTPS in production
- Regularly update dependencies
- Never commit `.env` files or sensitive credentials

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/)

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


