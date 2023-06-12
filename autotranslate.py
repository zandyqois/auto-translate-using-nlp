import nltk
from googletrans import Translator

# Download data pendukung NLTK jika belum ada
nltk.download('punkt')

# Fungsi untuk mendeteksi bahasa
def detect_language(text):
    return Translator().detect(text).lang

# Fungsi untuk menerjemahkan teks ke bahasa Jepang
def translate_to_japanese(text):
    return Translator().translate(text, dest='ja').text

# Membaca input dari pengguna
input_text = input("Masukkan teks dalam bahasa apapun: ")

# Mendeteksi bahasa
detected_language = detect_language(input_text)
print("Bahasa yang terdeteksi:", detected_language)

# Menerjemahkan teks ke bahasa Jepang
translated_text = translate_to_japanese(input_text)
print("Hasil terjemahan ke bahasa Jepang:", translated_text)
