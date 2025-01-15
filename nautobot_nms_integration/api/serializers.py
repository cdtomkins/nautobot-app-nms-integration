"""API serializers for nautobot_nms_integration."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from nautobot_nms_integration import models


class NautobotNMSIntegrationExampleModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """NautobotNMSIntegrationExampleModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.NautobotNMSIntegrationExampleModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
