import json
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('planets')



def lambda_handler(event, context):
    response = table.update_item(
    Key={"id": "mercury"},
    UpdateExpression="set size=:value",
        ExpressionAttributeValues={
            ":value": "900000000km2"
        },
        ReturnValues="UPDATED_NEW"
)
    
    
    print (response)
    # TODO implement
    return {
        'statusCode': 200,
        'body': response
    }
