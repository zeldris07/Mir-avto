from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from catalog.models import PartList


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    extra_context = {PartList.objects.all(): 'parts'}
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'
