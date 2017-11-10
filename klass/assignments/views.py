from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from member.forms import User
from .forms import AssignmentForm, SubmitAssignmentForm
from .models import Assignment, SubmitAssignment


@login_required(login_url='member:login')
def assignment_list(request):
    asm_lists = Assignment.objects.all()
    context = {
        'asm_lists': asm_lists,
    }
    return render(request, 'assignment/assignment_list.html', context)


@login_required(login_url='member:login')
def assignment_detail(request, pk):
    asm = get_object_or_404(
        Assignment,
        pk=pk,
    )
    context = {
        'asm': asm,
    }
    return render(request, 'assignment/assignment_detail.html', context)


@login_required(login_url='member:login')
def submit_assignment_list(request, pk):
    user = User.objects.get(pk=pk)
    my_asms = SubmitAssignment.objects.filter(user=user)
    context = {
        'my_asms': my_asms,
    }
    return render(request, 'assignment/submit_assignment_list.html', context)


@login_required(login_url='member:login')
def submit_assignment_detail(request, pk):
    my_asm = get_object_or_404(
        SubmitAssignment,
        pk=pk,
    )
    context = {
        'my_asm': my_asm,
    }
    return render(request, 'assignment/submit_assignment_detail.html', context)


@login_required(login_url='member:login')
def assignment_add(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment:assignment_list')
    else:
        form = AssignmentForm()
    context = {
        'form': form
    }
    return render(request, 'assignment/assignment_form.html', context)


@login_required(login_url='member:login')
def assignment_delete(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('index')
    if request.method == 'POST':
        asm = get_object_or_404(Assignment, pk=pk)
        asm.delete()
    return redirect('assignment:assignment_list')


@login_required(login_url='member:login')
def submit_assignment_add(request, pk):
    if request.method == 'POST':
        form = SubmitAssignmentForm(request.POST)
        ams = get_object_or_404(Assignment, pk=pk)
        if form.is_valid():
            submit_ams = form.save(commit=False)
            submit_ams.user = request.user
            submit_ams.assignment = ams
            submit_ams.save()
            return redirect('assignment:assignment_detail', pk=pk)
    else:
        form = SubmitAssignmentForm()
    context = {
        'form': form
    }
    return render(request, 'assignment/submit_assignment_form.html', context)


@login_required(login_url='member:login')
def submit_assignment_delete(request, pk):
    if request.method == 'POST':
        sub_asm = get_object_or_404(SubmitAssignment, pk=pk)
        if not request.user.is_superuser or not request.user.is_staff or not request.user == sub_asm.user:
            return redirect('index')
        sub_asm.delete()
    return redirect('assignment:assignment_list')
