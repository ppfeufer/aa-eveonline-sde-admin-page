"""Tests for the aa_eveonline_sde_admin_page views."""

# Standard Library
from http import HTTPStatus

# Django
from django.urls import reverse
from django.utils import timezone

# EVE Online SDE
# EVE SDE
from eve_sde.models import EveSDE, EveSDESection

# Alliance Auth EVE Online SDE Admin Page
from aa_eveonline_sde_admin_page.tests import BaseTestCase
from aa_eveonline_sde_admin_page.tests.utils import create_fake_user, random_id


class IndexViewTests(BaseTestCase):
    """Tests for the index view in aa_eveonline_sde_admin_page."""

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up users and categories

        :return:
        :rtype:
        """

        super().setUpClass()

        cls.user_with_access = create_fake_user(
            character_id=random_id(),
            character_name="Jean Luc Picard",
            permissions=["eve_sde.admin_access"],
        )
        cls.user_without_access = create_fake_user(
            character_id=random_id(), character_name="Wesly Crusher"
        )

        # create the singleton global settings
        EveSDE.objects.create(build_number=42, release_date=timezone.now())

        # create a sample section to be listed in the view
        EveSDESection.objects.create(
            sde_section="Test Section",
            build_number=42,
            last_update=timezone.now(),
            total_lines=100,
            total_rows=10,
        )

    def test_index_requires_login(self):
        """Unauthenticated users are redirected when accessing the index."""

        response = self.client.get(reverse("aa_eveonline_sde_admin_page:index"))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_index_requires_admin_permission(self):
        """Logged in users without the eve_sde.admin_access permission are redirected."""

        self.client.force_login(user=self.user_without_access)

        response = self.client.get(reverse("aa_eveonline_sde_admin_page:index"))

        # Django's permission_required decorator redirects to login on failure
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_index_renders_with_global_and_sections_for_permitted_user(self):
        """A user with the eve_sde.admin_access permission sees the page with context."""

        self.client.force_login(user=self.user_with_access)

        response = self.client.get(reverse("aa_eveonline_sde_admin_page:index"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "aa_eveonline_sde_admin_page/index.html")

        # context contains the singleton global and the sections queryset
        self.assertIn("global", response.context)
        self.assertIn("sections", response.context)

        global_obj = response.context["global"]
        sections = list(response.context["sections"])

        self.assertIsInstance(global_obj, EveSDE)
        self.assertGreaterEqual(len(sections), 1)
        self.assertEqual(sections[0].sde_section, "Test Section")
