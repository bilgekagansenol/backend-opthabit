# OptHabit API Dokümantasyonu

Frontend geliştiriciler için API kullanım kılavuzu.

---

## Base URL
```
http://localhost:8000
```

---

## Authentication

API, JWT (JSON Web Token) tabanlı kimlik doğrulama kullanır.

### Token Yapısı
- **Access Token**: API isteklerinde kullanılır (1 gün geçerli)
- **Refresh Token**: Access token yenilemek için kullanılır (30 gün geçerli)

### Header Formatı
```
Authorization: Bearer <access_token>
```

---

## Endpoints

### 1. Kimlik Doğrulama (Auth)

#### 1.1 Kullanıcı Kaydı
```http
POST /api/auth/register/
Content-Type: application/json
```

**Request Body:**
```json
{
    "username": "kullanici_adi",
    "email": "email@example.com",
    "password": "sifre123"
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "username": "kullanici_adi",
    "email": "email@example.com"
}
```

**Hatalar:**
- `400`: Username veya email zaten kullanımda

---

#### 1.2 Giriş (Login)
```http
POST /api/auth/login/
Content-Type: application/json
```

**Request Body:**
```json
{
    "username": "kullanici_adi",
    "password": "sifre123"
}
```

**Response (200 OK):**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Hatalar:**
- `401`: Geçersiz kullanıcı adı veya şifre

---

#### 1.3 Token Yenileme
```http
POST /api/auth/token/refresh/
Content-Type: application/json
```

**Request Body:**
```json
{
    "refresh": "<refresh_token>"
}
```

**Response (200 OK):**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Hatalar:**
- `401`: Geçersiz veya süresi dolmuş refresh token

---

#### 1.4 Profil Görüntüleme
```http
GET /api/auth/profile/
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
    "id": 1,
    "username": "kullanici_adi",
    "email": "email@example.com",
    "created_at": "2026-01-29T10:00:00Z"
}
```

---

#### 1.5 Profil Güncelleme
```http
PATCH /api/auth/profile/
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
    "email": "yeni_email@example.com"
}
```

**Response (200 OK):**
```json
{
    "id": 1,
    "username": "kullanici_adi",
    "email": "yeni_email@example.com",
    "created_at": "2026-01-29T10:00:00Z"
}
```

---

#### 1.6 Şifre Değiştirme
```http
POST /api/auth/change-password/
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
    "old_password": "eski_sifre",
    "new_password": "yeni_sifre123"
}
```

**Response (200 OK):**
```json
{
    "detail": "Şifre başarıyla değiştirildi."
}
```

**Hatalar:**
- `400`: Eski şifre yanlış

---

#### 1.7 Hesap Silme
```http
DELETE /api/auth/delete-account/
Authorization: Bearer <access_token>
```

**Response (204 No Content)**

> ⚠️ **Dikkat:** Bu işlem geri alınamaz!

---

### 2. Çalışma Oturumları (Study Sessions)

#### 2.1 Oturum Oluşturma (Başlatma)
```http
POST /api/sessions/
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
    "date": "2026-01-29",
    "topic": "Django REST Framework",
    "planned_duration": 60
}
```

| Alan | Tip | Zorunlu | Açıklama |
|------|-----|---------|----------|
| date | string (YYYY-MM-DD) | Evet | Çalışma tarihi |
| topic | string | Hayır | Çalışma konusu |
| planned_duration | integer | Evet | Planlanan süre (dakika) |

**Response (201 Created):**
```json
{
    "id": 1,
    "date": "2026-01-29",
    "topic": "Django REST Framework",
    "planned_duration": 60,
    "created_at": "2026-01-29T10:00:00Z"
}
```

> 💡 `started_at` otomatik olarak kaydedilir.

---

#### 2.2 Oturumları Listeleme
```http
GET /api/sessions/
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
[
    {
        "id": 1,
        "date": "2026-01-29",
        "topic": "Django REST Framework",
        "planned_duration": 60,
        "started_at": "2026-01-29T10:00:00Z",
        "status": null,
        "difficulty": null,
        "actual_duration": null,
        "score": null,
        "created_at": "2026-01-29T10:00:00Z",
        "updated_at": "2026-01-29T10:00:00Z"
    }
]
```

> 💡 Sadece giriş yapmış kullanıcının oturumları döner. Sıralama: en yeni tarih önce.

---

#### 2.3 Oturum Detayı
```http
GET /api/sessions/{id}/
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
    "id": 1,
    "date": "2026-01-29",
    "topic": "Django REST Framework",
    "planned_duration": 60,
    "started_at": "2026-01-29T10:00:00Z",
    "status": null,
    "difficulty": null,
    "actual_duration": null,
    "score": null,
    "created_at": "2026-01-29T10:00:00Z",
    "updated_at": "2026-01-29T10:00:00Z"
}
```

**Hatalar:**
- `404`: Oturum bulunamadı

---

#### 2.4 Oturum Güncelleme
```http
PATCH /api/sessions/{id}/
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
    "topic": "Django Advanced",
    "planned_duration": 90
}
```

**Response (200 OK):**
```json
{
    "id": 1,
    "date": "2026-01-29",
    "topic": "Django Advanced",
    "planned_duration": 90,
    "started_at": "2026-01-29T10:00:00Z",
    "status": null,
    "difficulty": null,
    "actual_duration": null,
    "score": null,
    "created_at": "2026-01-29T10:00:00Z",
    "updated_at": "2026-01-29T10:05:00Z"
}
```

---

#### 2.5 Oturumu Tamamlama
```http
POST /api/sessions/{id}/complete/
Authorization: Bearer <access_token>
Content-Type: application/json
```

**Request Body:**
```json
{
    "status": "completed",
    "difficulty": 3
}
```

| Alan | Tip | Zorunlu | Değerler |
|------|-----|---------|----------|
| status | string | Evet | `completed`, `partial`, `distracted` |
| difficulty | integer | Hayır | 1-5 arası |

**Status Değerleri:**
| Değer | Açıklama |
|-------|----------|
| `completed` | Tamamlandı |
| `partial` | Kısmen tamamlandı |
| `distracted` | Dikkat dağıldı |

**Response (200 OK):**
```json
{
    "id": 1,
    "date": "2026-01-29",
    "topic": "Django Advanced",
    "planned_duration": 90,
    "started_at": "2026-01-29T10:00:00Z",
    "status": "completed",
    "difficulty": 3,
    "actual_duration": 45,
    "score": null,
    "created_at": "2026-01-29T10:00:00Z",
    "updated_at": "2026-01-29T10:45:00Z"
}
```

> 💡 `actual_duration` otomatik hesaplanır:
> - Geçen süre < planlanan süre → geçen süre yazılır
> - Geçen süre >= planlanan süre → planlanan süre yazılır

**Hatalar:**
- `400`: Oturum zaten tamamlanmış
- `404`: Oturum bulunamadı

---

#### 2.6 Oturum Silme
```http
DELETE /api/sessions/{id}/
Authorization: Bearer <access_token>
```

**Response (204 No Content)**

---

## Hata Kodları

| Kod | Açıklama |
|-----|----------|
| 200 | Başarılı |
| 201 | Oluşturuldu |
| 204 | Silindi (içerik yok) |
| 400 | Geçersiz istek (validation hatası) |
| 401 | Yetkisiz (token geçersiz veya eksik) |
| 404 | Bulunamadı |
| 500 | Sunucu hatası |

---

## Hata Response Formatı

```json
{
    "detail": "Hata mesajı"
}
```

veya validation hataları için:

```json
{
    "field_name": ["Hata mesajı"]
}
```

---

## Tipik Kullanım Akışı

### 1. Kullanıcı Kaydı ve Giriş
```
1. POST /api/auth/register/  → Kayıt ol
2. POST /api/auth/login/     → Token al
3. Token'ı sakla (localStorage, SecureStorage, vb.)
```

### 2. Çalışma Oturumu Akışı
```
1. POST /api/sessions/              → Oturum başlat (started_at kaydedilir)
2. [Kullanıcı çalışır...]
3. POST /api/sessions/{id}/complete/ → Oturumu tamamla (actual_duration hesaplanır)
```

### 3. Token Yenileme
```
Access token süresi dolduğunda:
1. POST /api/auth/token/refresh/ → Yeni access token al
2. 401 hatası alırsan → Kullanıcıyı login sayfasına yönlendir
```

---

## Swagger UI

Interaktif API dokümantasyonu:
```
http://localhost:8000/api/docs/
```

---

## Postman Koleksiyonu

Proje dizininde `postman_collection.json` dosyası mevcut. Postman'e import ederek tüm endpoint'leri test edebilirsiniz.

**Kullanım:**
1. Postman → Import → `postman_collection.json`
2. Login isteğini çalıştır (token otomatik kaydedilir)
3. Diğer istekleri sırasıyla test et
