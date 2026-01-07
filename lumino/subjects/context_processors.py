from users.models import Profile

def subjects_list(request) -> dict:
    if request.user.is_authenticated:
        if request.user.profile.role == Profile.Role.TEACHER:
            return {'subjects': request.user.teaching.all()}
        else:
            return {'subjects': request.user.enrolled.all()}
    return {}