# 🎓 CampusFound – Smart Lost & Found Campus System

A web-based Lost and Found Management System built with **Django**, designed specifically for college campuses to help students and staff report, track, and recover lost belongings in a secure and organized way.

---

## 📌 Project Description

In many colleges, there is no proper platform to report lost items or verify claims. **CampusFound** solves this by providing a centralized digital platform where:

- Users can register and log in
- Users can report lost or found items with images
- The system displays possible item matches
- Users can submit claim requests with proof
- Admins can approve or reject claims
- Approved users receive handover instructions and contact details

---

## 🎯 Objectives

- Reduce confusion in item recovery
- Make lost item reporting simple and accessible
- Provide a proper claim verification process
- Improve transparency and security
- Create a proper admin-managed handover workflow

---

## ✨ Features

### 👤 User Features
- User Registration, Login & Logout
- Report Lost Item (with image, location, date)
- Report Found Item (with image, location, date)
- View all Lost & Found items
- View possible matched items
- Submit claim request for a lost item
- View notifications (item reported, claim submitted, approved/rejected)
- View approved and rejected claims
- View handover instructions after claim approval

### 🛠️ Admin Features
- Admin login via Django superuser account
- Separate Admin Dashboard
- View total Lost Items, Found Items, and Claims
- View Pending, Approved, and Rejected claims
- View all item details and matched items
- Approve or Reject claim requests
- Add handover instructions while approving

---

## 🛠️ Technologies Used

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite3 |
| Authentication | Django Authentication System |
| Image Support | Pillow |

---

## ⚙️ Project Modules

| Module | Description |
|---|---|
| Authentication | Registration, Login, Logout |
| Lost Item | Submit lost item details, image, location, date |
| Found Item | Submit found item details, image, location, date |
| Match | Compares lost & found items, shows possible matches |
| Claim | User submits proof; stored in database |
| Admin Dashboard | Manage all data, approve/reject claims |
| Notification | Messages for key actions (reported, submitted, approved/rejected) |

---

## 🔄 Project Workflow

### User Workflow
1. User opens the system and registers a new account
2. User logs in
3. User reports a lost item or submits a found item
4. System displays lost and found item lists
5. System shows possible matched items
6. User submits a claim request with proof
7. Admin reviews and approves or rejects the request
8. If **approved** → User sees contact details and handover instructions
9. If **rejected** → User sees rejected claim status

### Admin Workflow
1. Admin logs in via Django superuser account
2. Admin views dashboard (lost items, found items, matched items, claims)
3. Admin checks proof details
4. Admin approves or rejects the claim (with optional handover note)
5. Approved user receives handover information

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed on your system:

- Python 3.x
- pip
- Git
- VS Code (or any code editor)

---
## 🌐 Live Demo

**Live URL:** https://lost-found-system-vagj.onrender.com

---

## 🔑 Login Information

### 🛠️ Admin Login
Use the following default credentials to access the admin panel from the same login page:

- **Username:** `admin`
- **Password:** `1234`

> After admin login, the user will be redirected to the **Admin Dashboard**.

> **Note:** This default admin account was created locally using Django's `createsuperuser` command and included for project demonstration purposes.

---

### 👤 Student / Client Login
There is **no default student/client username and password**.

Please use the **Register** option in the web application to create a new account, then log in using your registered credentials.

> Student/client users will be redirected to the **User Dashboard** after login.


### Installation

```bash
# Clone the repository
git clone https://github.com/pratham3900/lost-found-system.git
cd lost-found-system

# Create virtual environment
python -m venv env

# Activate virtual environment (Windows)
env\Scripts\activate

# Activate virtual environment (Mac/Linux)
source env/bin/activate

# Install dependencies
pip install django
pip install pillow

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create admin superuser
python manage.py createsuperuser

# (Optional) Create media folder manually if not exists
mkdir media

# Run the development server
python manage.py runserver
```

Then open your browser and visit: **http://127.0.0.1:8000/**

---

### Open in VS Code

```bash
code .
```

---

## 🔐 Admin Login

Admin does **not** register from the normal registration page.

To create an admin account, run:

```bash
python manage.py createsuperuser
```

You will be prompted to enter the following details:
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.

> ⚠️ Choose a strong password. Django will warn you if the password is too short or too common.

Then log in from the **same login page** as normal users:
**http://127.0.0.1:8000/**

- If the user has **`is_staff = True`** → Redirected to **Admin Dashboard**
- If the user is a **normal user** → Redirected to **User Dashboard**
---

## 📁 Project Structure Notes

| Item | Description |
|---|---|
| `env/` | Virtual environment — do **not** upload to GitHub |
| `db.sqlite3` | Local database — can be excluded via `.gitignore` |
| `media/` | Stores uploaded item images |

---

## ⚠️ Important Notes

- The `env/` folder should **not** be uploaded to GitHub
- The `db.sqlite3` file is local and should be added to `.gitignore`
- The `media/` folder stores uploaded images and is created automatically on first upload
- Make sure **Pillow** is installed for image upload support
- Set `TIME_ZONE = 'Asia/Kolkata'` in `settings.py` to display IST time correctly

---

## 📄 License

This project is developed for academic and educational purposes.

---

## 👨‍💻 Author

**Pratham** – [GitHub Profile](https://github.com/pratham3900)
