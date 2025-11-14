from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AddEchoForm, EditEchoForm
from .models import Echo


@login_required
def echo_list(request):
    print(f'{request.user}')
    echos = Echo.objects.all()
    return render(request, 'echos/echo/list.html', {'echos': echos})


@login_required
def echo_detail(request, echo: Echo):
    return render(request, 'echos/echo/detail.html', {'echo': echo})


@login_required
def add_echo(request):
    if request.method == 'POST':
        if (form := AddEchoForm(request.user, request.POST)).is_valid():
            form.save()
            messages.success(request, 'Echo added successfully')
            return redirect('echos:echo-list')
    else:
        form = AddEchoForm(request.user)
    return render(request, 'echos/echo/add.html', dict(form=form))


def edit_echo(request, echo: Echo):
    if request.method == 'post':
        if (form := EditEchoForm(request.echo, instance=echo)).is_valid():
            form.save()
            messages.success(request, 'Echo added successfully')
            return redirect('echos:echo-list')
    else:
        form = EditEchoForm(instance=echo)
    return render(request, 'echos/echo/edit.html', dict(echo=echo, form=form))


def delete_echo(request, echo: Echo):
    try:
        messages.success(request, 'echo deleted successfully')

    except echo.DoesNotExist:
        messages.error(request, 'echo does not exist')

    echos = echo.objects.all()
    return render(request, 'echos/echo/list.html', {'echos': echos})
