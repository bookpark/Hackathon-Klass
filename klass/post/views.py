from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

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
def record_list(request):
    rec_list = Post.objects.filter(type='REC', is_active=True)
    context = {
        "rec_list": rec_list,
    }
    return render(request, 'post/rec_list.html', context)


@login_required(login_url='member:login')
def question_list(request):
    qst_list = Post.objects.filter(type='QST', is_active=True)
    context = {
        "qst_list": qst_list
    }
    return render(request, 'post/qst_list.html', context)


@login_required(login_url='member:login')
def document_question_detail(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
    )
    context = {
        'post': post,
    }
    return render(request, 'post/document_question_detail.html', context)


@login_required(login_url='member:login')
def record_detail(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
    )
    context = {
        'post': post,
    }
    return render(request, 'post/record_detail.html', context)
