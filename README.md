# WiFi Password Recovery Tool

Alat Python untuk mengambil password WiFi yang tersimpan di sistem Anda.
(Python tool to retrieve saved WiFi passwords from your system.)

## Deskripsi (Description)

Tool ini memungkinkan Anda untuk melihat password WiFi yang telah tersimpan di komputer Anda. Berguna ketika Anda lupa password WiFi sendiri yang sudah pernah tersambung sebelumnya.

This tool allows you to view WiFi passwords that are saved on your computer. Useful when you forget your own WiFi password that was previously connected.

## Fitur (Features)

- ✅ Mendukung Windows, Linux, dan macOS
- ✅ Menampilkan semua jaringan WiFi yang tersimpan
- ✅ Menampilkan password untuk setiap jaringan
- ✅ Menggunakan hanya Python standard library (tidak perlu instalasi tambahan)
- ✅ Cross-platform compatibility

## Persyaratan (Requirements)

- Python 3.6 atau lebih tinggi (Python 3.6 or higher)
- Administrator/root privileges (untuk hasil terbaik / for best results)

### Platform-specific Requirements:

**Windows:**
- Netsh command (built-in)
- Administrator privileges recommended

**Linux:**
- NetworkManager dengan nmcli, atau
- Akses ke `/etc/NetworkManager/system-connections/`
- Root privileges required

**macOS:**
- Security command (built-in)
- Keychain access privileges

## Instalasi (Installation)

```bash
# Clone repository
git clone https://github.com/edwinjordan/phyton-wifi.git
cd phyton-wifi

# Tidak perlu instalasi dependencies (hanya menggunakan standard library)
# No need to install dependencies (uses only standard library)
```

## Cara Penggunaan (Usage)

### Windows:

Jalankan sebagai Administrator untuk hasil terbaik:
```bash
# Buka Command Prompt sebagai Administrator
python wifi_password.py
```

### Linux:

Jalankan dengan sudo:
```bash
sudo python3 wifi_password.py
```

### macOS:

Jalankan dengan sudo:
```bash
sudo python3 wifi_password.py
```

## Contoh Output (Example Output)

```
============================================================
WiFi Password Recovery Tool - Windows
============================================================

Found 3 saved WiFi network(s):

SSID: HomeNetwork
Password: MySecurePassword123
------------------------------------------------------------
SSID: OfficeWiFi
Password: Office2024!
------------------------------------------------------------
SSID: GuestNetwork
Password: No password or open network
------------------------------------------------------------
```

## Catatan Keamanan (Security Notes)

⚠️ **PENTING / IMPORTANT:**

- Tool ini hanya mengambil password yang SUDAH TERSIMPAN di komputer Anda sendiri
- JANGAN gunakan untuk mengakses jaringan WiFi orang lain tanpa izin
- Gunakan secara bertanggung jawab dan legal
- This tool only retrieves passwords that are ALREADY SAVED on your own computer
- DO NOT use to access other people's WiFi networks without permission
- Use responsibly and legally

## Cara Kerja (How It Works)

### Windows:
Menggunakan `netsh wlan show profiles` untuk mendapatkan daftar profil WiFi dan `netsh wlan show profile [name] key=clear` untuk mendapatkan password.

### Linux:
Menggunakan `nmcli` (NetworkManager CLI) atau membaca file konfigurasi dari `/etc/NetworkManager/system-connections/`.

### macOS:
Menggunakan `security` command untuk mengakses Keychain dan `airport` utility untuk mendapatkan informasi jaringan.

## Troubleshooting

### "No saved WiFi networks found"
- Pastikan Anda menjalankan script dengan privileges yang cukup (Administrator/sudo)
- Pastikan ada jaringan WiFi yang tersimpan di sistem

### "Permission denied"
- Jalankan dengan administrator/root privileges
- Windows: Klik kanan Command Prompt → Run as Administrator
- Linux/macOS: Gunakan `sudo`

### Linux: "nmcli not found"
- Install NetworkManager: `sudo apt-get install network-manager` (Ubuntu/Debian)
- Atau gunakan sudo untuk akses langsung ke file konfigurasi

## Lisensi (License)

Project ini dibuat untuk tujuan edukasi dan penggunaan personal yang legal.
This project is created for educational purposes and legal personal use.

## Kontributor (Contributors)

- Edwin Jordan

## Disclaimer

Pembuat tool ini tidak bertanggung jawab atas penyalahgunaan tool ini. Gunakan hanya untuk mengakses jaringan WiFi Anda sendiri atau dengan izin eksplisit dari pemilik jaringan.

The creator of this tool is not responsible for misuse of this tool. Use only to access your own WiFi networks or with explicit permission from the network owner.