"""App URLs"""

# Django
from django.urls import path

from . import views

app_name: str = "aa_eveonline_sde_admin_page"  # pylint: disable=invalid-name

urlpatterns = [
    path("", views.index, name="index"),
]
