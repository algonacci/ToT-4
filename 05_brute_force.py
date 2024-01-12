import requests
import json

# URL endpoint untuk permintaan POST
url = 'http://localhost:5000/add_data'  # Sesuaikan dengan alamat server Anda

# Data yang akan dikirim dalam permintaan POST
data_to_post = {"data": "Contoh Data"}

# Jumlah permintaan yang akan dikirim
num_requests = 100

# Looping untuk mengirim 100 permintaan POST
for _ in range(num_requests):
    response = requests.post(url, json=data_to_post)

    # Mengecek status respons
    if response.status_code == 201:
        print("Data berhasil ditambahkan.")
    else:
        print("Gagal menambahkan data. Status Code:", response.status_code)

# Menampilkan pesan ketika selesai
print("Selesai mengirim", num_requests, "permintaan POST.")
