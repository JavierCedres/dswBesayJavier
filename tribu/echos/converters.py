from django.shortcuts import get_object_or_404

from .models import Echo


class EchoConverter:
    regex = r'[\w-]+'

    def to_python(self, echo_pk: str) -> Echo:
        return get_object_or_404(Echo, pk=echo_pk)

    def to_url(self, echo: Echo) -> str:
        return echo.pk
