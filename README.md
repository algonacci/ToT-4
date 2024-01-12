# ToT-4
Briancore Training of Trainer: Securing our Flask Application

## 01_xss.py
Aplikasi web sederhana menggunakan Flask yang menunjukkan contoh kerentanan Cross-Site Scripting (XSS). Pengguna dapat melakukan login dan aplikasi akan menampilkan pesan selamat datang.
```
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Selamat datang, {username}!"
```

## 02_seeder.py
Skrip Python untuk mengisi database SQLite dengan data pengguna sampel. Skrip ini membuat tabel 'users' jika belum ada dan memasukkan beberapa baris data.
```
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)",
               ('user1', 'user1@example.com'))
```

## 02_sql_injection.py
Aplikasi web Flask yang menunjukkan contoh kerentanan SQL Injection. Pengguna dapat mencari pengguna lain berdasarkan nama pengguna.
```
@app.route('/search', methods=['POST'])
def search():
    username = request.form['username']
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
```

## 03_csrf.py
Aplikasi web Flask yang menunjukkan contoh kerentanan Cross-Site Request Forgery (CSRF). Aplikasi ini memiliki dua form, satu dengan proteksi CSRF dan satu tanpa.
```
@app.route('/search', methods=['POST'])
def search():
    username = request.form['username']
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
```

## 04_cors.py
Aplikasi web Flask yang menunjukkan penggunaan Cross-Origin Resource Sharing (CORS). Aplikasi ini memungkinkan permintaan dari beberapa origin yang ditentukan.
```
CORS(app, origins=["https://example.com", "http://127.0.0.1:5500"])
```

## 05_brute_force.py
Skrip Python yang menunjukkan contoh serangan brute force dengan mengirim banyak permintaan POST ke server.
```
for _ in range(num_requests):
    response = requests.post(url, json=data_to_post)
```

## 05_rate_limiter.py
Aplikasi web Flask yang menggunakan rate limiting untuk mencegah serangan brute force. Aplikasi ini membatasi jumlah permintaan yang dapat dilakukan pengguna dalam satu menit.
```
@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return jsonify(message="Login successful")
```
