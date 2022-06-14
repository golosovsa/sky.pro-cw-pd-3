"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Model from api blueprint
"""


# local imports
from feed.data import RawPost, PostHandler


class ApiPost:
    """ Api Posts helper class """
    def __init__(self):
        self.post_handler = PostHandler(RawPost)

    def get_all(self) -> list[RawPost]:
        """ Get all posts """
        return self.post_handler.select_all()

    def get_one(self, post_id: int) -> RawPost:
        """ Get one posts """
        return self.post_handler.select_one_by_pk(post_id)
