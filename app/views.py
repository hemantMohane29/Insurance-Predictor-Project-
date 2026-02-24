from django.shortcuts import render, HttpResponse
from django.conf import settings
import joblib
import pandas as pd
import os

# Load the trained model and the column list with proper paths
model_path = os.path.join(settings.BASE_DIR, 'linear_regression_model.pkl')
columns_path = os.path.join(settings.BASE_DIR, 'model_columns.pkl')

model = joblib.load(model_path)
model_columns = joblib.load(columns_path)

def index(requests):
    return render(requests, 'index.html')

def predict_insurance(request):
    predicted_charges = None

    if request.method == 'POST':
        # Get data directly from the form
        age = float(request.POST.get('age'))
        gender = request.POST.get('gender')
        bmi = float(request.POST.get('bmi'))
        smoker = request.POST.get('smoker')
        children = int(request.POST.get('children'))
        region = request.POST.get('region')

        # Create a dictionary of the user's data
        user_data = {
            'age': [age], 
            'bmi': [bmi],
            'children': [children], 
            'sex_male': [1 if gender == 'male' else 0],
            'smoker_yes': [1 if smoker == 'yes' else 0],
            'region_northwest': [1 if region == 'northwest' else 0],
            'region_southeast': [1 if region == 'southeast' else 0],
            'region_southwest': [1 if region == 'southwest' else 0]
        }

        # Create a DataFrame and re-order columns to match the model
        df_input = pd.DataFrame(user_data)
        df_input = df_input[model_columns]

        # Get the prediction
        predicted_charges = model.predict(df_input)[0]

    context = {
        'predicted_charges': predicted_charges
    }
    return render(request, 'index.html', context)