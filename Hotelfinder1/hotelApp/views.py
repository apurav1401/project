''' from django.shortcuts import render
from django.views.generic.base import TemplateView
import amadeus
# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)'''
from .forms import HotelForm
from django.views.generic.base import TemplateView
import amadeus
from amadeus import Hotels


class HotelView(TemplateView):
    template_name='form.html'
    form_class=HotelForm

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        location = request.POST.get('location' ,None)
        check_in = request.POST.get('check_in' , None)
        check_out = request.POST.get('check_out' ,None)
        hotels = Hotels('k8aoh1A2jdvL2FzowmGrM30GOffQzIbJ')
        resp = hotels.search_airport(
            check_in='2017-12-08',
            check_out='2017-12-13',
            location='DEL',
            currency='USD',
            max_rate=100)
        context['data']=resp
        return self.render_to_response(context)







