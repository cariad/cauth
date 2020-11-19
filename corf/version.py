from sys import version_info
from types import ModuleType

if version_info.major == 3 and version_info.minor <= 6:
    import importlib_resources as resources_legacy
else:
    from importlib import resources


def get_version() -> str:
    """
    Gets the package version.
    """
    try:
        pkg_resources: ModuleType = resources
    except NameError:
        pkg_resources = resources_legacy

    with pkg_resources.open_text(__package__, "VERSION") as stream:  # type: ignore
        return str(stream.readline())
