from django.contrib.auth.backends import ModelBackend
from users.models import CustomUser

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):  # Verifies hashed password
                return user
        except CustomUser.DoesNotExist:
            return None
        return None
