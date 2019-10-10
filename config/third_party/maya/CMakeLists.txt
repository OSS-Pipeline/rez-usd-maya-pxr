set(PXR_INSTALL_SUBDIR "third_party/maya")

if (NOT ${PXR_BUILD_USD_CORE})
    # If we are not building the USD core libraries and binaries, we make sure that the headers of some necessary
    # libraries are correctly exposed to CMake.
    include_directories(${Boost_INCLUDE_DIRS} ${TBB_INCLUDE_DIRS} ${GLEW_INCLUDE_DIR})
endif()

pxr_add_extra_plugins(plugin)

# Additional defines for building against Maya
add_definitions(-D_BOOL -DREQUIRE_IOSTREAM)

if (APPLE)
   add_definitions(-DOSMac_ -DMAC_PLUGIN)
endif()

add_subdirectory(lib)
add_subdirectory(plugin)