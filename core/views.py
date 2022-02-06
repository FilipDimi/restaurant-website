from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import MealCategory, Side, Meal, Special, BeverageCategory, Beverage, Soup, Dessert

import random


# Helper Functions
def modify_today_specials_menu(temp_model, pk, is_it_special):
    temp_query = temp_model.objects.get(pk=pk)
    temp_query.is_today_special = is_it_special
    temp_query.save()


def home(request):
    return render(request, 'core/home.html')


def menu(request):
    meals_all = Meal.objects.all()
    meals_categories = MealCategory.objects.all()
    sides_all = Side.objects.all()
    sides_specials = Side.objects.filter(meal_category=MealCategory.objects.get(name="Specials"))
    beverage_categories = BeverageCategory.objects.all()
    beverages_all = Beverage.objects.all()
    soups = Soup.objects.filter(is_today_special=True)
    desserts = Dessert.objects.filter(is_today_special=True)
    surprise_meal = ""
    surprise_side = ""

    try:
        special_all = Special.objects.filter(is_today_special=True)
        surprise_meal = special_all[random.randint(0, len(special_all) - 1)]
        surprise_side = sides_specials[random.randint(0, len(sides_specials) - 1)]
    except:
        pass

    if not surprise_meal:
        surprise_meal = meals_all[random.randint(0, len(meals_all) - 1)]

    passing_dict = {
        "meals_categories": meals_categories,
        "specials": special_all,
        "meals_all": meals_all,
        "sides_all": sides_all,
        "sides_specials": sides_specials,
        "beverages_all": beverages_all,
        "beverage_categories": beverage_categories,
        "surprise_meal": surprise_meal,
        "surprise_side": surprise_side,
        "soups": soups,
        "desserts": desserts
    }
    return render(request, 'core/menu.html', passing_dict)


def about(request):
    return render(request, 'core/about.html')


def catering(request):
    catering_all = Meal.objects.filter(meal_category=MealCategory.objects.get(name="Catering"))
    additional_all = Meal.objects.filter(meal_category=MealCategory.objects.get(name="Additional_Catering"))
    sides_all = Side.objects.filter(meal_category=MealCategory.objects.get(name="Catering"))

    passing_dict = {
        "catering_all": catering_all,
        "additional_all": additional_all,
        "sides_all": sides_all
    }
    return render(request, 'core/catering.html', passing_dict)


@login_required(login_url="/root_dash/login/?next=/root_dash/")
def specials_root(request):
    all_specials = Special.objects.all().order_by('meal__name')
    all_soups = Soup.objects.all().order_by('name')
    all_desserts = Dessert.objects.all().order_by('name')

    passing_dict = {
        "all_specials": all_specials,
        "all_soups": all_soups,
        "all_desserts": all_desserts
    }
    return render(request, 'core/specials_root.html', passing_dict)


@login_required(login_url="/root_dash/login/?next=/root_dash/")
def search_specials(request):
    all_specials = Special.objects.all()
    search_result = []

    if request.method == 'POST':
        if not request.POST['search_term']:
            return redirect('specials_root')
        for special in all_specials:
            if special.meal.name.lower().find(request.POST['search_term'].lower()) != -1:
                search_result.append(special)

    passing_dict = {
        "all_specials": search_result
    }
    return render(request, 'core/specials_root.html', passing_dict)


@login_required(login_url="/root_dash/login/?next=/root_dash/")
def add_special(request, pk):
    modify_today_specials_menu(Special, pk, True)
    return redirect('specials_root')


@login_required(login_url="/root_dash/login/?next=/root_dash/")
def remove_special(request, pk):
    modify_today_specials_menu(Special, pk, False)
    return redirect('specials_root')


@login_required(login_url="/root_dash/login/?next=/root_dash/")
def add_soup(request, pk):
    modify_today_specials_menu(Soup, pk, True)
    return redirect('specials_root')


@login_required(login_url="/root_dash/login/?next=/root_dash/")
def remove_soup(request, pk):
    modify_today_specials_menu(Soup, pk, False)
    return redirect('specials_root')


@login_required(login_url="/root_dash/login/?next=/root_dash/")
def add_dessert(request, pk):
    modify_today_specials_menu(Dessert, pk, True)
    return redirect('specials_root')


@login_required(login_url="/root_dash/login/?next=/root_dash/")
def remove_dessert(request, pk):
    modify_today_specials_menu(Dessert, pk, False)
    return redirect('specials_root')


