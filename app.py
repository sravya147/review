from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BartTokenizer, BartForConditionalGeneration, pipeline
import nltk

nltk.download('punkt')

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load the BART model and tokenizer
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def summarize_reviews(reviews):
    combined_reviews = ' '.join(reviews)
    
    inputs = tokenizer([combined_reviews], return_tensors='pt', max_length=1024, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=50, num_beams=5, early_stopping=True, no_repeat_ngram_size=2)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    reviews = data.get('reviews', [])
    
    if not reviews:
        return jsonify({"error": "No reviews provided"}), 400
    
    summary = summarize_reviews(reviews)
    
    # Perform sentiment analysis on each review
    sentiments = sentiment_pipeline(reviews)
    
    # Extract keywords using a simple approach (e.g., most frequent words)
    words = ' '.join(reviews).split()
    keywords = list(set(words))
    
    # Return the results as JSON
    return jsonify({
        "keywords": keywords[:10],
        "sentiments": sentiments,
        "summary": summary
    })

if __name__ == '__main__':
    app.run(debug=True)
