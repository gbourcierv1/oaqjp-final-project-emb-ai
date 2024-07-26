import requests

# Watson NLP Configuration
WATSON_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {
    "Content-Type": "application/json",
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyze):
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(WATSON_URL, headers=HEADERS, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch emotion data"}
