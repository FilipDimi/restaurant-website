from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('root_dash/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('about', views.about, name='about'),
    path('catering', views.catering, name='catering'),
    path('specials_root', views.specials_root, name='specials_root'),
    path('specials_root/search_specials', views.search_specials, name='search_specials'),
    path('specials_root/add_special/<int:pk>', views.add_special, name="add_special"),
    path('specials_root/remove_special/<int:pk>', views.remove_special, name="remove_special"),
    path('specials_root/add_soup/<int:pk>', views.add_soup, name="add_soup"),
    path('specials_root/remove_soup/<int:pk>', views.remove_soup, name="remove_soup"),
    path('specials_root/add_dessert/<int:pk>', views.add_dessert, name="add_dessert"),
    path('specials_root/remove_dessert/<int:pk>', views.remove_dessert, name="remove_dessert"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
