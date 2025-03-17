cmake_minimum_required(VERSION 3.5.0)
project(svd_project)

include(CTest)
enable_testing()

# Manually specify Eigen if it's not globally available
set(pybind11_DIR "/home/alvaro/.conda/envs/env_svd/lib/python3.12/site-packages/pybind11/share/cmake/pybind11")
# set(pybind11 "/home/alvaro/.conda/envs/env_svd/lib/python3.12/site-packages/pybind11/share/cmake/pybind11")
find_package(pybind11 REQUIRED)

set(EIGEN3_INCLUDE_DIR "/data/alvaro/cplusplus_libraries/eigen-3.4.0")
include_directories(${EIGEN3_INCLUDE_DIR})

pybind11_add_module(svd_module src/svd_module.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
include(CPack)
