# Credit Scoring Project

## Overview

This project involves creating a credit scoring model for Bati Bank using eCommerce transaction data. The objective is to build models that can:

1. Classify transactions as fraudulent or non-fraudulent.
2. Assign risk probability to new customers.
3. Map risk probabilities to credit scores.
4. Predict the optimal loan amount and duration for customers.

## Project Structure

- `data/`: Contains raw data files.
- `src/`: Contains source code for data loading, EDA, feature engineering, and modeling.
- `notebooks/`: Contains Jupyter notebooks for exploratory analysis and model building.
- `tests/`: Contains unit tests for the code in `src/`.
- `.github/workflows/`: Contains CI/CD workflow configuration.
- `requirements.txt`: Lists the dependencies for the project.

## Getting Started

1. Clone the repository.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tests:
   ```bash
   pytest tests/
   ```

## Tasks

### Task 1: Data Loading and Preprocessing

- Load the eCommerce transaction data.
- Clean and preprocess the data, handling missing values and encoding categorical variables.

### Task 2: Exploratory Data Analysis (EDA)

- Perform exploratory data analysis to understand the data distribution, correlations, and identify potential features.
- Calculate Weight of Evidence (WOE) and Information Value (IV) for feature selection.

### Task 3: Feature Engineering

- Engineer new features from the existing data to improve model performance.
- Normalize and scale the features as needed.

## Weight of Evidence (WOE) and Information Value (IV) Calculation

Weight of Evidence (WOE) and Information Value (IV) are used in credit scoring for variable transformation and selection. They provide insights for feature selection and feature engineering, commonly associated with inputs for machine learning models (often logistic regression models). They are widely used in credit scoring to measure the separation of good vs bad customers.

### Advantages of WOE Transformation:

- Handles missing values.
- Handles outliers.
- Transformation is based on the logarithmic value of distributions, aligning with the logistic regression output function.
- No need for dummy variables.
- Establishes a monotonic relationship (either increase or decrease) between the independent and dependent variable using proper binning techniques.

### Task 4: Modeling

- **Model Selection and Training:**

  - Split the data into training and testing sets.
  - Choose at least two models from the following: Logistic Regression, Decision Trees, Random Forest, Gradient Boosting Machines (GBM).
  - Train the models on the training data.

- **Hyperparameter Tuning:**

  - Use techniques like Grid Search and Random Search to improve model performance.

- **Model Evaluation:**

  - Assess model performance using metrics like Accuracy, Precision, Recall, F1 Score, and ROC-AUC.

- **Develop a Model for Risk Probability:**

  - Develop a function to assign risk probability to new customers using the trained models.

- **Develop a Model for Credit Score:**

  - Map risk probabilities to credit scores using a custom mapping function.

- **Develop a Model for Loan Amount and Duration:**
  - Train regression models to predict the optimal loan amount and duration based on customer data.

## CI/CD

The project uses GitHub Actions for continuous integration and deployment. The configuration is in `.github/workflows/ci-cd.yaml`.

### Example CI/CD Configuration

```yaml
name: CI/CD

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.8"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest tests/
```
