from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AddEchoForm, EditEchoForm
from .models import Echo


def echo_list(request):
    print(f'{request.user}')
    echos = Echo.objects.all()
    return render(request, 'echos/echo_list.html', {'echos': echos})


def echo_detail(request, echo: Echo):
    return render(request, 'echos/echo_detail.html', {'echo': echo})


@login_required
def add_echo(request):
    if request.method == 'echo':
        if (form := AddEchoForm(request.user, request.echo)).is_valid():
            echo = form.save(commit=False)
            echo.save()
            return redirect('echos:echo-list')
    else:
        form = AddEchoForm(request.user)
    return render(request, 'echos/add.html', dict(form=form))


def edit_echo(request, echo: Echo):
    if request.method == 'echo':
        if (form := EditEchoForm(request.echo, instance=echo)).is_valid():
            echo = form.save(commit=False)
            echo.save()
            return redirect('echos:echo-list')
    else:
        form = EditEchoForm(instance=echo)
    return render(request, 'echos/edit.html', dict(echo=echo, form=form))


def delete_echo(request, echo: Echo):
    try:
        messages.success(request, 'echo deleted successfully')

    except echo.DoesNotExist:
        messages.error(request, 'echo does not exist')

    echos = echo.objects.all()
    return render(request, 'echos/echo_list.html', {'echos': echos})
