from django import template
from django.template.defaultfilters import stringfilter
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension as gfm

register = template.Library()
md = markdown.Markdown(extensions=[gfm()])

@register.filter
@stringfilter
def md2html(value):
    """Render GitHub Flavored Markdown to HTML"""
    return md.convert(value)
