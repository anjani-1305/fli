import requests
from .models import APIData
from django.http import JsonResponse

def fetch_and_store_data(request):
    # Fetch data from API
    api_url = 'https://api.weather.gov/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Store data in the database
        for item in data:
            api_data = APIData(
                name=item['name'],
                description=item['description'],
                # Map other fields accordingly
            )
            api_data.save()

        return JsonResponse({'message': 'Data stored successfully'})
    else:
        return JsonResponse({'error': 'Failed to fetch data from API'}, status=500)
