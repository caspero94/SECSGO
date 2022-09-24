import functionsDynamo
import pandas as pd
import streamlit as st
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

st.set_page_config(
    page_title="PENI CHARTS",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)
hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                .css-18e3th9 {
                padding-top: 2%;
                padding-botton: 0%;
                }
                .css-1yjuwjr {
                min-height: 0.5rem;
                font-size: 0pt;
                }
                .css-12w0qpk {
                width: calc(10% - 1rem);
                flex: none;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
activos = functionsDynamo.get_tables()
filtro_activo = st.selectbox("ACTIVOS",options=activos)
datachart = pd.DataFrame(functionsDynamo.get_chart())
datachart = datachart.drop(0)
print(datachart)



