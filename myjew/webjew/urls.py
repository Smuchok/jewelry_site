from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all/", views.all_jew, name='all_jew'),
    path("catalog/", views.catalog, name='catalog'),
    path("catalog/<category>/", views.jews_by_catalog, name='category'),
    path("catalog/<category>/<int:jew_id>", views.jew_details, name='jew_details'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("steps/", views.steps, name="steps"),
    path("3D/", views.jew3d, name="jew3d"),

    path("test/", views.test, name='test'),

    # path("api/catalog/", views.api_catalog, name='api_catalog'),
    # path("api/catalog/<category>/", views.api_jews_by_category, name='api_category'),
]
