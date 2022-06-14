"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Model from feed blueprint
"""

# global imports
import operator

# local imports
from ..data import PostHandler, RawPost, ShortPost
from .data import BookmarkHandler, Bookmark


class Bookmarks:
    """ Bookmark model class """

    def __init__(self):
        # init handlers
        post_handler = PostHandler(ShortPost)
        bookmark_handler = BookmarkHandler(Bookmark)

        # create page data
        bookmarks = bookmark_handler.select_all()
        self.data = []
        for bookmark in bookmarks:
            the_post = post_handler.select_one_by_pk(bookmark.post_id)
            if the_post:
                self.data.append({
                    "post": post_handler.select_one_by_pk(bookmark.post_id),
                    "bookmark": bookmark
                })
        self.data = sorted(self.data, key=operator.itemgetter("post"))


class BookmarksApi:
    """ BookmarksApi model class """

    def __init__(self):
        # init handlers
        self.bookmark_handler = BookmarkHandler(Bookmark)
        self.post_handler = PostHandler(RawPost)

    def add(self, post_id: int) -> None:
        """ Add bookmark """
        self.bookmark_handler.insert(post_id)

    def remove(self, bookmark_id: int) -> int:
        """ Remove bookmark """
        self.bookmark_handler.delete(bookmark_id)

    def check_post_id(self, post_id: int) -> bool:
        """ Check post exists by primary key """
        post = self.post_handler.select_one_by_pk(post_id)
        return post is not None

    def check_bookmark_id(self, bookmark_id: int) -> bool:
        """ Check bookmark exists by primary key """
        return self.bookmark_handler.select_one_by_pk(bookmark_id) is not None
