import os
import time
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


gemini_model = genai.GenerativeModel("gemini-flash-latest")

def generate_feedback(product, review, sentiment):
    prompt = f"""
    Produk : {product}
    Review : {review}
    Sentiment : {sentiment}

    Jika sentiment positif:
    - dukung review tersebut
    - berikan saran kepada penjual

    Jika sentiment negatif:
    - jelaskan masalah utama
    - berikan solusi kepada penjual
    """
    
    maksimal_percobaan = 3
    for percobaan in range(maksimal_percobaan):
        try:
            # Mencoba request ke Gemini API
            response = gemini_model.generate_content(prompt)
            return response.text
            
        except ResourceExhausted:
         
            print(f"Kuota Gratis Habis! Menunggu 35 detik... (Percobaan {percobaan + 1}/{maksimal_percobaan})")
            time.sleep(35)
            
        except Exception as e:
            
            print(f" Error pada Gemini API: {e}")
            return "Gagal membuat feedback otomatis karena gangguan sistem backend AI."
            
    return "Sistem AI sedang sibuk (Limit harian/menit paket gratis tercapai). Silakan coba beberapa saat lagi."