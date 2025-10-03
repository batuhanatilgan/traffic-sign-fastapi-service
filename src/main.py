import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
from tensorflow import keras
from fastapi import FastAPI, File, UploadFile, HTTPException, status
import os


MODEL_PATH = "Traffic_signs_model.keras"
MODEL = None
IMAGE_SIZE = (32, 32) 
MAX_FILE_SIZE = 5 * 1024 * 1024

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


def load_model():
    """Loads the Keras model on application startup."""
    global MODEL
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    
    MODEL = keras.models.load_model(MODEL_PATH) 


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    load_model()

@app.get("/")
def index():
    """Health check endpoint."""
    return {"message": "Image Classification API is running!"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Handles image upload and returns classification prediction."""
    if MODEL is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="Model is not yet loaded."
        )

    image_data = await file.read()
    if len(image_data) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File size cannot exceed {MAX_FILE_SIZE / (1024 * 1024):.0f} MB."
        )

    try:
        image = Image.open(BytesIO(image_data))
        image = image.resize(IMAGE_SIZE)
        image_array = np.array(image)
        
        if image_array.ndim == 2:
            image_array = np.stack((image_array,) * 3, axis=-1)
        
        processed_image = np.expand_dims(image_array, axis=0).astype('float32') / 255.0

        predictions = MODEL.predict(processed_image)
        predicted_class_index = np.argmax(predictions, axis=1)[0]
        confidence = np.max(predictions, axis=1)[0]
        predicted_class_name = CLASS_NAMES[predicted_class_index]
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Error processing image or making prediction: {e}"
        )

    return {
        "prediction": predicted_class_name,
        "confidence": float(confidence),
        "class_index": int(predicted_class_index)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
