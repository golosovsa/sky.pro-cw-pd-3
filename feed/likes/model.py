"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Model from likes blueprint
"""

# local imports
from ..data import PostHandler, RawPost


class LikesApi:
    """ Likes api model """
    def __init__(self, post_id):

        # init handler
        post_handler = PostHandler(RawPost)

        self.post = post_handler.select_one_by_pk(post_id)

        if self.post:

            # increment likes
            post_handler.increment_likes_count_by_pk(post_id)
