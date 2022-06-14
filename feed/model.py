"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Model from feed blueprint
"""

# local imports
from .bookmarks.data import BookmarkHandler, Bookmark
from .data import PostHandler, ShortPost


class Feed:
    """ Feed model class """
    def __init__(self):
        # get handlers
        post_handler = PostHandler(ShortPost)
        bookmark_handler = BookmarkHandler(Bookmark)
        # save page data to class fields
        self.posts = sorted(post_handler.select_all())
        self.bookmarks = bookmark_handler.select_all()

    def is_post_in_bookmarks(self, post_id: int) -> bool:
        """ Is post in bookmarks helper method"""
        for bookmark in self.bookmarks:
            if bookmark.post_id == post_id:
                return True
        return False

