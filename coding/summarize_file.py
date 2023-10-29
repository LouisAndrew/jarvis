# filename: summarize_file.py

import os
import re
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    text = [i for i in tokens if not i in stop_words]
    return text

def summarize_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            text = file.read().replace('\n', '')
        words = preprocess(text)
        word_frequencies = Counter(words)
        most_common_words = [word for word, count in word_frequencies.most_common(10)]
        sentences = sent_tokenize(text)
        summary_sentences = [sentence for sentence in sentences if any(word in sentence for word in most_common_words)]
        summary = ' '.join(summary_sentences)
        return summary
    else:
        return "File path does not exist."

file_path = './output.txt'
summary = summarize_file(file_path)
print("Summary:\n")
print(summary)