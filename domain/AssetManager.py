from os import path

layout_dir, drawable_dir = "layout", "drawable"


def get_layout_path(filename: str) -> str:
    if not filename.endswith(".ui"):
        raise FileNotFoundError
    return path.dirname(__file__)[:-6:] + layout_dir + "\\" + filename
