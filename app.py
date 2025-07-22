import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned dataset


@st.cache_data
def load_data():
    return pd.read_csv("telecom_customers.csv")


df = load_data()

# ---------------------- Sidebar Navigation ----------------------
st.sidebar.title("MTN Telecom Dashboard")
section = st.sidebar.radio("Navigate", [
    "Customer Segmentation",
    "Churn Risk Analysis",
    "Top Users & Revenue",
    "KYC Compliance",
    "Plan Performance",
    "Network Quality",
    "Payment Behavior",
    "Support Demand",
    "Customer Loyalty",
    "Device Usage"
])

# ---------------------- Customer Segmentation ----------------------
if section == "Customer Segmentation":
    st.title("Customer Segmentation")
    seg = df.groupby(['state', 'plan_type'])[
        'customer_id'].nunique().reset_index()
    seg = seg.rename(columns={'customer_id': 'customer_count'})
    fig = px.bar(seg, x='state', y='customer_count', color='plan_type',
                 title='Customer Count by State and Plan Type')
    st.plotly_chart(fig)

# ---------------------- Churn Risk Analysis ----------------------
elif section == "Churn Risk Analysis":
    st.title(" Churn Risk Analysis")
    churn_df = df[(df['payment_status'].isin(['Unpaid', 'Overdue'])) &
                  (df['data_usage_mb'] == 0) &
                  (df['voice_usage_minutes'] == 0) &
                  (df['sms_count'] == 0)]
    st.write("### Customers at High Risk of Churn")
    st.dataframe(churn_df[['customer_id', 'full_name', 'payment_status']])

# ---------------------- Top Users & Revenue ----------------------
elif section == "Top Users & Revenue":
    st.title("Top Users and Revenue Contributors")
    top_data_users = df.nlargest(10, 'data_usage_mb')
    fig1 = px.bar(top_data_users, x='full_name', y='data_usage_mb',
                  title='Top 10 Data Users', text='data_usage_mb')
    st.plotly_chart(fig1)

    revenue = df.groupby(['customer_id', 'full_name'])[
        'bill_amount'].sum().reset_index()
    top_payers = revenue.nlargest(10, 'bill_amount')
    fig2 = px.bar(top_payers, x='full_name', y='bill_amount',
                  title='Top 10 Revenue-Contributing Customers', text='bill_amount')
    st.plotly_chart(fig2)

# ---------------------- KYC Compliance ----------------------
elif section == "KYC Compliance":
    st.title("KYC Compliance Check")
    kyc_df = df.groupby('kyc_status').agg(
        total_users=('customer_id', 'count'),
        defaulters=('payment_status', lambda x: x.isin(
            ['Unpaid', 'Overdue']).sum())
    ).reset_index()
    fig = px.bar(kyc_df, x='kyc_status', y=['total_users', 'defaulters'],
                 barmode='group', title='KYC Status vs Defaulters')
    st.plotly_chart(fig)

# ---------------------- Plan Performance ----------------------
elif section == "Plan Performance":
    st.title("Plan Performance")
    plans = df.groupby(['plan_name', 'plan_type'])[
        'bill_amount'].sum().reset_index()
    fig = px.treemap(plans, path=['plan_type', 'plan_name'], values='bill_amount',
                     title='Revenue by Plan')
    st.plotly_chart(fig)

# ---------------------- Network Quality ----------------------
elif section == "Network Quality":
    st.title("Network Quality Evaluation")
    net = df.groupby('state').agg(
        avg_score=('network_quality_score', 'mean'),
        avg_drops=('call_drop_rate', 'mean')
    ).reset_index()
    fig = px.bar(net, x='state', y='avg_score',
                 title='Average Network Quality by State')
    st.plotly_chart(fig)

# ---------------------- Payment Behavior ----------------------
elif section == "Payment Behavior":
    st.title("Payment Method Trends")
    payments = df['payment_method'].value_counts().reset_index()
    payments.columns = ['payment_method', 'count']
    fig = px.pie(payments, names='payment_method', values='count',
                 title='Distribution of Payment Methods')
    fig.update_traces(textinfo='percent+label')
    st.plotly_chart(fig)

# ---------------------- Support Demand ----------------------
elif section == "Support Demand":
    st.title("Customer Support Demand")
    support = df[df['support_tickets_count'] >= 3]
    fig = px.scatter(support, x='support_tickets_count', y='customer_satisfaction',
                     color='full_name', title='Support Tickets vs Satisfaction')
    st.plotly_chart(fig)

# ---------------------- Customer Loyalty ----------------------
elif section == "Customer Loyalty":
    st.title("Loyalty and Referrals")
    loyalty = df.groupby('customer_tier').agg(
        avg_referrals=('referrals_made', 'mean'),
        total_referrals=('referrals_made', 'sum')
    ).reset_index()
    fig = px.bar(loyalty, x='customer_tier', y='total_referrals',
                 title='Total Referrals by Loyalty Tier')
    st.plotly_chart(fig)

# ---------------------- Device Usage ----------------------
elif section == "Device Usage":
    st.title("📱 Device Type and OS Usage")
    usage = df.groupby(['device_type', 'os_type'])[
        'customer_id'].count().reset_index()
    usage.rename(columns={'customer_id': 'user_count'}, inplace=True)
    fig = px.sunburst(usage, path=['device_type', 'os_type'], values='user_count',
                      title='Device Usage Patterns')
    fig.update_traces(textinfo='label+percent parent')
    st.plotly_chart(fig)
