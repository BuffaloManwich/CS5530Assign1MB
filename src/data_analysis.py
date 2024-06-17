import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE  

def load_data(filepath):
    return pd.read_csv(filepath)

def split_data(data):
    math = data[['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score']]
    reading = data[['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'reading score']]
    writing = data[['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'writing score']]
    
    math.to_csv('data_clean/clean_math.csv', index=False)
    reading.to_csv('data_clean/clean_reading.csv', index=False)
    writing.to_csv('data_clean/clean_writing.csv', index=False)
    print("Data split into individual score files.")

def perform_tests_and_save(data):
    categories = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
    scores = ['math score', 'reading score', 'writing score']
    results = []

    for score in scores:
        for category in categories:
            if data[category].dtype == 'int64':  # Binary categorical
                group1 = data[data[category] == 0][score]
                group2 = data[data[category] == 1][score]
                t_stat, p_val = stats.ttest_ind(group1, group2)
                results.append(f"P-value for {score} vs {category}: {p_val:.5f}")
            else:  # Non-binary categorical, use ANOVA
                groups = data.groupby(category)[score].apply(list)
                f_stat, p_val = stats.f_oneway(*groups)
                results.append(f"P-value for {score} vs {category}: {p_val:.5f}")

    with open('results/p_scores.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')
            print(result)
    print("P-values saved to p_scores.txt.")

def generate_tsne(data, score_type):
    """Generate and save t-SNE plots for the given score type."""
    features = data.select_dtypes(include=[np.number])
    tsne = TSNE(n_components=2, random_state=42)
    tsne_results = tsne.fit_transform(features)

    plt.figure(figsize=(10, 6))
    plt.scatter(tsne_results[:, 0], tsne_results[:, 1], c=data[score_type], cmap='viridis')
    plt.colorbar(label=score_type.capitalize() + ' Score')  # Adding a label to the colorbar
    plt.title(f't-SNE Visualization for {score_type.capitalize()}')
    plt.xlabel('t-SNE Feature 1')  # More informative
    plt.ylabel('t-SNE Feature 2')  # More informative
    plt.savefig(f'results/tsne_{score_type.replace(" ", "_")}.png')
    plt.close()
    print(f"t-SNE plot saved for {score_type}")


def generate_heatmap(data, score_type):
    """Generate and save heatmap for correlations in the given score type."""
    numeric_data = data.select_dtypes(include=['number'])
    correlation_matrix = numeric_data.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f'Correlation Heatmap for {score_type.capitalize()}')
    plt.xlabel('Features')  # More descriptive x-label
    plt.ylabel('Features')  # More descriptive y-label
    plt.savefig(f'results/heatmap_{score_type.replace(" ", "_")}.png')
    plt.close()
    print(f"Heatmap saved for {score_type}")

