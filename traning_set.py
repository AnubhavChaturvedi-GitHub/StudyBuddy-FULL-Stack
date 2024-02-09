import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the JSON data
with open(r'F:\J.A.R.V.I.S\DATA\BRAIN_DATA\QNQ_DATA\qna.json') as file:
    data = json.load(file)

# Extract training data
training_data = []
for intent in data.get('intents', []):
    if 'patterns' in intent:
        for pattern in intent['patterns']:
            training_data.append((pattern, intent['tag']))
    else:
        print(f"Warning: 'patterns' key is missing in intent: {intent}")

# Check if training_data is empty
if not training_data:
    print("Error: No training data found.")
else:
    # Prepare features and labels
    X, y = zip(*training_data)

    # Convert text data to numerical format
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X)

    # Train a naive Bayes classifier
    classifier = MultinomialNB()
    classifier.fit(X, y)

    def get_response(user_input):
        # Convert user input to numerical format
        user_input_vectorized = vectorizer.transform([user_input])

        # Predict the intent
        predicted_intent = classifier.predict(user_input_vectorized)[0]

        # Get a random response for the predicted intent
        for intent in data.get('intents', []):
            if intent.get('tag') == predicted_intent:
                responses = intent.get('responses', [])
                if responses:
                    return random.choice(responses)
                else:
                    return "I'm sorry, I don't have a response for that."

    # Example usage



