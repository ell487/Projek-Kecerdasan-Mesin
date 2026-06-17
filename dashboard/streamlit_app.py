import streamlit as st
import requests
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="SentimenAI - Dashboard Kecerdasan Mesin",
    layout="wide"
)

API_BASE_URL = 'http://127.0.0.1:8000'

st.markdown("""
<style>
    .main-title {
        font-size: 2.8rem !important;
        font-weight: 800;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #6B7280;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
    }
</style>
""", unsafe_allow_html=True)

# Header Utama Aplikasi
st.markdown('<p class="main-title"> AI Sentiment & Analytics Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Projek Aplikasi Kecerdasan Mesin — Integrasi Model LSTM & LLM Feedback</p>', unsafe_allow_html=True)


tab_predict, tab_analytics = st.tabs(["Predict Review", " Analytics Dashboard"])


with tab_predict:
    st.markdown("### Analisis Sentimen Ulasan")
    
    # Membagi layout menjadi 2 kolom (Kiri input, Kanan hasil)
    col_input, col_result = st.columns([1, 1.2], gap="large")
    
    with col_input:
        st.info(" **Petunjuk:** Masukkan nama produk dan teks ulasan pelanggan untuk menguji prediksi model LSTM.")
        
        # Menggunakan Form agar input lebih rapi
        with st.form("sentiment_form"):
            product = st.text_input('Nama Produk', placeholder="Contoh: AirPods Pro")
            review = st.text_area('Input Review', placeholder="Contoh: Barangnya bagus banget, suara jernih bass mantap!", height=150)
            submit_button = st.form_submit_button('Analyze Sentiment ')

    with col_result:
        if submit_button:
            if not product or not review:
                st.warning(" Nama Produk dan Teks Review wajib diisi!")
            else:
                payload = {
                    'product': product,
                    'text': review
                }
                
                with st.spinner('Memproses text preprocessing & inferensi model...'):
                    try:
                        response = requests.post(f'{API_BASE_URL}/predict', json=payload)
                        
                        if response.status_code == 200:
                            result = response.json()
                            sentiment = result['sentiment']
                            score = result['score']
                            feedback = result['feedback']
                            
                            st.markdown("Hasil Prediksi")
                            
                            # Tampilan Metrik Score
                            col_sentiment, col_score = st.columns(2)
                            with col_sentiment:
                                if sentiment == 'Positive':
                                    st.success(f"### Sentimen: **{sentiment}** ")
                                else:
                                    st.error(f"### Sentimen: **{sentiment}** ")
                            with col_score:
                                st.metric(label="LSTM Confidence Score", value=f"{score:.4f}")
                            
                            st.markdown("---")
                            
                            # Tampilan AI Feedback (Gemini)
                            st.markdown("AI Smart Feedback (Saran untuk Penjual)")
                            st.info(feedback)
                            
                        else:
                            st.error(f" Predict API Error (Status Code: {response.status_code})")
                    except Exception as e:
                        st.error(f" Gagal terhubung ke server backend: {e}")
        else:
            st.write("Menunggu Input")
            st.caption("Silakan isi form di sebelah kiri dan klik tombol **Analyze Sentiment** untuk melihat hasil analisis kecerdasan mesin.")


with tab_analytics:
    st.markdown("### Statistik & Performa Produk")
    
    try:
        analytics = requests.get(f'{API_BASE_URL}/analytics')
        
        if analytics.status_code == 200:
            data = analytics.json()
            total_sentiment_dict = data.get('total_sentiment', {})
            
            if not total_sentiment_dict:
                st.warning("Belum ada riwayat data ulasan di database harian.")
            else:
                # 1. Section Ringkasan Metrik Atas
                pos_total = total_sentiment_dict.get('Positive', 0)
                neg_total = total_sentiment_dict.get('Negative', 0)
                grand_total = pos_total + neg_total
                
                col_m1, col_m2, col_m3 = st.columns(3)
                with col_m1:
                    st.markdown(f"<div class='metric-card'><h5>Total Data Riwayat</h5><h2>{grand_total} Ulasan</h2></div>", unsafe_allow_html=True)
                with col_m2:
                    st.markdown(f"<div class='metric-card' style='border-left-color: #10B981;'><h5>Total Sentimen Positif</h5><h2>{pos_total} </h2></div>", unsafe_allow_html=True)
                with col_m3:
                    st.markdown(f"<div class='metric-card' style='border-left-color: #EF4444;'><h5>Total Sentimen Negatif</h5><h2>{neg_total} </h2></div>", unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # 2. Section Visualisasi Grafik (Plotly Express)
                col_chart1, col_chart2 = st.columns(2)
                
                with col_chart1:
                    st.markdown("Top 5 Produk Sentimen Positif")
                    if data['top_positive']:
                        positive_df = pd.DataFrame(list(data['top_positive'].items()), columns=['Product', 'Total'])
                        fig_pos = px.bar(positive_df, x='Total', y='Product', orientation='h', 
                                         color_discrete_sequence=['#10B981'], text='Total')
                        fig_pos.update_layout(yaxis={'categoryorder':'total ascending'}, height=300, margin=dict(l=0, r=0, t=10, b=0))
                        st.plotly_chart(fig_pos, use_container_width=True)
                    else:
                        st.caption("Belum ada data produk ber-sentimen positif.")
                        
                with col_chart2:
                    st.markdown(" Top 5 Produk Sentimen Negatif")
                    if data['top_negative']:
                        negative_df = pd.DataFrame(list(data['top_negative'].items()), columns=['Product', 'Total'])
                        fig_neg = px.bar(negative_df, x='Total', y='Product', orientation='h', 
                                         color_discrete_sequence=['#EF4444'], text='Total')
                        fig_neg.update_layout(yaxis={'categoryorder':'total ascending'}, height=300, margin=dict(l=0, r=0, t=10, b=0))
                        st.plotly_chart(fig_neg, use_container_width=True)
                    else:
                        st.caption("Belum ada data produk ber-sentimen negatif.")
                
                # 3. Section Tabel Detail (Expander)
                st.markdown("<br>", unsafe_allow_html=True)
                with st.expander("Lihat Detail Tabel Data Mentah"):
                    st.subheader('Total Sentimen Keseluruhan')
                    sentiment_df = pd.DataFrame(list(total_sentiment_dict.items()), columns=['Sentiment', 'Total'])
                    st.dataframe(sentiment_df, use_container_width=True)
        else:
            st.error(f" Analytics API Error (Status Code: {analytics.status_code})")
            
    except Exception as e:
        st.error(f"Gagal mengambil data analitik dari server backend: {e}")