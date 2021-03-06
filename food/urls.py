from django.conf import settings
from django.urls import  path, include
from rest_framework_nested import routers
from . import views
from django.conf.urls.static import static
from django import urls


router= routers.DefaultRouter()

router.register('category', views.MenuCategoryViewSet)
router.register('items', views.MenuItemsViewSet, basename="items")
s_path = path('chat', views.lobby)
# router.register('chat',views.lobby)
# chat = urls(r"^chat/admin/$",  views.lobby)
router.register('table', views.TableViewSet)
urlpatterns = router.urls #+ chat

# urlpatterns = [
#     path('category/', views.MenuCategoryViewSet.as_view),
#     path('items/', views.MenuItemsViewSet.as_view),
#     path('chat/', views.lobby),
#     path('table/', views.TableViewSet.as_view({'get':('list')}))
# ]