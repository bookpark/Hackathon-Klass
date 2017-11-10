from django.shortcuts import render, get_object_or_404

from .models import Assignment


def assignment_list(request):
    asm_lists = Assignment.objects.all()
    context = {
        'asm_lists': asm_lists,
    }
    return render(request, 'assignment/assignment_list.html', context)


def assignment_detail(request, pk):
    asm = get_object_or_404(
        Assignment,
        pk=pk,
    )
    context = {
        'asm': asm,
    }
    return render(request, 'assignment/assignment_detail.html', context)