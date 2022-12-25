from rest_framework.serializers import ModelSerializer
from .models import Artikel

class ArtikelSerializer(ModelSerializer):
    class Meta:
        model = Artikel
        fields = ['id', 'judul', 'body', 'kategory', 'date']