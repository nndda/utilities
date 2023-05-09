import os
from PIL import Image

tiles_width = 16
tiles_height = 16
tileset_file = "./tileset.png"

tileset = Image.open( tileset_file )

print( tileset.width )
print( tiles_width )
print( tileset.width / tiles_width )

for x in range( int( tileset.width / tiles_width ) ):
    for y in range( int( tileset.height / tiles_height ) ):
        print(x,y)
        x_n = x * tiles_width
        y_n = y * tiles_height
        tileset_n = tileset
        cropped = tileset_n.crop( ( x_n, y_n, x_n + tiles_width, y_n + tiles_height ) )
        cropped.save(
            os.path.splitext( tileset_file )[0] + "." + str(x) + "." + str(y) + ".webp",
            format = "webp", lossless = 1 )
