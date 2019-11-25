import argparse
import glob
import os.path
import os

parser = argparse.ArgumentParser()

def create_folder(module_name):
    try:
        os.mkdir(module_name)
    except FileExistsError:
        pass

def get_bitmap_filepaths(folderpath, mask_suffix):
    all_files = glob.glob(os.path.join(folderpath, "*.xbm"))
    return [fp for fp in all_files if not fp.endswith(f"{mask_suffix}.xbm")]


def get_file_contents(path, mask_suffix):
    *filepath, filename = os.path.split(path)
    mask_filename = filename.split(".")[0] + f'{mask_suffix}.' + filename.split(".")[1]
    varname = filename.split(".")[0].replace("-", "_")
    code = ""
    code += varname + " = "
    with open(os.path.join(*filepath, filename)) as f:
        code += '"""\n' + "".join([line for line in f]) + '"""\n'
    code += "\n{varname}_mask = "
    with open(os.path.join(*filepath, mask_filename)) as f:
        code += '"""\n' + "".join([line for line in f]) + '"""\n'
    return varname, code

parser.add_argument("-folderpath", default="assets")
parser.add_argument("-modulename", default="assets")
parser.add_argument("-masksuffix", default="-mask")
args = parser.parse_args()
create_folder("dist")
create_folder(os.path.join("dist", args.modulename))

for filepath in get_bitmap_filepaths(args.folderpath, args.masksuffix):
    py_fname, pycode = get_file_contents(filepath, args.masksuffix)
    with open(os.path.join("dist", args.modulename, py_fname + ".py"), "w") as f:
        f.write(pycode)
    with open(os.path.join("dist", args.modulename, "__init__.py"), "a") as f:
        f.write(f"from .{py_fname} import {py_fname}, {py_fname + '_mask'}\n")
