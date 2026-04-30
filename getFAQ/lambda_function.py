import json

FAQS = {
    "reset_pin": "To reset your PIN, visit any BankOne ATM and select 'PIN Services', or call our 24/7 hotline on 1800-BANKONE.",
    "open_account": "To open a new account, visit your nearest BankOne branch with a valid photo ID and proof of address.",
    "transfer_limit": "Your daily transfer limit is $5,000 for online transfers. Visit a branch to request a higher limit.",
    "dispute_transaction": "To dispute a transaction, log into your BankOne app, find the transaction and tap 'Dispute'. We will investigate within 5 business days.",
    "lost_card": "If your card is lost or stolen, use this chatbot to block your card immediately, or call 1800-BANKONE 24/7."
}

def lambda_handler(event, context):
    params = event.get('queryStringParameters') or {}
    question = params.get('question', '')

    if not question:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'question parameter is required', 'available': list(FAQS.keys())})
        }

    answer = FAQS.get(question)

    if not answer:
        return {
            'statusCode': 404,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Question not found', 'available': list(FAQS.keys())})
        }

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'question': question, 'answer': answer})
    }
