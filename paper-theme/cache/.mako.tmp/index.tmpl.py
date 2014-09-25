# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1411570913.331272
_enable_loop = True
_template_filename = u'themes/paper/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{% import "index_helper.tmpl" as helper with context %}\n{% import "disqus_helper.tmpl" as disqus with context %}\n{% extends "base.tmpl" %}\n{% block content %}\n  {% for post in posts %}\n    <article>\n      <h2><a href="{{ post.permalink() }}">{{ post.title() }}</a></h2>\n      <div class="metadata">\n\t<span class="date">{{ post.formatted_date(date_format) }}</span>\n\t<span class="writer">Shahin Azad</span>\n      </div><!--/metadata-->\n      <p>\n\t{{ post.text(teaser_only=index_teasers) }}\n      </p>\n      {% if not post.meta(\'nocomments\') %}\n        {{ disqus.html_disqus_link(post.permalink()+"#disqus_thread", post.base_path) }}\n    </article>\n  {% endif %}\n{% endfor %}\n{{ helper.html_pager() }}\n{{ disqus.html_disqus_script() }}\n{% endblock %}\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


