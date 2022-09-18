import os
import pandas as pd
from datetime import *
from dateutil.relativedelta import *
from binance.client import Client
client = Client(os.environ['apiKeyBinance'], os.environ['apiSecBinance'], tld='com')

dStart = datetime.now()
nEnd = dStart + relativedelta(years=-1)


def getklineshistorial(p_symbol="BTCUSDT",p_interval='1m',nEnd=(dStart + relativedelta(years=-1)),dStart=datetime.now()):

    while nEnd < dStart:
        nDate = dStart + relativedelta(days=-1)
        dateStart = date.strftime(dStart,"%d %b, %Y")
        nextEnd = date.strftime(nDate,"%d %b, %Y")
        dStart = dStart + relativedelta(days=-1)
        print(nextEnd+" - "+dateStart)
        frame = pd.DataFrame(client.get_klines(symbol=p_symbol, interval=p_interval, limit=p_limit,startTime=nextEnd,endTime=dateStart),
                columns = ['Open_time','Open','High','Low','Close','Volume','Close_time',
                'Quote_asset_volume','Number_of_trades','Taker_buy_base_asset_volume','Taker_buy_quote_asset_volume','Can_be_ignored'])
        frame = frame.iloc[:,:11]
        frame.Open_time = pd.to_datetime(frame.Open_time, unit='ms')
        frame.Close_time = pd.to_datetime(frame.Close_time, unit='ms')
        print(frame)
    return frame



def getklines(p_symbol,p_interval='1h',p_limit=1000,timeStart=,timeEnd):
    frame = pd.DataFrame(client.get_klines(symbol=p_symbol, interval=p_interval, limit=p_limit,startTime=timeStart,endTime=timeEnd),
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
