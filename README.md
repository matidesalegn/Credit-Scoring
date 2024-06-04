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
