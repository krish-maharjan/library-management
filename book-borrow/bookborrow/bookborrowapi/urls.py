from django.urls import path
from .views import BorrowView, ReturnView

urlpatterns = [
    path('book', BorrowView.as_view()),
    path('return', ReturnView.as_view())
]