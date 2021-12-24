# Work It

#### Video Demo: TK: URL

#### Description:

Work It is an exercise tracking app designed to record each of your exercise sets over time. It is a Django project with a SQLite database and some light CSS styling.

## The Structure

### The `workout` Module

The main settings are found in the `workout.settings` module and mostly contains Django defaults. A few of the settings (like timezone and login URL were added to leverage Django's out-of-the-box functionality.  I installed two "apps" beyond the defaults: the `exercises` app, which I wrote, and [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/) to make styling forms and templates a little easier.

Account management URLs (registration, login, and logout) can be found in the `workout.urls` module, though the views that they pass requests to are in the `exercises` app. I put them there because the `workout` module didn't come with a `views` module out-of-the-box, but upon reflection, I think it would make more sense to add one so the account management logic stays separate from the exercise tracking logic and keeping each more modular in design. But I was working fast.

I used Django's `User` model to handle authentication and authorization, as well as a way of associating a user's created routines and workouts with them. It was by far the easiest thing to do.

### Static Assets

The project has a fun emoji-based favicon (the flexing muscle arm) and a single CSS stylesheet. Django's templating system allowed me to get away with quite a lot without too much trouble, and I found light Bootstrap touches gave the project a polished look without too much trouble.

### The `exercises` App

This is where the app's core functionality lives.

#### The Models

There are five models for this app:
* Routine
* AbstractExercise
* Workout
* Set
* Exercise

Users can define there own `routine` that holds references to many `abstract exercises` (that is, just the name of the exercise). Users can then create a `workout` based on that `routine` that holds references to `exercise` instances of those `abstract exercises`. The `exercise` instances keep track of the sets (weight and reps) for a given workout. I also added

```
User --< Routine --< AbstractExercise
 |        v
 |        |
  `----< Workout --< Exercise >--< Set
```

I created the `AbstractExercise` because I realized the `Routine` needed, essentially, an exercise template, and a separate model would be needed to handle particular instances of a user _performing_ the exercise. This allowed my logic in the views to remain eaasier to read and intuitive than if the routines and workouts had shared the same exercise model.

I wrote utility functions on two of the models to make displaying them easier in the templates while keeping that presentational logic outside of the templates. `Routine` got a `__str__` method, and `Exercise` got a `set_summary` property that was very handy for the `history` page.

#### The Views

At 190 lines, this is the longest file I wrote completely. I leaned heavily on Django's native toolset to develop a lot of complex behavior very quickly.

`Register` handles the form submissions for new users and logs them in, redirecting to the index page.

`index` shows the button to start a new workout.

`RoutineList` shows a list of the user's created Routines and their exercises.

`CreateRoutine` handles form submissions when users create a new routine. These then become available in the workout form. Redirects to the create workout form.

`CreateWorkout` handles the form submissions when users want to start a new workout. The form is populated with their routines, allowing them to start a workout based on that routine. When submitted, any existing workouts that have not been completed are marked as completed, and a new `Workout` is created along with new `Exercise` instances based on the chosen routine's abstract exercises. Redirects to the active workout page for that workout.

`CreateSet` handles form submissions for exercise sets. It displays a form for weight and reps and associates them with the active workout. It redirects to the active workout page and displays the updated set information for a seemless workout experience.

`UpdateWorkout` handles a workout in-progress until it is completed. It displays a form for adding sets to the active workout's exercises, marking the user's progress through the workout. To add a set, the user must go to a separate form and come back. I had hoped to make the form out of JavaScript so it was easier to add sets to exercises (or even add-on exercises) to a dynamic form, but I ran out of time. When submitted, the workout is marked as completed, and it redirects to the exercise history page.

`WorkoutHistory` displays the user's completed workouts in reverse chronological order (most recent first).

#### The Forms

Django forms are straightforward things when constructing relatively simple webpages and web forms. I relied on Django's way of doing that for simplicity. The following forms exist to manage user input:

* `CreateWorkoutForm`: Creates an active workout.
* `UpdateWorkoutForm`: Completes an active workout.
* `CreateSetForm`: Creates a completed set for an exercise in an active workout.
* `CreateRoutineForm`: Creates a routine with exercises with which a user can start a workout.

#### The URLs

Mappings for the exercise pages to their associated views. They include:

* `/exercises/` for the index.
* `/exercises/routines` for the routines list.
* `/exercises/create` to create an active workout.
* `/exercises/active` to participate in an active workout.
* `/exercises/history` to view a user's workout history.
* `/exercises/<slug:exercise_id>/sets/create` for creating an exercise's set (where `exercise_id` is the ID of the particular exercise.
* `/exercises/routines/create` for creating new routines.
