import tensorflow as tf
import json
def model(event, context):
 try:
    data = json.loads(event.get('body'))
    data = data['text']
    newModel = tf.keras.models.load_model('./myModel',compile=False)
    predict = newModel.predict([data])
    data = float(predict[0][0])
    pred = "Suicidal" if data>=0 else "Not suicidal"
    body = {
        "prediction": pred
    }
    return {"statusCode":200, "body":json.dumps(body)}
 except:
     return {"statusCode":500}



