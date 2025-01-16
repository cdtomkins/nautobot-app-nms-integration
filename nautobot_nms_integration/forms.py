"""Forms for nautobot_nms_integration."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from nautobot_nms_integration import models


class NautobotNMSIntegrationExampleModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """NautobotNMSIntegrationExampleModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.NautobotNMSIntegrationExampleModel
        fields = [
            "name",
            "description",
        ]


class NautobotNMSIntegrationExampleModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """NautobotNMSIntegrationExampleModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(
        queryset=models.NautobotNMSIntegrationExampleModel.objects.all(), widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class NautobotNMSIntegrationExampleModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.NautobotNMSIntegrationExampleModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
