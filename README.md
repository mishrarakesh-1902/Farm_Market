<div align="center">

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
- [App Screenshots](#-app-screenshots)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [ML Model — Crop Intelligence](#-ml-model--crop-intelligence-engine)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started-local-setup)
- [Project Structure](#-project-structure)
- [Environment Variables](#-environment-variables)
- [Roadmap](#-roadmap)
- [Author](#-author)

---

## 🌱 Overview

**FarmDirect** is a full-stack Django web application that reimagines agricultural commerce in India. It provides farmers with a direct digital channel to sell their produce to institutional buyers — cutting out costly intermediaries — while equipping them with AI-powered tools to make smarter farming decisions.

> _"45,000+ verified farmers. 1.2M tons traded. Zero middlemen."_

### The Problem It Solves

| Pain Point | FarmDirect Solution |
|---|---|
| Farmers earn ~30% less due to middlemen | Direct-to-buyer marketplace with zero commission |
| No data-driven crop planning | AI Crop Recommendation Engine (99.5% accuracy) |
| No harvest volume forecasting | Yield Prediction Suite with state/season/crop inputs |
| Manual quality verification | Verified listing system with quality badges |
| No real-time pricing visibility | Live Market Pulse — tracks 500+ regional mandis |
| Hard to source certified farm inputs | Premium Inputs procurement module |

---

## 🚀 Live Demo

🔗 **[https://farm-market-1.onrender.com](https://farm-market-1.onrender.com)**

> Register a free account to access the full platform — AI Suite, Marketplace, Control Panel, and My Produce dashboard.

---

## 📸 App Screenshots

### 🏠 Homepage — Hero & Market Pulse

> Dark-green hero section with bold typography, live mandi price ticker at the bottom scrolling real-time commodity rates (Rice ₹4,200/q · Cotton ₹6,800/q · Soybean ₹3,900/q · Maize ₹1,950/q).

<img width="1568" height="715" alt="image" src="https://github.com/user-attachments/assets/378316ce-4901-4383-b3a4-abed1e44f0b2" />


---

### 🛒 Marketplace Core — Live Listings

> 16 verified produce listings (Fresh Tomatoes ₹25 · Organic Wheat ₹40 · Green Chilli ₹60 · Mango ₹120 · Potatoes ₹20 · Rice Basmati ₹90 · Lady Finger ₹45 · Onions ₹25) with real Cloudinary product images, verified badges, farmer ratings, and Add to Tray buttons.

<img width="1516" height="784" alt="image" src="https://github.com/user-attachments/assets/f16a5f69-c615-459a-96d7-d0cff99bede1" />


---

### 🤖 AI Suite — Crop Intelligence Engine

> Neural Core Active — input 7 multi-spectral soil metrics (N, P, K, pH, Temperature, Humidity, Rainfall) and hit **Initialize Neural Synthesis** to get a high-precision crop recommendation.

<img width="1568" height="761" alt="image" src="https://github.com/user-attachments/assets/12a81cb2-3c1e-48b4-bf90-318004e666dc" />


---

### 📊 Yield Forecast Suite — Orbital Data Sync

> Input State, Crop Type, Season, Crop Year, Area (ha), Annual Rainfall, Fertilizer & Pesticide used → **Generate Yield Projection** to predict production volume from historical climatic and operational data.

<img width="1523" height="784" alt="image" src="https://github.com/user-attachments/assets/952412ed-68e5-4db5-a7d2-200ff2b5b08a" />


---

## ✨ Key Features

### 🛒 Marketplace Core
- **Direct Selling Portal** — Farmers list produce with Cloudinary-hosted photos, pricing, and descriptions
- **Live Listings** — 16+ verified crop listings with Search Pulse, Filters, and pagination
- **Cart (Tray) System** — Add-to-tray, quantity management, and full checkout flow
- **Verified Badges** — Quality-assured listings with 4.8★ avg farmer rating

### 🤖 AI Intelligence Suite
- **Crop Recommendation Engine** — Predicts optimal crops from 7 soil & climate inputs using an ensemble ML model (**99.5% accuracy**)
- **Yield Forecast Suite** — Projects harvest volume using state, season, crop type, area, rainfall, fertilizer, and pesticide data
- **Market Pulse Feed** — Live commodity prices scrolling in real-time across the hero banner

### 👤 User Ecosystem
- **Authenticated Dashboard** — Post-login nav shows Market, Control Panel, My Produce, AI Suite, Contact + Welcome back greeting
- **Secure Auth** — Django session-based auth with email password reset
- **Farmer Profiles** — Verified badges, star ratings, and produce history

### 📦 Quality Inputs Module
- Procurement portal for certified seeds, organic fertilizers, and smart farm equipment

### 📊 Admin Panel
- Full Django admin for listing moderation, user management, and order oversight

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
| **Static Files** | WhiteNoise |
| **Email** | Django SMTP Backend |

</div>

---

## 🧠 ML Model — Crop Intelligence Engine

The AI core is a **multi-class crop recommendation classifier** trained on real agricultural data.

```
Input Parameters         →    Model Pipeline    →    Output
──────────────────────────────────────────────────────────────
N   (Nitrogen, %)
P   (Phosphorus, %)           VotingClassifier     Recommended Crop
K   (Potassium, %)        →   Random Forest    →   + Confidence Score
pH  (Soil pH level)           Gradient Boost       (e.g., Rice, Wheat,
Temperature (°C)              SVM                   Cotton, Maize ...)
Humidity (%)
Rainfall (mm)
```

### Model Performance

| Metric | Score |
|---|---|
| **Accuracy** | **99.5%** |
| Cross-Validation | 5-Fold Stratified CV |
| Algorithm | VotingClassifier (RF + GBM + SVM) |
| Hyperparameter Tuning | GridSearchCV |
| Dataset | 2,200 samples × 7 features |
| Output Classes | 22 crop types |

### Yield Prediction Model

| Input | Description |
|---|---|
| State | Indian state (e.g., Andhra Pradesh) |
| Crop Type | e.g., Arecanut, Rice, Wheat |
| Season | Kharif / Rabi / Autumn / Whole Year |
| Area (ha) | Farm area in hectares |
| Annual Rainfall (mm) | Regional rainfall data |
| Fertilizer Used (kg) | Total fertilizer input |
| Pesticide Used (kg) | Total pesticide input |

> Both models use proper train/test splits before fitting — no data leakage. `GridSearchCV` used for hyperparameter optimization.

---

## 🏗 System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                     Client (Browser)                         │
│              Django Templates + Tailwind CSS                 │
└──────────────────────────┬───────────────────────────────────┘
                           │ HTTP
┌──────────────────────────▼───────────────────────────────────┐
│                     Django Backend                           │
│                                                              │
│  ┌──────────────┐  ┌───────────────┐  ┌──────────────────┐  │
│  │  Auth Views  │  │  Marketplace  │  │    AI Suite      │  │
│  │  /login      │  │  /direct-sell │  │  /predict-crop   │  │
│  │  /register   │  │  /cart        │  │  /yeild-predict  │  │
│  └──────────────┘  └───────────────┘  └────────┬─────────┘  │
│                                                │             │
│        ┌──────────────────────────────────────▼──────────┐   │
│        │           scikit-learn ML Pipeline              │   │
│        │   Crop: VotingClassifier (RF + GBM + SVM)       │   │
│        │   Yield: Regression model (State/Season/Area)   │   │
│        └──────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────┐     ┌────────────────────────────┐ │
│  │    PostgreSQL DB     │     │      Cloudinary CDN        │ │
│  │  Users, Products,   │     │   Product Images,          │ │
│  │  Orders, Listings   │     │   Auth Banners             │ │
│  └──────────────────────┘     └────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
                           │
               ┌───────────▼──────────┐
               │    Render (PaaS)     │
               │  WhiteNoise + SMTP   │
               └──────────────────────┘
```

---

## ⚙ Getting Started (Local Setup)

### Prerequisites

- Python 3.11+
- pip / virtualenv
- PostgreSQL (or SQLite for dev)
- Cloudinary account (free tier works)

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

Create a `.env` file in the root directory (see [Environment Variables](#-environment-variables) below).

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

Visit **[http://localhost:8000](http://localhost:8000)**

---

## 📁 Project Structure

```
Farm_Market/
│
├── core/                        # Main Django app
│   ├── models.py                # Product, Order, Cart, UserProfile
│   ├── views.py                 # Marketplace, Cart, Auth, AI views
│   ├── urls.py                  # URL routing
│   └── ml/
│       ├── crop_model.pkl       # Serialized VotingClassifier (crop recommendation)
│       ├── yield_model.pkl      # Serialized yield regression model
│       └── predict.py           # Prediction logic
│
├── templates/                   # Django HTML templates
│   ├── base.html
│   ├── home.html
│   ├── marketplace.html
│   ├── ai_suite.html
│   ├── predict_crop.html
│   ├── yield_predict.html
│   └── auth/
│       ├── login.html
│       └── register.html
│
├── static/
│   ├── css/                     # Tailwind + custom styles
│   ├── js/                      # Market pulse ticker, cart interactions
│   └── images/                  # Hero & auth banners
│
├── screenshots/                 # ← Commit the 4 PNG screenshots here
│   ├── ss_homepage.png
│   ├── ss_marketplace.png
│   ├── ss_ai_crop.png
│   └── ss_yield.png
│
├── requirements.txt
├── manage.py
└── .env.example
```

---

## 🔐 Environment Variables

Create a `.env` file in the root with these keys:

```env
# Django
SECRET_KEY=your_django_secret_key_here
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
DEFAULT_FROM_EMAIL=noreply@farmdirect.tech
```

---

## 🗺 Roadmap

- [x] Direct marketplace with verified farmer listings
- [x] Cart (Tray) system with add/remove functionality
- [x] AI crop recommendation engine (99.5% accuracy)
- [x] Yield prediction suite (state/season/crop/area inputs)
- [x] Live Market Pulse ticker (500+ mandis)
- [x] Cloudinary image CDN integration
- [x] Secure auth with email password reset
- [x] Post-login dashboard (Control Panel, My Produce)
- [x] Deployed on Render with PostgreSQL
- [ ] Razorpay payment gateway integration
- [ ] Real-time mandi price API (live data feed)
- [ ] Farmer analytics dashboard
- [ ] React Native mobile app
- [ ] Multi-language support (Hindi, Marathi, Tamil)
- [ ] Logistics & delivery tracking

---

## 👨‍💻 Author

<div align="center">

**Rakesh Kumar Mishra**
*Full Stack Developer & AI/ML Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-mishrarakesh--1902-181717?style=for-the-badge&logo=github)](https://github.com/mishrarakesh-1902)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/rakesh-kumar-mishra)
[![Email](https://img.shields.io/badge/Email-mishrarakeshkumar766%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mishrarakeshkumar766@gmail.com)

*B.Tech CSE @ VIT Bhopal University (2023–2027) | CGPA: 8.2*

*🏅 AWS Solutions Architect Associate (SAA-C03) | Oracle Cloud Infrastructure 2025 Certified Developer*

*🏆 Hackathon Finalist — Solvit 2025 | ET AI Concierge | Canara Suraksha (Top 100 / 4,000+ teams)*

</div>

---

<div align="center">

**⭐ If this project helped you or impressed you — drop a star! It means a lot.**

*Built with 💚 to empower India's farming community through technology*

</div>
