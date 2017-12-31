from django.shortcuts import render
from django.utils import timezone
from .models import Createpost

def list_detail (request):
    createposts = Createpost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogapp/list_detail.html', {'createposts': createposts})
    
