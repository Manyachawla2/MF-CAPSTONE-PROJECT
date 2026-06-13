# Bluestock Mutual Fund Analytics Capstone Project

## Project Overview

This project analyzes Mutual Fund data to provide insights into fund performance, risk, assets under management (AUM), and category-wise trends. The objective is to build a complete data analytics pipeline involving data extraction, transformation, analysis, and dashboard visualization.

## Objectives

* Collect and process mutual fund datasets.
* Perform data cleaning and transformation.
* Conduct Exploratory Data Analysis (EDA).
* Analyze fund performance and risk metrics.
* Create an interactive dashboard using Power BI.
* Generate actionable insights and recommendations.

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite
* Power BI
* Git & GitHub

## Project Structure

project/

├── data/

│   ├── raw/

│   └── processed/

├── scripts/

│   ├── etl.py

│   ├── eda.py

│   ├── performance_analysis.py

│   └── run_pipeline.py

├── dashboard/

│   └── Bluestock_MF_Dashboard.pbix

├── reports/

│   ├── Final_Report.pdf

│   └── Bluestock_MF_Presentation.pptx

├── outputs/

│   ├── charts/

│   └── metrics/

├── README.md

└── requirements.txt

## Datasets Used

1. Fund Master Data

   * Fund information
   * Fund house details
   * Fund category

2. NAV History Data

   * Historical NAV values
   * Date-wise performance tracking

3. AUM Data

   * Assets Under Management
   * Fund size comparison

4. Category Mapping Data

   * Category classification
   * Fund grouping

5. Performance Data

   * Returns analysis
   * Growth trends

## ETL Pipeline

### Extract

* Read raw CSV datasets.

### Transform

* Handle missing values.
* Convert data types.
* Standardize column names.
* Create derived metrics.

### Load

* Store cleaned datasets for analysis and dashboard creation.

## Exploratory Data Analysis

Key analyses performed:

* Category-wise fund distribution
* AUM trend analysis
* NAV growth trends
* Fund house comparison
* Return distribution analysis
* Risk metric evaluation

## Dashboard Features

The Power BI dashboard includes:

* Total Funds Overview
* Category Analysis
* AUM Analysis
* NAV Performance Tracking
* Fund House Comparison
* Interactive Filters and Slicers

## Key Findings

* Equity funds dominate the mutual fund market.
* Top fund houses manage the majority of AUM.
* Certain categories consistently outperform others.
* Historical NAV trends reveal long-term growth opportunities.
* Risk and return profiles vary significantly across categories.

## How to Run the Project

### Install Dependencies

pip install -r requirements.txt

### Execute Complete Pipeline

python run_pipeline.py

### Run Individual Modules

python etl.py

python eda.py

python performance_analysis.py

## Dashboard

Open:

dashboard/Bluestock_MF_Dashboard.pbix

using Microsoft Power BI Desktop.

## Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* Power BI Dashboard
* Clean Python Scripts
* README.md
* GitHub Repository

## Future Improvements

* Real-time mutual fund data integration
* Predictive analytics using Machine Learning
* Portfolio recommendation engine
* Automated reporting dashboard

## Author

Manya Chawla

BCA, IITM

Bluestock Mutual Fund Analytics Capstone Project
