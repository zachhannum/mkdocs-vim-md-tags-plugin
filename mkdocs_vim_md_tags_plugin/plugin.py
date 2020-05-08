import os
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

class VimMdTags(BasePlugin):

    config_scheme = (
        ('tags_file', config_options.Type(str, default='md_tags')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    def on_files(self, files, config):
        f = open(self.config['tags_file'], "w")
        md_pages = sorted(files.documentation_pages(), key=lambda page: os.path.basename(page.src_path))
        for page in md_pages:
            filename = os.path.basename(page.src_path)
            f.write(os.path.splitext(filename)[0] + "\t" + page.abs_src_path + "\t1;\"language:markdown\n") 
            f.write(filename + "\t" + page.abs_src_path + "\t1;\"language:markdown\n")
        f.close()
