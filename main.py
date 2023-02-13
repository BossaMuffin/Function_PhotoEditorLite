# Lite photo editor
# This is a little training project
# From "Internet Made Coder" on Youtube

from PIL import Image, ImageEnhance, ImageFilter
import os


def start(p_path: str, p_pathOut: str) -> object:
    g_factor = 1.5

    for l_filename in os.listdir(p_path):
        l_img = Image.open(f"{p_path}/{l_filename}")

        l_edit = l_img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

        enhancer = ImageEnhance.Contrast(l_edit)
        l_edit = enhancer.enhance(g_factor)

        l_clean_name = os.path.splitext(l_filename)[0]

        l_edit.save(f".{p_pathOut}/{l_clean_name}_edited.jpg")


if __name__ == '__main__':
    path = "./imgs"
    pathOut = "/editedImgs"
    start(path, pathOut)
