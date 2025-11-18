from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from waves.forms import AddWaveForm

from .forms import AddEchoForm, EditEchoForm
from .models import Echo


@login_required
def echo_list(request):
    echos = Echo.objects.all()
    return render(request, 'echos/echo/list.html', {'echos': echos})


@login_required
def echo_detail(request, echo: Echo):
    waves = echo.waves.all()[:5]
    return render(request, 'echos/echo/detail.html', dict(echo=echo, waves=waves))


@login_required
def add_echo(request):
    if request.method == 'POST':
        if (form := AddEchoForm(request.user, request.POST)).is_valid():
            echo = form.save()
            messages.success(request, 'Echo added successfully')
            return redirect(echo)
    else:
        form = AddEchoForm(request.user)
    return render(request, 'echos/echo/add.html', dict(form=form))


@login_required
def edit_echo(request, echo: Echo):
    if request.user != echo.user:
        return HttpResponseForbidden('You are not the autor of this echo')

    if request.method == 'POST':
        if (form := EditEchoForm(request.POST, instance=echo)).is_valid():
            if request.user == echo.user:
                form.save()
                messages.success(request, 'Echo updated successfully')
                return redirect(echo)
    else:
        form = EditEchoForm(instance=echo)
    return render(request, 'echos/echo/edit.html', dict(echo=echo, form=form))


@login_required
def delete_echo(request, echo: Echo):
    if request.user != echo.user:
        return HttpResponseForbidden('You are not the autor of this echo')

    try:
        if request.user == echo.user:
            echo.delete()
            messages.success(request, 'Echo deleted successfully')
    except echo.DoesNotExist:
        messages.error(request, 'Echo does not exist')
    return redirect('echos:echo-list')


@login_required
def wave_list(request, echo: Echo):
    waves = echo.waves.all()
    return render(request, 'waves/wave/list.html', dict(waves=waves, echo=echo))


@login_required
def add_wave(request, echo: Echo):
    if (form := AddWaveForm(request.POST or None)).is_valid():
        form.save(request.user, echo)
        messages.success(request, 'Wave added successfully')
        return redirect(echo)
    return render(request, 'waves/wave/add.html', dict(form=form, echo=echo))
