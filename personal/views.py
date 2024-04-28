from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import DetailView, UpdateView

from core.models import User

from .forms import ProfileUpdateForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile_id.html'
    context_object_name = 'profile_id'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'profile_id_update_form.html'
    template_name_suffix = "_update_form"
    context_object_name = 'profile_id_update'
    fields = ['email', 'skills', 'mobile_phone']
#    form_class = ProfileUpdateForm
#    success_url = reverse_lazy('profile_id', kwargs={"pk": 2})

    # код для возврата именно на ту страницу, с которой ушли
    def dispatch(self, request, *args, **kwargs):
        print('request: ', request, 'pk: ', request.user.pk,
              'skills: ', request.user.skills)
        self.user_id = request.user.pk
        return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_id', kwargs={"pk": self.user_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.user_id
        return context
