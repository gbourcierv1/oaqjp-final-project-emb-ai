from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='World')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    watson_response = emotion_detector(text)
    if "error" not in watson_response:
        emotions = watson_response.get('emotion_predictions', [{}])[0].get('emotion', {})
        analyzed_text = watson_response.get('text', '')
    else:
        emotions = {}
        analyzed_text = text
    return render_template('result.html', text=analyzed_text, emotions=emotions)

if __name__ == '__main__':
    app.run(debug=True)
