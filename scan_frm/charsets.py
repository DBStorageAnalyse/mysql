# -*- coding: utf-8 -*-
import sqlite3

_CHARSET_INDEXES = ID, CHARACTER_SET_NAME, COLLATION_NAME, MAXLEN, IS_DEFAULT = range(0, 5)
# 在mysql的数据库中查出数据集信息,已经取出到本地sqlite里了。
_CHARSET_QUERY = """
SELECT CL.ID,CL.CHARACTER_SET_NAME,CL.COLLATION_NAME,CS.MAXLEN, CL.IS_DEFAULT FROM INFORMATION_SCHEMA.CHARACTER_SETS CS, INFORMATION_SCHEMA.COLLATIONS CL
WHERE CS.CHARACTER_SET_NAME=CL.CHARACTER_SET_NAME ORDER BY CHARACTER_SET_NAME
"""


class CharsetInfo(object):
    """
    Read character set information for lookup. Methods include:
      - get_charset_name(id) : get the name for a characterset id
      - get_default_collation(name) : get default collation name
      - get_name_by_collation(name) : given collation, find charset name
      - print_charsets() : print the character set map
    """

    def __init__(self, options=None):
        if options is None:
            options = {}
        self.verbosity = 0
        self.format = "grid"
        self.charset_map = None
        conn = sqlite3.connect(r'.\charset.db')
        cursor = conn.cursor()
        cursor.execute("select * from charset")
        self.charset_map = cursor.fetchall()  # 取出数据

    def print_charsets(self):
        """Print the character set list
        """
        print(self.format, self.charset_map)
        print(len(self.charset_map) + "rows in set.")

    def get_name(self, chr_id):
        """Get the character set name for the given id

        chr_id[in]     id for character set (as read from .frm file)

        Returns string - character set name or None if not found.
        """
        for cs in self.charset_map:
            if int(chr_id) == int(cs[ID]):
                return cs[CHARACTER_SET_NAME]
        return None

    def get_collation(self, col_id):
        """Get the collation name for the given id

        col_id[in]     id for collation (as read from .frm file)

        Returns string - collation name or None if not found.
        """
        for cs in self.charset_map:
            if int(col_id) == int(cs[ID]):
                return cs[COLLATION_NAME]
        return None

    def get_name_by_collation(self, colname):
        """Get the character set name for the given collation

        colname[in]    collation name

        Returns string - character set name or None if not found.
        """
        for cs in self.charset_map:
            if cs[COLLATION_NAME] == colname:
                return cs[CHARACTER_SET_NAME]
        return None

    def get_default_collation(self, col_id):
        """Get the default collation for the character set

        col_id[in]     id for collation (as read from .frm file)

        Returns tuple - (default collation id, name) or None if not found.
        """
        # Exception for utf8
        if col_id == 83:
            return "utf8_bin"
        for cs in self.charset_map:
            if int(cs[ID]) == int(col_id) and cs[IS_DEFAULT].upper() == "YES":
                return cs[COLLATION_NAME]
        return None

    def get_maxlen(self, col_id):
        """Get the maximum length for the character set

        col_id[in]     id for collation (as read from .frm file)

        Returns int - max length or 1 if not found.
        """
        for cs in self.charset_map:
            if int(cs[ID]) == int(col_id):
                return int(cs[MAXLEN])
        return int(1)
