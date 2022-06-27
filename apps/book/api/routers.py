from rest_framework.routers import DefaultRouter
from apps.book.api.api import *

router = DefaultRouter()
router.register('book_list', BookListViewSets, basename="book_list")
router.register('book', BookViewSets, basename="book")
urlpatterns = router.urls
