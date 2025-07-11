# -*- coding: utf-8 -*-
"""Copy of SMOTE  python file

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OhY6kodTH3QD9-QB8Mb1P04ZP10FgAA7
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE

# Load the data and labels
data = pd.read_csv('/content/drive/MyDrive/Machine learning/EDA/MEDIUM.csv')
labels = pd.read_csv('/content/drive/MyDrive/Machine learning/EDA/MEDLABEL.csv')

# Separate features (X) and labels (y)
X = data.values
y = labels.values.ravel()

# Check for missing values
missing_values = np.isnan(X)
if np.any(missing_values):
    # Replace NaN values with the median
    imputer = SimpleImputer(strategy='median')
    X = imputer.fit_transform(X)

# Calculate the desired minority class size based on the sampling rate
original_minority_size = np.sum(y == 2)  # Replace '2' with your actual minority class label
desired_sampling_rate = 8.18044608418581
desired_minority_size = int(original_minority_size * desired_sampling_rate)

# Apply SMOTE with the desired minority class size
smote = SMOTE(sampling_strategy={2: desired_minority_size}, k_neighbors=5)  # Replace '2' with your actual minority class label
X_smote, y_smote = smote.fit_resample(X, y)

# Create a DataFrame for the synthetic data with labels
synthetic_data = pd.DataFrame(X_smote, columns=data.columns[:-1])  # Exclude the label column
synthetic_data['label'] = y_smote  # Add the label column

# Save the synthetic data to a CSV file with labels
synthetic_data_only = synthetic_data[~synthetic_data.index.isin(data.index)]  # Select only the synthetic data rows
synthetic_data_only.to_csv('/content/drive/MyDrive/Machine learning/EDA/SMOTE med.csv', index=False)

from google.colab import drive
drive.mount('/content/drive')