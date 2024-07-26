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
        emotions = response.json().get('emotion_predictions', [{}])[0].get('emotion', {})
        if emotions:
            emotion_scores = {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant_emotion'] = dominant_emotion
            return emotion_scores
        else:
            return {"error": "No emotion data found"}
    else:
        return {"error": "Unable to fetch emotion data"}
