# 🤖 TikTok Live Auto Comment Bot

Bot otomatis untuk mengirim komentar di TikTok Live menggunakan Selenium dan Chrome DevTools Protocol.

---

## 📋 Daftar Isi

- [Requirement](#requirement)
- [Cara Setup](#cara-setup)
- [Cara Menjalankan](#cara-menjalankan)
- [Konfigurasi](#konfigurasi)
- [Penjelasan Script](#penjelasan-script)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Peringatan](#peringatan)

---

## Requirement

Pastikan sudah terinstall:

| Software | Versi | Link |
|---|---|---|
| Python | 3.8+ | https://python.org |
| Google Chrome | Terbaru | https://chrome.google.com |
| ChromeDriver | Sesuai versi Chrome | https://chromedriver.chromium.org |
| Selenium | 4.x | `pip install selenium` |

---

## Cara Setup

### 1. Install Selenium

```bash
pip install selenium
```

### 2. Download ChromeDriver

1. Cek versi Chrome kamu: buka Chrome → `chrome://settings/help`
2. Download ChromeDriver yang sesuai di: https://chromedriver.chromium.org/downloads
3. Simpan `chromedriver.exe` ke folder project:
   ```
   C:\Users\hi\Documents\Projeck\Komentar Otomatis Tiktok\chromedriver.exe
   ```

### 3. Buka Chrome dengan Remote Debugging

Buka **Command Prompt** dan jalankan perintah ini:

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"
```

> ⚠️ Jangan tutup CMD ini selama bot berjalan!

### 4. Login TikTok

Di Chrome yang terbuka tadi, login ke akun TikTok kamu secara manual di https://tiktok.com

### 5. Buka TikTok Live

Navigasi ke halaman TikTok Live yang ingin dikomentari. Pastikan URL mengandung `tiktok.com/live` atau `tiktok.com/@.../live`

---

## Cara Menjalankan

```bash
cd "C:\Users\hi\Documents\Projeck\Komentar Otomatis Tiktok"
python tiktok_live.py
```

Output yang muncul jika berhasil:

```
✅ Tab: MPL Indonesia (@mpl.id.official) is LIVE - TikTok LIVE
🚀 Kirim komentar NONSTOP... (Ctrl+C untuk stop)

✅ Terkirim: LB SATSET ABANGKU 🥶🥶🥶🥶🥶...
✅ Terkirim: LB SAT SET ABANGKUU 💜💜💜💜💜...
```

Tekan **Ctrl+C** untuk menghentikan bot.

---

## Konfigurasi

Edit bagian ini di file `tiktok_live.py`:

### Ganti Path ChromeDriver

```python
CHROMEDRIVER_PATH = r"C:\Users\hi\Documents\Projeck\Komentar Otomatis Tiktok\chromedriver.exe"
```

### Ganti Daftar Komentar

```python
KOMENTAR_LIST = [
    "LB SATSET ABANGKU 🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶🥶",
    "LB SAT SET ABANGKUU 💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜💜",
]
```

### Ganti Kecepatan Kirim

```python
time.sleep(0.5)  # Jeda antar komentar dalam detik
```

| Nilai | Kecepatan |
|---|---|
| `0.3` | Sangat cepat (risiko tinggi) |
| `0.5` | Cepat ✅ (recommended) |
| `1.0` | Normal |
| `2.0` | Aman (risiko rendah) |

---

## Penjelasan Script

### Cara Kerja

```
Chrome (--remote-debugging-port=9222)
        ↓
Selenium connect via debuggerAddress
        ↓
Deteksi tab TikTok Live
        ↓
Temukan input box [data-e2e="room-chat-input-field"]
        ↓
Inject teks via JavaScript execCommand
        ↓
Kirim dengan Keys.RETURN
        ↓
Loop ulang setiap 0.5 detik
```

### Elemen yang Digunakan

| Selector | Fungsi |
|---|---|
| `[data-e2e="room-chat-input-field"]` | Input box komentar |
| `[data-e2e="room-chat-send-btn"]` | Tombol kirim (alternatif) |
| `[data-e2e="live-chat-input-container"]` | Container area chat |

### Struktur File

```
Komentar Otomatis Tiktok/
├── chromedriver.exe      # ChromeDriver
├── tiktok_live.py        # Script utama
├── tiktok_debug.png      # Screenshot debug (auto-generated)
└── README.md             # File ini
```

---

## Troubleshooting

### ❌ Tab TikTok tidak ditemukan

```
Tidak ada output "✅ Pindah ke tab"
```

**Solusi:**
- Pastikan Chrome dibuka dengan `--remote-debugging-port=9222`
- Pastikan sudah buka halaman TikTok Live di Chrome tersebut
- Cek apakah URL mengandung kata `live`

---

### ❌ ChromeDriver version mismatch

```
SessionNotCreatedException: Message: session not created: 
This version of ChromeDriver only supports Chrome version XX
```

**Solusi:**
- Cek versi Chrome: `chrome://settings/help`
- Download ChromeDriver yang versinya sama di https://chromedriver.chromium.org/downloads

---

### ❌ Komentar tidak terkirim / input kosong

```
✅ Terkirim: ... (tapi tidak muncul di live chat)
```

**Solusi:** Ganti metode input di script:

```python
# Ganti execCommand dengan send_keys biasa
input_box.send_keys(teks)
```

---

### ❌ ERR_BLOCKED_BY_CLIENT di console browser

Ini **normal** dan tidak mempengaruhi script. Error ini muncul karena AdBlocker memblokir sistem tracking TikTok (`mon.tiktokv.com`). Abaikan saja.

---

### ❌ Komentar tiba-tiba berhenti

Kemungkinan akun terkena **temporary comment ban** oleh TikTok karena spam.

**Solusi:**
- Tunggu 10-30 menit sebelum mencoba lagi
- Naikkan jeda menjadi `time.sleep(2)`
- Tambahkan variasi komentar

---

## FAQ

**Q: Apakah komentar terlihat oleh orang lain?**

Ya. Komentar yang dikirim bot sama persis seperti komentar manual — tampil di live chat publik dan bisa dilihat semua penonton.

---

**Q: Apakah bisa kena banned?**

Bisa, jika TikTok mendeteksi pola spam (komentar identik berulang dengan jeda sangat cepat). Gunakan variasi komentar dan jeda yang wajar.

---

**Q: Apakah perlu login ulang setiap kali?**

Tidak, selama menggunakan `--user-data-dir` yang sama saat membuka Chrome, sesi login tersimpan.

---

**Q: Bisa dipakai di akun berbeda?**

Bisa. Ganti `--user-data-dir` ke folder berbeda untuk setiap akun:

```bash
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeAkun2"
```
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![Stars](https://img.shields.io/github/stars/username/tiktok-live-bot)
---

## ⚠️ Peringatan

- Penggunaan bot komentar **melanggar Terms of Service TikTok**
- Risiko akun dibatasi, di-shadowban, atau di-suspend
- Gunakan hanya untuk keperluan pribadi / testing
- Developer tidak bertanggung jawab atas akun yang terkena banned

---

*Dibuat dengan Python + Selenium | TikTok Live Auto Comment Bot*
# -tiktok-live-spammer
