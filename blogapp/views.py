from django.shortcuts import render

def list_detail (request):
    return render (request, "blogapp/list_detail.html")
