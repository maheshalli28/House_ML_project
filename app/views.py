from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from joblib import load
import numpy as np

# Load the model
model = load('./Notebooks/model.joblib')

def home(request):
    result = None  # Initialize result as None
    if request.method == 'POST':
         
        # Retrieve values from the POST request
         val1 = request.POST.get('bedrooms')
         val2 = request.POST.get('bathrooms')
         val3 = request.POST.get('floors')
         val4 = request.POST.get('yr_built')

         # Prepare data for prediction
         arr = np.array([val1, val2, val3, val4])
         arr = arr.astype(np.float64)

         # Perform prediction
         pred = model.predict([arr])
         result = str(pred).strip("[]")  # Convert to string and clean bracket
        
    # Render the page and pass the result
    return render(request, 'home.html', {'result': result})
