"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:nautobot_nms_integration:nautobotnmsintegrationexamplemodel_list",
        name="NMS Integration",
        permissions=["nautobot_nms_integration.view_nautobotnmsintegrationexamplemodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_nms_integration:nautobotnmsintegrationexamplemodel_add",
                permissions=["nautobot_nms_integration.add_nautobotnmsintegrationexamplemodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="NMS Integration", items=tuple(items)),),
    ),
)
