import math


def get_range(data):
    return max(data) - min(data)


def to_interval_table(data):
    sorted_data = sorted(data)
    range_val = get_range(data)

    class_count = 1 + math.log2(len(data))  # nilai k
    class_width = math.ceil(range_val / class_count)  # lebar kelas

    table = [{"low": sorted_data[0], "high": sorted_data[0] + class_width - 1}]
    current_index = 0
    while table[-1]["high"] < sorted_data[-1]:
        current_index += 1
        new_low = table[current_index - 1]["high"] + 1
        table.append({"low": new_low, "high": new_low + class_width - 1})  # Membagikan berdasarkan lebar kelas

    table = [
        {
            **tb,
            "count": len([d for d in data if tb["low"] <= d <= tb["high"]]),
            "percentage": (len([d for d in data if tb["low"] <= d <= tb["high"]]) / len(data)) * 100,
        }
        for tb in table
    ]  # Menghitung frekuensi & frekuensi relatif

    return {
        "data": table,
        "display_table": lambda: display_interval_table(table),
    }


def display_interval_table(table):
    print("NO | INTERVAL | FREK | FREK %")
    for i, tb in enumerate(table):
        print(f"{i + 1}. | {tb['low']} - {tb['high']} | {tb['count']} | {tb['percentage']:.2f} %")