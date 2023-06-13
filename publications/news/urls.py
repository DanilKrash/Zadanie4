from django.urls import path
from news.views import records_views, records_detail, records_create


app_name = 'records'


urlpatterns = [
    path('<int:rec_id>', records_detail, name='detail'),
    path('', records_views, name='record'),
    path('create', records_create, name='create'),
]