from PIL import Image
import sys
import os

# The lower the quality the more pixeled the image will be
def compress( image_file, extension, quality ):

    filepath = os.path.join(os.getcwd(), image_file)

    image = Image.open(filepath)

    image.save( '_{}'.format( image_file ),
                 extension,
                 optimize = True,
                 quality = quality )
    return


def compressAllIn( path, quality ):
    for image in os.listdir( path ):
        for extension in [ 'jpeg', 'jpg', 'png' ]:
            if image.endswith( extension ):
                compress( image, extension, quality )

if __name__ == '__main__':
    quality = 10
    if len( sys.argv ) > 1:
        quality = int( sys.argv[ 1 ] )
    compressAllIn( './', quality )
