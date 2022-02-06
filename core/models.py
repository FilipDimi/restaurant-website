from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Side(models.Model):
    name = models.CharField(max_length=255)
    meal_category = models.ForeignKey('MealCategory', on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class MealCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def generate_html_id(self):
        valid_id = self.name.replace(" ", "").replace(".", "").replace("/", "").replace("(", "").replace(")", "").replace("1", "one").replace("'", "")
        return valid_id


class Meal(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    second_price = models.FloatField(default=-1)
    ingredients = models.ManyToManyField('Ingredient', blank=True)
    meal_category = models.ForeignKey(MealCategory, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({}) - ${}".format(self.name, self.meal_category.name, self.get_price())

    def get_price(self):
        return format(self.price, '.2f')

    def get_second_price(self):
        return format(self.second_price, '.2f')

    def check_for_ingredients_not_empty(self):
        if self.ingredients.exists():
            return True
        return False

    def get_ingredients(self):
        all_ingredients = self.ingredients.all()
        list_ingredients = ""

        for counter in range(0, len(all_ingredients)):
            if counter < len(all_ingredients) - 1:
                list_ingredients += str(all_ingredients[counter])
                list_ingredients += ", "
            else:
                list_ingredients += str(all_ingredients[counter])

        return list_ingredients


class Soup(models.Model):
    name = models.CharField(max_length=255)
    is_today_special = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(max_length=255)
    is_today_special = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Special(models.Model):
    meal = models.OneToOneField('Meal', on_delete=models.CASCADE)
    is_today_special = models.BooleanField(default=False)

    def __str__(self):
        if self.is_today_special:
            return "{} is Today's special!".format(self.meal.name)
        else:
            return self.meal.name


class BeverageCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField(blank=True, default=-1.00)

    def __str__(self):
        return "{} - ${}".format(self.name, self.get_price())

    def get_price(self):
        if self.price > -1:
            return format(self.price, '.2f')
        else:
            return ""


class Beverage(models.Model):
    beverage_category = models.ForeignKey('BeverageCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField(blank=True, default=-1)

    def __str__(self):
        return "{} ({}) - ${}".format(self.name, self.beverage_category.name, self.get_price())

    def get_price(self):
        if self.price > -1:
            return format(self.price, '.2f')
        else:
            return ""


