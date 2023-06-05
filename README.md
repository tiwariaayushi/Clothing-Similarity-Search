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

A. Using POSTMAN 

1. Save the similarity_app file in your repository.
2. Build the Docker image using the following command : docker build -t similarity-app .
3. Run the Docker container locally using the following command : docker run -p 8080:5000 similarity-app
4. Open POSTMAN website and create a new POST request with the following URL: http://localhost:8080/find_similar_items. Download the POSTMAN's Desktop Agent for running the POSTMAN. Set the request's Content-Type to application/json. In the request body, provide a JSON payload with the input text and the desired number of similar items. 
{
  "input_text": "Your input text goes here.",
  "n": 5
}
Send the request, and you will receive a JSON response with the ranked list of similar item URLs.


B. Using Google Cloud 

 To containerize the application using Docker and deploy it on Google Cloud Functions or Google Cloud Run, follow these steps:
 
1. Set up your environment:

Install Docker: Visit the Docker website (https://www.docker.com/) and follow the instructions to install Docker on your machine.
Install the Google Cloud SDK: Follow the instructions provided by Google Cloud (https://cloud.google.com/sdk/docs/install) to install the Google Cloud SDK.

2. Save the similarity_app file in your repository. 

3. Deploy to Google Cloud Functions or Google Cloud Run:
Choose either Google Cloud Functions or Google Cloud Run based on your preference and requirements.
a. Google Cloud Functions:
Deploy the Docker container as a Google Cloud Function by following the instructions in the Google Cloud Functions documentation (https://cloud.google.com/functions/docs/deploying/docker).
b. Google Cloud Run:
Deploy the Docker container to Google Cloud Run by following the instructions in the Google Cloud Run documentation (https://cloud.google.com/run/docs/deploying).
When deploying to either Google Cloud Functions or Google Cloud Run, make sure to specify the correct entrypoint and port (8080) for your application.


