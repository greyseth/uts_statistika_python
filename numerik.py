import math

def get_mean(data):
    return sum(data) / len(data)
    # sum semua data / jumlah data


def get_median(data):
    sorted_data = sorted(data)

    if len(sorted_data) % 2 == 0:
        return sorted_data[len(sorted_data) // 2]  # (n+1) / 2
    else:
        return [sorted_data[(len(sorted_data) - 1) // 2], sorted_data[len(sorted_data) // 2]]  # n/2 && (n+1)/2


def get_modus(data):
    unique_values = list({v: 0 for v in data}.keys())
    unique_values = [{"value": v, "count": 0} for v in unique_values]  # Ambil semua nilai unik

    for u in unique_values:
        for d in data:
            if d == u["value"]:
                u["count"] += 1  # Hitung jumlah kemunculan

    return max(unique_values, key=lambda x: x["count"])  # Return data dengan nilai kemunculan paling banyak


def get_varians(data):
    mean = get_mean(data)  # Xrata

    sigma = sum((d - mean) ** 2 for d in data)  # Sigma (xi - Xrata)^2
    return sigma / (len(data) - 1)  # Sigma / n-1


def get_standard_deviation(data):
    return math.sqrt(get_varians(data))  # v(s^2)


def get_quarters(data):
    sorted_data = sorted(data)  # urutkan data

    n = len(sorted_data)
    q1_index = math.floor(n * 0.25)
    q2_index = math.floor(n * 0.5)
    q3_index = math.floor(n * 0.75)  # Pembagian kuartil menggunakan fungsi floor

    return [sorted_data[q1_index], sorted_data[q2_index], sorted_data[q3_index], sorted_data[n - 1]]


def get_skewness(data):
    mean = get_mean(data)
    modus = get_modus(data)
    standard_deviation = get_standard_deviation(data)

    return (mean - modus["value"]) / standard_deviation  # (Xrata - Mo) / sd


def get_kurtosis(data):
    n = len(data)
    mean = get_mean(data)
    sd = get_standard_deviation(data)

    sigma = sum((x - mean) ** 4 for x in data)

    return sigma / (n * sd ** 4)