"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Model from search blueprint
"""

# global imports
from flask import current_app

# local imports
from ..data import PostHandler, ShortPost
from ..bookmarks.data import BookmarkHandler, Bookmark


class Search:
    """ Search model class """

    def __init__(self, substring: str):
        post_handler = PostHandler(ShortPost)
        bookmark_handler = BookmarkHandler(Bookmark)

        search_depth = current_app.config.get("SEARCH_DEPTH", 10)

        if substring and not    substring.isspace():
            self.posts = sorted(post_handler.select_by_substring(substring, depth=search_depth))
            self.count_posts = f"Найдено постов {post_handler.get_posts_count_by_substring(substring)}"
            self.value = substring
        else:
            self.posts = sorted(post_handler.select_all(depth=search_depth))
            self.count_posts = f"Всего постов {post_handler.get_posts_count()}"
            self.value = ""
        self.bookmarks = bookmark_handler.select_all()

    def is_post_in_bookmarks(self, post_id):
        """ Is post in bookmarks?

        :param post_id: post primary key
        :return: True or False
        """
        for bookmark in self.bookmarks:
            if bookmark.post_id == post_id:
                return True
        return False
