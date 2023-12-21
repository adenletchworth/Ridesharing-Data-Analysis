import re
import glob

def get_files_by_regex(pattern):
    file_names = glob.glob(pattern)
    return file_names