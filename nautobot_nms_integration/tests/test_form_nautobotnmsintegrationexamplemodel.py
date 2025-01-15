"""Test nautobotnmsintegrationexamplemodel forms."""

from django.test import TestCase

from nautobot_nms_integration import forms


class NautobotNMSIntegrationExampleModelTest(TestCase):
    """Test NautobotNMSIntegrationExampleModel forms."""

    def test_specifying_all_fields_success(self):
        form = forms.NautobotNMSIntegrationExampleModelForm(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.NautobotNMSIntegrationExampleModelForm(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_nautobotnmsintegrationexamplemodel_is_required(self):
        form = forms.NautobotNMSIntegrationExampleModelForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
