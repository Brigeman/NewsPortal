from django import forms
from news.models import Category
from .models import Subscriptions

class SubscriptionForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите категории для подписки'
    )

class UnsubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriptions
        fields = ['category']
        labels = {
            'category': 'Выберите категории для отписки'
        }