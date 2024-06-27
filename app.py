from flask import Flask, render_template, jsonify # Import library Flask untuk membuat aplikasi web dan jsonify untuk mengirim response JSON import serial # Import library serial untuk komunikasi dengan perangkat serial (seperti Arduino)
import serial

app = Flask(__name__) # Inisialisasi aplikasi Flask

ser = serial.Serial('COM4', 9600) # Membuka koneksi serial dengan port COM4 dan baudrate 9600

def read_distance():
    if ser.in_waiting > 0: # Memeriksa apakah ada data yang tersedia untuk dibaca dari serial
        line = ser.readline().decode('utf-8').rstrip() # Membaca data dari serial, kemudian didekode dari byte ke string dan dibersihkan dari karakter newline
        ser.flushInput() # Membersihkan buffer input serial
        return line # Mengembalikan data jarak yang telah dibaca
    return None # Mengembalikan None jika tidak ada data yang tersedia

@app.route('/')
def index():
    return render_template('index.html') # Mengembalikan halaman HTML untuk route utama '/'

@app.route('/distance')
def distance():
    data = read_distance() # Memanggil fungsi read_distance() untuk membaca data jarak
    if data:
        return jsonify(distance=data) # Mengirimkan response JSON berisi data jarak jika data tersedia
    return jsonify(distance="Error: No data received") # Mengirimkan response JSON dengan pesan error jika tidak ada data yang diterima

if __name__ == '__main__':
    app.run(debug=False) # Menjalankan aplikasi Flask jika file dieksekusi langsung (bukan di-import sebagai modul)

