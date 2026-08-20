"""
app.py - Customer Churn Detector Dashboard (Sesi 15 - Mini Project).

Prediksi apakah seorang pelanggan berpotensi churn (berhenti berlangganan),
memakai model Decision Tree yang dilatih di Sesi 10, dengan riwayat
prediksi disimpan ke SQLite (Sesi 6) dan ditampilkan lewat Streamlit
(Sesi 14).

Jalankan dengan:
    streamlit run app.py
"""
import sqlite3

import joblib
import pandas as pd
import streamlit as st
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

st.title("Customer Churn Detector Dashboard")
st.write("Prediksi apakah seorang pelanggan berpotensi churn (berhenti berlangganan), berdasarkan model yang sudah dilatih di Sesi 10.")

# Load model dan encoder dari churn_model.pkl - sama persis dipakai di
# churn-prediction-app (Sesi 14).
bundle = joblib.load("churn_model.pkl")
model = bundle["model"]
encoders = bundle["encoders"]
feature_cols = bundle["feature_cols"]
cat_cols = bundle["cat_cols"]

DB_PATH = "riwayat_churn.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS prediksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenure_bulan INTEGER,
            contract TEXT,
            monthly_charges REAL,
            hasil TEXT
        )
        """
    )
    conn.commit()
    conn.close()


init_db()

st.write("### Form Prediksi")
with st.form("form_prediksi"):
    tenure = st.number_input("Lama Berlangganan (bulan)", min_value=0, max_value=100, value=12)
    monthly = st.slider("Monthly Charges", 0, 200, 70)
    total = st.number_input("Total Charges", min_value=0.0, value=800.0)
    senior = st.selectbox("Senior Citizen?", ["Tidak", "Ya"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    contract = st.selectbox("Jenis Kontrak", ["Month-to-month", "One year", "Two year"])
    payment = st.selectbox(
        "Metode Pembayaran",
        ["Bank transfer", "Credit card", "Electronic check", "Mailed check"],
    )
    submit = st.form_submit_button("Prediksi")

if submit:
    row = {
        "senior_citizen": 1 if senior == "Ya" else 0,
        "tenure_bulan": tenure,
        "internet_service": internet,
        "contract": contract,
        "payment_method": payment,
        "monthly_charges": monthly,
        "total_charges": total,
    }

    # Encode kolom kategorikal jadi angka pakai encoder yang sama dipakai
    # saat training, lalu panggil model.predict().
    for col in cat_cols:
        row[col] = encoders[col].transform([row[col]])[0]
    X = pd.DataFrame([row])[feature_cols]
    hasil = model.predict(X)[0]
    hasil_text = "Churn" if hasil == 1 else "Tidak Churn"

    st.write("### Hasil Prediksi:", hasil_text)

    # Simpan hasil prediksi ke SQLite.
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO prediksi (tenure_bulan, contract, monthly_charges, hasil) VALUES (?, ?, ?, ?)",
        (tenure, contract, monthly, hasil_text),
    )
    conn.commit()
    conn.close()

st.write("### Riwayat Prediksi")
conn = sqlite3.connect(DB_PATH)
riwayat_df = pd.read_sql_query("SELECT * FROM prediksi ORDER BY id DESC", conn)
conn.close()
st.dataframe(riwayat_df)

# Evaluasi model: confusion matrix dan feature importance, supaya
# dashboard ini juga mereinforce evaluasi model dari Sesi 10.
st.write("### Evaluasi Model")
df_eval = pd.read_csv("telco_churn.csv")
df_eval_enc = df_eval.copy()
for col in cat_cols:
    df_eval_enc[col] = encoders[col].transform(df_eval_enc[col])
X_eval = df_eval_enc[feature_cols]
y_eval = df_eval_enc["churn"].map({"No": 0, "Yes": 1})
_, X_test, _, y_test = train_test_split(X_eval, y_eval, test_size=0.2, random_state=42, stratify=y_eval)

cm = confusion_matrix(y_test, model.predict(X_test))
cm_df = pd.DataFrame(cm, index=["Aktual: Tidak Churn", "Aktual: Churn"], columns=["Prediksi: Tidak Churn", "Prediksi: Churn"])
st.write("Confusion Matrix:")
st.dataframe(cm_df)

importances = pd.Series(model.feature_importances_, index=feature_cols)
st.write("Feature Importance:")
st.bar_chart(importances)
