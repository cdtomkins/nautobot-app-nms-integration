"""Test NautobotNMSIntegrationExampleModel."""

from django.test import TestCase

from nautobot_nms_integration import models


class TestNautobotNMSIntegrationExampleModel(TestCase):
    """Test NautobotNMSIntegrationExampleModel."""

    def test_create_nautobotnmsintegrationexamplemodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        nautobotnmsintegrationexamplemodel = models.NautobotNMSIntegrationExampleModel.objects.create(name="Development")
        self.assertEqual(nautobotnmsintegrationexamplemodel.name, "Development")
        self.assertEqual(nautobotnmsintegrationexamplemodel.description, "")
        self.assertEqual(str(nautobotnmsintegrationexamplemodel), "Development")

    def test_create_nautobotnmsintegrationexamplemodel_all_fields_success(self):
        """Create NautobotNMSIntegrationExampleModel with all fields."""
        nautobotnmsintegrationexamplemodel = models.NautobotNMSIntegrationExampleModel.objects.create(name="Development", description="Development Test")
        self.assertEqual(nautobotnmsintegrationexamplemodel.name, "Development")
        self.assertEqual(nautobotnmsintegrationexamplemodel.description, "Development Test")
