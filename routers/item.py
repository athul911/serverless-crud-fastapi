import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ItemsTable')


def create_item(event, context):
    body = json.loads(event['body'])
    table.put_item(Item=body)
    return {
        'statusCode': 200,
        'body': json.dumps('Item created successfully')
    }


def get_item(event, context):
    item_id = event['pathParameters']['id']
    response = table.get_item(Key={'id': item_id})
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Item not found')
        }


def update_item(event, context):
    item_id = event['pathParameters']['id']
    body = json.loads(event['body'])
    table.update_item(
        Key={'id': item_id},
        UpdateExpression="SET %s = :val1" % ', '.join(map(lambda x: x + ' = :' + x, body.keys())),
        ExpressionAttributeValues={':' + k: v for k, v in body.items()}
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Item updated successfully')
    }


def delete_item(event, context):
    item_id = event['pathParameters']['id']
    table.delete_item(Key={'id': item_id})
    return {
        'statusCode': 200,
        'body': json.dumps('Item deleted successfully')
    }
