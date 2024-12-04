from django.shortcuts import render, redirect
from .models import Program


def program_list(request):
    program = Program.objects.all
    ctx = {'programs': program}
    return render(request, 'programs/program_list.html', ctx)

def program_add(request):
    title = request.POST.get('title')
    description = request.POST.get('description')

    if title and description :
        Program.objects.create(
            title=title,
            description=description,
        )
        return redirect('programs:list')

    return render(request, 'programs/program_add.html')