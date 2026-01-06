from django import template

from users.models import Profile

register = template.Library()

@register.filter
def is_student(user):
    return user.profile.role == Profile.Role.STUDENT