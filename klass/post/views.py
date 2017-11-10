from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm, PostForm
from .models import Post, Comment


# List Views
@login_required(login_url='member:login')
def document_list(request):
    post_list = Post.objects.filter(type='DOC', is_active=True)
    context = {
        "post_list": post_list,
    }
    return render(request, 'post/document_list.html', context)


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


# Detail Views
@login_required(login_url='member:login')
def document_question_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/document_question_detail.html', context)


@login_required(login_url='member:login')
def record_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/record_detail.html', context)


# Comment
@login_required(login_url='member:login')
def comment_create(request, post_pk):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(post.get_absolute_url())
    return redirect('index')


@login_required(login_url='member:login')
def comment_delete(request, comment_pk):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            post = get_object_or_404(Post, pk=comment.post_id)
            comment.delete()
            return redirect(post.get_absolute_url())
    return redirect('index')


@login_required(login_url='member:login')
def question_upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.type = 'QST'
            post.user = request.user
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'post/question_upload.html', context)


@login_required(login_url='member:login')
def question_delete(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        post.delete()
        return redirect(post.get_absolute_url())
    return redirect('index')


@login_required(login_url='member:login')
def post_create(request):
    if request.user.is_superuser or request.user.is_staff:
        if request.method == 'POST':
            form = PostForm(request.POST)
            form_link = form.data['link']
            if form_link:
                if not form_link[:24] == "https://gist.github.com/":
                    form.add_error('link', "https://gist.github.com/ 으로 시작하는 주소여야 합니다.")
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.type = "DOC"
                post.save()
                return redirect(post.get_absolute_url())
        else:
            form = PostForm
        context = {
            'form': form,
        }
        return render(request, 'post/document_create.html', context)
    return redirect('index')
