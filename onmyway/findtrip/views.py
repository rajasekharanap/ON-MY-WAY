from django.shortcuts import render

def post(request):
    return render(request, 'findtrip/findtrip.html')
