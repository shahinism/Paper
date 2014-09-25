# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1411570913.3171
_enable_loop = True
_template_filename = u'themes/paper/templates/story.tmpl'
_template_uri = u'story.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{% extends "post.tmpl" %}\n{% import "post_helper.tmpl" as helper with context %}\n{% block extra_head %}\n{{ helper.twitter_card_information(post) }}\n{% endblock %}\n{% block content %}\n<div id="coreCentent">\n  <div class="post hentry single">\n    <div class="postContent">\n      {% if title %}\n      <h2 class="entry-title">{{ title }}</h2>\n      {% endif %}\n      <div class="entry-content">\n        {{ post.text() }}\n      </div>\n    </div>\n  </div>\n  {% if enable_comments and not post.meta(\'nocomments\') %}\n  {{ disqus.html_disqus(post.permalink(absolute=True), post.title(), post.base_path) }}\n  {% endif %}\n</div>\n{% endblock %}')
        return ''
    finally:
        context.caller_stack._pop_frame()


