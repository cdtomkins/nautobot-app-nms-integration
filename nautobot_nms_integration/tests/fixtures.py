"""Create fixtures for tests."""

from nautobot_nms_integration.models import NautobotNMSIntegrationExampleModel


def create_nautobotnmsintegrationexamplemodel():
    """Fixture to create necessary number of NautobotNMSIntegrationExampleModel for tests."""
    NautobotNMSIntegrationExampleModel.objects.create(name="Test One")
    NautobotNMSIntegrationExampleModel.objects.create(name="Test Two")
    NautobotNMSIntegrationExampleModel.objects.create(name="Test Three")
