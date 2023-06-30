# Plausible Data Analysis

## Description

This project uses data from [Plausible Analytics](https://plausible.io/) to provide insights into website traffic. The project includes data fetching, processing, analysis, and visualization.

## Installation and Setup

1. Clone the repository.
   ```
   git clone https://github.com/dimsome/sismo-analytics.git
   ```
2. Navigate to the project directory.
   ```
   cd sismo-analytics
   ```
3. Create a virtual environment.
   ```
   python3.11 -m venv .venv
   ```
4. Activate the virtual environment.
   ```
   source .venv/bin/activate
   ```
5. Install the required Python packages.
   ```
   pip install -r requirements.txt
   ```
6. Create a new API Token from Plausible, create a `.env` file in the project directory and add the following environment variable:
   ```
   API_TOKEN=your_plausible_api_token
   ```

## Notebooks

The `notebooks/` directory contains the Jupyter notebooks that perform the analysis.

## Scripts

The `scripts/` directory contains Python scripts used for data fetching and processing.
