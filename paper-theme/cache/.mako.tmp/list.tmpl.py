# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1411570913.314418
_enable_loop = True
_template_filename = u'themes/paper/templates/list.tmpl'
_template_uri = 'list.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{% extends "base.tmpl" %}\n{% block content %}\n<!--Body content-->\n<div id="coreContent">\n  <div id="links" class="single hentry">\n    <div class="postContent">\n      <h2 class="entry-title">{{ title }}</h2>\n      <div class="entry-content">\n        <ul class="linkList">\n          {% for text, link in items %}\n          <li><a href="{{ link }}">{{ text }}</a>\n          {% endfor %}\n        </ul>\n      </div>\n    </div>\n  </div>\n</div>\n<!--End of body content-->\n{% endblock %}')
        return ''
    finally:
        context.caller_stack._pop_frame()


