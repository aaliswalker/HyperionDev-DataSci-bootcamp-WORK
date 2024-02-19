import spacy
import pandas as pd
from textblob import TextBlob

nlp = spacy.load('en_core_web_sm')

# Load data
print("----- LOAD DATA -----")
print("")
filepath = "C:\\Users\\User\\Dropbox\\PI23110010635\\Data Science (Fundamentals)\\T21 - Capstone Project - NLP Applications\\amazon_product_reviews.csv.csv"

dataframe = pd.read_csv(filepath)
print(dataframe)

print(" ")
print("----- PREPROCESSING -----")
print(" ")

# Define a function to clean text
def clean_text(text):
    # Process the text with spaCy
    doc = nlp(text)
    # Filter out stop words, strip whitespace, and convert to lowercase
    cleaned_tokens = [token.text.strip().lower() for token in doc if not token.is_stop]
    # Join the cleaned tokens back into a single string
    cleaned_text = ' '.join(cleaned_tokens)
    return cleaned_text

# Remove missing values and clean the reviews
clean_data = dataframe.dropna(subset=['reviews.text'])
clean_data['cleaned_reviews'] = clean_data['reviews.text'].apply(clean_text)
cleaned_reviews = clean_data['cleaned_reviews']
print(cleaned_reviews)

def sentiment_analysis(review): 
    blob = TextBlob(review)
    sentiment = blob.sentiment 
    print(f"{review}: {sentiment}")

def test_model():
    # Test the sentiment analysis model on sample product reviews
    print(" ")
    sample_reviews = [
        "This product is amazing!",
        "The quality of this product is poor.",
        "I'm satisfied with my purchase.",
        "This product exceeded my expectations."
    ]
    for review in sample_reviews:
        sentiment_analysis(review) 

def product_review(): 
    print("")
    review = input("Type in a review: ")
    sentiment_analysis(review)

# Test the sentiment analysis function on sample reviews
test_model()

# Prompt user for a review input
product_review()

# Random reviews from database 
review1_doc = nlp(cleaned_reviews[44])
review2_doc = nlp(cleaned_reviews[88])

# Calculate similarity 
similarity = review1_doc.similarity(review2_doc)
print(f"The similarity between '{cleaned_reviews[44]}' and '{cleaned_reviews[88]}' is: {similarity}")
