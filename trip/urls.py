from django.urls import path
from .views import HomeView , trip_list , TripCreateView , TripDetailView , NoteDetailView , NoteListView , CreatrNoteView , UpdateNoteView , DeleteNoteView , TripUpdateView , TripDeleteView

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('dashboard/' , trip_list , name='trip-list'),
    path('dashboard/notes' , NoteListView.as_view() , name='note-list'),
    path('dashboard/trip/create' , TripCreateView.as_view() , name='trip-create'),
    path('dashboard/note/create' , CreatrNoteView.as_view() , name='note-create'),
    path('dashboard/trip/<int:pk>' , TripDetailView.as_view() , name='trip-detail'),
    path('dashboard/trip/<int:pk>/update' , TripUpdateView.as_view() , name='trip-update'),
    path('dashboard/trip/<int:pk>/delete' , TripDeleteView.as_view() , name='trip-delete'),
    path('dashboard/note/<int:pk>' , NoteDetailView.as_view() , name='note-detail'),
    path('dashboard/note/<int:pk>/update' , UpdateNoteView.as_view() , name='note-update'),
    path('dashboard/note/<int:pk>/delete' , DeleteNoteView.as_view() , name='note-delete'),
    
]