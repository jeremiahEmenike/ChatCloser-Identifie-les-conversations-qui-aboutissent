from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# 1) Charger le pipeline sauvegardé
model_pipeline = joblib.load("chat_classifier.pkl")

# 2) Définir une classe pour le format d'entrée
class ChatRequest(BaseModel):
    messages: list  # liste de messages (strings ou objects)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, your Chat2Sale API is up and running!"}

@app.post("/predict")
def predict_chat(chat_data: ChatRequest):
    """
    Prends en entrée un JSON du type:
    {
      "messages": [
        "Bonsoir, c'est disponible ?",
        "Oui, toujours !"
      ]
    }
    et renvoie la classe prédite: "positive" ou "negative".
    """

    # 1) Concaténer les messages en un seul texte
    all_messages = " ".join(chat_data.messages)

    # 2) Prédire
    prediction = model_pipeline.predict([all_messages])[0]
    
    # 3) Retourner la prédiction
    return {
        "prediction": prediction
    }
