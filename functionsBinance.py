import functionsDynamo
import os
import pandas as pd

from datetime import *
from dateutil.relativedelta import *
from binance.client import Client
client = Client(os.environ['apiKeyBinance'], os.environ['apiSecBinance'], tld='com')

def getklineshistorial(p_symbol="BTCUSDT",p_interval='1m'):
    import time
    # CREAR TABLA SI NO EXITE
    print("--------------- REVISANDO TABLA ----------------")
    print("------------------------------------------------")   
    try:
        functionsDynamo.create_table(p_symbol+p_interval)
        print("Tabla no encontrada, se ha creado nueva tabla")
        time.sleep(10)
    except:
        print("Tabla "+(p_symbol+p_interval)+" encontrada con exito")
        
       
    dStart = datetime.now()
    nEnd = dStart + relativedelta(days=-2000)
    dateStart = date.strftime(dStart,"%d %b, %Y")
    
    
    # OBTENER REG SI EXITE SINO CREARLO  
    print("------------------------------------------------")  
    print("------------- REVISANDO HISTORIAL --------------")
    print("------------------------------------------------")     
    try:
        reg = functionsDynamo.get_reg(p_symbol+p_interval)
        dStart = datetime.strptime(reg,"%d %b, %Y")
    except:
        functionsDynamo.create_item((p_symbol+p_interval),"REGISTRO","BASE",dateStart,dateStart,dateStart,dateStart,dateStart)
        print("No hay historial previo, registro creado")  
        
    print("------------------------------------------------")    
    print("------------- OBTENIENDO HISTORIAL -------------")
    print("------------------------------------------------") 
    
    while nEnd < dStart:
        nDate = dStart + relativedelta(days=-1)
        dateStart = date.strftime(dStart,"%d %b, %Y")
        nextEnd = date.strftime(nDate,"%d %b, %Y")
        dStart = dStart + relativedelta(days=-1)
        
        frame = pd.DataFrame(client.get_historical_klines(p_symbol, p_interval,nextEnd,dateStart),
                columns = ['Open_time','Open','High','Low','Close','Volume','Close_time',
                'Quote_asset_volume','Number_of_trades','Taker_buy_base_asset_volume','Taker_buy_quote_asset_volume','Can_be_ignored'])
        frame = frame.iloc[:,:11]
        frame.Open_time = pd.to_datetime(frame.Open_time, unit='ms')
        frame.Close_time = pd.to_datetime(frame.Close_time, unit='ms')
        
        functionsDynamo.create_multiple((p_symbol+p_interval),frame,p_interval)
        
        '''for x in frame.index:
            functionsDynamo.create_item((p_symbol+p_interval),p_interval,str(frame["Open_time"][x]),frame["Open"][x],frame["High"][x],frame["Low"][x],frame["Close"][x],frame["Volume"][x])
            print("INSERTADO: "+p_symbol,p_interval,str(frame["Open_time"][x]),frame["Open"][x],frame["High"][x],frame["Low"][x],frame["Close"][x],frame["Volume"][x])'''
        functionsDynamo.create_item((p_symbol+p_interval),"REGISTRO","BASE",dateStart,dateStart,dateStart,dateStart,dateStart)
        print("Registro actualizado "+nextEnd+" - "+dateStart)
        time.sleep(2)
    return frame
    print("------------------------------------------------")   


def getklines(p_symbol,p_interval='1h',p_limit=1000):
    frame = pd.DataFrame(client.get_klines(symbol=p_symbol, interval=p_interval, limit=p_limit),
            columns = ['Open_time','Open','High','Low','Close','Volume','Close_time',
            'Quote_asset_volume','Number_of_trades','Taker_buy_base_asset_volume','Taker_buy_quote_asset_volume','Can_be_ignored'])
    frame = frame.iloc[:,:11]
    frame.Open_time = pd.to_datetime(frame.Open_time, unit='ms')
    frame.Close_time = pd.to_datetime(frame.Close_time, unit='ms')
    return frame

def getsymbolinfo(p_symbol): # PENDIENTE MEJORAR ESTRUCTURA DATOS
    frame = pd.DataFrame(client.get_symbol_info(p_symbol),
                                columns=['symbol','status','baseAsset','baseAssetPrecision',
                                        'quoteAsset','quotePrecision','quoteAssetPrecision',
                                        'baseCommissionPrecision','quoteCommissionPrecision',
                                        'orderTypes','icebergAllowed','ocoAllowed',
                                        'quoteOrderQtyMarketAllowed','allowTrailingStop',
                                        'cancelReplaceAllowed','isSpotTradingAllowed',
                                        'isMarginTradingAllowed'])
    return frame

def getaccountsnapshot(a_type): # PENDIENTE MEJORAR ESTRUCTURA DATOS
    frame = pd.DataFrame(client.get_account_snapshot(type=a_type))
    return frame

def getrecentrades(p_symbol,p_limit=1000):
    frame = pd.DataFrame(client.get_recent_trades(symbol=p_symbol,limit=p_limit))
    return frame

def getaggregatetrades(p_symbol,p_limit=1000):
    frame = pd.DataFrame(client.get_aggregate_trades(symbol=p_symbol,limit=p_limit))
    return frame
