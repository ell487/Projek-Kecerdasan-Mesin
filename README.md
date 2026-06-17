

---

# 🚀 AI Sentiment Analysis Dashboard with Agentic AI

## 📌 Project Overview

This project is an end-to-end Artificial Intelligence application for sentiment analysis of Indonesian e-commerce product reviews.

The system classifies user reviews into **Positive** or **Negative** sentiment using a Deep Learning LSTM model and provides intelligent recommendations through a Large Language Model (Google Gemini).

The project also implements Agentic AI concepts by combining:

* Deep Learning sentiment prediction
* Vector Memory using ChromaDB
* Generative AI feedback using Gemini
* Analytics Dashboard
* REST API deployment

---

## 🎯 Problem Statement

Online marketplaces receive thousands of customer reviews every day.

Manually analyzing reviews is time-consuming and inefficient.

This project aims to:

* Automatically classify customer sentiment
* Identify positive and negative product trends
* Store customer review memory
* Generate AI-powered seller recommendations
* Provide analytics for business decision making

---

# 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit Dashboard
  │
  ▼
FastAPI Backend
  │
  ├── LSTM Sentiment Model
  │
  ├── ChromaDB Vector Memory
  │
  └── Gemini AI Agent
  │
  ▼
Analytics Dashboard
```

---

# 📂 Project Structure

```text
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
│   └── sentiment_analysis.ipynb
│
├── api
│   ├── app.py
│   ├── gemini_agent.py
│   └── chroma_db.py
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

# 📊 Dataset

Dataset:

**PRDECT-ID Dataset**

Contains Indonesian e-commerce product reviews with sentiment labels.

Example:

| Review                        | Sentiment |
| ----------------------------- | --------- |
| Barang bagus dan original     | Positive  |
| Produk rusak dan mengecewakan | Negative  |

---

# 🔧 Technologies Used

## Programming Language

* Python 3.11+

## Libraries

### Data Engineering

* Pandas
* NumPy
* NLTK

### Traditional Machine Learning

* Scikit-Learn
* TF-IDF
* Multinomial Naive Bayes

### Deep Learning

* TensorFlow
* Keras
* LSTM

### Backend

* FastAPI
* Uvicorn

### Dashboard

* Streamlit

### Agentic AI

* Google Gemini API

### Vector Database

* ChromaDB

---

# 📈 Machine Learning Pipeline

## 1. Data Cleaning

The reviews are preprocessed through:

* Lowercasing
* Tokenization
* Stopword removal
* Text normalization

Example:

```text
Original:
Barangnya bagus banget

Processed:
barang bagus
```

---

## 2. Feature Extraction

Traditional Machine Learning model uses:

```text
TF-IDF Vectorization
```

---

## 3. Traditional Machine Learning

Algorithm:

```text
Multinomial Naive Bayes
```

Purpose:

* Baseline model
* Performance comparison

---

## 4. Deep Learning

Architecture:

```text
Embedding Layer
        ↓
LSTM Layer (128 Units)
        ↓
Dense Layer (64 ReLU)
        ↓
Output Layer (Sigmoid)
```

Loss Function:

```text
Binary Crossentropy
```

Optimizer:

```text
Adam
```

---

# 🤖 Agentic AI Integration

The project extends beyond sentiment classification by integrating a Large Language Model.

Model:

```text
Google Gemini 2.0 Flash
```

Responsibilities:

### Positive Review

Generate suggestions such as:

```text
Customers are satisfied.

Recommendation:
Increase stock availability.
Maintain product quality.
```

### Negative Review

Generate suggestions such as:

```text
Customers reported product damage.

Recommendation:
Improve packaging quality.
Enhance customer support response.
```

---

# 🧠 Vector Memory (ChromaDB)

Every user review is stored in ChromaDB.

Stored Information:

```text
Product Name
Review
Sentiment
Score
```

Benefits:

* Long-term memory
* Review retrieval
* Future RAG implementation
* Agent context enhancement

---

# 🌐 API Endpoints

## Home

```http
GET /
```

Response:

```json
{
  "message":"Sentiment API Running"
}
```

---

## Predict Review

```http
POST /predict
```

Request:

```json
{
  "product":"Laptop",
  "text":"Barang bagus dan cepat"
}
```

Response:

```json
{
  "product":"Laptop",
  "sentiment":"Positive",
  "score":0.95,
  "feedback":"Increase stock availability."
}
```

---

## Analytics

```http
GET /analytics
```

Response:

```json
{
  "total_sentiment":{},
  "top_positive":{},
  "top_negative":{}
}
```

---

# 📊 Dashboard Features

### Sentiment Prediction

Users can:

* Input product name
* Input review
* Predict sentiment

---

### Analytics Dashboard

Displays:

* Total sentiment count
* Top positive products
* Top negative products

---

# 🚀 Installation Guide

## Clone Repository

```bash
git clone https://github.com/ell487/Projek-Kecerdasan-Mesin.git
```

```bash
cd Projek-Kecerdasan-Mesin
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API

Create file:

```text
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run FastAPI

```bash
cd api

python -m uvicorn app:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

## Run Streamlit Dashboard

Open another terminal:

```bash
cd dashboard

streamlit run streamlit_app.py
```

Dashboard:

```text
http://localhost:8501
```

---

# 🧪 Example Prediction

Input:

```text
Product:
Laptop

Review:
Barang bagus dan cepat
```

Output:

```text
Sentiment:
Positive

Score:
0.95

AI Feedback:
Increase stock availability and maintain quality.
```

---

# 📚 Future Improvements

* MySQL Integration
* Retrieval-Augmented Generation (RAG)
* LangChain Agent
* Multi-Class Sentiment Analysis
* Product Recommendation System
* Real-time Dashboard Analytics

