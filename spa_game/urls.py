from django.urls import path
from . import views
from django.urls import re_path
from django.views.generic import TemplateView

app_name = "spa_game"
urlpatterns = [
	path('api/page-data/', views.page_data, name='page_data'),
	re_path(r'^.*$', views.game_home, name="game_home"),
]