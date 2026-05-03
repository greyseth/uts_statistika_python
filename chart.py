import matplotlib.pyplot as plt

def display_education_bar_chart(edu_data, math_data):
    grouped_data = {}
    for edu, score in zip(edu_data, math_data):
        if edu not in grouped_data:
            grouped_data[edu] = []
        grouped_data[edu].append(score)
    
    avg_scores = {}
    for edu, scores in grouped_data.items():
        avg_scores[edu] = sum(scores) / len(scores)
    
    sorted_items = sorted(avg_scores.items(), key=lambda x: x[1])
    categories = [item[0] for item in sorted_items]
    averages = [item[1] for item in sorted_items]

    plt.figure(figsize=(12, 7))
    
    bars = plt.barh(categories, averages, color='#4472C4', height=0.6)

    plt.title("BAR CHART MATH SCORE BERDASARKAN PARENTS' LEVEL OF EDUCATION", fontsize=11, pad=20)
    plt.xlabel('Average of math score', fontsize=10)
    
    plt.grid(axis='x', linestyle='-', alpha=0.5)
    
    plt.xlim(58, 72)

    # Menghilangkan garis frame atas dan kanan
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.2, bar.get_y() + bar.get_height()/2, 
                 f'{width:.2f}', va='center', fontsize=9)

    plt.tight_layout()
    plt.show()