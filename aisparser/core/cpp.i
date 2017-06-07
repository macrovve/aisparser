%module cpp

%{
#define SWIG_FILE_WITH_INIT
#include "cpp/vdm_opt.h"
#include "cpp/srcdata_opt.h"
#include "cpp/vdm_parse_core.h"
%}
%include "std_string.i"
using namespace std;

%include "cpp/vdm_opt.h"
%include "cpp/srcdata_opt.h"
%include "cpp/vdm_parse_core.h"
