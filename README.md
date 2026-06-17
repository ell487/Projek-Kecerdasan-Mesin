
# AI Sentiment Analysis with LSTM, FastAPI, Streamlit, ChromaDB, and Gemini

## Deskripsi Proyek

Project ini merupakan sistem analisis sentimen ulasan produk berbahasa Indonesia menggunakan Deep Learning (LSTM). Sistem dapat memprediksi sentimen suatu review, menyimpan riwayat prediksi, melakukan analytics sederhana, menyimpan memori menggunakan ChromaDB, dan memberikan feedback otomatis menggunakan Gemini LLM.

---

# Fitur

* Prediksi sentimen review produk
* Model Deep Learning LSTM
* Dashboard Streamlit
* REST API menggunakan FastAPI
* History prediksi tersimpan ke CSV
* Analytics Dashboard
* Vector Database menggunakan ChromaDB
* Agentic AI menggunakan Gemini
* Feedback otomatis untuk penjual berdasarkan review pelanggan

---

# Struktur Folder

```
Tubes_KecerdasanMesin_SentimenProjek
│
├── dataset
│   └── PRDECT-ID Dataset.csv
│
├── model
│   ├── sentiment_lstm.keras
│   └── tokenizer.pkl
│
├── history
│   └── history_review.csv
│
├── notebook
│   └── sentiment_training.ipynb
│
├── api
│   ├── app.py
│   ├── gemini_agent.py
│   ├── chroma_db.py
│   └── .env
│
├── dashboard
│   └── streamlit_app.py
│
├── vector_db
│   └── chroma
│
├── requirements.txt
│
└── README.md
```

---

# Dataset

Dataset yang digunakan:

```
PRDECT-ID Dataset.csv
```

Kolom utama:

* Product Name
* Customer Review
* Sentiment

---

# Instalasi

Clone repository

```bash
git clone https://github.com/username/Projek-Kecerdasan-Mesin.git
```

Masuk ke folder project

```bash
cd Projek-Kecerdasan-Mesin
```

---

# Install Library

```bash
pip install -r requirements.txt
```

atau

```bash
pip install tensorflow pandas numpy matplotlib seaborn scikit-learn nltk fastapi uvicorn streamlit chromadb google-generativeai python-dotenv
```

//note:python-dotenv tidak di file requirements.txt

---

# Training Model

Masuk ke folder notebook

```
notebook/sentiment_training.ipynb
```

Jalankan seluruh cell.

Output yang dihasilkan:

```
model/sentiment_lstm.keras
model/tokenizer.pkl
```

---

# Menambahkan API Key Gemini

Buat file:

```
api/.env
```

Isi:

```env
GEMINI_API_KEY=ISI_API_KEY_ANDA
```

Contoh:

```env
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxx
```

---

# Menjalankan FastAPI

Masuk ke folder api

```bash
cd api
```

Jalankan server

```bash
python -m uvicorn app:app --reload
```

Jika berhasil akan muncul

```
Uvicorn running on http://127.0.0.1:8000
```

---

# Testing API

Buka browser

```
http://127.0.0.1:8000/docs
```

Endpoint yang tersedia:

### GET /

Menampilkan status API.

### POST /predict

Contoh request:

```json
{
  "product": "Laptop",
  "text": "Barang bagus dan original"
}
```

Contoh response:

```json
{
  "product": "Laptop",
  "review": "Barang bagus dan original",
  "sentiment": "Positive",
  "score": 0.95,
  "feedback": "Pelanggan puas terhadap produk. Penjual disarankan menambah stok."
}
```

### GET /analytics

Menampilkan:

* Total sentiment
* Top positive product
* Top negative product

---

# Menjalankan Streamlit Dashboard

Masuk ke folder dashboard

```bash
cd dashboard
```

Jalankan:

```bash
streamlit run streamlit_app.py
```

Dashboard akan berjalan di:

```
http://localhost:8501
```

---

# Cara Menggunakan

1. Masukkan nama produk.

Contoh:

```
Laptop
```

2. Masukkan review.

Contoh:

```
Barang bagus dan original
```

3. Klik tombol Predict.

4. Sistem akan menampilkan:

* Sentiment
* Score
* Product
* Feedback dari Gemini

5. Data otomatis tersimpan ke:

```
history/history_review.csv
```

6. Data review juga disimpan pada ChromaDB sebagai vector memory.

---

# ChromaDB

Lokasi database vector:

```
vector_db/chroma
```

Fungsi:

* Menyimpan review sebelumnya.
* Sebagai memory untuk Agentic AI.
* Memungkinkan retrieval review lama.

---

# Analytics Dashboard

Menampilkan:

### Total Sentiment

Jumlah Positive dan Negative.

### Top Positive Product

Produk dengan review positif terbanyak.

### Top Negative Product

Produk dengan review negatif terbanyak.

---

# Machine Learning

## Traditional Machine Learning

Model:

```
Multinomial Naive Bayes
```

Feature Extraction:

```
TF-IDF Vectorizer
```

Evaluasi:

* Accuracy
* Classification Report
* Confusion Matrix

---

## Deep Learning

Model:

```
Embedding
↓
LSTM
↓
Dense(64)
↓
Dense(1,sigmoid)
```

Optimizer:

```
Adam
```

Loss Function:

```
Binary Crossentropy
```

Epoch:

```
10
```

---

# Agentic AI

Model LLM:

```
Gemini 2.0 Flash
```

Tugas agent:

### Jika review positif

* Mendukung review pelanggan.
* Memberikan saran kepada penjual.
* Menyarankan menambah stok.

### Jika review negatif

* Menjelaskan masalah utama.
* Memberikan solusi kepada penjual.
* Memberikan rekomendasi perbaikan layanan.

---

# Tools dan Library

* Python
* TensorFlow
* Keras
* Pandas
* NumPy
* Scikit-Learn
* NLTK
* FastAPI
* Streamlit
* ChromaDB
* Google Gemini
* Matplotlib
* Seaborn

---

