# API Testing Guide

This guide provides examples of testing all available API endpoints.

## Base URL
```
http://127.0.0.1:8000
```

## Authentication Endpoints

### 1. Register a New User

**Endpoint:** `POST /api/auth/register/`

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepass123"
  }'
```

**Success Response (201):**
```json
{
  "message": "Users registered Successfully"
}
```

**Error Response (400):**
```json
{
  "email": ["This field must be unique."],
  "password": ["This field may not be blank."]
}
```

---

### 2. Login

**Endpoint:** `POST /api/auth/login/`

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepass123"
  }'
```

**Success Response (200):**
```json
{
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Save the tokens for subsequent requests!**

---

## Patient Endpoints

### 3. Create a Patient

**Endpoint:** `POST /api/patients/`

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "name": "Jane Smith",
    "age": 35,
    "gender": "Female",
    "phone": "+1234567890",
    "address": "123 Main St, City"
  }'
```

---

### 4. Get All Patients

**Endpoint:** `GET /api/patients/`

**Request:**
```bash
curl -X GET http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 5. Get Single Patient

**Endpoint:** `GET /api/patients/{id}/`

**Request:**
```bash
curl -X GET http://127.0.0.1:8000/api/patients/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 6. Update Patient

**Endpoint:** `PUT /api/patients/{id}/`

**Request:**
```bash
curl -X PUT http://127.0.0.1:8000/api/patients/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "name": "Jane Smith Updated",
    "age": 36,
    "gender": "Female",
    "phone": "+1234567890",
    "address": "456 New St, City"
  }'
```

---

### 7. Delete Patient

**Endpoint:** `DELETE /api/patients/{id}/`

**Request:**
```bash
curl -X DELETE http://127.0.0.1:8000/api/patients/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## Doctor Endpoints

### 8. Create a Doctor

**Endpoint:** `POST /api/doctors/`

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/api/doctors/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "name": "Dr. Smith",
    "specialization": "Cardiology",
    "phone": "+9876543210",
    "email": "dr.smith@hospital.com"
  }'
```

---

### 9. Get All Doctors

**Endpoint:** `GET /api/doctors/`

**Request:**
```bash
curl -X GET http://127.0.0.1:8000/api/doctors/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 10. Get Single Doctor

**Endpoint:** `GET /api/doctors/{id}/`

**Request:**
```bash
curl -X GET http://127.0.0.1:8000/api/doctors/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## Appointment Endpoints

### 11. Create an Appointment

**Endpoint:** `POST /api/appointment/`

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/api/appointment/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "patient_id": 1,
    "doctor_id": 1,
    "appointment_date": "2026-02-20",
    "appointment_time": "10:00:00",
    "reason": "Regular checkup"
  }'
```

---

### 12. Get All Appointments

**Endpoint:** `GET /api/appointment/`

**Request:**
```bash
curl -X GET http://127.0.0.1:8000/api/appointment/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 13. Get Single Appointment

**Endpoint:** `GET /api/appointment/{id}/`

**Request:**
```bash
curl -X GET http://127.0.0.1:8000/api/appointment/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 14. Update Appointment

**Endpoint:** `PUT /api/appointment/{id}/`

**Request:**
```bash
curl -X PUT http://127.0.0.1:8000/api/appointment/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d '{
    "patient_id": 1,
    "doctor_id": 1,
    "appointment_date": "2026-02-21",
    "appointment_time": "11:00:00",
    "reason": "Follow-up"
  }'
```

---

### 15. Delete Appointment

**Endpoint:** `DELETE /api/appointment/{id}/`

**Request:**
```bash
curl -X DELETE http://127.0.0.1:8000/api/appointment/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## Testing with Postman

### Import Collection

1. Open Postman
2. Click "Import"
3. Create a new collection called "HMS API"
4. Add environment variables:
   - `base_url`: `http://127.0.0.1:8000`
   - `access_token`: (will be set after login)

### Setup Authorization

1. After login, copy the `access` token from response
2. For each protected endpoint, add to Headers:
   ```
   Authorization: Bearer {{access_token}}
   ```

### Quick Test Flow

1. **Register** a new user
2. **Login** with credentials
3. **Copy access token** from login response
4. **Create a patient**
5. **Create a doctor**
6. **Create an appointment** linking patient and doctor
7. **View all appointments**

---

## Testing with Python Requests

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# 1. Register
register_data = {
    "name": "Test User",
    "email": "test@example.com",
    "password": "testpass123"
}
response = requests.post(f"{BASE_URL}/api/auth/register/", json=register_data)
print(response.json())

# 2. Login
login_data = {
    "email": "test@example.com",
    "password": "testpass123"
}
response = requests.post(f"{BASE_URL}/api/auth/login/", json=login_data)
tokens = response.json()
access_token = tokens['access']

# 3. Create Patient (with auth)
headers = {"Authorization": f"Bearer {access_token}"}
patient_data = {
    "name": "John Patient",
    "age": 30,
    "gender": "Male",
    "phone": "+1234567890",
    "address": "123 Street"
}
response = requests.post(f"{BASE_URL}/api/patients/", json=patient_data, headers=headers)
print(response.json())

# 4. Get All Patients
response = requests.get(f"{BASE_URL}/api/patients/", headers=headers)
print(response.json())
```

---

## Common HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Missing or invalid token |
| 403 | Forbidden | No permission to access |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Internal server error |

---

## Error Handling Examples

### Invalid Credentials (400)
```json
{
  "non_field_errors": ["Invalid credentials"]
}
```

### Token Expired (401)
```json
{
  "detail": "Given token not valid for any token type",
  "code": "token_not_valid"
}
```

### Missing Required Fields (400)
```json
{
  "name": ["This field is required."],
  "email": ["This field is required."]
}
```

---

## Tips

1. **Always include `Content-Type: application/json`** for POST/PUT requests
2. **Store access token** after login for subsequent requests
3. **Tokens expire in 15 minutes** - use refresh token to get new access token
4. **Use browsable API** at `http://127.0.0.1:8000/api/` during development
5. **Check Django logs** for detailed error messages

---

