# Praktikum Tkinter Sesi 11 – Pendaftaran Kegiatan Mahasiswa

## Tujuan
Membangun aplikasi GUI dengan Python Tkinter yang memanfaatkan berbagai widget, event handling, validasi input, menu, dan dialog.

## Daftar Widget
| Widget | Kegunaan |
| --- | --- |
| Entry | Input nama |
| Combobox (readonly) | Pilih program studi |
| Radiobutton | Pilih jenis kelamin |
| Checkbutton | Pilih kegiatan (boleh lebih dari satu) |
| Text + Scrollbar | Alasan mengikuti kegiatan, dan area ringkasan |
| Listbox + Scrollbar | Menampilkan kegiatan yang dipilih (update langsung) |
| Button | Submit, Reset, Keluar |
| Menu | File (Submit, Reset, Keluar) dan Bantuan (About) |
| Toplevel | Jendela About |
| Messagebox | Notifikasi sukses, peringatan validasi, konfirmasi keluar |
| Frame / LabelFrame | Penataan antarmuka (grid dan pack) |

## Fitur
- Submit menampilkan ringkasan pendaftaran pada area informasi.
- Validasi: nama tidak boleh kosong, program studi dan jenis kelamin harus dipilih, minimal satu kegiatan.
- Reset mengosongkan semua jenis widget.
- Event keyboard: `Enter` = Submit (di kolom alasan, Enter tetap membuat baris baru), `Ctrl+R` = Reset, `Ctrl+Q` = Keluar, `F1` = About.
- Konfirmasi saat keluar (menu, tombol, maupun tombol close jendela).

## Cara Menjalankan
1. Pastikan Python 3 terpasang (Tkinter sudah termasuk pada instalasi standar Windows/macOS; di Linux: `sudo apt install python3-tk`).
2. Jalankan:
   ```
   python main.py
   ```

## Struktur Repository
```
praktikum-tkinter-sesi-11/
├── main.py
├── README.md
└── screenshots/
    ├── form-pendaftaran.png
    ├── pilihan-widget.png
    └── hasil-submit.png
```

## Screenshot
| File | Keterangan |
| --- | --- |
| `form-pendaftaran.png` | Formulir pendaftaran yang sudah terisi |
| `pilihan-widget.png` | Pilihan Combobox dan Checkbutton, dengan Listbox terisi |
| `hasil-submit.png` | Ringkasan pendaftaran setelah Submit |