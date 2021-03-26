from tensorflow.keras.models import load_model

new_model = load_model('nlp_model.h5',custom_objects={'KerasLayer':hub.KerasLayer})
pred_test = np.argmax(new_model.predict(X_test), axis=1)