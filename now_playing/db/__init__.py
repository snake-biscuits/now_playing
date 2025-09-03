__all__ = [
    "base",
    "UserData"]

from . import base
# TODO: modules adding methods to the DB class
# -- each module should be focused on a specific system
# -- e.g. db.podcast, db.youtube, db.queue

from .base import UserData
# TODO: monkey-patch methods onto UserData
