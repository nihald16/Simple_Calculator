from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        a=(request.POST['num1'])
        b=eval(a)

        return render(request,'result.html',{'key':b})
    return render(request,'index.html')

def res(request):
    return render(request,'result.html')