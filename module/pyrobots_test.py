from module import pyrobots

print(pyrobots.allowed_by_robots("""\
User-Agent: *
Disallow: /
""", "GoogleBot", "/"))