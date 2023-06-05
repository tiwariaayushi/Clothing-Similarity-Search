from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/find_similar_items', methods=['POST'])
def find_similar_items():
    # Load preprocessed CSV file into a pandas DataFrame
    data = pd.read_csv('preprocessed_data.csv')

    # Fill missing values with an empty string
    data['cleaned_text'].fillna('', inplace=True)

    # Extract features using TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    text_features = vectorizer.fit_transform(data['cleaned_text'])

    # Get the input text from the JSON payload
    input_text = request.json['input_text']

    # Compute similarity between input text and texts in the database
    input_vector = vectorizer.transform([input_text])
    similarity_scores = cosine_similarity(input_vector, text_features)
    similarity_scores = similarity_scores.flatten()

    # Get the number of top-N similar items from the JSON payload
    n = request.json['n']

    # Find top-N similar items
    top_n_indices = similarity_scores.argsort()[-n:][::-1]
    similar_items = data.loc[top_n_indices, 'link']

    # Create a JSON response with the ranked list of similar item URLs
    response = {'similar_items': similar_items.tolist()}

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
