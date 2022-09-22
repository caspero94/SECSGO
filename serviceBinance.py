import functionsBinance
import functionsDynamo
import time
coin = "BTCUSDT"
tFrame = "6h"
print("------------------------------------------------") 
print("----------- RECOLECTOR SECSGO BINANCE ----------")
print("------------------------------------------------") 
print("--------- ACTIVOS CON HISTORIAL CREADO ---------")
functionsDynamo.get_tables()
print("------------------------------------------------") 
print("------------------------------------------------") 
print("---------- INGRESA ACTIVO SELECIONADO ----------")
print("------------------------------------------------") 
coin = input()
print("------------------------------------------------") 
print("--------- INGRESA TIMEFRAME SELECIONADO --------")
print("------------------------------------------------") 
tFrame = input()

print("------------------------------------------------") 
print("---- INICIANDO RECOLECTOR DE "+coin+" EN "+tFrame+" ----")
print("------------------------------------------------") 
# CREAR TABLA Y REVISAR HISTORIAL
ticker = functionsBinance.getklineshistorial(coin,tFrame)
time.sleep(1)

# ACTUALIZAR 2 ULTIMAS VELAS
print("------------------------------------------------") 
print("----------- ACTUALIZAR ULTIMAS VELAS -----------")
print("------------------------------------------------") 
while True:
        ticker = functionsBinance.getklines(coin,tFrame,1)
        time.sleep(5)
