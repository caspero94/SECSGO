import functionsDynamo
import pandas as pd
import streamlit as st
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import datetime

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
ini = st.date_input(
    "Desde",
    datetime.date.now(datetime.now()))
fin = st.date_input(
    "Hasta",
    datetime.date(datetime.now()))

sini = str(ini)
sfin = str(fin)

st.write(sfin)

data_activo = pd.DataFrame(functionsDynamo.get_chart(filtro_activo,sini,sfin))
#data_activo = data_activo.drop(0)


fig = go.Figure()

fig.add_trace(go.Candlestick(x=data_activo["OpenTime"], open=data_activo["Open"], high=data_activo["High"], low=data_activo["Low"], close=data_activo["Close"]))
#fig.add_trace(go.Histogram(x=data_activo[7]))
fig.update_layout(
    #xaxis_title='Tiempo',
    #yaxis_title='Precio',

    height = 750,
    margin=dict(l=0, r=0, t=0, b=0,pad=0),
    xaxis_rangeslider_visible=False)
fig.update_yaxes(automargin='left+top+right',ticklabelposition="inside")
#fig.update_xaxes(automargin='left+right')
configs = dict({'modeBarButtonsToAdd':['drawline',
                            'drawopenpath',
                            'drawcircle',
                            'drawrect',
                            'eraseshape',
                        ],'scrollZoom': True})
st.plotly_chart(fig,use_container_width=True,config=configs)



