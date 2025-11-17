from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import EditWaveForm
from .models import Wave


@login_required
def delete_wave(request, wave):
    if request.user != wave.user:
        return HttpResponseForbidden('You are not the autor of this wave')

    try:
        if request.user == wave.user:
            Wave.objects.get(pk=wave.pk).delete()
            messages.success(request, 'Wave deleted successfully')
    except wave.DoesNotExist:
        messages.error(request, 'Wave does not exist')
    return redirect(wave.echo)


@login_required
def edit_wave(request, wave):
    if request.user != wave.user:
        return HttpResponseForbidden('You are not the autor of this wave')

    if request.method == 'POST':
        if (form := EditWaveForm(request.POST, instance=wave)).is_valid():
            form.save()
            messages.success(request, 'Wave updated successfully')
            return redirect(wave.echo)
    else:
        form = EditWaveForm(instance=wave)
    return render(request, 'echos/echo/edit.html', dict(echo=wave.echo, form=form))
