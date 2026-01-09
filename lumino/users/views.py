from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditProfileForm
from .models import Profile


@login_required
def user_detail(request, username):
    userProfile = get_object_or_404(get_user_model(), username=username)
    return render(request, 'users/user/detail.html', dict(userProfile=userProfile))


@login_required
def my_user_detail(request):
    return redirect(request.user.profile)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        if (
            form := EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        ).is_valid():
            form.save()
            messages.success(request, 'User profile has been successfully saved.')
            return redirect(request.user.profile)
    else:
        form = EditProfileForm(instance=request.user.profile)
    return render(request, 'users/user/edit.html', dict(form=form, profile=request.user.profile))


@login_required
def leave(request):
    if request.user.profile.role != Profile.Role.STUDENT:
        return HttpResponseForbidden('Only students can leave the platform.')

    get_user_model().objects.get(pk=request.user.pk).delete()
    messages.success(request, 'Good bye! Hope to see you soon.')
    return redirect('index')
