"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from nautobot_nms_integration import models
from nautobot_nms_integration.tests import fixtures


class NautobotNMSIntegrationExampleModelViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the NautobotNMSIntegrationExampleModel views."""

    model = models.NautobotNMSIntegrationExampleModel
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }
    csv_data = (
        "name",
        "Test csv1",
        "Test csv2",
        "Test csv3",
    )

    @classmethod
    def setUpTestData(cls):
        fixtures.create_nautobotnmsintegrationexamplemodel()
