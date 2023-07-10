from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .functions import get_openai

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = get_openai(message)
        return JsonResponse({'message':message,'response': response})
    return render(request, 'chatbot.html')