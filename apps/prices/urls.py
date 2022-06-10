from .views import PriceCreateView
from .views import PriceDeleteView
from .views import PriceDetailView
from .views import PriceListView
from .views import PriceUpdateView
from django.urls import path


app_name = 'prices'
urlpatterns = [
    path('', PriceListView.as_view(), name='all'),
    path('<int:pk>/detail', PriceDetailView.as_view(), name='detail'),
    path('create/', PriceCreateView.as_view(), name='create'),
    path('<int:pk>/update/', PriceUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PriceDeleteView.as_view(), name='delete'),
]
