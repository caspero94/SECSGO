import functionsBinance
import functionsDynamo
import time
coin = "BTCUSDT"
tFrame = "1m"
# CREATE TABLE IF NO EXITS
try:
        functionsDynamo.create_table(coin)
except:
        print("DB NAME REPEAT")
# REVISAR HISTORIAL


#####
ticker = functionsBinance.getklines(coin,tFrame,1)
        try:
                functionsDynamo.create_item(coin,tFrame,str(ticker["Open_time"][0]),ticker["Open"][0],ticker["High"][0],ticker["Low"][0],ticker["Close"][0],ticker["Volume"][0])
                print(coin,tFrame,str(ticker["Open_time"][0]),ticker["Open"][0],ticker["High"][0],ticker["Low"][0],ticker["Close"][0],ticker["Volume"][0])
        except:
                print("ERROR INSERTANDO DATOS")
        
while True:
        ticker = functionsBinance.getklines(coin,tFrame,1)
        try:
                functionsDynamo.create_item(coin,tFrame,str(ticker["Open_time"][0]),ticker["Open"][0],ticker["High"][0],ticker["Low"][0],ticker["Close"][0],ticker["Volume"][0])
                print(coin,tFrame,str(ticker["Open_time"][0]),ticker["Open"][0],ticker["High"][0],ticker["Low"][0],ticker["Close"][0],ticker["Volume"][0])
        except:
                print("ERROR INSERTANDO DATOS")
        time.sleep(5)
