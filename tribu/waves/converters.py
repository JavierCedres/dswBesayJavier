from django.shortcuts import get_object_or_404

from .models import Wave

class WaveConverter:
    regex = r'[\w-]+'

    def to_python(self, wave_pk: str) -> Wave:
        return get_object_or_404(Wave, pk=wave_pk)

    def to_url(self, wave: Wave) -> str:
        return wave
