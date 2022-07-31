import tensorflow as tf
import json
def model(event, context):
 try:
    data = json.loads(event.get('body'))
    data = data['text']
    newModel = tf.keras.models.load_model('./final_model')
    predict = newModel.predict([data])
    data = float(predict[0][0][0])
    body = {
        "prediction": data
    }
    return {"statusCode":200, "body":json.dumps(body)}
 except:
     return {"statusCode":500}

