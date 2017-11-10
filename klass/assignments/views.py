from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from member.forms import User
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
