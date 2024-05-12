from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

from users.models import Payment
from users.serializers import PaymentSerializer


# Create your views here.
class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['date', ]
    filterset_fields = ['course', ]


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
