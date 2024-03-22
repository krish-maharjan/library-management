from django.urls import path
from .views import BooksViews, BookMgmtViews

urlpatterns = [
    path('archive', BooksViews.as_view()),
    path('single/<int:pk>', BookMgmtViews.as_view())
]