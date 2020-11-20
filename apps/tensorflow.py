import os
import numpy as np
from werkzeug.utils import secure_filename 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import (
	Xception, preprocess_input,decode_predictions)
from tensorflow.keras.models import load_model

def load_model():
    	# load the pre-trained Keras model
	global model
	model = Xception(weights='imagenet', include_top=True)
print('**Keras Model Loading**')
load_model()
print('**KERAS MODEL LOADED**')


def getfile(request):
	# Setup file retrieve from post
	f = request.files['file']

	# Save the file to uploads folder
	basepath = os.path.dirname(__file__)
	file_path = os.path.join(
		basepath, 'Uploads', secure_filename(f.filename))
	f.save(file_path)
	return file_path


def prepare_model(image_path, model):
    	# resize the input image and preprocess it
    
    img = image.load_img(image_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # predict
    predict = model.predict(x)
    # return the processed plot
    return predict
def DataResult1():
    if request.method == 'POST':
        print(request)
        filesave2 = getfile(request)
        print(filesave2)
        preds = prepare_model(filesave2, model)

        pclass = decode_predictions(preds, top=5)
        #test prediction
        
        bad_chars=[';',':','_','!','*']
        result = str(pclass[0][0][1])

        for i in bad_chars:
            result = result.replace(i, ' ')
            result = result.title()
            
        print(result)