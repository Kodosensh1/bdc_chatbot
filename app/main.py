import os
from dotenv import load_dotenv
import psycopg2

# .env faylını yükləmək
load_dotenv()

# DATABASE_URL-i .env faylından əldə etmək
DATABASE_URL = os.getenv("DATABASE_URL")

# PostgreSQL-ə qoşulma
try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Verilənlər bazasına uğurla qoşuldum!")
except Exception as e:
    print("Verilənlər bazasına qoşularkən xəta baş verdi:", e)

# Bağlantını bağlamaq
finally:
    if conn:
        conn.close()
        print("Verilənlər bazası ilə əlaqə bağlandı.")
