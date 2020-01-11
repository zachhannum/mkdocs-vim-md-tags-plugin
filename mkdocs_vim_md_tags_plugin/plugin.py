import os
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

class VimMdTags(BasePlugin):

    config_scheme = (
        ('tags_file', config_options.Type(mkdocs_utils.string_types, default='.md_tags')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_files(self, files, config):
        f = open(self.config['tags_file'], "w")
        for file in files.documentation_pages():
            filename = os.path.basename(file.src_path)
            f.write(filename + "\t" + file.src_path + "\tlanguage:markdown\n")
        f.close()
