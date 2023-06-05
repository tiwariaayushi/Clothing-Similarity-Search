The goal of this project is to create a machine learning model capable of receiving text describing a clothing item and returning a ranked list of links to similar items from different websites. The solution is be a function deployed on POSTMAN API that accepts a text string and returns JSON responses with ranked suggestions.

Steps:

1. Collect and preprocess data.
A dataset of clothing item descriptions and their corresponding URLs from multiple e-commerce websites is collected. The dataset used is https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset 
The text data is preprocessed by cleaning it (remove special characters, lowercasing, etc.), and by applying some form of text normalization (like stemming or lemmatization).

2. Measure similarity.
Useful features from the text descriptions are extracted using TF-IDF technique. Similarity between the input text and the texts in the database is computed using
cosine similarity.

3. Return ranked results.
A function is designed that accepts a text string, extracts its features, computes similarities with the items in the database, ranks them based on similarity, and returns the URLs of the top-N most similar items.

4. Deploy the function.
Application is containerized using Docker and the function is deployed on POSTMAN API. The function accepts a JSON payload with the input text and returns a JSON response with the ranked list of similar item URLs.


INSTRUCTIONS FOR DEPLOYMENT - 


