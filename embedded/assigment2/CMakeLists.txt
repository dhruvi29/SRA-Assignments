
cmake_minimum_required(VERSION 3.10)
project(Assignment2)

set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
file(DOWNLOAD
https://sravjti.tech/embedded-systems-study-group/assets/week2/code2.zip
${CMAKE_SOURCE_DIR}/code2.zip 
SHOW_PROGRESS)
#file(ARCHIVE_EXTRACT INPUT ${CMAKE_SOURCE_DIR}/code2.zip)
execute_process(unzip ${CMAKE_SOURCE_DIR}/code2.zip)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
include_directories("${PROJECT_SOURCE_DIR}/build/06/include")

add_executable(library ${PROJECT_SOURCE_DIR}/build/06/main.c ${PROJECT_SOURCE_DIR}/build/06/string_add.c ${PROJECT_SOURCE_DIR}/build/06/library.c)
