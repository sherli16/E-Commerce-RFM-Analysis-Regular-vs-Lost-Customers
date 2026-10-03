# E-Commerce Customer Segmentation Dashboard - RFM Analysis

## Project Overview
* This project segments e-commerce customers using RFM (Recency, Frequency, Monetary) analysis to identify valuable customers and churned customers.

* An interactive Power BI Dashboard was built to visualize customer distribution and revenue contribution by segment.

## Key Insights
- 90K (90.48%) Customers are identified as LOST segment - High Recency, Low Frequency
- LOST customers contributed 90.48% of Total Historical Revenue ($16.01M)
- Only 1K (1.14%) are Regular Customers generating $182.28K revenue
- 8K customers are classified as Normal Customers
- Business Problem Identified: Heavy churn - urgent need for re-engagement campaigns for Lost segment.

## RFM Logic Used
- Recency: Days since last purchase
- Frequency: Total number of purchases
- Monetary: Total spend

Segmentation Rules:
- Regular Customer: Low Recency + High Frequency + High Monetary
- Normal Customer: Medium Recency + Medium Frequency
- Lost Customer: High Recency + Low Frequency

## Dashboard Features
1. KPI Cards:
   - Count of customer_id (Total Customers - 99.44K)
   - Total Revenue (SUM of Monetary - 16.01M)
   - Regular Revenue (SUM of Monetary with Regular Filter - 182.28K)

2. Visuals:
   - Customer Count by Segment (Bar Chart)
   - Revenue Contribution by Segment (Donut Chart)

## Tech Stack
- Power BI Desktop
- DAX - SUM(), DISTINCTCOUNT(), CALCULATE()
- Data Cleaning & RFM Scoring
- E-Commerce Transaction Data

## Repository Structure
- data - Raw transaction data
- E-Commerce RFM Dashboard.pbix - Power BI file
- README.md

## How to Use
1. Download the .pbix file
2. Open in Power BI Desktop
3. Refresh data if needed



