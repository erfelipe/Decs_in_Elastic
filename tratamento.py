import tkinter as tk
from tkinter import filedialog
import fnmatch
import os
import hashlib
import tika
from tika import parser


# Calcula o hash de uma arquivo
def calc_hash(f):
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(f, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print(hasher.hexdigest())
    return hasher.hexdigest()


def extraiPDF(f):
    raw = parser.from_file(f)
    raw = str(raw)
    safe_text = raw.encode('utf-8', errors='ignore')
    safe_text = str(safe_text).replace("\n", "").replace("\\", "")
    print('--- safe text ---')
    print(safe_text)
    return safe_text

# DialogBox for choose the local directory
root = tk.Tk()
root.withdraw()
dir_path = filedialog.askdirectory()

# List of files from directory choosed 
for file in os.listdir(dir_path):
    if fnmatch.fnmatch(file, '*.pdf'):
        print(dir_path)
        print(os.path.join(dir_path, file))
        calc_hash(os.path.join(dir_path, file))
        extraiPDF(os.path.join(dir_path, file))


