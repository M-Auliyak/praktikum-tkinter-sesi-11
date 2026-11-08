import tkinter as tk
from tkinter import ttk, messagebox

PROGRAM_STUDI = [
    "Teknik Informatika",
    "Sistem Informasi",
    "Teknologi Informasi",
    "Teknik Elektro",
    "Manajemen",
    "Akuntansi",
    "Teknik Sipil",
    "Pendidikan Bahasa Inggris",
]

KEGIATAN = [
    "Seminar Teknologi",
    "Workshop Coding",
    "Lomba Olahraga",
    "Bakti Sosial",
    "Pentas Seni",
    "Kepanitiaan Orientasi",
]


class AplikasiPendaftaran:
    def __init__(self, root):
        self.root = root
        self.root.title("Pendaftaran Kegiatan Mahasiswa")
        self.root.geometry("820x640")
        self.root.minsize(760, 600)

        # Variabel kontrol
        self.var_nama = tk.StringVar()
        self.var_prodi = tk.StringVar()
        self.var_gender = tk.StringVar()
        self.var_kegiatan = {k: tk.BooleanVar() for k in KEGIATAN}

        self.buat_menu()
        self.buat_form()
        self.buat_area_hasil()
        self.buat_tombol()
        self.pasang_event()

        self.entry_nama.focus_set()

    # ------------------------------------------------------------------ Menu
    def buat_menu(self):
        menubar = tk.Menu(self.root)

        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Submit", accelerator="Enter", command=self.submit)
        menu_file.add_command(label="Reset", accelerator="Ctrl+R", command=self.reset)
        menu_file.add_separator()
        menu_file.add_command(label="Keluar", accelerator="Ctrl+Q", command=self.keluar)
        menubar.add_cascade(label="File", menu=menu_file)

        menu_bantuan = tk.Menu(menubar, tearoff=0)
        menu_bantuan.add_command(label="About", accelerator="F1", command=self.tampilkan_about)
        menubar.add_cascade(label="Bantuan", menu=menu_bantuan)

        self.root.config(menu=menubar)

    # ------------------------------------------------------------------ Form
    def buat_form(self):
        header = ttk.Label(
            self.root,
            text="Formulir Pendaftaran Kegiatan Mahasiswa",
            font=("Segoe UI", 15, "bold"),
        )
        header.pack(pady=(12, 6))

        body = ttk.Frame(self.root, padding=(14, 4))
        body.pack(fill="both", expand=True)
        body.columnconfigure(0, weight=1)
        body.columnconfigure(1, weight=1)

        # --- Frame kiri: data diri + alasan
        frame_kiri = ttk.LabelFrame(body, text="Data Mahasiswa", padding=10)
        frame_kiri.grid(row=0, column=0, sticky="nsew", padx=(0, 6))
        frame_kiri.columnconfigure(1, weight=1)

        # Entry: nama
        ttk.Label(frame_kiri, text="Nama").grid(row=0, column=0, sticky="w", pady=4)
        self.entry_nama = ttk.Entry(frame_kiri, textvariable=self.var_nama)
        self.entry_nama.grid(row=0, column=1, sticky="ew", pady=4, padx=(8, 0))

        # Combobox: program studi 
        ttk.Label(frame_kiri, text="Program Studi").grid(row=1, column=0, sticky="w", pady=4)
        self.combo_prodi = ttk.Combobox(
            frame_kiri, textvariable=self.var_prodi, values=PROGRAM_STUDI, state="readonly"
        )
        self.combo_prodi.grid(row=1, column=1, sticky="ew", pady=4, padx=(8, 0))
        self.combo_prodi.set("-- Pilih Program Studi --")

        # Radiobutton: jenis kelamin
        ttk.Label(frame_kiri, text="Jenis Kelamin").grid(row=2, column=0, sticky="w", pady=4)
        frame_gender = ttk.Frame(frame_kiri)
        frame_gender.grid(row=2, column=1, sticky="w", pady=4, padx=(8, 0))
        for teks in ("Laki-laki", "Perempuan"):
            ttk.Radiobutton(
                frame_gender, text=teks, value=teks, variable=self.var_gender
            ).pack(side="left", padx=(0, 12))

        # Text: alasan mengikuti kegiatan
        ttk.Label(frame_kiri, text="Alasan Mengikuti Kegiatan").grid(
            row=3, column=0, columnspan=2, sticky="w", pady=(10, 2)
        )
        frame_alasan = ttk.Frame(frame_kiri)
        frame_alasan.grid(row=4, column=0, columnspan=2, sticky="nsew")
        frame_kiri.rowconfigure(4, weight=1)
        self.text_alasan = tk.Text(frame_alasan, height=7, width=30, wrap="word")
        scroll_alasan = ttk.Scrollbar(frame_alasan, orient="vertical", command=self.text_alasan.yview)
        self.text_alasan.config(yscrollcommand=scroll_alasan.set)
        self.text_alasan.pack(side="left", fill="both", expand=True)
        scroll_alasan.pack(side="right", fill="y")

        # --- Frame kanan: kegiatan (Checkbutton) + Listbox pilihan
        frame_kanan = ttk.LabelFrame(body, text="Pilihan Kegiatan", padding=10)
        frame_kanan.grid(row=0, column=1, sticky="nsew", padx=(6, 0))

        ttk.Label(frame_kanan, text="Pilih kegiatan (boleh lebih dari satu):").pack(anchor="w")
        for k in KEGIATAN:
            ttk.Checkbutton(
                frame_kanan, text=k, variable=self.var_kegiatan[k],
                command=self.perbarui_listbox,
            ).pack(anchor="w", pady=1)

        ttk.Separator(frame_kanan).pack(fill="x", pady=8)
        ttk.Label(frame_kanan, text="Kegiatan yang dipilih:").pack(anchor="w")
        frame_list = ttk.Frame(frame_kanan)
        frame_list.pack(fill="both", expand=True, pady=(2, 0))
        self.listbox = tk.Listbox(frame_list, height=5)
        scroll_list = ttk.Scrollbar(frame_list, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scroll_list.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        scroll_list.pack(side="right", fill="y")

    # ------------------------------------------------------------ Area hasil
    def buat_area_hasil(self):
        frame_hasil = ttk.LabelFrame(self.root, text="Ringkasan Pendaftaran", padding=8)
        frame_hasil.pack(fill="x", padx=14, pady=(6, 4))
        self.text_hasil = tk.Text(
            frame_hasil, height=8, state="disabled", bg="#f4f4f4", wrap="word"
        )
        self.text_hasil.pack(fill="x")
        self.tulis_hasil("Belum ada data. Isi formulir lalu klik Submit.")

    # ---------------------------------------------------------------- Tombol
    def buat_tombol(self):
        frame_tombol = ttk.Frame(self.root, padding=(14, 4, 14, 12))
        frame_tombol.pack(fill="x")
        ttk.Button(frame_tombol, text="Submit", command=self.submit).pack(side="left")
        ttk.Button(frame_tombol, text="Reset", command=self.reset).pack(side="left", padx=8)
        ttk.Button(frame_tombol, text="Keluar", command=self.keluar).pack(side="right")

    # ----------------------------------------------------------------- Event
    def pasang_event(self):
        self.root.bind("<Return>", self.event_enter)
        self.root.bind("<KP_Enter>", self.event_enter)
        self.root.bind("<Control-r>", lambda e: self.reset())
        self.root.bind("<Control-q>", lambda e: self.keluar())
        self.root.bind("<F1>", lambda e: self.tampilkan_about())
        self.root.protocol("WM_DELETE_WINDOW", self.keluar)

    def event_enter(self, event):
        # Enter pada kolom Text (alasan) tetap membuat baris baru
        if event.widget is self.text_alasan:
            return
        self.submit()

    # ------------------------------------------------------------- Fungsi inti
    def kegiatan_terpilih(self):
        return [k for k in KEGIATAN if self.var_kegiatan[k].get()]

    def perbarui_listbox(self):
        self.listbox.delete(0, tk.END)
        for k in self.kegiatan_terpilih():
            self.listbox.insert(tk.END, k)

    def tulis_hasil(self, teks):
        self.text_hasil.config(state="normal")
        self.text_hasil.delete("1.0", tk.END)
        self.text_hasil.insert("1.0", teks)
        self.text_hasil.config(state="disabled")

    def validasi(self):
        nama = self.var_nama.get().strip()
        if not nama:
            messagebox.showwarning("Validasi", "Nama tidak boleh kosong!")
            self.entry_nama.focus_set()
            return False
        if self.var_prodi.get() not in PROGRAM_STUDI:
            messagebox.showwarning("Validasi", "Silakan pilih program studi.")
            self.combo_prodi.focus_set()
            return False
        if not self.var_gender.get():
            messagebox.showwarning("Validasi", "Silakan pilih jenis kelamin.")
            return False
        if not self.kegiatan_terpilih():
            messagebox.showwarning("Validasi", "Pilih minimal satu kegiatan.")
            return False
        return True

    def submit(self):
        if not self.validasi():
            return
        nama = self.var_nama.get().strip()
        alasan = self.text_alasan.get("1.0", tk.END).strip() or "-"
        kegiatan = self.kegiatan_terpilih()

        ringkasan = (
            f"Nama           : {nama}\n"
            f"Program Studi  : {self.var_prodi.get()}\n"
            f"Jenis Kelamin  : {self.var_gender.get()}\n"
            f"Kegiatan       : {', '.join(kegiatan)}\n"
            f"Alasan         : {alasan}"
        )
        self.tulis_hasil(ringkasan)
        messagebox.showinfo(
            "Pendaftaran Berhasil",
            f"Terima kasih, {nama}!\nAnda terdaftar pada {len(kegiatan)} kegiatan.",
        )

    def reset(self):
        self.var_nama.set("")
        self.combo_prodi.set("-- Pilih Program Studi --")
        self.var_prodi.set("")
        self.var_gender.set("")
        for var in self.var_kegiatan.values():
            var.set(False)
        self.text_alasan.delete("1.0", tk.END)
        self.listbox.delete(0, tk.END)
        self.tulis_hasil("Belum ada data. Isi formulir lalu klik Submit.")
        self.entry_nama.focus_set()
        messagebox.showinfo("Reset", "Formulir telah dikosongkan.")

    def keluar(self):
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar?"):
            self.root.destroy()

    def tampilkan_about(self):
        about = tk.Toplevel(self.root)
        about.title("About")
        about.geometry("340x200")
        about.resizable(False, False)
        about.transient(self.root)
        about.grab_set()

        ttk.Label(about, text="Pendaftaran Kegiatan Mahasiswa",
                  font=("Segoe UI", 12, "bold")).pack(pady=(20, 6))
        ttk.Label(about, text="Praktikum Tkinter Sesi 11\nAdvanced Widgets dan Event Handling",
                  justify="center").pack()
        ttk.Label(about, text="Versi 1.0").pack(pady=6)
        ttk.Button(about, text="Tutup", command=about.destroy).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    AplikasiPendaftaran(root)
    root.mainloop()