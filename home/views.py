from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    # return HttpResponse("THIS is my homePage (/)")
    context = {'name' : 'Srikanth', 'course': 'django'}
    return render(request, 'home.html',context)

def about(request):
    # return HttpResponse("THIS is my aboutPage (/about)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("THIS is my projectsPage (/projects)")
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        desc= request.POST['desc']
        # print("\n",name,"\n" ,email,"\n" , phone,"\n" , desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("Data has been written into db")
        
    # return HttpResponse("THIS is my contactPage (/contact)")
    return render(request, 'contact.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    extrainbtwnspaceremover = request.POST.get(
        'extrainbtwnspaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': "Removing Punctuations",
                  'analyzed_text': analyzed}
        djtext = analyzed

    if capfirst == "on":
        analyzed = djtext.capitalize()
        params = {'purpose': 'Capitalize first letter',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = djtext.replace(" ", "")
        params = {'purpose': 'remove space b/w a word',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'count characters', 'analyzed_text': analyzed}
        djtext = analyzed

    if extrainbtwnspaceremover == "on":
        analyzed = ""
        for i, char in enumerate(djtext):
            if djtext[i] == " " and djtext[i-1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extra in between space remover',
                  'analyzed_text': analyzed}

    if (removepunc != "on" and capfirst != "on" and uppercase != "on" and newlineremover != "on" and extraspaceremover != "on" and extrainbtwnspaceremover != "on" and charcount != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
