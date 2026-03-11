<<<<<<< HEAD
# Simple LMS – Docker & Django Foundation

# 🐳 Docker Services

Project ini menggunakan **Docker Compose** dengan 2 service utama.

## 1️⃣ Web Service (Django)

Image dibangun dari Dockerfile.

Port:

```
8000:8000
```

Service ini menjalankan:

```
python manage.py runserver 0.0.0.0:8000
=======
# Simple LMS – Progress 2

# 🗄 Data Models

## User

Menggunakan Django User model dengan tambahan field **role**:

* admin
* instructor
* student

Relasi:

* Instructor dapat membuat banyak Course
* Student dapat melakukan Enrollment

---

## Category

Digunakan untuk mengelompokkan course.

Fitur:

* Self-referencing relationship
* Mendukung kategori bertingkat

Contoh:

```
Programming
 ├── Web Development
 └── Mobile Development
>>>>>>> 1deced3158211d92a52f9dc8cbc865c3ccff0cea
```

---

<<<<<<< HEAD
## 2️⃣ Database Service (PostgreSQL)

Image:

```
postgres:15
```

Environment variables:

```
POSTGRES_DB=lms_db
POSTGRES_USER=lms_user
POSTGRES_PASSWORD=lms_password
```

Database data disimpan menggunakan **Docker volume**.

---

# ⚙️ Environment Variables

File `.env` digunakan untuk menyimpan konfigurasi database.

Contoh `.env.example`:

```
DEBUG=True

POSTGRES_DB=lms_db
POSTGRES_USER=lms_user
POSTGRES_PASSWORD=lms_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

Copy file ini menjadi `.env` sebelum menjalankan project.

---

# 🚀 Cara Menjalankan Project

## 1️⃣ Clone Repository

```
git clone https://github.com/Kkickp/Progress-1-Simple-LMS---Docker-Django-Foundation
cd simple-lms
```

---

## 2️⃣ Build Docker Image

```
docker compose build
```

---

## 3️⃣ Jalankan Container

```
docker compose up
```

Docker akan menjalankan:

* Django container
* PostgreSQL container

---

## 4️⃣ Jalankan Migration

Buka terminal baru:

```
=======
## Course

Merepresentasikan kursus dalam LMS.

Relasi:

* Instructor → User
* Category → Category

Field utama:

* title
* description
* instructor
* category
* created_at

---

## Lesson

Materi pembelajaran dalam Course.

Relasi:

* Course → Course

Fitur:

* Memiliki field **order** untuk menentukan urutan lesson.

---

## Enrollment

Merepresentasikan student yang mengikuti course.

Relasi:

* Student → User
* Course → Course

Constraint:

```
unique_together = ('student', 'course')
```

Artinya satu student hanya dapat enroll sekali pada course yang sama.

---

## Progress

Digunakan untuk melacak progress student pada lesson.

Relasi:

* Student → User
* Lesson → Lesson

Field utama:

* completed
* completed_at

---

# ⚡ Query Optimization

Untuk menghindari **N+1 Query Problem**, digunakan:

### Course QuerySet

```
Course.objects.for_listing()
```

Optimasi:

* `select_related('instructor', 'category')`
* `prefetch_related('lessons')`

Digunakan untuk menampilkan daftar course secara efisien.

---

### Enrollment QuerySet

```
Enrollment.objects.for_student_dashboard()
```

Optimasi:

* `select_related('course')`
* `prefetch_related('course__lessons')`

Digunakan untuk dashboard student.

---

# ⚙ Django Admin Configuration

Django Admin dikonfigurasi agar lebih informatif.

Fitur yang digunakan:

* **list_display**
* **search_fields**
* **list_filter**
* **Inline models**

Lesson ditampilkan sebagai **inline dalam Course Admin**.

---

# 🔄 Migrations

Migration digunakan untuk membuat tabel database berdasarkan models.

Menjalankan migration:

```
docker compose exec web python manage.py makemigrations
>>>>>>> 1deced3158211d92a52f9dc8cbc865c3ccff0cea
docker compose exec web python manage.py migrate
```

---

<<<<<<< HEAD
## 5️⃣ Akses Django

Buka browser:

```
http://localhost:8000
```

Jika berhasil akan muncul halaman:

```
The install worked successfully! Congratulations!
```

---

## Docker Containers Running

```
docker ps
```

Menampilkan container:

```
django_app
postgres_db
```

---

# 🧪 Testing Database Connection

Jalankan migration:

```
docker compose exec web python manage.py migrate
```
=======
# 📦 Initial Data Fixtures

Initial data dapat dimuat menggunakan fixture.

Contoh:

```
python manage.py loaddata initial_data.json
```

Fixture digunakan untuk:

* sample categories
* sample courses
* sample users

---

# 🧪 Query Optimization Demo

Contoh **N+1 Query Problem**:

```
courses = Course.objects.all()

for course in courses:
    print(course.instructor.username)
```

Solusi menggunakan `select_related`:

```
courses = Course.objects.select_related('instructor')
```

Hasil:

* jumlah query lebih sedikit
* performa lebih baik

---
>>>>>>> 1deced3158211d92a52f9dc8cbc865c3ccff0cea
