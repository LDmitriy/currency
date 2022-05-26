from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User


class MyProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'my_profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    def get_object(self, queryset=None):
        return self.request.user
