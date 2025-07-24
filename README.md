# MTN Telecom Customer Analytics Dashboard

This project is an **interactive data dashboard** built with **Streamlit** and **Plotly**, showcasing key insights from a simulated MTN Nigeria telecom dataset. It answers 10 strategic business questions through SQL-driven analysis and intuitive visualizations.

---

## Project Objective

To help telecom stakeholders (like MTN Nigeria) make data-driven decisions by:
- Understanding customer behavior
- Identifying risk and performance trends
- Evaluating product impact
- Highlighting areas for operational improvement

---

## Dataset

The dataset (`telecom_customers.csv`) contains **10,000 rows** and includes customer-level data like:
- Demographics (Age, Gender, State)
- Subscription details (Plan type, Bill amount, Validity)
- Usage metrics (Data, Voice, SMS)
- Network experience (Call drop rate, Speed, Satisfaction)
- Behavioral patterns (Payment history, KYC, Referrals)

---

# Key Questions Answered

1. **Customer Segmentation**  
   Segmenting customers by age, gender, location, and plan type.

2. **Churn Risk Analysis**  
   Identifying customers with unpaid/overdue bills and zero activity.

3. **Top Users & Revenue Contributors**  
   Finding the highest data users and top revenue-generating customers.

4. **KYC Compliance Check**  
   Measuring KYC status against default rates.

5. **Plan Performance**  
   Comparing plan types and names based on user count and revenue.

6. **Network Quality Evaluation**  
   Analyzing call drops and quality scores by state.

7. **Payment Behavior Trends**  
   Visualizing how customers pay: bank, card, USSD, etc.

8. **Customer Support Demand**  
   Exploring ticket counts and satisfaction to flag high-need customers.

9. **Customer Loyalty and Referrals**  
   Correlating loyalty tier with referral count.

10. **Device Usage Patterns**  
   Understanding what types of devices and OS customers use.

---

## Dashboard Features

- **Interactive bar charts, pie charts, treemaps, sunbursts**
- **Hover tooltips** for added context
- **Filtering logic** built-in (e.g., only customers with ≥5 support tickets)
- **Groupby summaries** and **percent breakdowns**
- **Built with:**
  - `Streamlit`
  - `Pandas`
  - `Plotly Express`

