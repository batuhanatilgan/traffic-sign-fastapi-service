from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import os

# -------------------------------------------------------------
# 1. Sabitler ve Model Tanımlamaları
# -------------------------------------------------------------
MODEL_PATH = "Traffic_signs_model.keras"
IMAGE_SIZE = (32, 32)
MAX_FILE_SIZE = 5 * 1024 * 1024  # Maksimum dosya boyutu: 5 MB

# Trafik işareti sınıf isimleri listesi
CLASS_NAMES = [
    "Hız Limidi (20km/h)", "Hız Limidi (30km/h)", "Hız Limidi (50km/h)", 
    "Hız Limidi (60km/h)", "Hız Limidi (70km/h)", "Hız Limidi (80km/h)", 
    "Hız Limidi Sonu (80km/h)", "Hız Limidi (100km/h)", "Hız Limidi (120km/h)", 
    "Geçme Yasağı", "3.5 Ton Üstü Geçme Yasağı", "Kavşaklarda Öncelik", 
    "Ana Yol", "Yol Ver", "Dur", "Giriş Yok", "3.5 Ton Üstü Kamyon Girişi Yok", 
    "Genel Yasaklar Sonu", "Dikkat", "Sola Tehlikeli Viraj", "Sağa Tehlikeli Viraj", 
    "Çift Viraj", "Kasisli Yol", "Kaygan Yol", "Yol Daralması (Sağdan)", 
    "Yol Çalışması", "Trafik Lambası", "Yaya Geçidi", "Çocuk Geçidi", 
    "Bisiklet Geçidi", "Buzlanma/Kar", "Vahşi Hayvan Geçidi", "Genel Zorunlu Yön", 
    "Sağa Dönüş Zorunluluğu", "Sola Dönüş Zorunluluğu", "İleri Git Zorunluluğu", 
    "İleri veya Sağa Git", "İleri veya Sola Git", "Sağdan Geçme Zorunluluğu", 
    "Soldan Geçme Zorunluluğu", "Dönel Kavşak", "Geçme Yasağı Sonu", 
    "3.5 Ton Üstü Geçme Yasağı Sonu"
]

# Model değişkeni global olarak tanımlanır
model = None

# -------------------------------------------------------------
# 2. FastAPI Uygulama Başlatma ve CORS Ayarları
# -------------------------------------------------------------
app = FastAPI(title="Trafik İşareti Sınıflandırma Servisi")

# CORS yapılandırması: Tüm kaynaklardan erişime izin verir
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Uygulama başlatıldığında modeli yükleme
@app.on_event("startup")
def load_ml_model():
    global model
    try:
        model = load_model(MODEL_PATH)
        print("Makine öğrenimi modeli başarıyla yüklendi.")
    except Exception as e:
        print(f"Model yüklenirken hata oluştu: {e}")
        # Hata durumunda uygulama başlatılmadan sonlandırılabilir
        # raise RuntimeError("Model yüklenemedi.")

# 3. API Uç Noktaları

# Kök Uç Noktası (Root Endpoint)
@app.get("/")
async def root():
    return {"message": "Trafik İşareti Sınıflandırma Servisi Çalışıyor 🚦"}

# Tahmin Uç Noktası (Prediction Endpoint)
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if model is None:
        raise HTTPException(status_code=503, detail="Model henüz yüklenmedi veya yüklenirken hata oluştu.")
        
    try:
        image_bytes = await file.read()

        # Dosya boyutu kontrolü
        if len(image_bytes) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=413, 
                detail=f"Dosya boyutu {MAX_FILE_SIZE / (1024*1024):.0f} MB'dan büyük olamaz."
            )

        # Görüntü ön işleme adımları
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = image.resize(IMAGE_SIZE)
        image_array = np.array(image).astype("float32") / 255.0
        processed_image = np.expand_dims(image_array, axis=0)

        # Makine öğrenimi modelinden tahmin alma
        predictions = model.predict(processed_image)
        predicted_index = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_index])
        predicted_label = CLASS_NAMES[predicted_index]

        # Başarılı tahmin yanıtı
        return JSONResponse(content={
            "status": 200,
            "filename": file.filename,
            "predicted_label": predicted_label,
            "probability": round(confidence, 4)
        })

    except Exception as e:
        # Genel hata yakalama ve 500 yanıtı döndürme
        raise HTTPException(status_code=500, detail=f"Tahmin sırasında hata: {e}")