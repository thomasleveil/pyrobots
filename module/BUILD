load("//module:py.bzl", "py_extension")

py_extension(
    name = "pyrobots",
    srcs = ["pyrobots.cc"],
    deps = [
        "//third_party/python_runtime:headers",
        "@pybind11",
        "@com_google_robotstxt//:robots"
    ],
)

py_test(
    name = "pyrobots_test",
    size = "small",
    srcs = ["pyrobots_test.py"],
    deps = [":pyrobots"],
    python_version = "PY3",
)