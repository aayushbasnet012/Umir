from django.conf import settings
from django.urls import  path, include
from rest_framework_nested import routers
from . import views
from django.conf.urls.static import static


router= routers.DefaultRouter()

# router.register('category', views.MenuCategoryViewSet)
# router.register('items', views.MenuItemsViewSet, basename="items")
# cos_path = path('chat/', views.lobby)
# urlpatterns = router.urls + cos_path

urlpatterns = [
    path('category/', views.MenuCategoryViewSet.as_view({'get': 'list'})),
    path('items/', views.MenuItemsViewSet.as_view({'get': 'list'})),
    path('chat/', views.lobby)
]