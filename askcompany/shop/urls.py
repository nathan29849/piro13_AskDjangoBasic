from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'
urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
    path('', views.item_list),
    path('<int:pk>/', views.item_detail),  # r'^(?P<pk>\d+)/$'로도 쓸 수 있음 (같은 의미)
    # path('panda/', views.response_csv)
]