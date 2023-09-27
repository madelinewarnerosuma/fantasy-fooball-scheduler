import json

def lambda_handler(event, context):
    # TODO implement
    print("Event body:")
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello, first attempt at deployment!')
    }