import os
from PIL import Image

	"""
	Converts any image files of the type in {format_img}
	in the directory and sub-directory of {target_dir}
	to WebP
	"""

target_dir = "./"
format_img = ( ".png", ".jpg", ".jpeg", ".bmp", ".gif" )
files = []

os.system("color")


for ( dir_path, dir_names, file_names ) in os.walk( target_dir ):

	file_names_f = tuple(
		filter( lambda n: n.endswith( format_img ), file_names ) )

	if file_names_f:
		files.append( ( dir_path, file_names_f ) )


def getFullDir( target ):
	files = []
	for n in target[1]:
		files.append( target[0] + "\\" + n )
	return tuple( files )

def getFileSize( target ):
	return round( os.stat( target ).st_size / (1024 * 1024), 2 )

def getPercentages( a, b ):
	return round( 100 - ( 100 * a / b ) , 2 )

def printCompareSize( a, b ):
	print( f"  {round(a,2)} MB -> {round(b,2)} MB, \u001b[36mCompressed {getPercentages(b,a)}% " )


files_total = 0
for n in files:
	for img_file in getFullDir( n ): files_total += 1


print( f"\n {files_total} files in {len(files)} directories" )


img_file_sizes = [0,0]
for n in files:
	for img_file in getFullDir( n ):
		img = Image.open( img_file )

		print( f"\n\u001b[0m  Converting {img_file}" )

		img_webp = os.path.splitext( img_file )[0] + ".webp"
		img.save( img_webp, format = "webp", lossless = 1 )

		img_file_size = ( getFileSize( img_file ), getFileSize( img_webp ) )
		compressed = getPercentages( img_file_size[1], img_file_size[0] )

		printCompareSize( img_file_size[0], img_file_size[1] )

		img_file_sizes[0] += img_file_size[0]
		img_file_sizes[1] += img_file_size[1]


compressed_total = getPercentages( img_file_sizes[1], img_file_sizes[0] )
print(
		"\n\u001b[0m  ===================================================",
		f"\n  Finished converting {files_total} files"
	)

printCompareSize( img_file_sizes[0], img_file_sizes[1] )
print("\u001b[0m")
