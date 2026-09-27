# Standard Library
from http import HTTPStatus

# Django
from django.urls import reverse

# Alliance Auth EVE Online SDE Admin Page
from aa_eveonline_sde_admin_page.tests import BaseTestCase
from aa_eveonline_sde_admin_page.tests.utils import create_fake_user, random_id


class TestHooks(BaseTestCase):
    """
    Test the app hook into allianceauth
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up groups and users
        """

        super().setUpClass()

        # User can access
        cls.user_with_access = create_fake_user(
            character_id=random_id(),
            character_name="Jean Luc Picard",
            permissions=["eve_sde.admin_access"],
        )

        # User cannot access
        cls.user_without_access = create_fake_user(
            character_id=random_id(), character_name="Wesly Crusher"
        )

        cls.html_menu = f"""
            <li class="d-flex flex-wrap m-2 p-2 pt-0 pb-0 mt-0 mb-0 me-0 pe-0">
                <i class="nav-link fa-solid fa-table-list fa-fw fa-fw align-self-center me-3"></i>
                <a class="nav-link flex-fill align-self-center me-auto" href="{reverse('aa_eveonline_sde_admin_page:index')}">
                    EVE SDE
                </a>
            </li>
        """

    def test_render_hook_success(self):
        """
        Test should show the link to the app in the navigation to user with access

        :return:
        :rtype:
        """

        self.client.force_login(user=self.user_with_access)

        response = self.client.get(path=reverse(viewname="authentication:dashboard"))

        self.assertEqual(first=response.status_code, second=HTTPStatus.OK)
        self.assertContains(response=response, text=self.html_menu, html=True)

    def test_render_hook_fail(self):
        """
        Test should not show the link to the app in the
        navigation to user without access

        :return:
        :rtype:
        """

        self.client.force_login(user=self.user_without_access)

        response = self.client.get(path=reverse(viewname="authentication:dashboard"))

        self.assertEqual(first=response.status_code, second=HTTPStatus.OK)
        self.assertNotContains(response=response, text=self.html_menu, html=True)
