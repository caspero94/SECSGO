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

