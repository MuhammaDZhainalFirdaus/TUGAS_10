from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Inisialisasi variabel default
    probability = None
    formula = None
    n = None
    k = None
    p = None

    if request.method == 'POST':
        try:
            # Ambil data dari form input
            n = int(request.form['n'])  # Jumlah paket yang dikirim
            k = int(request.form['k'])  # Jumlah paket yang terkirim tepat waktu
            p = float(request.form['p'])  # Probabilitas pengiriman tepat waktu

            # Validasi input
            if k > n:
                raise ValueError("Jumlah keberhasilan (k) tidak boleh lebih besar dari jumlah percobaan (n).")

            # Perhitungan distribusi binomial
            prob = (math.comb(n, k)) * (p ** k) * ((1 - p) ** (n - k))
            
            # Format hasil perhitungan dan rumus
            probability = round(prob, 6)  # Membulatkan hasil
            formula = f"P(X = {k}) = C({n}, {k}) * ({p})^{k} * (1 - {p})^{({n} - {k})}"

        except ValueError as e:
            # Menangani error jika input tidak valid
            probability = f"Error: {e}"

    # Kirim variabel ke template
    return render_template('index.html', probability=probability, formula=formula, n=n, k=k, p=p)

if __name__ == '__main__':
    app.run(debug=True)
