Trafik İşareti Sınıflandırma Servisi (FastAPI & Docker)
Bu proje, bir Keras/TensorFlow modeli kullanılarak eğitilmiş Trafik İşareti Sınıflandırma Modelini (GTSRB) bir Docker konteyneri içinde FastAPI mikro servisi olarak çalıştırmayı amaçlamaktadır.

Proje yapısı, staj görevi gereksinimlerine uygun olarak ashmibanerjee/img-classifier-fastapi referans deposunun minimalist mimarisi temel alınarak oluşturulmuştur. Depo, çıkarım (inference) için gerekli olan 5 temel bileşeni içermektedir.

🚀 Kurulum ve Çalıştırma
Projenin yerel olarak başlatılması ve test edilmesi Docker ve Docker Compose ile çok kolaydır.

Depoyu Klonlayın:

git clone [https://github.com/batuhanatilgan/traffic-sign-fastapi-service](https://github.com/batuhanatilgan/traffic-sign-fastapi-service)
cd traffic-sign-fastapi-service

Servisi Başlatın:
Modeli içeren Docker imajını oluşturur ve servisi http://localhost:7001 adresinde başlatır.

docker-compose up --build

🛠️ Servis Kullanımı
Servis başarıyla başladıktan sonra aşağıdaki endpoint'ler üzerinden kullanılabilir:

Endpoint

Amaç

Yöntem

/

Sağlık kontrolü (Health Check)

GET

/predict

Görüntü yükleme ve sınıflandırma

POST

/docs

Swagger UI ile interaktif test

GET

Test Adresi: http://localhost:7001/docs

English Documentation
🚦 Traffic Sign Classification Service (FastAPI & Docker)
This project aims to deploy a pre-trained Keras/TensorFlow Traffic Sign Classification Model (GTSRB) as a FastAPI microservice running inside a Docker container.

The project structure is built upon the minimalist architecture of the required reference repository (ashmibanerjee/img-classifier-fastapi) to meet the internship assignment's compliance requirements. The repository contains only the 5 core components necessary for model inference.

🚀 Setup and Execution
Starting and testing the project locally is straightforward using Docker and Docker Compose.

Clone the Repository:

git clone [https://github.com/batuhanatilgan/traffic-sign-fastapi-service](https://github.com/batuhanatilgan/traffic-sign-fastapi-service)
cd traffic-sign-fastapi-service

Start the Service:
This command builds the Docker image containing the model and starts the service on http://localhost:7001.

docker-compose up --build

🛠️ Service Usage
Once the service is successfully running, it can be accessed using the following endpoints:

Endpoint

Purpose

Method

/

Health Check

GET

/predict

Image upload and classification

POST

/docs

Interactive testing with Swagger UI

GET

Testing URL: http://localhost:7001/docs
