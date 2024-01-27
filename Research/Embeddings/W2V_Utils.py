import os
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Function to read text files from a directory
def read_files(directory):
    documents = []
    stop_words = set(stopwords.words('english'))
    try:
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                text = file.read().lower()
                # Tokenize the text
                words = word_tokenize(text)
                # Remove stopwords and single-character tokens
                words = [word for word in words if word not in stop_words and len(word) > 1]
                # Remove non-alphanumeric characters
                words = [re.sub(r'[^a-zA-Z0-9]', '', word) for word in words]
                documents.append(words)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return documents