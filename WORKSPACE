load("//third_party/py:python_configure.bzl", "python_configure")
load("//third_party:repo.bzl", "tf_http_archive")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# GoogleTest/GoogleMock framework. Used by unit-tests.
http_archive(
     name = "com_google_robotstxt",
     urls = ["https://github.com/google/robotstxt/archive/bacd8ba94b6d066ff6c0eb622b46bf655490994d.zip"],  # 2019-01-07
     strip_prefix = "robotstxt-bacd8ba94b6d066ff6c0eb622b46bf655490994d",
     sha256 = "448c8f3d20e8ed33a00ea9d1c8d534970f51e46fc32a58e19facb8229beb6e88",
)

http_archive(
    name = "com_google_absl",
    strip_prefix = "abseil-cpp-master",
    urls = ["https://github.com/abseil/abseil-cpp/archive/master.zip"],
)

# GoogleTest/GoogleMock framework. Used by unit-tests.
http_archive(
     name = "com_google_googletest",
     urls = ["https://github.com/google/googletest/archive/b6cd405286ed8635ece71c72f118e659f4ade3fb.zip"],  # 2019-01-07
     strip_prefix = "googletest-b6cd405286ed8635ece71c72f118e659f4ade3fb",
     sha256 = "ff7a82736e158c077e76188232eac77913a15dac0b22508c390ab3f88e6d6d86",
)


tf_http_archive(
    name = "pybind11",
    urls = [
        "https://mirror.bazel.build/github.com/pybind/pybind11/archive/v2.2.4.tar.gz",
        "https://github.com/pybind/pybind11/archive/v2.2.4.tar.gz",
    ],
    sha256 = "b69e83658513215b8d1443544d0549b7d231b9f201f6fc787a2b2218b408181e",
    strip_prefix = "pybind11-2.2.4",
    build_file = str("//third_party:pybind11.BUILD"),
)

python_configure(name = "local_config_python")