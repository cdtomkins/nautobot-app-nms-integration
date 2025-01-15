"""Django API urlpatterns declaration for nautobot_nms_integration app."""

from nautobot.apps.api import OrderedDefaultRouter

from nautobot_nms_integration.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("nautobotnmsintegrationexamplemodel", views.NautobotNMSIntegrationExampleModelViewSet)

urlpatterns = router.urls
