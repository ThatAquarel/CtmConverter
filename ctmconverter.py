from PIL import Image

tiles_presets = [[int(j.replace("\n", "")) for j in i.split(",")] for i in open("tiles.txt", "r").readlines()]
compact_images = [Image.open("./in/{0}.png".format(i)) for i in range(5)]
compact_tiles = []

width = compact_images[0].size[0]
height = compact_images[0].size[1]
if width != height:
    raise Exception("Image not square.")

if width % 2 != 0:
    raise Exception("Image resolution cannot be divided into 4 tiles, a width and height of 2^x is needed.")
tile_size = int(width / 2)


def concat_tiles(tile0, tile1, tile2, tile3):
    global width, height, tile_size

    out = Image.new("RGB", (width, height))
    out.paste(tile0, (0, 0))
    out.paste(tile1, (tile_size, 0))
    out.paste(tile2, (0, tile_size))
    out.paste(tile3, (tile_size, tile_size))
    return out


def main():
    global tiles_presets, compact_images, compact_tiles, tile_size

    for image in compact_images:
        tiles = []
        for y in range(2):
            for x in range(2):
                x1 = x * tile_size
                y1 = y * tile_size
                x2 = (x + 1) * tile_size
                y2 = (y + 1) * tile_size

                tiles.append(image.crop((x1, y1, x2, y2)))
        compact_tiles.append(tiles)

    for preset in tiles_presets:
        tiles = [compact_tiles[preset[i]][i - 1] for i in range(1, 5)]
        tile = concat_tiles(tiles[0], tiles[1], tiles[2], tiles[3])
        tile.save("./out/{0}.png".format(preset[0]), "PNG")

    print("Conversion complete.")


if __name__ == '__main__':
    main()
