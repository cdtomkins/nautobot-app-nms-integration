"""API views for nautobot_nms_integration."""

from nautobot.apps.api import NautobotModelViewSet

from nautobot_nms_integration import filters, models
from nautobot_nms_integration.api import serializers


class NautobotNMSIntegrationExampleModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """NautobotNMSIntegrationExampleModel viewset."""

    queryset = models.NautobotNMSIntegrationExampleModel.objects.all()
    serializer_class = serializers.NautobotNMSIntegrationExampleModelSerializer
    filterset_class = filters.NautobotNMSIntegrationExampleModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
