import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024,8,1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024,8,5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
        }
        response = requests.post(f"{API_URL}/analytics/", json=payload)
        #st.write("Status Code:", response.status_code)
        #st.write("Raw Response:", response.text)

        try:
            data = response.json()

            inf = {
                'Category': list(data.keys()),
                'Total': [data[category]['total'] for category in data],
                'Percentage': [data[category]['percentage'] for category in data]
            }
            df = pd.DataFrame(inf)
            df_sorted = df.sort_values(by=['Percentage'], ascending=False)
            st.table(df_sorted)

            st.title('Expense Breakdown by Category')
            st.bar_chart(df_sorted.set_index('Category')['Percentage'])

        except requests.exceptions.JSONDecodeError:
            st.error("Response is not valid JSON")