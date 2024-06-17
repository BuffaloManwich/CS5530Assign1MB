import pandas as pd
from data_prep import load_data, clean_data, encode_categorical, save_clean_data
from data_analysis import split_data, perform_tests_and_save, generate_tsne, generate_heatmap
from data_visuals import plot_mean_score_by_race_lunch, plot_mean_score_by_parent_edu_prep, plot_scatter_by_gender_ethnicity

def main():
    # Data Preparation Steps
    input_filepath = 'data_raw/StudentsPerformance.csv'
    output_filepath = 'data_clean/cleaned_data.csv'

    # Load and preprocess data
    data = load_data(input_filepath)
    if data is not None:
        cleaned_data = clean_data(data)
        encoded_data = encode_categorical(cleaned_data)
        save_clean_data(encoded_data, output_filepath)

    # Data Analysis Steps
    cleaned_data_path = 'data_clean/cleaned_data.csv'
    data = load_data(cleaned_data_path)
    split_data(data)
    perform_tests_and_save(data)

    # Visualizations for each score type
    score_types = ['math score', 'reading score', 'writing score']
    for score in score_types:
        score_data = pd.read_csv(f'data_clean/clean_{score.split()[0].lower()}.csv')
        generate_tsne(score_data, score)
        generate_heatmap(score_data, score)

        # Data Visualizations
        plot_mean_score_by_race_lunch(score_data, score)
        plot_mean_score_by_parent_edu_prep(score_data, score)
        plot_scatter_by_gender_ethnicity(score_data, score)

if __name__ == "__main__":
    main()
