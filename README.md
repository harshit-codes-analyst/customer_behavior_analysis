Data Analytics Project
Data analytics project showcasing Customer behavior using python, SQL, and Power BI

Customer Shopping Behavior Analysis
Project Overview
This project analyzes customer shopping behavior using transactional data from 3,900 purchases across various product categories.
The goal is to uncover spending patterns, customer segments, product preferences, and subscription behavior to support data-driven business decisions.

Tools & Technologies
Python: Data loading, cleaning, and EDA (Pandas, NumPy, Matplotlib, Seaborn) SQL (PostgreSQL): Running queries and extracting business insights Power BI: Dashboard creation for visual analytics Gamma: Report and presentation design VS Code: Development environment GitHub: Version control and project documentation |

Dataset Summary
Rows: 3,900
Columns: 18
Key Features:
Customer Demographics: Age, Gender, Location, Subscription Status
Purchase Details: Item Purchased, Category, Purchase Amount, Season, Size, Color
Shopping Behavior: Discount Applied, Promo Code Used, Previous Purchases, Frequency of Purchases, Review Rating, Shipping Type
Missing Data: 37 missing values in Review Rating (handled with median imputation per category)
Data Cleaning & Feature Engineering (Python)
Performed all preprocessing using Python (pandas):

Loaded dataset and standardized column names to snake_case.
Imputed missing review_rating values using category-wise median.
Created new features:
age_group — binned customer ages into segments.
purchase_frequency_days — mapped frequency labels to numeric days.
Dropped redundant column promo_code_used.
Loaded the cleaned dataset into PostgreSQL for SQL-based business analysis.
🖼 Dashboard Preview
Below is a snapshot of the Power BI Dashboard developed for this project:

Dashboard Preview

SQL-Based Business Analysis (PostgreSQL)
Key business questions answered:

Revenue by Gender — Compare total revenue by male vs. female customers.
High-Spending Discount Users — Identify customers who used discounts but spent above average.
Top 5 Products by Rating — Find highest-rated products.
Shipping Type Comparison — Compare spending on Standard vs. Express shipping.
Subscribers vs Non-Subscribers — Analyze average spend and total revenue.
Discount-Dependent Products — Detect products relying heavily on discounts.
Customer Segmentation — Classify into New, Returning, and Loyal based on purchase history.
Top 3 Products per Category — Most-purchased products by category.
Repeat Buyers & Subscriptions — Check correlation between frequent buyers and subscriptions.
Revenue by Age Group — Find which age group contributes most to total revenue.
Power BI Dashboard
An interactive Power BI dashboard was built to visualize key findings:

KPIs: Total Revenue, Avg Order Value, Subscription Share
Charts: Revenue by Age & Gender, Top Products by Rating, Category-wise Sales
Slicers: Category, Season, Subscription Status, Age Group
Insights: Identified loyal customers, seasonal trends, and revenue-driving segments.
Business Recommendations
Boost Subscriptions — Offer exclusive benefits and early access to increase subscriber ARPU.
Loyalty Program — Introduce tiered rewards to retain returning customers.
Discount Strategy — Optimize discounts using A/B testing to protect profit margins.
Product Promotion — Highlight top-rated, high-margin products in campaigns.
Targeted Marketing — Focus on high-revenue age groups and express-shipping users
Sample Code Snippets
Python Cleaning Example:

df['review_rating'] = df.groupby('category')['review_rating'].transform(
    lambda x: x.fillna(x.median())
)
## Contact
Author: Harshit Tiwari
LinkedIn: https://www.linkedin.com/in/harshit-tiwari-aa92a3373
Email: ht725608@gmail.com
