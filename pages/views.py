from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
class HomeDevoloperView(TemplateView):
    template_name = 'dasturchi.html'
class HomeSignuploginView(TemplateView):
    template_name = 'yoriqnoma.html'
class HomeLogintestView(TemplateView):
    template_name = 'logintest.html'
# class HomePasswordChangeView(TemplateView):
#     template_name = 'password_change_form.html'
# class HomePasswordDoneView(TemplateView):
#     template_name = 'password_change_done.html'
