def clear_playback_queue(db):
    db.execute("DELETE FROM QueuedToPlay")


def clear_download_queue(db):
    db.execute("DELETE FROM QueuedToDownload")


# TODO: linked list -> list & playhead index
# -- https://stackoverflow.com/questions/515749/how-do-i-sort-a-linked-list-in-sql
