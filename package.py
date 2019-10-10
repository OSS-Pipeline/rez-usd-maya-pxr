name = "usd_maya_pxr"

version = "19.07"

authors = [
    "Pixar"
]

description = \
    """
    USD plugin for Autodesk Maya from Pixar's repository.
    """

requires = [
    "cmake-3+",
    "gcc-6+",
    "maya-2018+",
    "usd-{version}".format(version=str(version))
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "usd_maya-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python")
    env.MAYA_PLUG_IN_PATH.append("{root}/third_party/maya/plugin")
    env.MAYA_SCRIPT_PATH.append("{root}/third_party/maya/lib/usd/usdMaya/resources")
    env.MAYA_SCRIPT_PATH.append("{root}/third_party/maya/plugin/pxrUsdPreviewSurface/resources")
    env.MAYA_SHELVES_ICONS = "{root}/third_party/maya/lib/usd/usdMaya/resources"
    env.MAYA_SHELF_PATH.append("{root}/third_party/maya/lib/usd/usdMaya/resources")
    env.XBMLANGPATH.append("{root}/third_party/maya/share/usd/plugins/usdMaya/resources")

    # Helper environment variables.
    env.USD_MAYA_INCLUDE_PATH.set("{root}/include")
    env.USD_MAYA_LIBRARY_PATH.set("{root}/lib")
