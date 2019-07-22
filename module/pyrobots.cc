#include <pybind11/pybind11.h>
#include "robots.h"

namespace py = pybind11;


bool allowedByRobots(std::string robots_content, std::string user_agent, std::string url) {
    std::vector<std::string> user_agents(1, user_agent);
    googlebot::RobotsMatcher matcher;
    bool allowed = matcher.AllowedByRobots(robots_content, &user_agents, url);
    return allowed;
}


PYBIND11_MODULE(pyrobots, m) {
    m.doc() = R"pbdoc(
        Python wrapper module for Google robots.txt parser
        -----------------------
        .. currentmodule:: pyrobots
        .. autosummary::
           :toctree: _generate
           allowed_by_robots
    )pbdoc";


    m.def("allowed_by_robots", &allowedByRobots, R"pbdoc(
        Returns True if 'url' is allowed to be fetched by any member of the
        "user_agents" list. 'url' must be %-encoded according to RFC3986.
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}