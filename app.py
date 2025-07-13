# caprae_leadgen_fresher

# This is a basic lead generation tool for Caprae Capital's AI Readiness Challenge
# Built in under 5 hours with beginner-level code and tools

import streamlit as st
import pandas as pd
import time

# Sample Data (Since scraping Google/LinkedIn requires API or browser automation)
sample_leads = [
    {"Company": "ABC Logistics", "Website": "https://abclogistics.in", "Email": "info@abclogistics.in"},
    {"Company": "XYZ Movers", "Website": "https://xyzmovers.com", "Email": "contact@xyzmovers.com"},
    {"Company": "QuickShip", "Website": "https://quickship.io", "Email": "support@quickship.io"},
    {"Company": "ShipFast India", "Website": "https://shipfast.in", "Email": "hello@shipfast.in"},
    {"Company": "SafeMove Express", "Website": "https://safemoveexpress.com", "Email": "admin@safemoveexpress.com"}
]

# Convert to DataFrame
leads_df = pd.DataFrame(sample_leads)

# Streamlit UI
st.set_page_config(page_title="Lead Generation Tool", layout="wide")
st.title("🚀 Simple Lead Generation Tool")
st.write("This tool simulates scraping top logistics startups in India and outputs business leads.")

# Display sample leads
time.sleep(1)
st.success("Scraped 5 leads successfully!")
st.dataframe(leads_df)

# Download CSV button
csv = leads_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Leads CSV",
    data=csv,
    file_name='leads_sample.csv',
    mime='text/csv',
)

# Future Enhancements
st.markdown("""
### ✅ Future Enhancements
- Add Google/Bing scraping using `requests`, `Selenium`
- Integrate `Hunter.io` or `Clearbit` to get verified emails
- Add deduplication and domain filters
- Save to database or connect with CRMs

This version is kept intentionally simple to reflect a beginner-level (fresher) implementation.
""")
