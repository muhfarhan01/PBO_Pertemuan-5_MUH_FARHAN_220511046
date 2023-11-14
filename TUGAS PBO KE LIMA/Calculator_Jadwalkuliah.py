import tkinter as tk
from tkinter import messagebox

class JadwalKuliahApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jadwal Kuliah Muhamad Farhan")


        # Variables
        self.jadwal = []

        # Labels and Entries

        tk.Label(root, text="Hari:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_hari = tk.Entry(root)
        self.entry_hari.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Mata Kuliah:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_matkul = tk.Entry(root)
        self.entry_matkul.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Waktu:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_waktu = tk.Entry(root)
        self.entry_waktu.grid(row=2, column=1, padx=10, pady=5)


        # Buttons
        tk.Button(root, text="Tambah Jadwal", command=self.tambah_jadwal, bg="red", fg="white").grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Simpan ke File", command=self.simpan_ke_file, bg="green", fg="white").grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Tampilkan Jadwal", command=self.tampilkan_jadwal, bg="blue", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

        # Output Text
        self.output_text = tk.Text(root, height=10, width=40)
        self.output_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def tambah_jadwal(self):
        hari = self.entry_hari.get()
        matkul = self.entry_matkul.get()
        waktu = self.entry_waktu.get()

        if hari and matkul and waktu:
            jadwal_info = f"Hari: {hari}, Mata Kuliah: {matkul}, Waktu: {waktu}"
            self.jadwal.append(jadwal_info)
            self.output_text.insert(tk.END, jadwal_info + "\n")
            messagebox.showinfo("Info", "Jadwal berhasil ditambahkan!")
            self.entry_hari.delete(0, tk.END)
            self.entry_matkul.delete(0, tk.END)
            self.entry_waktu.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Harap isi semua field!")

    def simpan_ke_file(self):
        with open("jadwal_kuliah.txt", "w") as file:
            for jadwal in self.jadwal:
                file.write(jadwal + "\n")
            messagebox.showinfo("Info", "Jadwal berhasil disimpan ke file!")

    def tampilkan_jadwal(self):
        if self.jadwal:
            jadwal_text = "\n".join(self.jadwal)
            self.output_text.delete(1.0, tk.END)  # Clear previous text
            self.output_text.insert(tk.END, jadwal_text)
        else:
            messagebox.showwarning("Peringatan", "Jadwal masih kosong!")

if __name__ == "__main__":
    root = tk.Tk()
    app = JadwalKuliahApp(root)
    root.mainloop()
