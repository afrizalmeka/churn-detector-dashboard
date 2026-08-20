# Customer Churn Detector Dashboard

Mini Project Sesi 15 (Python Programming for AI - Batch 8) - Project 2 dari 5 opsi. Dashboard untuk memprediksi apakah pelanggan berpotensi churn (berhenti berlangganan), memakai model Decision Tree yang dilatih di Sesi 10.

Cocok untuk peserta dengan latar belakang: bisnis, perbankan, telekomunikasi, keuangan.

## Status

Aplikasi ini **sudah 100% jadi** dan siap dijalankan langsung - tidak ada bagian kosong yang perlu diisi. Cocok dipakai sebagai referensi belajar: baca `app.py` untuk lihat bagaimana model (Sesi 10), SQLite (Sesi 6), dan Streamlit (Sesi 14) digabung jadi 1 aplikasi utuh, termasuk evaluasi model (confusion matrix dan feature importance).

## Struktur Folder

```
churn-detector-dashboard/
├── app.py                # Streamlit - dashboard (skeleton, ada TODO)
├── churn_model.pkl        # Model terlatih dari Sesi 10
├── telco_churn.csv        # Dataset asli (untuk TODO 4, evaluasi model)
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalasi

```bash
pip install -r requirements.txt
```

## Menjalankan

Setelah semua TODO diisi:

```bash
streamlit run app.py
```

## Konteks

Bagian dari Sesi 15 - Mini Project: Connecting the Dots, kurikulum Python Programming for AI Batch 8 (rubythalib.ai). Menggabungkan Sesi 6 (SQLite), Sesi 10 (Decision Tree), dan Sesi 14 (Streamlit deployment).
