from django.urls import path
from .views import ProductCreateView
from .views import ProductDeleteView
from .views import ProductDetailView
from .views import ProductListView
from .views import ProductUpdateView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='all'),
    path('<int:pk>/detail', ProductDetailView.as_view(), name='detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
]
