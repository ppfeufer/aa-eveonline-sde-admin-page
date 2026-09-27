"""Hook into Alliance Auth"""

# Django
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# Alliance Auth EVE Online SDE Admin Page
from aa_eveonline_sde_admin_page import urls


class ESDEMenuItem(MenuItemHook):
    """
    Menu item for EVE SDE
    """

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _("EVE SDE"),
            "fa-solid fa-table-list fa-fw",
            "aa_eveonline_sde_admin_page:index",
            navactive=["aa_eveonline_sde_admin_page:"],
        )

    def render(self, request):
        """Render the menu item"""

        if request.user.has_perm("eve_sde.admin_access"):
            return MenuItemHook.render(self, request)

        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """Register the menu item"""

    return ESDEMenuItem()


@hooks.register("url_hook")
def register_urls():
    """Register app urls"""

    return UrlHook(
        urls=urls, namespace="aa_eveonline_sde_admin_page", base_url=r"^eve-sde/"
    )
