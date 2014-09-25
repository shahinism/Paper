# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1411570913.418366
_enable_loop = True
_template_filename = u'themes/paper/templates/listing.tmpl'
_template_uri = u'listing.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{% extends "base.tmpl" %}\n{% block content %}\n<ul class="breadcrumb">\n  {% for link, crumb in crumbs %}\n  <li><a href="{{ link }}">/ {{ crumb }}</a></li>\n  {% endfor %}\n</ul>\n{{ code }}\n{% endblock %}')
        return ''
    finally:
        context.caller_stack._pop_frame()


