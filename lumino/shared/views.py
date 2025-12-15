from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return redirect('subjects:subject-list')
    return render(request, 'index.html')
