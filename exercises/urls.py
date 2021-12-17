from django.urls import path

from exercises import views

app_name = "exercises"


urlpatterns = [
    path("", views.index, name="index"),
    path("routines", views.RoutineList.as_view(), name="routines_list"),
    path("create", views.CreateWorkout.as_view(), name="create_workout"),
    path("active", views.UpdateWorkout.as_view(), name="active_workout"),
    path("history", views.WorkoutHistory.as_view(), name="history"),
    path(
        "<slug:exercise_id>/sets/create", views.CreateSet.as_view(), name="create_set"
    ),
    path("routines/create", views.CreateRoutine.as_view(), name="create_routine"),
]
