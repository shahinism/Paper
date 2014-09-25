# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1411570913.341283
_enable_loop = True
_template_filename = u'themes/paper/templates/gallery.tmpl'
_template_uri = u'gallery.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{% extends "base.tmpl" %}\n{% import \'disqus_helper.tmpl\' as disqus with context %}\n{% block sourcelink %}{% endblock %}\n{% block content %}\n<ul class="breadcrumb">\n  {% for link, crumb in crumbs %}\n  <li><a href="{{ link }}">/ {{ crumb }}</a></li>\n  {% endfor %}\n</ul>\n{% if text %}\n<p>\n  {{ text }}\n</p>\n{% endif %}\n<ul>\n  {% for folder in folders %}\n  <li><a href="{{ folder }}"><i class="icon-folder-open"></i>&nbsp;{{ folder }}</a></li>\n  {% endfor %}\n</ul>\n<ul class="thumbnails">\n  {% for image in images %}\n  <li><a href="{{ image[0] }}" class="thumbnail image-refrence" {{ image[2] }}>\n    <img src="{{ image[1] }}" /></a></li>\n  {% endfor %}\n</ul>\n{% if enable_comments %}\n{{ disqus.html_disqus(None, permalink, title) }}\n{% endif %}\n{% endblock %}')
        return ''
    finally:
        context.caller_stack._pop_frame()


