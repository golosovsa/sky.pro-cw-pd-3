"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Data from posts blueprint
"""

# global imports
from flask import current_app
from dataclasses import dataclass, field, asdict
import os

# local imports
from grm import DAO, Singleton


@dataclass(frozen=True, order=True)
class Comment:
    """ Comment data class """
    post_id: int = field(compare=False)
    commenter_name: str = field(compare=False)
    comment: str = field(compare=False)
    pk: int

    def __post_init__(self):
        pass


class CommentHandler(DAO, metaclass=Singleton):
    """ Comment handler singleton class (handle database operations) """

    def __init__(self, data_class: dataclass):
        folder = current_app.config.get("APP_DATA_FOLDER")
        filename = current_app.config.get("APP_DATA_COMMENTS")
        self._filename = os.path.join(folder, filename)
        self.DataClass = data_class

    def load(self) -> list[dataclass]:
        """ Load comments """
        data = super(CommentHandler, self).load(self._filename)
        data = [self.DataClass(**record) for record in data]
        return data

    def save(self, data: list[dataclass]) -> None:
        """ Save comments

        :param data: List of dataclasses
        :return: None
        """
        data = [asdict(record) for record in data]
        super(CommentHandler, self).save(self._filename, data)

    def select_by_post_id(self, post_id: int) -> list[dataclass]:
        """ Select comments by post_id

        :param post_id: Post primary key
        :return: List of comments
        """
        data = super(CommentHandler, self).load(self._filename)
        data = super(CommentHandler, self).select_all_by_field(data, "post_id", post_id)
        data = [self.DataClass(**record) for record in data]
        return data

    def select_by_pk(self, pk):
        data = super(CommentHandler, self).load(self._filename)
        data = super(CommentHandler, self).select_one_by_field(data, "pk", pk)
        data = self.DataClass(**data)
        return data
