# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1411570913.413679
_enable_loop = True
_template_filename = u'themes/paper/templates/tag.tmpl'
_template_uri = u'tag.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{% extends "list_post.tmpl" %}\n{% block extra_head %}\n{% for language in translations %}\n<link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for tag {{ tag }} {{ language }}" href="{{ _link("tag_rss", tag, language) }}">\n{% endfor %}\n{% endblock %}')
        return ''
    finally:
        context.caller_stack._pop_frame()


