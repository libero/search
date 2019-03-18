import os

from lxml import etree


def get_asset_path(name: str) -> str:
    return os.path.join(os.path.dirname(__file__), name)


def get_asset(name: str) -> str:
    asset = etree.parse(get_asset_path(name))
    return etree.tostring(asset, encoding=str)
