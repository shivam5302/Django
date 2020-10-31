from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'shivam', 'place': 'udr'}
    return render(request,'index2.html',params)

def analyzed(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    analyzed = ""
    punctuations = '''!(){}[]*&^%$#@?/;'\|.,<>'''
    if removepunc=="on":
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}

            return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")
#
# def charcount(request):
#     return HttpResponse("charcount")