from distutils.core import setup, Extension
import os

os.environ["CXX"] = "g++"

setup(ext_modules=[Extension(name='_example',
                             sources=["example.i", "testcpp.cpp"],
                             swig_opts=['-c++'])])
