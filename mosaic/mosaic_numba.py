# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: SaltFish
# @file: mosaic_numba.py
# @date: 2020/06/03
import os
import sys

from PIL import Image
from numba import cuda
from numba.typed import List

TILE_SIZE = 32  # 块的高度/宽度（以像素为单位）
TILE_MATCH_RES = 8  # 块匹配分辨率（值越高，拟合度越好，但需要更多处理），与TILE_SIZE相等时，图像保持原有品质
ENLARGEMENT = 2  # 马赛克图像的宽度和高度将比原始图像大的倍数

TILE_BLOCK_SIZE = TILE_SIZE / max(min(TILE_MATCH_RES, TILE_SIZE), 1)
OUT_FILE = "mosaic_numba.png"


def get_target_data(target_file_path):
    print("Processing main image...")
    img = Image.open(target_file_path)
    w = img.size[0] * ENLARGEMENT
    h = img.size[1] * ENLARGEMENT
    large_img = img.resize((w, h), Image.ANTIALIAS)
    w_diff = (w % TILE_SIZE) / 2
    h_diff = (h % TILE_SIZE) / 2
    # 裁切图像使用完整的小图片
    if w_diff or h_diff:
        large_img = large_img.crop((w_diff, h_diff, w - w_diff, h - h_diff))
    small_img = large_img.resize(
        (int(w / TILE_BLOCK_SIZE), int(h / TILE_BLOCK_SIZE)), Image.ANTIALIAS
    )
    image_data = (large_img.convert("RGB"), small_img.convert("RGB"))
    print("Main image processed.")
    return image_data


def process_tile(tile_file_path):
    try:
        img = Image.open(tile_file_path)
        # 裁剪图像获得最大正方形
        w = img.size[0]
        h = img.size[1]
        if w != h:
            min_dimension = min(w, h)
            # 居中裁剪
            w_crop = (w - min_dimension) / 2
            h_crop = (h - min_dimension) / 2
            img = img.crop((w_crop, h_crop, w - w_crop, h - h_crop))
        large_tile_img = img.resize((TILE_SIZE, TILE_SIZE), Image.ANTIALIAS)
        small_tile_img = img.resize(
            (int(TILE_SIZE / TILE_BLOCK_SIZE), int(TILE_SIZE / TILE_BLOCK_SIZE)),
            Image.ANTIALIAS,
        )
        return large_tile_img.convert("RGB"), small_tile_img.convert("RGB")
    except:
        return None, None


def get_tiles_data(tiles_file_path):
    large_tiles = []
    small_tiles = []
    print("Reading tiles from {}...".format(tiles_file_path))
    # 递归搜索tiles目录
    for root, subFolders, files in os.walk(tiles_file_path):
        for tile_name in files:
            print("Reading {:40.40}".format(tile_name), flush=True, end="\r")
            tile_path = os.path.join(root, tile_name)
            large_tile, small_tile = process_tile(tile_path)
            if large_tile:
                large_tiles.append(large_tile)
                small_tiles.append(small_tile)
    print("Processed {} tiles.".format(len(large_tiles)))
    return large_tiles, small_tiles


@cuda.jit()
def get_tile_diff(t1, t2, bail_out_value):
    diff = 0
    for i in range(len(t1)):
        diff += (
            (t1[i][0] - t2[i][0]) ** 2
            + (t1[i][1] - t2[i][1]) ** 2
            + (t1[i][2] - t2[i][2]) ** 2
        )
        if diff > bail_out_value:
            # 我们已经知道这将不是最合适的，因此继续使用此图块将毫无意义
            return diff
    return diff


def get_best_fit_tile(img_data, tiles_data):
    best_fit_tile_index = None
    min_diff = sys.maxsize
    tile_index = 0
    # 依次浏览每个图块，以寻找与"img_data"代表的图像部分的最佳匹配
    img_data = List(img_data)
    for tile_data in tiles_data:
        diff = get_tile_diff(img_data, tile_data, 1048575)
        if diff < min_diff:
            min_diff = diff
            best_fit_tile_index = tile_index
        tile_index += 1
    return best_fit_tile_index


class MosaicImage:
    def __init__(self, original_img):
        self.image = Image.new(original_img.mode, original_img.size)
        self.x_tile_count = int(original_img.size[0] / TILE_SIZE)
        self.y_tile_count = int(original_img.size[1] / TILE_SIZE)
        self.total_tiles = self.x_tile_count * self.y_tile_count

    def add_tile(self, tile_data, coords):
        img = Image.new("RGB", (TILE_SIZE, TILE_SIZE))
        img.putdata(tile_data)
        self.image.paste(img, coords)

    def save(self, path):
        self.image.save(path)


if __name__ == "__main__":
    target_path = "test.jpg"
    tiles_path = "tiles"
    target_data = get_target_data(target_path)
    tiles_data = get_tiles_data(tiles_path)

    original_img_large, original_img_small = target_data
    tiles_large, tiles_small = tiles_data

    mosaic = MosaicImage(original_img_large)
    all_tile_data_large = [list(tile.getdata()) for tile in tiles_large]
    all_tile_data_small = [list(tile.getdata()) for tile in tiles_small]
    total_num = mosaic.x_tile_count * mosaic.y_tile_count
    counter = 0

    all_tile_data_small = List(List(tt) for tt in all_tile_data_small)
    for x in range(mosaic.x_tile_count):
        for y in range(mosaic.y_tile_count):
            large_box = (
                x * TILE_SIZE,
                y * TILE_SIZE,
                (x + 1) * TILE_SIZE,
                (y + 1) * TILE_SIZE,
            )
            small_box = (
                x * TILE_SIZE / TILE_BLOCK_SIZE,
                y * TILE_SIZE / TILE_BLOCK_SIZE,
                (x + 1) * TILE_SIZE / TILE_BLOCK_SIZE,
                (y + 1) * TILE_SIZE / TILE_BLOCK_SIZE,
            )
            tile_index = get_best_fit_tile(
                list(original_img_small.crop(small_box).getdata()), all_tile_data_small
            )
            tile_data = all_tile_data_large[tile_index]
            mosaic.add_tile(tile_data, large_box)
            counter += 1
            print(
                "Progress: {:04.1f}%".format(100 * counter / total_num),
                flush=True,
                end="\r",
            )
    mosaic.save(OUT_FILE)
    sys.exit()
