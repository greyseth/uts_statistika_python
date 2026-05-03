import matplotlib.pyplot as plt

def display_histogram(data_math, frekuensi_module):
    res = frekuensi_module.to_interval_table(data_math)
    
    data_list = res.get('data', [])

    labels = []
    counts = []

    for item in data_list:
        label = f"{item['low']} - {item['high']}"
        count = item['count']
        
        labels.append(label)
        counts.append(count)

    if not counts:
        print("Data tidak ditemukan.")
        return

    plt.figure(figsize=(10, 6))
    
    plt.bar(labels, counts, color='#4472C4', edgecolor='black', width=0.6, zorder=3)

    plt.plot(labels, counts, color='black', marker='o', markersize=4, linestyle='-', linewidth=1.5, zorder=4)

    plt.title('HISTOGRAM TABEL DISTRIBUSI FREKUENSI', fontsize=12, fontweight='bold', pad=20)
    plt.grid(axis='y', linestyle='-', alpha=0.5, zorder=0)
    plt.xticks(rotation=45) 
    
    plt.ylim(0, max(counts) * 1.2)

    plt.tight_layout()
    plt.show()