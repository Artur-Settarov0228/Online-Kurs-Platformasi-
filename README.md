# Online-Kurs-Platformasi-

kurs_platformasi/
├── courses/          # Kurslar app
├── users/            # Foydalanuvchilar app  
├── payments/         # To'lovlar app
├── quizzes/          # Testlar app
└── templates/        # HTML shablonlar

2. Asosiy Modellar
Courses app:

Category (Kurs kategoriyalari)

Course (Kurslar)

Module (Modullar)

Lesson (Darslar)

Video (Video darslar)

Users app:

CustomUser (Foydalanuvchi)

Enrollment (Kursga yozilish)

Progress (Darslar progressi)

Quizzes app:

Quiz (Testlar)

Question (Savollar)

Answer (Javoblar)

Result (Test natijalari)

3. Asosiy Funktsiyalar
A. Foydalanuvchi Ro'yxatdan o'tish va Profil:
Registration/Login

Profil sozlamalari

Kurslar tarixi

B. Kurs Boshqaruvi:
Kurs yaratish (admin/teacher)

Modul va dars qo'shish

Video yuklash

PDF materiallar

C. O'qish Jarayoni:
Darsni boshlash

Progressni saqlash

Test topshirish

Certificate olish

D. To'lov Tizimi:
Kurs narxlari

Payment integration (Payme/Click)

Pul o'tkazmalari tarixi

4. Implementatsiya Qadamları
1-bosqich: Asosiy sozlamalar
Django loyiha yaratish

Database sozlash (PostgreSQL)

Static va media fayllar

Bootstrap yuklash

2-bosqich: User modeli
CustomUser yaratish

Login/Register viewlari

Profile sahifasi

3-bosqich: Kurslar tizimi
Category va Course modellari

Kurslar ro'yxati

Kurs detallari sahifasi

4-bosqich: O'qish tizimi
Module va Lesson modellari

Video player integratsiyasi

Progress tracking

5-bosqich: Test tizimi
Quiz va Question modellari

Test sahifasi

Natijalarni hisoblash

6-bosqich: To'lov tizimi
Payment model

Payme API integratsiyasi

Payment history

5. Muhim Texnik Jihatlar
Video hosting: YouTube yoki Vimeo API
File storage: AWS S3 yoki local storage
Database: PostgreSQL (production uchun)
Deployment: Nginx + Gunicorn

6. Qo'shimcha Funktsiyalar
Izohlar tizimi

Reyting va baholar

Qidiruv tizimi

Email bildirishnomalar

Mobile responsive design