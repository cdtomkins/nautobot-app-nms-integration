"""Filtering for nautobot_nms_integration."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from nautobot_nms_integration import models


class NautobotNMSIntegrationExampleModelFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for NautobotNMSIntegrationExampleModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.NautobotNMSIntegrationExampleModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = "__all__"
