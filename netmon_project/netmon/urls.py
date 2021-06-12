from django.urls import path
from . import views
from .views import DeviceListView, DeviceDetailView, DeviceCreateView, DeviceUpdateView, DeviceDeleteView

urlpatterns = [
    path('', DeviceListView.as_view(), name='netmon-home'),
    path('device/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('device/new/', DeviceCreateView.as_view(), name='device-create'),
    path('device/<int:pk>/update/', DeviceUpdateView.as_view(), name='device-update'),
    path('device/<int:pk>/delete/', DeviceDeleteView.as_view(), name='device-delete'),
    path('about/', views.about, name='netmon-about'),
]