from django.conf.urls import include
from rest_framework import routers
from django.urls import path, include

from Book.api.views import BookCRUD
router=routers.DefaultRouter()
router.register('books', BookCRUD)
urlpatterns = [
    path('', include(router.urls)),

]
