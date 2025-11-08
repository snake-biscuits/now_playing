__all__ = ["browse", "main", "tray", "queue"]

from . import browse  # audio, video, text & podcasts
# from . import calendar  # releases & plans
from . import main
# from . import play  # music, podcast, video, manga
from . import tray  # system tray [prototype]
from . import queue
# QueuedMedia & MediaQueue

# NOTE: currently just a mock-up, not linked to db yet

# TODO: widgets:
# -- Queue
# --- Simple Vertical List
# --- Calendar (Releases & Planned Watch Dates)
# --- Music (Play/Pause)
# --- Podcasts (Play/Pause, Speed & Timestamps)
# --- Video (Play/Pause, Speed, Timestamps & Subtitles)
# --- Books (Left-Right or Right-Left, Twin Pages, Magnifier)

# TODO: grid layout calendar (6x7)
# -- populate each day w/ info from db
# -- episode release dates etc.
# -- Player (Can Pop Out into another window)
