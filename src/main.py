from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import os

# -------------------------------------------------------------
# 1. Constants and Model Definitions
# -------------------------------------------------------------
MODEL_PATH = "Traffic_signs_model.keras"
IMAGE_SIZE = (32, 32)
MAX_FILE_SIZE = 5 * 1024 * 1024  # Max file size: 5 MB

# List of traffic sign class names
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

# Model variable is defined globally
model = None

# -------------------------------------------------------------
# 2. FastAPI App Initialization and CORS Settings
# -------------------------------------------------------------
app = FastAPI(
    title="Trafik İşareti Sınıflandırma Servisi",
    description="Bu servis, yüklenen bir trafik işareti görüntüsünü sınıflandırmak için eğitilmiş bir Keras modelini kullanır.",
    version="1.0.0"
)

# CORS configuration: Allows access from all sources
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def load_ml_model():
    """
    Loads the machine learning model when the application starts.
    """
    global model
    try:
        model = load_model(MODEL_PATH)
        print("Machine learning model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")

# -------------------------------------------------------------
# 3. API Endpoints
# -------------------------------------------------------------
@app.get("/", summary="Servis Durum Kontrolü")
async def root():
    """
    Root endpoint to check if the service is running.
    """
    return {"message": "Trafik İşareti Sınıflandırma Servisi Çalışıyor 🚦"}

@app.post("/predict", summary="Trafik İşareti Tahmini Yap")
async def predict(
    file: UploadFile = File(..., description="Sınıflandırılacak trafik işareti resim dosyası.")
):
    """
    Receives an image file, processes it, and returns the predicted traffic sign label.

    - **file**: Image file to be classified (JPG, PNG, etc.).
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model has not been loaded yet or an error occurred during loading.")
        
    try:
        image_bytes = await file.read()

        # File size check
        if len(image_bytes) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=413, 
                detail=f"File size cannot be larger than {MAX_FILE_SIZE / (1024*1024):.0f} MB."
            )

        # Image preprocessing steps
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = image.resize(IMAGE_SIZE)
        image_array = np.array(image).astype("float32") / 255.0
        processed_image = np.expand_dims(image_array, axis=0)

        # Getting prediction from the machine learning model
        predictions = model.predict(processed_image)
        predicted_index = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_index])
        predicted_label = CLASS_NAMES[predicted_index]

        # Successful prediction response
        return JSONResponse(content={
            "status": 200,
            "filename": file.filename,
            "predicted_label": predicted_label,
            "probability": round(confidence, 4)
        })

    except Exception as e:
        # General error handling and returning a 500 response
        raise HTTPException(status_code=500, detail=f"Error during prediction: {e}")

