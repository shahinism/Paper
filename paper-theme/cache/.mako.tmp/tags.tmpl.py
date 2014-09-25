# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1411570913.409398
_enable_loop = True
_template_filename = u'themes/paper/templates/tags.tmpl'
_template_uri = u'tags.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{% extends "base.tmpl" %}\n{% block content %}\n<div id="coreContent">\n  <div id="archives" class="single hentry">\n    <h2 class="entry-title">{{ title }}</h2>\n    <ul class="tagCloud">\n      {% for text, link in items %}\n      <li><a class="tag" href="{{ link }}"><span class="badge badge-info">{{ text }}</span></a>\n      {% endfor %}\n    </ul>\n  </div>\n</div>\n{% endblock %}')
        return ''
    finally:
        context.caller_stack._pop_frame()


