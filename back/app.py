from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
CORS(app)

# Load the model
model = joblib.load('spam_model.pkl')

# Load the vectorizer
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def index():
    return 'Spam Email Classifier'

@app.route('/classify', methods=['POST'])
def classify_email():
    data = request.get_json()
    email_text = data['email']
    
    # Feature extraction
    email_features = tfidf_vectorizer.transform([email_text])
    
    # Prediction
    prediction = model.predict(email_features)
    
    # Return the result
    return jsonify({'result': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
