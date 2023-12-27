from django.urls import path
from .views import *



urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("login/", LoginView.as_view()),
    path('vendors/', VendorView.as_view()),
    path('vendors/<int:pk>/', VendorView.as_view()),
    path('purchase_orders/', Purchase_orderView.as_view()),
    path('purchase_orders/<int:pk>/', Purchase_orderView.as_view()),
    path('vendor_performance/', Vendor_performance_HistoryView.as_view()),
    path('vendor_performance/<int:pk>/', Vendor_performance_HistoryView.as_view()),
    path('vendors/<int:pk>/performance', VendorPerformance.as_view()),
    path('purchase_orders/<int:pk>/acknowledge', PerchaseOrderAcknowledge.as_view()),
    # acknowledgment_date can be updated by put method in purchase order
]
