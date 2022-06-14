"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Model from users blueprint
"""

# local imports
from ..data import PostHandler, ShortPost
from ..bookmarks.data import BookmarkHandler, Bookmark


class Users:
    """ Users model class """
    def __init__(self, poster_name):
        post_handler = PostHandler(ShortPost)
        bookmark_handler = BookmarkHandler(Bookmark)
        self.posts = sorted(post_handler.select_by_username(poster_name))
        self.bookmarks = bookmark_handler.select_all()

    def is_post_in_bookmarks(self, post_id: int) -> bool:
        """ Is post in bookmarks?

        :param post_id: post primary key
        :return: True or False
        """
        for bookmark in self.bookmarks:
            if bookmark.post_id == post_id:
                return True
        return False
