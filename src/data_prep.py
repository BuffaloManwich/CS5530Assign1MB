import pandas as pd

def load_data(filepath):
    """Load the CSV data into a DataFrame."""
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def clean_data(data):
    """Clean the dataset by handling missing values."""
    cleaned_data = data.dropna()
    print("Missing values dropped.")
    return cleaned_data

def encode_categorical(data):
    """Encode categorical as binary entries."""
    data['gender'] = data['gender'].map({'male': 0, 'female': 1})
    data['lunch'] = data['lunch'].map({'free/reduced': 1, 'standard': 0})
    data['test preparation course'] = data['test preparation course'].map({'none': 0, 'completed': 1})
    print("Categorical variables encoded.")
    return data

def save_clean_data(data, output_filepath):
    """Save the cleaned and processed data to a new CSV file."""
    data.to_csv(output_filepath, index=False)
    print(f"Data saved to {output_filepath}")
