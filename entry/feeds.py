from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.urls import reverse
from .models import Entry

class RssFeed(Feed):
    title = 'blog entry'
    link = '/entries/'
    description = 'blog entries'

    def items(self):
        return Entry.objects.order_by('-published_at')[:5]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse('entry-show', args=[item.slug])


class AtomFeed(RssFeed):
    feed_type = Atom1Feed
    subtitle = RssFeed.description
