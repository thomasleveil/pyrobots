
# /!\ Work in progress /!\

**Current status:** not working 


# Python extension for Google Robots.txt Parser and Matcher Library

The repository contains the source code for a Python extension for 
[Google's robots.txt parser and matcher as a C++ library](https://github.com/google/robotstxt).


## Notice

Being myself ignorant regarding C++ and pybind11, this repository is adapted from https://github.com/av8ramit/pybind_example.

Hopefully I did not copied over too much unrelevant code. PR are much welcome.


## Building

```sh
git clone https://github.com/thomasleveil/pyrobots.git
cd pyrobots
bazel test module:pyrobots_test.py

```
