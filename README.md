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
