"""App declaration for nautobot_nms_integration."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class NautobotNMSIntegrationConfig(NautobotAppConfig):
    """App configuration for the nautobot_nms_integration app."""

    name = "nautobot_nms_integration"
    verbose_name = "NMS Integration"
    version = __version__
    author = "Chris Tomkins"
    description = "Nautobot App to integrate NMS functionality into Nautobot; initially aiming to support Observium.."
    base_url = "nms-integration"
    required_settings = []
    min_version = "2.3.1"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    docs_view_name = "plugins:nautobot_nms_integration:docs"


config = NautobotNMSIntegrationConfig  # pylint:disable=invalid-name
