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
