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

Gunakan virtual environment agar paket project ini tidak bentrok dengan paket Python lain yang sudah terpasang di sistem kamu (mis. error `command not found: streamlit` atau `ImportError` pada scipy/sklearn biasanya disebabkan oleh instalasi global yang tercampur atau versi Python yang sudah usang — lihat Troubleshooting):

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Menjalankan

```bash
source .venv/bin/activate      # jika belum aktif
streamlit run app.py
```

## Troubleshooting

- **`zsh: command not found: streamlit`** — venv belum diaktifkan, atau instalasi sebelumnya masuk ke `~/Library/Python/...` yang tidak ada di PATH. Aktifkan venv (`source .venv/bin/activate`) lalu jalankan lagi, atau jalankan sementara dengan `python3 -m streamlit run app.py`.
- **`ImportError: dlopen(...) scipy/sparse/linalg/_propack/...` (macOS)** — ini bukan soal instalasi paket, tapi versi Python sistem yang sudah lama (mis. Python 3.10 rilis 2022) tidak kompatibel di level loader dengan versi macOS yang jauh lebih baru. Reinstall scipy/numpy **tidak** memperbaiki ini. Solusinya: pakai Python yang lebih baru, misalnya lewat Homebrew:
  ```bash
  brew install python@3.12
  rm -rf .venv
  /opt/homebrew/bin/python3.12 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
  streamlit run app.py
  ```
- Untuk memastikan arsitektur venv sesuai mesin kamu, jalankan `python3 -c "import platform; print(platform.machine())"` dan `uname -m` — keduanya harus sama (mis. sama-sama `arm64` di Apple Silicon).

## Konteks

Bagian dari Sesi 15 - Mini Project: Connecting the Dots, kurikulum Python Programming for AI Batch 8 (rubythalib.ai). Menggabungkan Sesi 6 (SQLite), Sesi 10 (Decision Tree), dan Sesi 14 (Streamlit deployment).
