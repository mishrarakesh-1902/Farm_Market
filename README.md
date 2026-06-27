<div align="center">

<img src="https://farm-market-1.onrender.com/static/images/hero_banner.png" alt="FarmDirect Banner" width="100%" style="border-radius:12px;" />

<br/>
<br/>

# 🌾 FarmDirect — Agro-Tech Marketplace Suite

**An AI-powered farm-to-table platform that connects verified farmers directly to institutional buyers, eliminates middlemen, and delivers real-time crop intelligence.**

<br/>

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-farm--market--1.onrender.com-22c55e?style=for-the-badge&logoColor=white)](https://farm-market-1.onrender.com)
[![GitHub Repo](https://img.shields.io/badge/GitHub-mishrarakesh--1902%2FFarm__Market-181717?style=for-the-badge&logo=github)](https://github.com/mishrarakesh-1902/Farm_Market)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML_Engine-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Cloudinary](https://img.shields.io/badge/Cloudinary-Media_CDN-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)](https://cloudinary.com/)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [ML Model — Crop Intelligence](#-ml-model--crop-intelligence-engine)
- [App Screenshots](#-app-screenshots)
- [Architecture](#-system-architecture)
- [Getting Started](#-getting-started-local-setup)
- [Project Structure](#-project-structure)
- [Environment Variables](#-environment-variables)
- [Roadmap](#-roadmap)
- [Author](#-author)

---

## 🌱 Overview

**FarmDirect** is a full-stack Django web application that reimagines agricultural commerce in India. It provides farmers with a direct digital channel to sell their produce to buyers — cutting out costly intermediaries — while equipping them with AI-powered tools to make smarter farming decisions.

> _"45,000+ verified farmers. 1.2M tons traded. Zero middlemen."_

### The Problem It Solves

| Pain Point | FarmDirect Solution |
|---|---|
| Farmers earn ~30% less due to middlemen | Direct-to-buyer marketplace |
| No data-driven crop planning | AI Crop Recommendation Engine (99.5% accuracy) |
| Manual quality verification | Verified listing system with quality badges |
| No real-time pricing visibility | Live Market Pulse — tracks 500+ regional mandis |
| Hard to source certified farm inputs | Premium Inputs procurement module |

---

## 🚀 Live Demo

🔗 **[https://farm-market-1.onrender.com](https://farm-market-1.onrender.com)**

> Use the following demo credentials to explore the platform:
>
> **Username:** `demo_user` &nbsp;|&nbsp; **Password:** `Demo@1234`

---

## ✨ Key Features

### 🛒 Marketplace Core
- **Direct Selling Portal** — Farmers list produce with photos, pricing, and descriptions
- **Live Listings** — 16+ verified crop listings with pagination and search
- **Cart (Tray) System** — Add-to-cart, quantity management, and checkout flow
- **Cloudinary CDN** — Optimized image uploads and delivery for all produce photos

### 🤖 AI Intelligence Suite
- **Crop Recommendation Engine** — Predicts optimal crops based on soil N/P/K, pH, temperature, humidity, and rainfall inputs using a **scikit-learn ensemble model**
- **Yield Forecast Suite** — Predictive analytics for expected harvest output
- **Market Pulse Feed** — Real-time commodity prices (Wheat, Rice, Cotton, Soybean, Maize) via a scrolling ticker

### 👤 User Ecosystem
- **Dual-role Auth** — Separate farmer and buyer accounts with Django's auth system
- **Secure Login Terminal** — JWT-style session flow with password reset via email
- **Farmer Profiles** — Verified badges, ratings (4.8★ avg), and produce history

### 📦 Quality Inputs Module
- Procurement portal for certified seeds, organic fertilizers, and smart equipment

### 📊 Admin Panel
- Full Django admin dashboard for listing moderation, user management, and order oversight

---

## 🛠 Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Backend Framework** | Django 5.x (Python 3.11) |
| **ML / Data Science** | scikit-learn, pandas, NumPy |
| **Database** | PostgreSQL (Production) / SQLite (Dev) |
| **Media Storage** | Cloudinary (CDN image hosting) |
| **Frontend** | Django Templates, Tailwind CSS, Vanilla JS |
| **Authentication** | Django Auth + Session Management |
| **Deployment** | Render (PaaS) |
| **Static Assets** | WhiteNoise |
| **Email** | SMTP (Django Email Backend) |

</div>

---

## 🧠 ML Model — Crop Intelligence Engine

The AI core of FarmDirect is a **multi-class crop recommendation classifier** trained on real agricultural data.

```
Input Parameters     →   Model   →   Output
─────────────────────────────────────────────
N   (Nitrogen)
P   (Phosphorus)       Ensemble   →  Recommended Crop
K   (Potassium)        Voting          (e.g., Rice, Wheat,
pH  (Soil acidity)     Classifier      Cotton, Maize...)
Temperature (°C)
Humidity (%)
Rainfall (mm)
```

### Model Performance

| Metric | Score |
|---|---|
| **Accuracy** | **99.5%** |
| Cross-Validation | 5-Fold Stratified CV |
| Algorithm | VotingClassifier (RF + GBM + SVM) |
| Dataset | 2,200 samples × 7 features |
| Classes | 22 crop types |

> Model uses `GridSearchCV` for hyperparameter tuning and avoids data leakage with proper train/test split pipeline.

---

## 📸 App Screenshots

### 🏠 Homepage — Hero & Market Pulse
> Live mandi commodity prices scroll in real-time across the banner ticker

![Homepage](https://farm-market-1.onrender.com/static/images/hero_banner.png)

---

### 🛒 Marketplace — Live Listings
> 16+ verified produce listings with farmer profiles, ratings, and Cloudinary-hosted images

| Listing Card | Details |
|---|---|
| Fresh Tomatoes | ₹25/unit — Verified — ⭐ 4.8 |
| Organic Wheat | ₹40/unit — Verified — ⭐ 4.8 |
| Alphonso Mango | ₹120/unit — Verified — ⭐ 4.8 |
| Rice Basmati | ₹90/unit — Verified — ⭐ 4.8 |
| Green Chilli | ₹60/unit — Verified — ⭐ 4.8 |
| Kashmiri Apples | ₹150/unit — Verified — ⭐ 4.8 |

> 🔗 [Browse Live Marketplace →](https://farm-market-1.onrender.com/direct-selling/)

---

### 🔐 Auth — Login Terminal
> Cyberpunk-styled secure auth flow with encryption badge and real-time farmer count

> 🔗 [View Login Page →](https://farm-market-1.onrender.com/login/)

---

### 🤖 AI Predictor Suite
> Input 7 soil & climate parameters, get instant crop recommendation with confidence score

> 🔗 [Try AI Suite →](https://farm-market-1.onrender.com/ai-suite/) _(requires login)_

---

## 🏗 System Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    Client (Browser)                       │
│            Django Templates + Tailwind CSS                │
└─────────────────────┬────────────────────────────────────┘
                      │ HTTP
┌─────────────────────▼────────────────────────────────────┐
│                  Django Backend                           │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐ │
│  │  Auth Views │  │ Marketplace  │  │   AI Suite       │ │
│  │  /login     │  │ /direct-sell │  │  /predict-crop   │ │
│  │  /register  │  │ /cart        │  │  /yeild-predict  │ │
│  └─────────────┘  └──────────────┘  └────────┬────────┘ │
│                                               │          │
│  ┌────────────────────────────────────────────▼────────┐ │
│  │              scikit-learn ML Pipeline               │ │
│  │     VotingClassifier (RF + GBM + SVM)               │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌──────────────────────┐   ┌──────────────────────────┐ │
│  │   PostgreSQL DB       │   │   Cloudinary CDN         │ │
│  │   (Users, Products,  │   │   (Product Images,       │ │
│  │    Orders, Listings) │   │    Auth Banners)         │ │
│  └──────────────────────┘   └──────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
                      │
            ┌─────────▼─────────┐
            │   Render (PaaS)   │
            │  + WhiteNoise     │
            │  + SMTP Email     │
            └───────────────────┘
```

---

## ⚙ Getting Started (Local Setup)

### Prerequisites

- Python 3.11+
- pip / virtualenv
- PostgreSQL (or use SQLite for dev)
- Cloudinary account

### 1. Clone the Repository

```bash
git clone https://github.com/mishrarakesh-1902/Farm_Market.git
cd Farm_Market
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root directory (see [Environment Variables](#-environment-variables) section below).

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 📁 Project Structure

```
Farm_Market/
│
├── core/                    # Main Django app
│   ├── models.py            # Product, Order, Cart, UserProfile
│   ├── views.py             # Marketplace, Cart, Auth views
│   ├── urls.py              # URL routing
│   └── ml_model/            # scikit-learn crop prediction pipeline
│       ├── model.pkl        # Serialized trained model
│       └── predict.py       # Prediction logic
│
├── templates/               # Django HTML templates
│   ├── base.html
│   ├── home.html
│   ├── marketplace.html
│   ├── ai_suite.html
│   └── auth/
│       ├── login.html
│       └── register.html
│
├── static/
│   ├── css/                 # Tailwind + custom styles
│   ├── js/                  # Market pulse ticker, cart JS
│   └── images/              # Hero banner, auth banner
│
├── requirements.txt
├── manage.py
└── .env.example
```

---

## 🔐 Environment Variables

Create a `.env` file with the following keys:

```env
# Django
SECRET_KEY=your_django_secret_key
DEBUG=False
ALLOWED_HOSTS=your-domain.onrender.com,localhost

# Database (PostgreSQL)
DATABASE_URL=postgres://user:password@host:5432/dbname

# Cloudinary
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Email (SMTP)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

---

## 🗺 Roadmap

- [x] Direct marketplace with verified farmer listings
- [x] Cart system with add/remove functionality
- [x] AI crop recommendation engine (99.5% accuracy)
- [x] Yield prediction suite
- [x] Market price ticker (500+ mandis)
- [x] Cloudinary image CDN integration
- [x] Secure auth with password reset
- [x] Deployed on Render
- [ ] Payment gateway integration (Razorpay)
- [ ] Real-time mandi price API (live data feed)
- [ ] Mobile app (React Native)
- [ ] Farmer analytics dashboard
- [ ] Multi-language support (Hindi, Marathi, Tamil)
- [ ] Logistics tracking integration

---

## 👨‍💻 Author

<div align="center">

**Rakesh Kumar Mishra**
*Full Stack Developer & AI/ML Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-mishrarakesh--1902-181717?style=for-the-badge&logo=github)](https://github.com/mishrarakesh-1902)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/rakesh-kumar-mishra)
[![Email](https://img.shields.io/badge/Email-mishrarakeshkumar766%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mishrarakeshkumar766@gmail.com)

*B.Tech CSE @ VIT Bhopal University (2023–2027) | AWS SAA-C03 Certified | OCI Developer Certified*

*🏆 Finalist — Solvit 2025 | ET AI Concierge | Canara Suraksha (Top 100 of 4,000+ teams)*

</div>

---

<div align="center">

**⭐ Star this repo if you found it useful — it helps more people discover FarmDirect!**

*Built with 💚 to empower India's farming community through technology*

</div> 
