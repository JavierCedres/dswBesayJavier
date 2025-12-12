from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditProfileForm


@login_required
def user_detail(request, profile):
    userProfile = get_object_or_404(get_user_model(), username=profile)
    return render(request, 'users/user/detail.html', dict(userProfile=userProfile))


@login_required
def my_user_detail(request):
    return redirect('users:user-detail', request.user)


@login_required
def user_edit(request, profile):
    if request.user != profile.user:
        return HttpResponseForbidden('You are not the owner of this profile')

    if request.method == 'POST':
        if (form := EditProfileForm(request.POST, request.FILES, instance=profile)).is_valid():
            form.save()
            messages.success(request, 'User profile has been successfully saved')
            return redirect('users:my-user-detail')
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'users/user/edit.html', dict(form=form, profile=profile))


@login_required
def leave(request, profile):
    try:
        if profile.user.role == 'Student':
            user = profile.user
            user.delete()
            messages.success(request, 'Good bye! Hope to see you soon')
            return redirect('/')
        else:
            return HttpResponseForbidden('You are not a student')
    except user.DoesNotExist:
        messages.error(request, 'User does not exist')
    return redirect(profile.user)
