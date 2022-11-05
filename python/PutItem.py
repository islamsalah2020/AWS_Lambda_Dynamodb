import json
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('planets')



def lambda_handler(event, context):
    table.put_item(
    Item={'id': 'neptune', 'temp': 'spuer cool'}
    )
    
    response = {
        'message': 'item added'
    }
    print (response)
    # TODO implement
    return {
        'statusCode': 200,
        'body': response
    }
