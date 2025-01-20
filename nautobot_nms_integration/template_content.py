"""Templates."""

from nautobot.apps.ui import TemplateExtension


class DeviceContent(TemplateExtension):  # pylint: disable=abstract-method
    """Add a test panel to device."""

    model = "dcim.device"

    def right_page(self):
        """Boop."""
        return """
        <div class="panel panel-default">
            <div class="panel-heading">
                <strong>NMS Information</strong>
            </div>
            <div class="panel-body">
                Hello!
            </div>
        </div>
        """


template_extensions = [DeviceContent]  # Important to include!
