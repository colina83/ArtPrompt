from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import openai

OPENAIKEY ='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'
openai.api_key = OPENAIKEY

def get_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        temperature = 0.9,
        n=1,
        stop=None,
    )
    #print(response) # Just to check the output of openai
    anwser = response.choices[0].text.strip()
    return anwser

# Create your views here.
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = get_openai(message)
        return JsonResponse({'message':message,'response': response})
    return render(request, 'chatbot.html')