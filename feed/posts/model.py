"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Model from posts blueprint
"""

# local imports
from .data import CommentHandler, Comment
from ..data import PostHandler, FullPost
from ..bookmarks.data import BookmarkHandler, Bookmark


class Post:
    """ Post model class """
    def __init__(self, post_id):

        # init handlers
        post_handler = PostHandler(FullPost)
        comment_handler = CommentHandler(Comment)
        bookmark_handler = BookmarkHandler(Bookmark)

        # increment views
        post_handler.increment_views_count_by_pk(post_id)

        # select post data and comments, sort it
        self.post = post_handler.select_one_by_pk(post_id)

        if self.post is not None:
            self.comments = sorted(comment_handler.select_by_post_id(post_id))
        else:
            self.comments = []

        # check is bookmarked
        self.is_bookmarked = False
        bookmarks = bookmark_handler.select_all()
        for bookmark in bookmarks:
            if bookmark.post_id == post_id:
                self.is_bookmarked = True
                break

        # russian language rules
        count_comments = len(self.comments)
        # 0, 5-20, 25-30, ..., 100, 105-120, ...        комментариев    <- самый высокочастотный
        # 1, 21, 31, ..., 101, 121, ...                 комментарий     <- самый низкочастотный
        # 2-4, 22-24, 32-34, ..., 102-104, 122-124 ...  комментария
        self.the_word_comments = "комментариев"
        count_comments %= 100
        if count_comments > 20 or count_comments < 5:
            count_comments %= 10
            if 1 < count_comments < 5:
                self.the_word_comments = "комментария"
            elif count_comments == 1:
                self.the_word_comments = "комментарий"
