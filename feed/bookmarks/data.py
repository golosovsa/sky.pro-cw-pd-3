"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Data from bookmarks blueprint
"""

# global imports
import os
from dataclasses import dataclass, field, asdict
from flask import current_app

# local imports
from grm import DAO, Singleton


@dataclass(frozen=True, order=True)
class Bookmark:
    """ Bookmark data class """
    post_id: int = field(compare=False)
    pk: int

    def __post_init__(self):
        pass


class BookmarkHandler(DAO, metaclass=Singleton):
    """ Bookmark handler DAO extended and singleton class """

    def __init__(self, data_class: dataclass):
        folder = current_app.config.get("APP_DATA_FOLDER")
        filename = current_app.config.get("APP_DATA_BOOKMARKS")
        self._filename = os.path.join(folder, filename)
        self.DataClass = data_class
        data = sorted(self.select_all())
        self._next_pk = 0 if len(data) == 0 else data[-1].pk + 1

    @property
    def next_pk(self) -> int:
        """ Auto gen property next bookmark primary key """
        result = self._next_pk
        self._next_pk += 1
        return result

    def load(self) -> list[dataclass]:
        """ Load bookmarks """
        data = super(BookmarkHandler, self).load(self._filename)
        data = [self.DataClass(**record) for record in data]
        return data

    def save(self, data: list[dataclass]):
        """ Save bookmarks """
        data = [asdict(record) for record in data]
        super(BookmarkHandler, self).save(self._filename, data)

    def select_all(self) -> list[dataclass]:
        """ Select all bookmarks """
        return self.load()

    def select_one_by_pk(self, pk: int) -> dataclass:
        """ Select one bookmark by primary key """
        data = self.load()
        for record in data:
            if record.pk == pk:
                return record
        return None

    def select_one_by_post_id(self, post_id) -> dataclass or None:
        data = self.load()
        for record in data:
            if record.post_id == post_id:
                return record
        return None

    def insert(self, post_id: int):
        """ Insert new bookmark """
        already_exist = self.select_one_by_post_id(post_id)
        if already_exist:
            return
        data = self.load()
        data.append(self.DataClass(post_id=post_id, pk=self.next_pk))
        self.save(data)

    def delete(self, pk):
        """ Delete bookmark by primary key """
        data = self.load()
        index = 0
        for record in data:
            if record.pk == pk:
                break
            index += 1
        else:
            return
        del data[index]
        self.save(data)

    def flush(self):
        data = []
        self.save(data)
        self._next_pk = 0
