import os
from decouple import config

CLIPPINGS_FILE = config('CLIPPINGS_FILE', default="MyClippings.txt")
NOTION_TOKEN = config(
    'NOTION_TOKEN', default="5b247e27937dba1a03ca1b88833e05eed7b8ad84356d1cfdf7148797918e213e559d3af8a0c85a1d08726c10097a6d5181dcdec56fba78de1dc08f57be6947ee19d210a51ddcaa9536cb032c3583")
NOTION_TABLE_ID = config(
    'NOTION_TABLE_ID', default="https://www.notion.so/d61023cf4f134f12926bc34d785f097a?v=278b5c16962c4d6bbad0bbeeb7794054")
