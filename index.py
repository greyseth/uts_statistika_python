# untuk run,
# pip install openpyxl
# python index.py

import numerik
import frekuensi
import vis
import chart

import openpyxl

wb = openpyxl.load_workbook("StudentsPerformance.xlsx")
ws = wb.active

all_rows = list(ws.iter_rows(values_only=True))

# Header ada di baris index 2, data mulai dari index 3 sampai 1002 (1000 data)
data = [list(r) for r in all_rows[3:1003]]

# d[1] - gender
# d[2] - race/ethnicity
# d[3] - parental level of education
# d[4] - lunch
# d[5] - test preparation course
# d[6] - math score      (numerik)
# d[7] - reading score   (numerik)
# d[8] - writing score   (numerik)


# function numerik
def math_score():
    return [int(d[6]) for d in data]

def reading_score():
    return [int(d[7]) for d in data]

def writing_score():
    return [int(d[8]) for d in data]

# function kategorik
def parental_education():
    return [d[3] for d in data]


# function data numerik
def display_data(data, title):
    print(title)

    print("- Mean data: " + str(numerik.get_mean(data)))
    print("- Median data: " + str(numerik.get_median(data)))
    modus = numerik.get_modus(data)
    print(f"- Modus data: {modus['value']} ({modus['count']} data)")
    min_val = min(data)
    max_val = max(data)
    print(f"- Nilai min: {min_val}")
    print(f"- Nilai max: {max_val}")
    print(f"- Range data: {max_val - min_val}")
    print(f"- Varians (s^2) data: {numerik.get_varians(data)}")
    print(f"- Standar Deviasi (sd) data: {numerik.get_standard_deviation(data)}")

    quarters = numerik.get_quarters(data)
    print("- Ukuran Penyebaran Data:")
    for i, q in enumerate(quarters):
        print(f"   - Q{i + 1}: {q}")

    skewness = numerik.get_skewness(data)
    kurtosis = numerik.get_kurtosis(data)
    arah = "kiri" if skewness > 0.01 else ("tengah" if skewness == 0.01 else "kanan")
    print(f"- Skewness: {skewness} (Kurva condong ke {arah})")
    bentuk = "runcing/leptokurtic" if round(kurtosis) > 3 else ("normal/mesokurtic" if round(kurtosis) == 3 else "datar/platykurtic")
    print(f"- Kurtosis: {kurtosis} (Kurva {bentuk})")

    print(" ")

def display_data_variables(datasets):
    labels = [d[0] for d in datasets]
    data_list = [d[1] for d in datasets]

    def row(label, values):
        print(f"- {label}:")
        for lbl, val in zip(labels, values):
            print(f"  - {lbl}: {val}")

    row("Mean",    [numerik.get_mean(d) for d in data_list])
    row("Median",  [numerik.get_median(d) for d in data_list])
    row("Modus",   [f"{numerik.get_modus(d)['value']} ({numerik.get_modus(d)['count']} data)" for d in data_list])
    row("Min",     [min(d) for d in data_list])
    row("Max",     [max(d) for d in data_list])
    row("Range",   [max(d) - min(d) for d in data_list])
    row("Varians (s^2)",      [numerik.get_varians(d) for d in data_list])
    row("Standar Deviasi",    [numerik.get_standard_deviation(d) for d in data_list])

    print("- Kuartil:")
    for i in range(3):
        row(f"  Q{i+1}", [numerik.get_quarters(d)[i] for d in data_list])

    def skew_label(s):
        return "kiri" if s > 0.01 else ("tengah" if s == 0.01 else "kanan")

    def kurt_label(k):
        r = round(k)
        return "runcing/leptokurtic" if r > 3 else ("normal/mesokurtic" if r == 3 else "datar/platykurtic")

    row("Skewness", [f"{numerik.get_skewness(d)} (condong ke {skew_label(numerik.get_skewness(d))})" for d in data_list])
    row("Kurtosis", [f"{numerik.get_kurtosis(d)} ({kurt_label(numerik.get_kurtosis(d))})" for d in data_list])


# function data kategorik
def display_kategorik(data, title):
    print(title)

    unique_vals = []
    seen = []
    for v in data:
        if v not in seen:
            seen.append(v)
            unique_vals.append(v)

    counts = {v: data.count(v) for v in unique_vals}
    total = len(data)

    print("NO | KATEGORI | FREK | FREK %")
    for i, v in enumerate(unique_vals):
        pct = (counts[v] / total) * 100
        print(f"{i + 1}. | {v} | {counts[v]} | {pct:.2f} %")

    modus_val = max(counts, key=counts.get)
    print(f"- Modus: {modus_val} ({counts[modus_val]} data)")
    print(" ")


# perhitungan data numerik
# display_data(math_score(), "---MATH SCORE---")
# display_data(reading_score(), "---READING SCORE---")
# display_data(writing_score(), "---WRITING SCORE---")
display_data_variables([
    ("Math Score",    math_score()),
    ("Reading Score", reading_score()),
    ("Writing Score", writing_score()),
])

# data kategorik
# display_kategorik(parental_education(), "---PARENTAL LEVEL OF EDUCATION---")

# tabel distribusi frekuensi
print("---TABEL DISTRIBUSI FREKUENSI MATH SCORE---")
frekuensi.to_interval_table(math_score())["display_table"]()
# print()
# print("---TABEL DISTRIBUSI FREKUENSI READING SCORE---")
# frekuensi.to_interval_table(reading_score())["display_table"]()
# print()
# print("---TABEL DISTRIBUSI FREKUENSI WRITING SCORE---")
# frekuensi.to_interval_table(writing_score())["display_table"]()

vis.display_histogram(math_score(), frekuensi)

edu_list = parental_education()
math_list = math_score()

chart.display_education_bar_chart(edu_list, math_list)