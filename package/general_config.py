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
            "rss": "rss-icon.png",
            "youtube": "youtube-icon.png",
            "soundcloud": "soundcloud-icon.png",
            "default": "rss-icon.png",
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
        size = size if size in self._available_sizes else "small"
        icon = self._icons.get(icon_name.lower(), self._icons["default"])
        return os.path.join(self._icon_resource_folder, size, icon)
