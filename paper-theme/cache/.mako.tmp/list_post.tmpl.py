# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1411570913.309397
_enable_loop = True
_template_filename = u'themes/paper/templates/list_post.tmpl'
_template_uri = 'list_post.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{% extends "base.tmpl" %}\n{% block content %}\n<!--Body content-->\n<div id="coreContent">\n  <div id="archives" class="single hentry">\n      <h2 class="entry-title">{{ title }}</h2>\n      <ul id="recentPosts">\n        {% for post in posts %}\n        <li><a href="{{ post.permalink() }}">{{ post.title() }}</a>\n          <div class="postDate"><abbr class="published">{{ post.formatted_date(date_format) }}</abbr></div>\n        {% endfor %}\n      </ul>\n  </div>\n</div>\n<!--End of body content-->\n{% endblock %}')
        return ''
    finally:
        context.caller_stack._pop_frame()


