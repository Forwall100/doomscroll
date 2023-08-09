import json
from pathlib import Path
from random import choice


class FeedAdapter:
    def __init__(self, feed_path):
        self.path = Path(feed_path)
        self._feed = self._load_feed()

    def _load_feed(self):
        if self.path.exists():
            return json.loads(self.path.read_text())
        return {}

    def get_feed(self):
        return self._feed

    def set_feed(self, feed):
        self.path.write_text(json.dumps(feed))
        self._feed = feed

    def add_source(self, title, url, category="Other"):
        if category not in self._feed:
            self._feed[category] = []
        self._feed[category].append({"title": title, "url": url})
        self.set_feed(self._feed)

    def remove_source(self, title):
        deleted = 0
        for category in self._feed.values():
            to_remove = [i for i, item in enumerate(
                category) if item["title"] == title]
            for i in reversed(to_remove):
                del category[i]
            deleted += len(to_remove)
        self.set_feed(self._feed)
        return deleted

    def get_random_url(self):
        category = choice(list(self._feed.keys()))
        item = choice(self._feed[category])
        return item['url']

