from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Logika atau data dari Python
    judul_kotak = "Status Sistem"
    hasil_hitung = 25 * 4
    warna_kotak = "#2563eb"  # Biru (bisa diubah dinamis lewat logika Python)

    # Panggil file HTML dan kirim datanya
    return render_template(
        'index.html',
        judul=judul_kotak,
        angka=hasil_hitung,
        warna=warna_kotak
    )
