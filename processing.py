from keras import models
import numpy as np

def get_prediction(user_num):
    
    # Загрузка ранее обученной модели
    saved_model = models.load_model("model_age.keras")
    # Загрузка данных пользователей
    user_data_from_file = np.genfromtxt("X_age_test_np.csv", delimiter=",")
    
    # предсказания по возрасту из сохраненной модели
    saved_predictions = saved_model.predict(user_data_from_file)
    
    # Поиск возрастной группы пользователя
    return np.argmax(saved_predictions[int(user_num)])
