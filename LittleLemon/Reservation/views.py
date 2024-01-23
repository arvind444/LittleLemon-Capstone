from django.shortcuts import render
from rest_framework.response import Response
from . models import Booking, Menu
from . serializers import BookingSerializer, MenuSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.
def home(request):
    return render(request, "index.html", {})


class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class SingleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
