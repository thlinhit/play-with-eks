import json


def handler(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    print(event)

    return {"statusCode": 200, "body": json.dumps(body)}
