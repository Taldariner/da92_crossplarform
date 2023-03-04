%module example
%{
#include "testcpp.h"
%}
%include "std_string.i"

%include testcpp.h
