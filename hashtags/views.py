# from rest_framework import generics
# from .models import Hashtag
# from .serializers import HashtagSerializer

# class HashtagListCreateView(generics.ListCreateAPIView):
#     queryset = Hashtag.objects.all()
#     serializer_class = HashtagSerializer

# class HashtagDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hashtag.objects.all()
#     serializer_class = HashtagSerializer


from rest_framework import viewsets
from .models import Hashtag
from .serializers import HashtagSerializer


class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
