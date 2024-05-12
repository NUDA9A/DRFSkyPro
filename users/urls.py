from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListAPIView, PaymentCreateAPIView, PaymentRetrieveAPIView, PaymentUpdateAPIView, \
    PaymentDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payments'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment-get'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
    path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment-delete'),
]
