# 📊 Survey Data Analysis with Pandas

This project analyzes survey data related to social media usage and satisfaction levels using Python libraries like `pandas` and `matplotlib`.

## 📁 Dataset

The dataset includes the following fields:
- `respondent_id`
- `age`
- `gender`
- `country`
- `education_level`
- `uses_instagram`
- `uses_twitter`
- `uses_youtube`
- `daily_usage_minutes`
- `satisfaction_level`

## 🧠 What This Project Does

- Displays basic info and summary statistics about the dataset
- Handles missing values and checks for nulls
- Calculates average, median, min, and max values for:
  - Age
  - Daily usage time
  - Satisfaction level
- Analyzes and visualizes:
  - Instagram usage by country
  - YouTube usage distribution (pie chart)
  - Correlation between daily usage and satisfaction (scatter plot)
  - Social media behavior based on gender and education level

## 📊 Visualizations Included

- Bar chart: Instagram usage by country
- Pie chart: YouTube user distribution
- Scatter plot: Daily usage vs. satisfaction level

## 🛠️ Libraries Used

- `pandas`
- `matplotlib.pyplot`

## 📦 How to Run

1. Download the `survey_data.csv` file and place it in the specified path
2. Run the Python script:  
   ```bash
   python survey_analysis.py
