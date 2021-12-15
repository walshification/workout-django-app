from django.urls import path

from exercises import views

app_name = "exercises"


urlpatterns = [
    path("", views.index, name="index"),
    path("routines", views.RoutineList.as_view(), name="routines_list"),
]
