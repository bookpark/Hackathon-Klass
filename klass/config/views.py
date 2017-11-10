from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# fixme
@login_required(login_url='member:login')
def index(request):
    return render(request, 'index.html')
