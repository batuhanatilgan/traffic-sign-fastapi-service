🚦 Trafik İşareti Sınıflandırma Servisi - FastAPI

Bu proje, eğitilmiş bir trafik işareti sınıflandırma modelini FastAPI kullanarak Docker konteynerinde servis eder.
Servis, yüklenen bir trafik işareti görüntüsünü alır ve sınıflandırma sonucunu JSON formatında döner.

🎯 Projenin Amacı

CNN tabanlı model Google Colab üzerinde eğitildi ve Docker üzerinde FastAPI servisi olarak sunuldu.

Servis, bir görüntü alır, modeli kullanarak tahmin yapar ve sonucu JSON formatında döner.

Proje, gerçek dünya uygulamalarında ML modellerinin production ortamına taşınmasını göstermektedir.

🛠 Kullanılan Teknolojiler

Python 3.11

FastAPI

Uvicorn

TensorFlow / Keras

Docker & Docker Compose

Pillow, NumPy

⚙️ Kurulum ve Çalıştırma
1️⃣ Reponun klonlanması
git clone https://github.com/batuhanatilgan/traffic-sign-fastapi-service.git
cd traffic-sign-fastapi-service

2️⃣ Docker imajının oluşturulması
docker-compose build --no-cache

3️⃣ Servisin başlatılması
docker-compose up


Servis şu adreste çalışır:
👉 http://localhost:7001

Swagger UI dokümantasyonu:
👉 http://localhost:7001/docs

🧪 Servisi Test Etme

FastAPI UI üzerinden veya curl ile test edilebilir:

Örnek (cURL):
curl -X POST "http://localhost:7001/predict" -F "file=@test_sign.jpg"

Örnek JSON Çıktısı:
{
  "filename": "test_sign.jpg",
  "prediction": "Hız Limiti (50km/h)",
  "confidence": 0.98
}

📂 Proje Yapısı
traffic-sign-fastapi-service/
│── docker-compose.yml
│── Dockerfile
│── requirements.txt
│── app.py
│── src/
│   ├── pred/
│   │   ├── tf_pred.py
│   │   └── models/
│   │       └── Traffic_signs_model.keras
│── README.md

🌍 English Version
🚦 Traffic Sign Classification - FastAPI Service

This project serves a trained traffic sign classification model using FastAPI inside a Docker container.
The service accepts an uploaded traffic sign image and returns the classification result in JSON format.

🎯 Purpose

A CNN-based model trained in Google Colab is deployed as a FastAPI service inside Docker.

The service takes an image, performs classification using the model, and returns a JSON response.

Demonstrates how to deploy ML models into production environments.

🛠 Technologies

Python 3.11

FastAPI

Uvicorn

TensorFlow / Keras

Docker & Docker Compose

Pillow, NumPy

⚙️ Setup & Run
1️⃣ Clone the repository
git clone https://github.com/batuhanatilgan/traffic-sign-fastapi-service.git
cd traffic-sign-fastapi-service

2️⃣ Build the Docker image
docker-compose build --no-cache

3️⃣ Run the service
docker-compose up


Service runs at:
👉 http://localhost:7001

Swagger UI documentation:
👉 http://localhost:7001/docs

🧪 Testing the Service

Test via FastAPI UI or using curl:

Example (cURL):
curl -X POST "http://localhost:7001/predict" -F "file=@test_sign.jpg"

Example JSON Output:
{
  "filename": "test_sign.jpg",
  "prediction": "Speed Limit (50km/h)",
  "confidence": 0.98
}

📂 Project Structure
traffic-sign-fastapi-service/
│── docker-compose.yml
│── Dockerfile
│── requirements.txt
│── app.py
│── src/
│   ├── pred/
│   │   ├── tf_pred.py
│   │   └── models/
│   │       └── Traffic_signs_model.keras
│── README.md


✍️ Developed by Batuhan Atılgan
📧 Contact: batuhanatilgan54@gmail.com
