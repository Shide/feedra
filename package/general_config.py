import sys
import os


class GeneralConfig(object):
    """
    General Application Configuration
    ==================================

    """
    def __init__(self):
        self._icon_resource_folder = os.path.abspath("./package/img/icons")
        self._available_sizes = ["small", "medium", "large"]

        # TODO: Optimize icon finding
        self._icons = {
            "rss": os.path.join(self._icon_resource_folder, "rss-icon-small.png"),
            "youtube": {
                "small": os.path.join(self._icon_resource_folder, "youtube-icon-small.png"),
                "medium": None,
                "large": None,
            },
            "soundcloud": {
                "small": os.path.join(self._icon_resource_folder, "soundcloud-icon-small.png"),
                "medium": None,
                "large": None,
            },
            "default": {
                "small": os.path.join(self._icon_resource_folder, "rss-icon-small.png"),
                "medium": None,
                "large": None,
            },
        }

    def get_icon_path(self, icon_name, size="small"):
        """
        :param icon_name: Name of the icon
        :param size: Name of the size
        :return: Absolute path to icon

        Available icons:
            - rss
            - youtube
            - soundcloud

        Available sizes:
            - small
            - medium
            - large
        """
        # TODO: Optimize
        if size not in self._available_sizes:
            size = "small"

        icon_sizes = self._icons.get(icon_name.lower(), self._icons["default"])
        return icon_sizes.get(size.lower(), icon_sizes["small"])
