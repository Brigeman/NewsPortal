from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SubscriptionForm
from .models import Subscriptions
from news.models import Category
from django.contrib import messages

@login_required(login_url='/accounts/signup/')  # Декоратор для проверки аутентификации пользователя
def subscribe_categories(request):
    if request.method == 'POST':
        # Обработка POST-запроса
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            selected_categories = form.cleaned_data['categories']
            for category in selected_categories:
                subscription, created = Subscriptions.objects.get_or_create(user=request.user, category=category)
                if created:
                    messages.success(request, f"You have successfully subscribed to {category.name} category.")
            return redirect('subscription_success')  # Перенаправление на страницу успешной подписки

    else:
        # Обработка GET-запроса
        categories = Category.objects.all()
        form = SubscriptionForm()
        return render(request, 'subscriptions/subscriptions.html', {'form': form, 'categories': categories})


def subscription_success(request):
    return render(request, 'subscriptions/subscriptions_success.html')


@login_required(login_url='/accounts/signup/')
def unsubscribe_categories(request):
    if request.method == 'POST':
        selected_categories_ids = request.POST.getlist('categories')
        Subscriptions.objects.filter(user=request.user, category__id__in=selected_categories_ids).delete()
        messages.success(request, "You have successfully unsubscribed from selected categories.")
        return redirect('subscriptions')  # Перенаправление на страницу успешной отписки
    else:
        categories = Category.objects.filter(subscriptions__user=request.user)
        return render(request, 'subscriptions/unsubscribe.html', {'categories': categories})