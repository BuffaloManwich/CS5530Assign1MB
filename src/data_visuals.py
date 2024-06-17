import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_mean_score_by_race_lunch(data, score_type):
    # Convert binary to categorical labels for clarity
    data['lunch'] = data['lunch'].map({0: 'standard', 1: 'free/reduced'})

    # Ordering the racial groups alphabetically or logically
    order = sorted(data['race/ethnicity'].unique())
    plt.figure(figsize=(10, 6))
    sns.barplot(x='race/ethnicity', y=score_type, hue='lunch', data=data,
                palette={'standard': 'blue', 'free/reduced': 'red'}, order=order)
    plt.title(f'Mean {score_type.capitalize()} Scores by Race/Ethnicity and Lunch Type')
    plt.xlabel('Race/Ethnicity')
    plt.ylabel('Mean Scores')
    plt.legend(title='Lunch Type')
    plt.savefig(f'results/bar_{score_type.replace(" ", "_")}_race_lunch.png')
    plt.close()


def plot_mean_score_by_parent_edu_prep(data, score_type):
    # Convert binary to categorical labels for clarity
    data['test preparation course'] = data['test preparation course'].map({0: 'none', 1: 'completed'})

    # Ordering education levels logically
    education_order = [
        'some high school', 'high school', 'some college', 
        'associate\'s degree', 'bachelor\'s degree', 'master\'s degree'
    ]
    
    # Ensuring all categories are present for ordering
    data['parental level of education'] = pd.Categorical(
        data['parental level of education'],
        categories=education_order,
        ordered=True
    )
    
    # Plotting
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        x='parental level of education', y=score_type, 
        hue='test preparation course', data=data,
        palette={'none': 'red', 'completed': 'blue'},
        marker='o', linestyle='-'
    )
    plt.title(f'Mean {score_type.capitalize()} Scores by Parental Level of Education and Test Prep Course')
    plt.xlabel('Parental Level of Education')
    plt.xticks(rotation=-45)  # Rotate labels to improve readability
    plt.ylabel('Mean Scores')
    plt.legend(title='Test Prep Course', loc='upper left')
    plt.grid(True)  # Add grid for better readability of scales
    plt.tight_layout()  # Adjust layout to make room for label rotation
    plt.savefig(f'results/line_{score_type.replace(" ", "_")}_parent_edu_prep.png')
    plt.close()

def plot_scatter_by_gender_ethnicity(data, score_type):
    # Mapping numeric values back to categorical labels
    data['gender'] = data['gender'].map({0: 'Male', 1: 'Female'})

    # Preparing data for a color gradient based on the occurrence of scores
    # Counting occurrences for color scaling
    data['count'] = data.groupby([score_type, 'gender'])[score_type].transform('count')

    # Sorting ethnicity for consistent ordering
    data = data.sort_values(by='race/ethnicity')

    # Creating scatter plot
    fig = px.scatter(data, x='race/ethnicity', y=score_type, color='count',
                     hover_data=[score_type, 'count'],
                     color_continuous_scale='Blues',  # Using a single-color gradient for clarity
                     facet_col='gender',  # Creates two side-by-side plots for Male and Female
                     category_orders={"race/ethnicity": sorted(data['race/ethnicity'].unique())},
                     title=f'{score_type.capitalize()} Scores by Gender and Ethnicity',
                     labels={'race/ethnicity': 'Ethnicity', score_type: 'Scores', 'count': 'Occurrence Count'})

    # Customizing the layout
    fig.update_layout(xaxis_title='Ethnicity', yaxis_title=f'{score_type.capitalize()} Scores')
    fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))

    # Write to HTML for interactive use
    fig.write_html(f'results/race_gender__scatter_{score_type.replace(" ", "_")}.html')

    return fig
