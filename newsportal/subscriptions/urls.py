from django.urls import path
from .views import subscribe_categories, subscription_success, unsubscribe_categories
from accounts.views import SignUp



urlpatterns = [
    path('', subscribe_categories, name='subscriptions'),
    path('subscriptions/success/', subscription_success, name='subscription_success'),
    path('unsubscribe/', unsubscribe_categories, name='unsubscribe_categories'),
    path('accounts/login/', SignUp.as_view(), name='login'),
]

