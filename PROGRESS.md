# OptHabit Backend - Proje İlerleme Notu

## Proje Özeti
Alışkanlık/ders çalışma takip uygulaması backend'i. Google Play'de yayınlanacak bir mobil uygulama için tasarlandı.

## Teknoloji Stack
- Python 3.10.13
- Django 5.2.10
- Django REST Framework 3.16.1
- JWT Authentication (simplejwt)
- SQLite (development)
- drf-spectacular (Swagger)

## Proje Yapısı
```
backend-opthabit/
├── config/                 # Django proje ayarları
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/               # Kullanıcı sistemi
│   ├── models.py          # Custom User modeli
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── studies/                # Çalışma oturumları
│   ├── models.py          # StudySession modeli
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── .gitignore
```

## Tamamlanan Özellikler

### 1. Kullanıcı Sistemi (accounts app)
- [x] Custom User modeli (email unique)
- [x] JWT tabanlı authentication
- [x] Register, Login, Token Refresh
- [x] Profile görüntüleme/düzenleme
- [x] Şifre değiştirme
- [x] Hesap silme

**Endpoints:**
| Endpoint | Method | Açıklama |
|----------|--------|----------|
| `/api/auth/register/` | POST | Kayıt |
| `/api/auth/login/` | POST | Giriş (JWT token) |
| `/api/auth/token/refresh/` | POST | Token yenile |
| `/api/auth/profile/` | GET/PUT | Profil |
| `/api/auth/change-password/` | POST | Şifre değiştir |
| `/api/auth/delete-account/` | DELETE | Hesap sil |

### 2. Çalışma Oturumları (studies app)
- [x] StudySession modeli
- [x] Oturum başlatma (started_at otomatik)
- [x] Oturum tamamlama (actual_duration otomatik hesaplama)
- [x] CRUD işlemleri

**Model: StudySession**
| Alan | Tip | Açıklama |
|------|-----|----------|
| user | FK | Kullanıcı |
| date | Date | Tarih |
| topic | Char | Konu (opsiyonel) |
| planned_duration | Int | Planlanan süre (dk) |
| started_at | DateTime | Başlangıç zamanı (auto) |
| status | Choice | completed/partial/distracted |
| difficulty | Int | 1-5 zorluk |
| actual_duration | Int | Gerçek süre (dk, auto hesaplama) |
| score | Decimal | Puan (başka app hesaplayacak) |

**Endpoints:**
| Endpoint | Method | Açıklama |
|----------|--------|----------|
| `/api/sessions/` | GET | Listele |
| `/api/sessions/` | POST | Yeni oturum başlat |
| `/api/sessions/{id}/` | GET | Detay |
| `/api/sessions/{id}/` | PUT/PATCH | Güncelle |
| `/api/sessions/{id}/` | DELETE | Sil |
| `/api/sessions/{id}/complete/` | POST | Oturumu tamamla |

**Oturum Akışı:**
1. `POST /api/sessions/` → `{date, topic, planned_duration}` (started_at otomatik kaydedilir)
2. `POST /api/sessions/{id}/complete/` → `{status, difficulty}` (actual_duration otomatik hesaplanır)

**actual_duration Hesaplama Mantığı:**
- Geçen süre < planlanan süre → geçen süreyi yazar
- Geçen süre >= planlanan süre → planlanan süreyi yazar

### 3. API Dokümantasyonu
- [x] Swagger UI: `/api/docs/`
- [x] ReDoc: `/api/redoc/`
- [x] OpenAPI Schema: `/api/schema/`

### 4. Admin Panel
- [x] User admin (CustomUserAdmin)
- [x] StudySession admin
- URL: `/admin/`

## Yapılacaklar (TODO)
- [ ] Score hesaplama app'i
- [ ] Google Sign-In entegrasyonu (User modelde alanlar yorum satırı olarak hazır)
- [ ] Email doğrulama (production için)
- [ ] PostgreSQL migration (production için)
- [ ] Unit testler

## Çalıştırma
```bash
source myenv/bin/activate
python manage.py runserver
```

## Superuser Oluşturma
```bash
source myenv/bin/activate
python manage.py createsuperuser
```

## Son Güncelleme
2026-01-28
