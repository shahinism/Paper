# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1411570913.324679
_enable_loop = True
_template_filename = u'themes/paper/templates/post.tmpl'
_template_uri = u'post.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'{% import \'post_helper.tmpl\' as helper with context %}\n{% import \'disqus_helper.tmpl\' as disqus with context %}\n{% extends \'base.tmpl\' %}\n{% block extra_head %}\n{{ helper.twitter_card_information(post) }}\n{% if post.meta(\'keywords\') %}\n<meta name="keywords" content="{{ post.meta(\'keywords\') }}/>\n{% endif %}\n{% endblock %}\n{% block content %}\n<div id="coreContent">\n  <div class="post single hentry">\n    <div class="postContent">\n      <h3 class="entry-title">{{ helper.html_title() }}</h3>\n      <div class="entry-content">\n        {{ post.text() }}\n      </div>\n      <div class="postMeta">\n        <div class="postDate"><span>{{ messages("Posted") }}:</span> <abbr class="published">{{ post.formatted_date(date_format) }}</abbr></div>\n        {{ helper.html_translations(post) }}\n        <div class="categories">{{ helper.html_tags(post) }}</div>\n      </div>\n    </div>\n\n    <div class="pageNav">\n      {{ helper.html_pager(post) }}\n    </div>\n    <div class="postMeta">\n      {% if not post.meta(\'nocomments\') %}\n      {{ disqus.html_disqus(post.permalink(absolute=True), post.title(), post.base_path) }}\n      {% endif %}\n    </div>\n\n  </div>\n</div>\n  {% endblock %}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


