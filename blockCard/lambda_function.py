import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ChatBot')

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    account_id = body.get('accountId', '')
    reason = body.get('reason', 'Lost or stolen')
    
    if not account_id:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'accountId is required'})
        }
    
    table.update_item(
        Key={
            'PK': f'ACCOUNT#{account_id}',
            'SK': 'METADATA'
        },
        UpdateExpression='SET cardStatus = :status, blockedAt = :time, blockReason = :reason',
        ExpressionAttributeValues={
            ':status': 'BLOCKED',
            ':time': datetime.utcnow().isoformat(),
            ':reason': reason
        }
    )
    
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({
            'message': f'Card for account
