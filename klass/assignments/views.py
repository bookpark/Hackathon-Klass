from django.shortcuts import render

from .models import Assignment


def assignment_list(request):
    asm_lists = Assignment.objects.all()
    context = {
        'asm_lists': asm_lists,
    }
    return render(request, 'assignment/assignment_list.html', context)
