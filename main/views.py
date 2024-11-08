from django.shortcuts import render
from django.urls import reverse

def capture_view(request):
    result_url = reverse('result')  # Get the URL path for the 'result' view
    return render(request, 'capture.html', {'result_url': result_url})

def result_view(request):
    capture_url = reverse('capture')  # Get the URL path for the 'capture' view
    return render(request, 'result.html', {'capture_url': capture_url})
