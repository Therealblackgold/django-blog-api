from django.urls import path, include
from .views import BlogViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

# http://localhost:8000/api/blogs/
router.register("blogs", BlogViewSet, basename="blogs")

# creating a url pattern
urlpatterns = [
    path('api/', include(router.urls)),
]
