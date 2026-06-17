import os
import re
import pickle
import nltk
import pandas as pd
import numpy as np
import tensorflow as tf
from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from gemini_agent import generate_feedback
from chroma_db import save_review


nltk.download('stopwords')
nltk.download('punkt')

app = FastAPI()

model = tf.keras.models.load_model('../model/sentiment_lstm.keras')

with open('../model/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

df_full = pd.read_csv('../dataset/PRDECT-ID Dataset.csv')

stop_words = set(stopwords.words('indonesian'))

class Review(BaseModel):
    product: str
    text: str

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = word_tokenize(text)
    clean_words = [word for word in words if word not in stop_words]
    return ' '.join(clean_words)


@app.get('/')
def home():
    return {'message': 'Sentiment API Running'}


@app.post('/predict')
def predict(review: Review):
    # 1. Preprocessing teks ulasan
    clean = clean_text(review.text)
    seq = tokenizer.texts_to_sequences([clean])
    pad = pad_sequences(seq, maxlen=100)

    # 2. Prediksi Sentimen Menggunakan LSTM
    prediction = model.predict(pad)
    score = float(prediction[0][0])

    if score > 0.5:
        sentiment = 'Positive'
    else:
        sentiment = 'Negative'

    # 3. Simpan Review ke ChromaDB (Vector DB)
    try:
        save_review(review.text, sentiment)
    except Exception as e:
        print(f" Gagal menyimpan data ke ChromaDB: {e}")

    # 4. Ambil Feedback dari Gemini API (Aman dari crash rate-limit)
    feedback = generate_feedback(review.product, review.text, sentiment)

    # 5. Simpan Riwayat ke File CSV
    new_data = pd.DataFrame({
        'product': [review.product],
        'review': [review.text],
        'sentiment': [sentiment],
        'score': [score]
    })

    file_path = '../history/history_review.csv'
    
    # Membuat folder history otomatis jika belum ada di direktori
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    if not os.path.isfile(file_path):
        new_data.to_csv(file_path, index=False)
    else:
        new_data.to_csv(file_path, mode='a', header=False, index=False)
        
    # 6. Response JSON Akhir
    return {
        'product': review.product,
        'review': review.text,
        'sentiment': sentiment,
        'score': score,
        'feedback': feedback
    }


@app.get('/analytics')
def analytics():
    file_path = '../history/history_review.csv'

    # Cek apakah file history sudah ada
    if not os.path.isfile(file_path):
        return {
            'total_sentiment': {},
            'top_positive': {},
            'top_negative': {}
        }

    # Membaca data riwayat CSV
    df_history = pd.read_csv(file_path)

    # Jika file history ternyata kosong
    if df_history.empty:
        return {
            'total_sentiment': {},
            'top_positive': {},
            'top_negative': {}
        }

    # Menghitung total sentimen
    total_sentiment = df_history['sentiment'].value_counts().to_dict()

    # Mendapatkan 5 produk dengan sentimen positif terbanyak
    top_positive = (
        df_history[df_history['sentiment'] == 'Positive']['product']
        .value_counts()
        .head(5)
        .to_dict()
    )

    # Mendapatkan 5 produk dengan sentimen negatif terbanyak
    top_negative = (
        df_history[df_history['sentiment'] == 'Negative']['product']
        .value_counts()
        .head(5)
        .to_dict()
    )

    return {
        'total_sentiment': total_sentiment,
        'top_positive': top_positive,
        'top_negative': top_negative
    }