# Clinic Management System

## Overview
This project is a Django-based Clinic Management System that facilitates the management of hospital operations, including doctor recruitment, patient admission, appointment scheduling, and billing. The system provides distinct functionalities for Admin, Doctor, and Patient roles.

---

## Features and Functionalities

### Admin
- **Account Management**:
  - Signup and login without requiring approval.
- **Doctor Management**:
  - Register/view/approve/reject/delete doctors.
  - Approve doctors who apply for jobs in the hospital.
- **Patient Management**:
  - Admit/view/approve/reject/discharge patients.
  - Discharge patients after treatment completion.
- **Invoice Management**:
  - Generate and download invoice PDFs.
  - Invoices include charges for medicine, room, doctor, and other services.
- **Appointment Management**:
  - View/book/approve appointments.
  - Approve appointments requested by patients.

### Doctor
- **Job Application**:
  - Apply for a job at the hospital.
  - Login is enabled only after admin approval.
- **Patient Management**:
  - View assigned patient details, including symptoms, name, and mobile number.
  - View discharged patients (discharged by admin).
- **Appointment Management**:
  - View appointments booked by the admin.
  - Delete appointments after attending them.

### Patient
- **Account Management**:
  - Create an account for admission to the hospital.
  - Login is enabled only after admin approval.
- **Doctor Information**:
  - View assigned doctor’s details, including specialization, mobile, and address.
- **Appointment Management**:
  - View the status of booked appointments (pending/confirmed by admin).
  - Book new appointments (approval required by admin).
- **Invoice Management**:
  - View and download invoice PDFs (available only after discharge by admin).

---

## Technologies Used
- **Backend**: Django Framework
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, JavaScript

---

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Clinic_Management
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open the application in your browser at `http://127.0.0.1:8000`.

---

## User Roles and Access
- **Admin**: Full control over the system.
- **Doctor**: Limited access to assigned patients and appointments.
- **Patient**: Access to personal records, assigned doctor details, and invoices.

---

