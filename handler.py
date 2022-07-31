def index(event, context):
    data = ""
    with open('./index.html',mode='r') as f:
        data = f.read()

    response = {
        "statusCode": 200,
        "body": data,
        "headers": {"content-type": "text/html"}
    }
    return response
