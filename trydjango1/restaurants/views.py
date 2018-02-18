from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForms, RestaurantLocationCreateForms

# Create your views here.


@login_required(login_url='/login/')  # login_url="/login/" we change this in settings base.py along with CBV login_url
def restaurant_createview(request):
    form = RestaurantLocationCreateForms(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated:
            instance = form.save(commit=False)
        # pre save signal here
            instance.owner = request.user
            instance.save()
        # post save signal here
            return HttpResponseRedirect('/restaurants')
        else:
            return HttpResponseRedirect('/login/')

    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)


def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    # no need to give template name here bc default set and named as per deafult class naming
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(categories__iexact=slug) |
                Q(categories__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()  # .filter(categories__iexact='paki') this filters paki restaurants.

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = RestaurantLocationCreateForms
    template_name = 'restaurants/form.html'
    success_url = '/restaurants'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # instance.save() no need to save in CBV form,automatically saved
        return super(RestaurantCreateView, self).form_valid(form)
