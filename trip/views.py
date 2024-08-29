from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView , CreateView , DetailView , ListView , UpdateView , DeleteView
from django.urls import reverse_lazy
from .models import Trip , Note

# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip/index.html'


def trip_list(request): 
    trips = Trip.objects.filter(owner = request.user)
    context = {
        'trips':trips
    }
    return render(request , 'trip/trip_list.html' , context)


class TripCreateView(CreateView):
    model = Trip
    fields = ['city' , 'country' , 'start_date' , 'end_date']
    success_url = reverse_lazy('trip-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    

class TripDetailView(DetailView):
    model = Trip
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes        
        return context
    

class TripUpdateView(UpdateView):
    model = Trip
    fields = ['city' , 'country' , 'start_date' , 'end_date']
    success_url = reverse_lazy('trip-list')


class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    

class NoteDetailView(DetailView):
    model = Note


class NoteListView(ListView):
    model = Note
    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner = self.request.user)
        return queryset
    

class CreatrNoteView(CreateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = '__all__'

    def get_form(self):
        form =  super(CreatrNoteView , self).get_form()
        trips = Trip.objects.filter(owner = self.request.user)
        form.fields['trip'].queryset = trips
        return form
    

class UpdateNoteView(UpdateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = '__all__'

    def get_form(self):
        form =  super(UpdateNoteView , self).get_form()
        trips = Trip.objects.filter(owner = self.request.user)
        form.fields['trip'].queryset = trips
        return form
    
class DeleteNoteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

