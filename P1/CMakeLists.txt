cmake_minimum_required(VERSION 3.15)
project(P1)

# Enable C and C++ support
enable_language(C)
enable_language(CXX)

# Set C standard
set(CMAKE_C_STANDARD 99)

# Force use of /MDd for Debug runtime (dynamic debug runtime)
set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreadedDebugDLL")

# Add GTest
add_subdirectory(googletest)

enable_testing()

# Include directories
include_directories(include)

set(CMAKE_C_FLAGS_DEBUG "/MDd")
set(CMAKE_CXX_FLAGS_DEBUG "/MDd")

# Add your module
add_library(my_module STATIC src/my_module.c)

# Create test executable
add_executable(test_my_module tests/test_my_module.cpp)

# Link test with GTest and your module
target_link_libraries(test_my_module PRIVATE my_module gtest gtest_main)

# Enable test discovery
include(GoogleTest)
gtest_discover_tests(test_my_module)

# For MSVC: disable secure CRT warnings
if (MSVC)
    target_compile_definitions(my_module PRIVATE _CRT_SECURE_NO_WARNINGS)
endif()
