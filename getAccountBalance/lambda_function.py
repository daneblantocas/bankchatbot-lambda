import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ChatBot')

def lambda_handler(event, context):
    account_id = event.get('queryStringParameters', {}).get('accountId', '')
    
    if not account_id:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'accountId is required'})
        }
    
    response = table.get_item(
        Key={
            'PK': f'ACCOUNT#{account_id}',
            'SK': 'METADATA'
        }
    )
    
    item = response.get('Item')
    if not item:
        return {
            'statusCode': 404,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Account not found'})
        }
    
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({
            'name': item['name'],
            'balance': str(item['balance']),
            'accountId': account_id
        })
    }
