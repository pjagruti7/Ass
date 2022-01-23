from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('Living/', views.Living, name='Living'),
    path('Living/<slug:data>', views.Living, name='Livingdata'),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
