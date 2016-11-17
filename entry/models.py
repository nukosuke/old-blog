from django.db import models
from django.core.exceptions import ValidationError

import re
META_RE = re.compile(r'^[ ]{0,3}(?P<key>[A-Za-z0-9_-]+):\s*(?P<value>.*)')
META_MORE_RE = re.compile(r'^[ ]{4,}(?P<value>.*)')

class Entry(models.Model):
    slug         = models.SlugField()
    title        = models.CharField(max_length=255)
    body         = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=None)

    def clean(self):
        meta = Entry.extract_meta(self.body)

        if 'title' not in meta \
            and 'slug' not in meta \
            and 'published_at' not in meta:
            raise ValidationError('not found required form')

        self.title = meta['title'][0]
        self.slug = meta['slug'][0]
        self.published_at = meta['published_at'][0]

    def extract_meta(body):
        """ Extract Markdown Meta-Data. """
        lines = body.split('\n')
        meta = {}
        key = None
        while 1:
            line = lines.pop(0)
            if line.strip() == '':
                break # blank line - done
            m1 = META_RE.match(line)
            if m1:
                key = m1.group('key').lower().strip()
                value = m1.group('value').strip()
                try:
                    meta[key].append(value)
                except KeyError:
                    meta[key] = [value]
            else:
                m2 = META_MORE_RE.match(line)
                if m2 and key:
                    # Add another line to existing key
                    meta[key].append(m2.group('value').strip())
                else:
                    lines.insert(0, line)
                    break # no meta data - done
        return meta
