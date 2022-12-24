import sqlalchemy as sa
import pandas as pd
import streamlit as st
import mplfinance
import datetime
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
engine= sa.create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                     .format(user= "root",
                            pw= "ghar123+bi",
                            db= "mango"))

dataset= pd.read_sql(""" SELECT * from mango.stocks_report WHERE DATE(report_date) >= 
                     (SELECT max(DATE(report_date))from mango.stocks_report);""",engine)
engine.dispose()   
dataset= dataset.loc[:,['description','size','color','section','subfamily','brand','min',
                        'max','current_stock','total_requested','requested_to_order',
                        'current_stock_value','three_month_revenue','three_month_sales',
                        'three_month_profit','ordered_stock_value','product_mix','drivers','report_date','stock_cost']]
                  
dataset['report_date']= pd.to_datetime(dataset['report_date'])
dataset['three_month_cogs']= dataset['stock_cost']* dataset['three_month_sales']
all_subfamily= dataset.subfamily.unique()
all_section= dataset.section.unique()
all_brand= dataset.brand.unique()
all_items= dataset.description.unique()
all_drivers= dataset.drivers.unique()
all_abc= dataset.product_mix.unique()


def table_vis():
    with st.sidebar:
        st.write("Busnis overview")
        segment0 = st.selectbox("Select Segment",["---","all_drivers","all_brand","all_section","all_items","all_subfamily"])
    if segment0=="all_items":
        st.write(all_items)
    elif segment0=="all_drivers":
            st.write(all_drivers)
    elif segment0=="all_brand":
            st.write(all_brand)
    elif segment0=="all_section":
            st.write(all_section)
    elif segment0=="all_subfamily":
            st.write(all_subfamily)
table_vis()

with st.sidebar:
    st.write("Data for visualization:")
    segment1 = st.selectbox("Data for Pie",["---","all_abc","all_drivers","all_brand","all_section","all_items","all_subfamily"])
if segment1=="---":
    a=1
with st.sidebar:
    segment2 = st.selectbox("Choose X",["---","all_abc","all_drivers","all_brand","all_section","all_items","all_subfamily"])

table_vis()










