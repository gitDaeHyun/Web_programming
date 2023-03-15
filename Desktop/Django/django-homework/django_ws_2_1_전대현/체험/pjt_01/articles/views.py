from django.shortcuts import render

# Create your views here.
def qwer(request) :
    msg = "하하하"
    
    return render(request, 'articles/qwer.html', {'data' : msg})

def asdf(request) :
    msgs = "호호호"
    return render(request, 'articles/asdf.html',{'datas' : msgs})

