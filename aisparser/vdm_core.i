%module vdm_core

%{
#define SWIG_FILE_WITH_INIT
#include "core/vdm_opt.h"
#include "core/srcdata_opt.h"
#include "core/vdm_parse_core.h"
%}
%include <std_string.i>
%include "core/vdm_opt.h"
%include "core/srcdata_opt.h"
%include "core/vdm_parse_core.h"
