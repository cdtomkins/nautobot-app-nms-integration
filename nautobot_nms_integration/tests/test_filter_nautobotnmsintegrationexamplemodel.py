"""Test NautobotNMSIntegrationExampleModel Filter."""

from django.test import TestCase

from nautobot_nms_integration import filters, models
from nautobot_nms_integration.tests import fixtures


class NautobotNMSIntegrationExampleModelFilterTestCase(TestCase):
    """NautobotNMSIntegrationExampleModel Filter Test Case."""

    queryset = models.NautobotNMSIntegrationExampleModel.objects.all()
    filterset = filters.NautobotNMSIntegrationExampleModelFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for NautobotNMSIntegrationExampleModel Model."""
        fixtures.create_nautobotnmsintegrationexamplemodel()

    def test_q_search_name(self):
        """Test using Q search with name of NautobotNMSIntegrationExampleModel."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for NautobotNMSIntegrationExampleModel."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
