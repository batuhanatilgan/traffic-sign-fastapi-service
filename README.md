<<<<<<< HEAD
🚦 Traffic Sign Classification API with FastAPI & Docker
📌 Project Overview

This project demonstrates how to serve a trained traffic sign classification model using FastAPI inside a Docker container.
The API allows uploading an image of a traffic sign and returns the predicted class in JSON format.

🛠️ Tech Stack

Python 3.11

FastAPI

TensorFlow / Keras

Docker & Docker Compose

Uvicorn

🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/batuhanatilgan/traffic-sign-fastapi-service.git
cd traffic-sign-fastapi-service

2. Build the Docker Image
docker-compose build --no-cache

3. Run the Container
docker-compose up

4. Access the API

The API will be running at:
👉 http://localhost:7001

Swagger UI documentation:
👉 http://localhost:7001/docs

📷 Example Request
cURL Example
curl -X POST "http://localhost:7001/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test_sign.jpg"

Example JSON Response
{
  "prediction": "Speed Limit (50km/h)"
}

📂 Repository Structure
traffic-sign-fastapi-service/
│-- src/
│   ├── app/               # FastAPI application
│   ├── pred/              # Model loading & prediction logic
│   └── schemas/           # Pydantic schemas
│-- Dockerfile
│-- docker-compose.yml
│-- requirements.txt
│-- README.md

🧑‍💻 Author

👤 Batuhan Atılgan

GitHub: batuhanatilgan
Trafik İşareti Sınıflandırma API (FastAPI & Docker)
📌 Proje Özeti

Bu proje, eğitilmiş bir trafik işareti sınıflandırma modelinin FastAPI ve Docker kullanılarak nasıl servis edilebileceğini göstermektedir.
API’ye bir trafik işareti görseli yüklenir ve tahmin sonucu JSON formatında döner.

🛠️ Kullanılan Teknolojiler

Python 3.11

FastAPI

TensorFlow / Keras

Docker & Docker Compose

Uvicorn

🚀 Projeyi Çalıştırma
1. Repoyu Klonla
git clone https://github.com/batuhanatilgan/traffic-sign-fastapi-service.git
cd traffic-sign-fastapi-service

2. Docker İmajını Oluştur
docker-compose build --no-cache

3. Container’ı Başlat
docker-compose up

4. API’ye Erişim

API şu adreste çalışır:
👉 http://localhost:7001

Swagger UI dokümantasyonu:
👉 http://localhost:7001/docs

📷 Örnek İstek
cURL Örneği
curl -X POST "http://localhost:7001/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test_sign.jpg"

Örnek JSON Yanıtı
{
  "prediction": "Hız Sınırı (50km/h)"
}

📂 Repo Yapısı
traffic-sign-fastapi-service/
│-- src/
│   ├── app/               # FastAPI uygulaması
│   ├── pred/              # Model yükleme & tahmin işlemleri
│   └── schemas/           # Pydantic şemaları
│-- Dockerfile
│-- docker-compose.yml
│-- requirements.txt
│-- README.md

🧑‍💻 Yazar

👤 Batuhan Atılgan

GitHub: batuhanatilgan
=======
# 🚦 Traffic Sign Classification - FastAPI Service

Bu proje, **trafik işaretlerini sınıflandırmak için eğitilmiş bir derin öğrenme modelini** FastAPI kullanarak Docker konteyner üzerinde servis etmektedir.  
Servis, yüklenen bir trafik işareti görüntüsünü sınıflandırır ve sonucu **JSON formatında** döner.  

---

## 📖 İçindekiler
- [Projenin Amacı](#projenin-amacı)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
- [Servisi Test Etme](#servisi-test-etme)
- [Proje Yapısı](#proje-yapısı)
- [English Version](#english-version)

---

## 🎯 Projenin Amacı
- Google Colab üzerinde eğitilen CNN tabanlı model, Docker üzerinde FastAPI servisi olarak sunulmaktadır.
- Servis, bir görüntü alır, modeli kullanarak sınıflandırma yapar ve sonucu JSON formatında döner.
- Proje, gerçek dünya uygulamalarında **ML modellerinin nasıl production ortamına alınabileceğini** göstermektedir.

---

## 🛠 Kullanılan Teknolojiler
- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **TensorFlow / PyTorch**
- **Docker & Docker Compose**
- **Pillow, NumPy**

---

## ⚙️ Kurulum ve Çalıştırma

### 1️⃣ Reponun klonlanması
```bash
git clone https://github.com/batuhanatilgan/traffic-sign-fastapi-service.git
cd traffic-sign-fastapi-service
```

### 2️⃣ Docker imajının build edilmesi
```bash
docker-compose build
```

### 3️⃣ Servisin başlatılması
```bash
docker-compose up
```

Servis şu adreste çalışır:  
👉 [http://localhost:7001/docs](http://localhost:7001/docs)

---

## 🧪 Servisi Test Etme
FastAPI arayüzünden veya `curl` komutu ile test edebilirsiniz.

### Örnek (cURL ile):
```bash
curl -X POST "http://localhost:7001/predict/tf/" -F "file=@sample_sign.jpg"
```

### Örnek JSON çıktısı:
```json
{
  "filename": "sample_sign.jpg",
  "prediction": "Stop Sign",
  "confidence": 0.98
}
```

---

## 📂 Proje Yapısı
```
traffic-sign-fastapi-service/
│── docker-compose.yml
│── Dockerfile
│── requirements.txt
│── app.py
│── src/
│   ├── pred/
│   │   ├── tf_pred.py
│   │   └── models/
│   │       └── GTSRB_model.h5
│── README.md
```

---

# 🌍 English Version

## 🚦 Traffic Sign Classification - FastAPI Service

This project serves a **deep learning model trained for traffic sign classification** using FastAPI inside a Docker container.  
The service accepts an uploaded traffic sign image and returns the classification result in **JSON format**.

---

## 🎯 Purpose
- A CNN-based model trained in Google Colab is deployed as a FastAPI service inside Docker.
- The service takes an image, performs classification, and returns a JSON response.
- Demonstrates how to **deploy ML models into production environments**.

---

## 🛠 Technologies
- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **TensorFlow / PyTorch**
- **Docker & Docker Compose**
- **Pillow, NumPy**

---

## ⚙️ Setup & Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/batuhanatilgan/traffic-sign-fastapi-service.git
cd traffic-sign-fastapi-service
```

### 2️⃣ Build the Docker image
```bash
docker-compose build
```

### 3️⃣ Run the service
```bash
docker-compose up
```

Service runs at:  
👉 [http://localhost:7001/docs](http://localhost:7001/docs)

---

## 🧪 Testing the Service
You can test via FastAPI UI or using `curl`.

### Example (with cURL):
```bash
curl -X POST "http://localhost:7001/predict/tf/" -F "file=@sample_sign.jpg"
```

### Example JSON Output:
```json
{
  "filename": "sample_sign.jpg",
  "prediction": "Stop Sign",
  "confidence": 0.98
}
```

---

## 📂 Project Structure
```
traffic-sign-fastapi-service/
│── docker-compose.yml
│── Dockerfile
│── requirements.txt
│── app.py
│── src/
│   ├── pred/
│   │   ├── tf_pred.py
│   │   └── models/
│   │       └── GTSRB_model.h5
│── README.md
```

---

✍️ Developed by **Batuhan Atılgan**  
📧 Contact: staj@diginova.com.tr
>>>>>>> 04c2e68 (Update: merged into app.py,removed main.py, updated configs)
