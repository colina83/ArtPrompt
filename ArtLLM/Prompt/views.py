from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'Hi this is me'
        return JsonResponse({'message':message,'response': response})
    return render(request, 'chatbot.html')