"""Views for nautobot_nms_integration."""

from nautobot.apps.views import NautobotUIViewSet

from nautobot_nms_integration import filters, forms, models, tables
from nautobot_nms_integration.api import serializers


class NautobotNMSIntegrationExampleModelUIViewSet(NautobotUIViewSet):
    """ViewSet for NautobotNMSIntegrationExampleModel views."""

    bulk_update_form_class = forms.NautobotNMSIntegrationExampleModelBulkEditForm
    filterset_class = filters.NautobotNMSIntegrationExampleModelFilterSet
    filterset_form_class = forms.NautobotNMSIntegrationExampleModelFilterForm
    form_class = forms.NautobotNMSIntegrationExampleModelForm
    lookup_field = "pk"
    queryset = models.NautobotNMSIntegrationExampleModel.objects.all()
    serializer_class = serializers.NautobotNMSIntegrationExampleModelSerializer
    table_class = tables.NautobotNMSIntegrationExampleModelTable
