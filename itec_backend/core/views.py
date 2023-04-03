from django.shortcuts import render
from django.http import JsonResponse
from . import api
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

#This is the views file, here are the views that called by the urls file
#each view is responsible for a task

#this is the completion view, it takes the input from the frontend and calls the gpt3 api to get
#a completion of a given phrase
@csrf_exempt
def completionApi(request):
    if request.method == 'POST':
        text = request.POST.get('promptInput')
        # text = 'Foaie verde, trandafir, am baut azi-noapte vin'
        prompt = "Scrie o poezie care începe cu: \""+text+"\""+""
        
        poem = api.generate_poem(prompt)
        poem = poem.split(' ')
        lis = []
        c = 0
        for i in range(len(poem)):
            if poem[i] == poem[i].capitalize() and len(poem[i])>1:
                nr = i+c
                lis.append(nr)
                c+=1

        for i in lis:
            poem.insert(i, '\n')

        poem = ' '.join(poem)
        url_image = api.generate_image(text)

        dic = {'poem':poem, 'img':url_image}
        return JsonResponse(dic)
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
#this is the theme view, it takes the input from the frontend and calls the gpt3 api to get
#a poem for the given theme
@csrf_exempt
def themeApi(request):
    if request.method == 'POST':
        text = request.POST.get('promptInput')
        prompt=f"Write a poem that explores the beauty and complexity of {text}. Use rich language and descriptive imagery to capture the essence of this topic, and reflect on its significance and meaning in our lives."

        poem = api.generate_poem(prompt)

        poem = poem.split(' ')
        lis = []
        c = 0
        for i in range(len(poem)):
            if poem[i] == poem[i].capitalize() and len(poem[i])>1:
                nr = i+c
                lis.append(nr)
                c+=1

        for i in lis:
            poem.insert(i, '\n')

        poem = ' '.join(poem)
        prompt_img = f"Create an image that captures the essence of {text}. Use your imagination and creativity to represent this theme in a visually striking and memorable way. Consider the colors, textures, shapes, and objects that might be associated with this theme, and use them to create a composition that is both aesthetically pleasing and thematically relevant, but do NOT draw humans."
        url_image = api.generate_image(prompt_img)

        dic = {'poem':poem, 'img':url_image}
        return JsonResponse(dic)
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
    
#this is the mirror view, it takes the input from the frontend and calls the gpt3 api to get
#a similar version of the given poem
@csrf_exempt
def mirrorApi(request):
    if request.method == 'POST':
        text = request.POST.get('promptInput')
        prompt="Write a poem that reflects my innermost thoughts and feelings. Use imagery and metaphor to capture the essence of my emotions and experiences: "+text

        poem = api.generate_poem(prompt)

        poem = poem.split(' ')
        lis = []
        c = 0
        for i in range(len(poem)):
            if poem[i] == poem[i].capitalize() and len(poem[i])>1:
                nr = i+c
                lis.append(nr)
                c+=1

        for i in lis:
            poem.insert(i, '\n')

        poem = ' '.join(poem)

        url_image = api.generate_image(text)

        dic = {'poem':poem, 'img':url_image}
        return JsonResponse(dic)
    else:
        return JsonResponse({'error': 'Invalid request method'})