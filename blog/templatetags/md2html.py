from django import template
from django.template.defaultfilters import stringfilter
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension as gfm

register = template.Library()
md = markdown.Markdown(extensions=[gfm(), 'markdown.extensions.meta'])

@register.filter
@stringfilter
def md2html(value):
    """Render GitHub Flavored Markdown to HTML"""
    return md.convert(value)


import re
META_RE = re.compile(r'^[ ]{0,3}(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.*)')
META_MORE_RE = re.compile(r'^[ ]{4,}(?P<value>.*)')

@register.filter
@stringfilter
def truncate_meta(body):
    """ Truncate Markdown Meta-Data. """
    lines = body.split('\n')

    while 1:
        line = lines.pop(0)
        if line.strip() == '':
            break # blank line - done
        m1 = META_RE.match(line)
        if m1:
            key = m1.group('key').lower().strip()
        else:
            m2 = META_MORE_RE.match(line)
            if not m2 or not key:
                lines.insert(0, line)
                break # no meta data - done
    return ''.join(lines)
