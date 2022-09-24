import boto3
def create_table(nameTable):
    dynamodb = boto3.resource('dynamodb')
    response = dynamodb.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'Timeframe',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'OpenTime',
                'AttributeType': 'S',
            },
        ],
        KeySchema=[
            {
                'AttributeName': 'Timeframe',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'OpenTime',
                'KeyType': 'RANGE',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        },
        TableName=nameTable,
    )

def create_item(coin,tFrame,openTime,open,high,low,close,volume):
    item1 = {
        'Timeframe': tFrame,
        'OpenTime': openTime,
        'Open': open,
        'High': high,
        'Low': low,
        'Close': close,
        'Volume': volume
    }
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(coin)
    table.put_item(Item=item1)
def get_reg(TABLE_NAME):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    reg = table.get_item(
        Key={'Timeframe':'REGISTRO',
                'OpenTime':'BASE'}
        )
    rege = (reg['Item'])
    print("- Historial recuperado con fecha: "+rege['Open']+" -")
    return rege['Open']
def create_multiple(coin,frame,p_interval):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(coin)
    with table.batch_writer() as batch:
            for x in frame.index:
                content = {
                    'Timeframe': p_interval,
                    'OpenTime': str(frame["Open_time"][x]),
                    'Open':frame["Open"][x],
                    'High':frame["High"][x],
                    'Low':frame["Low"][x],
                    'Close':frame["Close"][x],
                    'Volume':frame["Volume"][x]
                    }
                batch.put_item(Item=content)
def get_tables():
    import pandas as pd
    dynamodb = boto3.resource('dynamodb')
    tables = list(dynamodb.tables.all())
    lista = ["gino234", "nor233", "lal453"]
    for x in tables:
        x = str(x).replace("dynamodb.Table(name='","")
        x = str(x).replace("')","")
        print(lista)
        listo = lista.append(str(x))
        print(listo)
    print(listo)
    #tables = pd.DataFrame (tables)
    #tables = [table.replace('dynamodb.Table','') for table in tables]
    #print(tables)
    #converted_list = [x.upper() for x in tables]
    converted_list = list(map(lambda x: x.replace('m1', ''), tables))
    print(converted_list)
    return tables
