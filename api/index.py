from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    judul_kotak = "Status Sistem"
    hasil_hitung = 25 * 4
    warna_kotak = "#2563eb"

    return render_template(
        'index.html',
        judul=judul_kotak,
        angka=hasil_hitung,
        warna=warna_kotak
    )
