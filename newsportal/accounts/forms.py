from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)

    # добавляем функционал направления email после регистрации группе common users
        send_mail(
            subject='Добро пожаловать!',
            message=f'{user.username}, вы успешно зарегистрировались!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email])
        return user