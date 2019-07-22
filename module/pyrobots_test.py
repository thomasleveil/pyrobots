from module import pyrobots

robotstxt = """\
User-Agent: *
Disallow: /
"""
assert pyrobots.allowed_by_robots(robotstxt, "GoogleBot", "/") is False
assert pyrobots.allowed_by_robots(robotstxt, "GoogleBot", "/test") is False
assert pyrobots.allowed_by_robots(robotstxt, "FooBot", "/") is False
assert pyrobots.allowed_by_robots(robotstxt, "FooBot", "/test") is False


robotstxt_test = """\
User-Agent: *
Disallow: /test
"""
assert pyrobots.allowed_by_robots(robotstxt_test, "GoogleBot", "/") is True
assert pyrobots.allowed_by_robots(robotstxt_test, "GoogleBot", "/test") is False
assert pyrobots.allowed_by_robots(robotstxt_test, "FooBot", "/") is True
assert pyrobots.allowed_by_robots(robotstxt_test, "FooBot", "/test") is False


robotstxt_foo = """\
User-Agent: FooBot
Disallow: /
"""
assert pyrobots.allowed_by_robots(robotstxt_foo, "GoogleBot", "/") is True
assert pyrobots.allowed_by_robots(robotstxt_foo, "GoogleBot", "/test") is True
assert pyrobots.allowed_by_robots(robotstxt_foo, "FooBot", "/") is False
assert pyrobots.allowed_by_robots(robotstxt_foo, "FooBot", "/test") is False
