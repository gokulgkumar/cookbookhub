from django.contrib.auth import login, logout, authenticate  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.contrib import messages  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from django.db.models import Q  # type: ignore
from django.contrib.auth import get_user_model  # type: ignore
from .forms import LoginAuthenticate, Userform
from .models import Recipes





def homePage(request):
    return render(request, "index.html")


@login_required
def user_dashboard(request):
    return render(request, "user_dashboard.html")


@login_required
def userappetizer(request):
    user = request.user
    recipes = Recipes.objects.filter(user=user, category="Appetizers")
    return render(request, "user_myrecipes_appetizer.html", {"recipes": recipes})


@login_required
def usermaindish(request):
    user = request.user
    recipes = Recipes.objects.filter(user=user, category="Main Dish")
    return render(request, "user_myrecipes_maindish.html", {"recipes": recipes})


@login_required
def userdessert(request):
    user = request.user
    recipes = Recipes.objects.filter(user=user, category="Dessert")
    return render(request, "user_myrecipes_dessert.html", {"recipes": recipes})


@login_required
def userview_recipe(request, id):
    user = request.user
    recipes = Recipes.objects.filter(id=id, user=user)
    return render(request, "user_recipe_view.html", {"recipes": recipes})


def recipe_view(request, id):
    recipes = Recipes.objects.filter(id=id)
    return render(request, "recipe_view.html", {"recipes": recipes})


def signupPage(request):
    if request.method == "POST":
        form = Userform(request.POST)

        if form.is_valid():
            form.save()
            message = messages.success(
                request, "Registration Successful, continue to Login"
            )
            return redirect("loginPage")
        return render(request, "signup.html", {"form": form})

    else:
        form = Userform()
    return render(request, "signup.html", {"form": form})


def loginPage(request):
    if request.method == "POST":
        form = LoginAuthenticate(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return render(request, "user_dashboard.html", {"user": user})

    else:
        form = LoginAuthenticate()

    return render(request, "login.html", {"form": form})


#


def list_allrecipes_appetizers(request):
    recipes = Recipes.objects.filter(category="Appetizers")
    return render(request, "appetizer.html", {"recipes": recipes})


def list_allrecipes_maindish(request):
    recipes = Recipes.objects.filter(category="Main Dish")
    return render(request, "maindish.html", {"recipes": recipes})


def list_allrecipes_dessert(request):
    recipes = Recipes.objects.filter(category="Dessert")
    return render(request, "dessert.html", {"recipes": recipes})


def logouts(request):
    logout(request)
    return redirect("loginPage")


@login_required
def user_recipes(request):
    recipes = Recipes.objects.all()
    return render(request, "user_recipes.html", {"recipes": recipes})


@login_required
def list_userrecipes_appetizers(request):
    recipes = Recipes.objects.filter(category="Appetizers")
    return render(request, "user_recipes_appetizer.html", {"recipes": recipes})


def search_app(request):
    user = get_user_model()
    if request.method == "GET":
        search_app = request.GET.get("searchappet", " ")
        if search_app:

            search = Recipes.objects.filter(
                Q(recipe_name__icontains=search_app)
                | Q(user__first_name__icontains=search_app)
                | Q(user__last_name__icontains=search_app)
            )
            return render(request, "user_recipes_search.html", {"recipes": search})
        else:
            return render(request, "user_recipes_search.html", {"recipes": search})
    else:
        messages.success("Sorry invalid request!!")
        return render(request, "user_dashboard.html")


@login_required
def list_userrecipes_dessert(request):
    recipes = Recipes.objects.filter(category="Dessert")
    return render(request, "user_recipes_dessert.html", {"recipes": recipes})


@login_required
def list_userrecipes_maindish(request):
    recipes = Recipes.objects.filter(category="Main Dish")
    return render(request, "user_recipes_maindish.html", {"recipes": recipes})


def logincontinue(request):
    return render(request, "logincontinue.html")


def recipesnav(request):
    return render(request, "recipes_nav.html")


@login_required
def addrecipe(request):
    user = request.user.id
    print(user)
    return render(request, "user_addrecipe.html", {"user": user})


def adding_recipe(request):
    if request.method == "POST":
        print(request.user.id)
        userid = request.user.id
        user = request.user
        recipename = request.POST["recipename"]
        category = request.POST["category"]
        incredients = request.POST["incredients"]
        nutrients = request.POST["nutrients"]
        recipe = request.POST["recipe"]
        image = request.FILES.get("image")
        print(recipename, "recipe")
        saverecipe = Recipes(
            user=user,
            recipe_name=recipename,
            category=category,
            incredients=incredients,
            nutrients=nutrients,
            recipe=recipe,
            image=image,
        )
        saverecipe.save()
        messages.success(request, "Recipe added succesfully!!")
        return render(request, "user_dashboard.html", {"user": user})
    else:
        return redirect("addrecipe")


@login_required
def updaterecipe(request):
    return render(request, "user_updateappetizer.html")


@login_required
def update_appetizer(request):
    user = request.user
    recipes = Recipes.objects.filter(category="Appetizers", user=user)
    return render(request, "user_updateappetizer.html", {"recipes": recipes})


def updaterecipe_appetizer(request, id):
    recipe = Recipes.objects.get(id=id)
    print(recipe)
    return render(request, "user_dashboard.html")


@login_required
def update_maindish(request):
    user = request.user
    recipes = Recipes.objects.filter(category="Main Dish", user=user)
    return render(request, "user_updatemaindish.html", {"recipes": recipes})


def updaterecipe_maindish(request, id):
    recipe = Recipes.objects.get(id=id)
    print(recipe)
    return render(request, "user_dashboard.html")


@login_required
def update_dessert(request):
    user = request.user
    recipes = Recipes.objects.filter(category="Dessert", user=user)
    return render(request, "user_updatedessert.html", {"recipes": recipes})


def updaterecipe_dessert(request, id):
    user = request.user
    recipe = Recipes.objects.get(id=id)
    print(recipe)
    return render(request, "user_dashboard.html")


def user_updaterecipe(request, id):
    user = request.user
    recipe = Recipes.objects.get(id=id)
    return render(request, "user_updaterecipe.html", {"recipe": recipe})


def user_update_recipe(request, id): # pylint: disable=inconsistent-return-statements
    if request.method == "POST":
        r = Recipes.objects.get(id=id)
        r.user = request.user
        r.recipe_name = request.POST["recipename"]
        r.category = request.POST["category"]
        r.incredients = request.POST["incredients"]
        r.nutrients = request.POST["nutrients"]
        r.recipe = request.POST["recipe"]
        oldImage = r.image
        print(oldImage)
        newImage = request.FILES.get("image")
        if oldImage != None and newImage == None:
            r.image = oldImage
        else:
            r.image = newImage
        if r.category == "Appetizers":
            r.save()
            return redirect("update_appetizer")
        elif r.category == "Main Dish":
            r.save()
            return redirect("update_maindish")
        else:
            r.save()
            return redirect("update_dessert")


@login_required
def delete_appetizer(request):
    user = request.user
    recipe = Recipes.objects.filter(category="Appetizers", user=user)
    return render(request, "user_deleteappetizer.html", {"recipes": recipe})


@login_required
def delete_maindish(request):
    user = request.user
    recipe = Recipes.objects.filter(category="Main Dish", user=user)
    return render(request, "user_deletemaindish.html", {"recipes": recipe})


@login_required
def delete_dessert(request):
    user = request.user
    recipe = Recipes.objects.filter(category="Dessert", user=user)
    return render(request, "user_deletedessert.html", {"recipes": recipe})


def delete_recipe(request, id):# pylint: disable=inconsistent-return-statements
    user = request.user
    recipe = Recipes.objects.get(id=id, user=user)
    print(recipe)
    if recipe.category == "Appetizers":
        recipe.delete()
        return redirect("delete_appetizer")
    elif recipe.category == "Main Dish":
        recipe.delete()
        return redirect("delete_maindish")
    else:
        recipe.delete()
        return redirect("delete_dessert")
