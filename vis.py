import matplotlib.pyplot as pl

def display_histogram(data, title, color='skyblue'):
    """
    Fungsi untuk menampilkan histogram menggunakan matplotlib
    """
    pl.figure(figsize=(10, 6))
    
    # Membuat histogram
    # bins=15 membagi data ke dalam 15 kelompok rentang nilai
    pl.hist(data, bins=15, color=color, edgecolor='black', alpha=0.7)
    
    # Menghitung mean untuk garis referensi
    mean_val = sum(data) / len(data)
    pl.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_val:.2f}')
    
    # Pengaturan Judul dan Label
    pl.title(f'Distribusi Frekuensi {title}', fontsize=14)
    pl.xlabel('Skor', fontsize=12)
    pl.ylabel('Jumlah Siswa (Frekuensi)', fontsize=12)
    pl.legend()
    pl.grid(axis='y', alpha=0.3)
    
    # Menampilkan grafik
    pl.show()