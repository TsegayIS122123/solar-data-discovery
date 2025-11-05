# Solar Data Discovery Project

## Project Overview
This project analyzes solar energy data to discover patterns, trends, and insights in solar power generation and consumption. The analysis focuses on data exploration, visualization, and preliminary findings for solar energy optimization.


## Installation & Setup

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Required Python packages (see requirements.txt)

### Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/TsegayIS122123/solar-data-discovery.git
   cd solar-data-discovery
   Install required packages:

pip install -r requirements.txt
Launch Jupyter Notebook:
jupyter notebook
Usage
Running the Analysis
Open notebooks/solar_analysis.ipynb in Jupyter

Execute cells sequentially to reproduce the analysis

Results will be displayed inline and saved in the images/ folder

Using Source Code
python
from src.data_loader import load_solar_data
from src.analysis import analyze_solar_trends

# Load data
data = load_solar_data('data/solar_samples.csv')

# Perform analysis
results = analyze_solar_trends(data)
Data Sources
Solar irradiation data

Energy production metrics

Weather correlation data

Geographical solar potential data

