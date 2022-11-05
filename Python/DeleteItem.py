import json
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('planets')



def lambda_handler(event, context):
    response = table.delete_item(
    Key={'id': 'earth'}
    )
    
    
    print (response)
    # TODO implement
    return {
        'statusCode': 200,
        'body': response
    }
