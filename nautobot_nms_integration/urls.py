"""Django urlpatterns declaration for nautobot_nms_integration app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter


from nautobot_nms_integration import views


router = NautobotUIViewSetRouter()

router.register("nautobotnmsintegrationexamplemodel", views.NautobotNMSIntegrationExampleModelUIViewSet)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("nautobot_nms_integration/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
