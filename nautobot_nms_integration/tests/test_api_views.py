"""Unit tests for nautobot_nms_integration."""

from nautobot.apps.testing import APIViewTestCases

from nautobot_nms_integration import models
from nautobot_nms_integration.tests import fixtures


class NautobotNMSIntegrationExampleModelAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for NautobotNMSIntegrationExampleModel."""

    model = models.NautobotNMSIntegrationExampleModel
    create_data = [
        {
            "name": "Test Model 1",
            "description": "test description",
        },
        {
            "name": "Test Model 2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_nautobotnmsintegrationexamplemodel()
