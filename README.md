# Credit Scoring Project

## Overview

This project involves creating a credit scoring model for Bati Bank using eCommerce transaction data.

## Project Structure

- `data/`: Contains raw data files.
- `src/`: Contains source code for data loading, EDA, feature engineering, and modeling.
- `notebooks/`: Contains Jupyter notebooks for exploratory analysis.
- `tests/`: Contains unit tests for the code in `src/`.
- `.github/workflows/`: Contains CI/CD workflow configuration.
- `requirements.txt`: Lists the dependencies for the project.

WOE and IV Calculation Plugin in Dataiku DSS
Weight of evidence (WOE) and Information value (IV) are often used in credit scoring to perform variable transformation and selection. It provides insight for feature selection and feature engineering, common associated with inputs for machine learning model (very often a logistic regression model).It is widely used in credit scoring to measure the separation of good vs bad customers.

The advantages of WOE transformation are

Handles missing values Handles outliers The transformation is based on logarithmic value of distributions. This is aligned with the logistic regression output function No need for dummy variables By using proper binning technique, it can establish monotonic relationship (either increase or decrease) between the independent and dependent variable

Credits to Sundar Krishnan for the amazing post and headstart. you can check out his codes here.

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

## CI/CD

The project uses GitHub Actions for continuous integration and deployment. The configuration is in `.github/workflows/ci-cd.yaml`.
