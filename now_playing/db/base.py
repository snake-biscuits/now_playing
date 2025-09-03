from __future__ import annotations
import os
import sqlite3
from typing import Any, Generator, List, Tuple

from .. import config


# TODO: datetime <-> str conversion

def sql_repr(obj: Any) -> str:
    return repr(obj) if obj is not None else "NULL"


class UserData:
    db: sqlite3.Connection

    def __init__(self):
        self.db = sqlite3.connect(":memory:")

    def run_script(self, filename: str):
        try:
            with open(filename) as sql_script:
                self.db.executescript(sql_script.read())
        except sqlite3.OperationalError:  # or DatabaseError
            # TODO: "script:line:char" error message
            # -- sqlite3 doesn't seem to provide this
            # -- might need to write our own validator
            raise RuntimeError(f'failed to run script: "{filename}"')
        except Exception as exc:
            raise exc

    def new(self):
        scripts = (
            "cd.tables.sql",
            "podcast.tables.sql",
            "youtube.tables.sql",
            "subscription.enums.sql",
            "subscription.tables.sql",
            "time.tables.sql",
            "tag.enums.sql",
            "tag.tables.sql")
        folder = os.path.dirname(__file__)
        for script in scripts:
            self.run_script(os.path.join(folder, script))

    def store(self, table: str, rows: List[str], values: List[Tuple[Any]]):
        rows_ = ",".join(rows)
        template = ",".join(("?",) * len(rows))
        self.db.executemany(
            f"INSERT INTO {table}({rows_}) VALUES ({template})", values)

    def dump_tables(self, tables: List[str]) -> Generator[str, None, None]:
        """for debugging"""
        query = [
            "SELECT m.name as table_name, p.name as column_name",
            "FROM sqlite_master AS m",
            "JOIN pragma_table_info(m.name) as p",
            "WHERE m.type='table'",
            "ORDER BY m.name, p.cid"]
        table_columns = self.db.execute("\n".join(query)).fetchall()
        for table in tables:
            fields = ", ".join([
                column
                for table, column in table_columns
                if table == table and column != "id"])
            yield f"INSERT INTO {table}({fields}) VALUES\n"
            entries = self.db.execute(
                f"SELECT {fields} FROM {table}").fetchall()
            for entry in entries[:-1]:
                yield "\t({}),\n".format(",".join(map(sql_repr, entry)))
            yield "\t({});\n\n\n".format(",".join(map(sql_repr, entries[-1])))

    @classmethod
    def from_cache(cls) -> UserData:
        out = cls()
        file = os.path.join(config.path["root"], "user.db")
        out.db = sqlite3.connect(file)
        return out
