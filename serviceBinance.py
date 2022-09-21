import functionsBinance
import functionsDynamo
import time
coin = "BTCUSDT"
tFrame = "12h"
print("------------------------------------------------") 
print("---- INICIANDO RECOLECTOR DE "+coin+" EN "+tFrame+" ----")
print("------------------------------------------------") 
# CREAR TABLA Y REVISAR HISTORIAL
ticker = functionsBinance.getklineshistorial(coin,tFrame)
time.sleep(5)

# ACTUALIZAR 2 ULTIMAS VELAS
print("------------------------------------------------") 
print("----------- ACTUALIZAR ULTIMAS VELAS -----------")
print("------------------------------------------------") 
while True:
        ticker = functionsBinance.getklines(coin,tFrame,1)
        try:
                functionsDynamo.create_item(coin,tFrame,str(ticker["Open_time"][0]),ticker["Open"][0],ticker["High"][0],ticker["Low"][0],ticker["Close"][0],ticker["Volume"][0])
                print("- ACTUALIZANDO: "+coin,tFrame,str(ticker["Open_time"][0]),ticker["Open"][0],ticker["High"][0],ticker["Low"][0],ticker["Close"][0],ticker["Volume"][0]+" -")
        except:
                print("------------ ERROR INSERTANDO DATOS ------------")
        time.sleep(5)
