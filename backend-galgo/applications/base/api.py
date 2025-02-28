from django.core.serializers import get_serializer
from rest_framework import generics


# Generics list view
class GeneralListApiView(generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state = True)
