"""
Views for the aa_eveonline_sde_admin_page app.
"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# EVE Online SDE
from eve_sde.models import EveSDE, EveSDESection


@login_required
@permission_required("eve_sde.admin_access")
def index(request: WSGIRequest) -> HttpResponse:
    """
    Index view for the EVE SDE admin page.

    :param request:
    :return:
    """

    sections = EveSDESection.objects.all()

    # render to template
    return render(
        request=request,
        template_name="aa_eveonline_sde_admin_page/index.html",
        context={"global": EveSDE.get_solo(), "sections": sections},
    )
