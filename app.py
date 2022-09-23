import psycopg2
from psycopg2 import Error
import pandas as pd
import streamlit as st
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
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

conn = psycopg2.connect(user="pyhthhhkvzqgfr",
                        password=os.environ['DB_PASS'],
                        host="ec2-35-168-122-84.compute-1.amazonaws.com",
                        port="5432",
                        database="d9o48u4ns2ug0a")

try:
    cur = conn.cursor()

    cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
    list_activos = cur.fetchall()
    list_activos = list(sum(list_activos,()))
    converted_list = [x.upper() for x in list_activos]
    converted_list = list(map(lambda x: x.replace('m1', ''), converted_list))
    converted_list = converted_list+converted_list+converted_list+converted_list+converted_list
    
    #with st.sidebar:
    #    st.title("PENI CHARTS BETA")
    #    filtro_activo = st.radio("ACTIVOS DISPONIBLES",options=converted_list)
    #activos_filter = st.selectbox("BTCUSDT", pd.unique(list_activos))
    #filtro_activo = converted_list[0]
    placeholder = st.empty()

        
        

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15 = st.tabs(["1M","3M","5M","15M","30M","1H","2H","4H","6H","8H","12H","1D","3D","1S","1M"])
    with tab1:
        placetab1 = st.empty()
    with tab2:
        placetab1 = st.empty()
    with tab3:
        placetab1 = st.empty()
    with tab4:
        placetab1 = st.empty()
    with tab5:
        placetab5 = st.empty()
    with tab6:
        placetab6 = st.empty()
    with tab7:
        placetab7 = st.empty()
    with tab8:
        placetab8 = st.empty()
    with tab9:
        placetab9 = st.empty()
    with tab10:
        placetab10 = st.empty()
    with tab11:
        placetab11 = st.empty()
    with tab12:
        placetab12 = st.empty()
    with tab13:
        placetab13 = st.empty()
    with tab14:
        placetab14 = st.empty()
    with tab15:
        placetab15 = st.empty()
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        placeh = st.empty()
    with col2:
        placep = st.empty()
    with col3:
        historial = st.slider("Nº DE VELAS", 10,360,60)
    with col4:
        ini_rango = st.date_input("INICIO")
    with col5:
        fin_rango = st.date_input("FIN") 
    cur.execute("SELECT * FROM "+"BTCUSDT"+" ORDER BY ID DESC LIMIT "+str(historial)+";")
    conn.commit()
    data_activo = pd.DataFrame(cur.fetchall())
    ffun=lambda x: (str(x) +(data_activo[6].iloc[0:1].to_string().replace("0 ",""))+" $")
    with placeh.container():
                    st.empty()
                    filtro_activo = st.selectbox("ACTIVOS",options=converted_list)
            
    with placetab1.container():
        while True:
            with placeholder.container():
                cur.execute("SELECT * FROM "+filtro_activo+" ORDER BY ID DESC LIMIT "+str(historial)+";")
                conn.commit()
                data_activo = pd.DataFrame(cur.fetchall())
                
                #with placeh.container():
                    #st.header((""+filtro_activo+"    ")+(data_activo[6].iloc[0:1].to_string().replace("0 ",""))+" $")
                    #filtro_activo = st.selectbox("",options=converted_list)
                
                with placep.container():
                    st.empty()
                    st.header("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  "+(data_activo[6].iloc[0:1].to_string().replace("0 ",""))+" $")
                fig = go.Figure()
                
                fig.add_trace(go.Candlestick(x=data_activo[2], open=data_activo[3], high=data_activo[4], low=data_activo[5], close=data_activo[6]))
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
                time.sleep(0)


    
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
