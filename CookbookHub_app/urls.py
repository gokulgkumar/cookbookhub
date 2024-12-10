from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # library home
    path("", views.homePage, name="homePage"),
    path("signupPage/", views.signupPage, name="signupPage"),
    path("loginPage/", views.loginPage, name="loginPage"),
    path("logouts/", views.logouts, name="logouts"),
    path("recipesnav/", views.recipesnav, name="recipesnav"),
    path("updaterecipe/", views.updaterecipe, name="updaterecipe"),
    path("update_appetizer/", views.update_appetizer, name="update_appetizer"),
    path("update_maindish/", views.update_maindish, name="update_maindish"),
    path("update_dessert/", views.update_dessert, name="update_dessert"),
    path("delete_appetizer/", views.delete_appetizer, name="delete_appetizer"),
    path("delete_maindish/", views.delete_maindish, name="delete_maindish"),
    path("delete_dessert/", views.delete_dessert, name="delete_dessert"),
    path("user_dashboard/", views.user_dashboard, name="user_dashboard"),
    path("addrecipe/", views.addrecipe, name="addrecipe"),
    path(
        "list_userrecipes_appetizers/",
        views.list_userrecipes_appetizers,
        name="list_userrecipes_appetizers",
    ),
    path(
        "list_userrecipes_dessert/",
        views.list_userrecipes_dessert,
        name="list_userrecipes_dessert",
    ),
    path(
        "list_userrecipes_maindish/",
        views.list_userrecipes_maindish,
        name="list_userrecipes_maindish",
    ),
    path(
        "updaterecipe_appetizer/<int:id>",
        views.updaterecipe_appetizer,
        name="updaterecipe_appetizer",
    ),
    path(
        "updaterecipe_maindish/<int:id>",
        views.updaterecipe_maindish,
        name="updaterecipe_maindish",
    ),
    path(
        "updaterecipe_dessert/<int:id>",
        views.updaterecipe_dessert,
        name="updaterecipe_dessert",
    ),
    path(
        "user_update_recipe/<int:id>",
        views.user_update_recipe,
        name="user_update_recipe",
    ),
    path(
        "user_updaterecipe/<int:id>", views.user_updaterecipe, name="user_updaterecipe"
    ),
    path("delete_recipe/<int:id>", views.delete_recipe, name="delete_recipe"),
    path("logincontinue/", views.logincontinue, name="logincontinue"),
    path("userappetizer/", views.userappetizer, name="userappetizer"),
    path("usermaindish/", views.usermaindish, name="usermaindish"),
    path("userdessert/", views.userdessert, name="userdessert"),
    path("userview_recipe/<int:id>", views.userview_recipe, name="userview_recipe"),
    path(
        "list_allrecipes_appetizers",
        views.list_allrecipes_appetizers,
        name="list_allrecipes_appetizers",
    ),
    path(
        "list_allrecipes_maindish",
        views.list_allrecipes_maindish,
        name="list_allrecipes_maindish",
    ),
    path(
        "list_allrecipes_dessert",
        views.list_allrecipes_dessert,
        name="list_allrecipes_dessert",
    ),
    path("recipe_view/<int:id>", views.recipe_view, name="recipe_view"),
    # GET
    path("search_app", views.search_app, name="search_app"),
    # POST
    # path('signupform',views.signupform,name='signupform'),
    path("adding_recipe", views.adding_recipe, name="adding_recipe"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
