from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Post


# fixme
@login_required(login_url='member:login')
def document_list(request):
    post_list = Post.objects.filter(type='DOC', is_active=True)
    context = {
        "post_list": post_list,
    }
    return render(request, 'post/document_list.html', context)


# fixme
@login_required(login_url='member:login')
def rec_list(request):
    record_list = Post.objects.filter(type='REC', is_active=True)
    context = {
        "rec_list": record_list,
    }
    return render(request, 'post/rec_list.html', context)


@login_required(login_url='member:login')
def question_list(request):
    qst_list = Post.objects.filter(type='QST', is_active=True)
    context = {
        "question_list": qst_list
    }
    return render(request, 'post/qst_list.html', context)
