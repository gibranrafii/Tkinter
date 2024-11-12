import tkinter as tk

def hasil_prediksi():
    # Menulis "Teknologi Informasi" ke dalam label hasil prediksi
    result_label.config(text="Prodi : Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry('500x500')  # Ukuran jendela (lebar x tinggi)
root.configure(bg='#2b2b2b')  # background Warna abu-abu gelap

# Label Judul Aplikasi
judul_label = tk.Label(root,
                       text='Prediksi Program Studi',
                       font=('Times New Roman', '16'),
                       fg='#00ffcc',  # Warna teks cerah
                       bg='#2b2b2b')  # Warna background judul
judul_label.pack(pady=20)  # Pakai padding atas dan bawah

# Frame untuk input nilai mata pelajaran
input_frame = tk.Frame(root, bg='#2b2b2b')
input_frame.pack()

# Input Nilai Mata Pelajaran
nilai_labels = []
nilai_entries = []

for i in range(10):
    label_nilai = tk.Label(input_frame,
                           text=f'Nilai {i+1}: ',
                           width=15,
                           anchor=tk.W,
                           fg='#ffffff',  # Warna teks putih
                           bg='#2b2b2b')  # Background gelap
    
    entry_nilai = tk.Entry(input_frame,
                           width=5,
                           bg='#3c3f41',  # Background input abu-abu gelap
                           fg='#ffffff',  # Warna teks putih
                           insertbackground='#ffffff')  # Warna cursor putih
    
    label_nilai.grid(row=i, column=0, padx=5, pady=2)
    entry_nilai.grid(row=i, column=1, padx=5, pady=2)
    
    nilai_labels.append(label_nilai)
    nilai_entries.append(entry_nilai)

# Button Bertuliskan Hasil Prediksi 
button_hasil_prediksi = tk.Button(root,
                                  text='Hasil Prediksi',
                                  command=hasil_prediksi,
                                  bg='#007acc',  # Warna button biru
                                  fg='#ffffff')  # Warna teks putih
button_hasil_prediksi.pack(pady=30)

# Label Luaran Hasil Prediksi 
result_label = tk.Label(root,
                        text='',
                        font=('Arial', '14'),
                        fg='#00ffcc',  # Warna teks hasil prediksi cerah
                        bg='#2b2b2b')  # Background gelap
result_label.pack(pady=10)

root.mainloop()
