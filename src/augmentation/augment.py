from keras.preprocessing.image import ImageDataGenerator
import io
from PIL import Image
datagen = ImageDataGenerator(
            rotation_range=5,
            height_shift_range=0.05,
            width_shift_range=0.05,
            # shear_range=0.05,
            zoom_range=0.1)

# Your image directories and saving directory.
# byteImgIO = io.BytesIO()
# byteImg = Image.open(r"C:/Users/User/Desktop/c")
# byteImg.save(byteImgIO, "PNG")
# byteImgIO.seek(0)
# byteImg = byteImgIO.read()

image_directory = 'C:/Users/User/Desktop/a'
# image_directory = Image.open(r'C:/Users/User/Documents/research/c').tobytes()
save_directory = 'C:/Users/User/Desktop/new_augment/VT-GT'

i = 0
for batch in datagen.flow_from_directory(directory=image_directory,
                                         batch_size=64,
                                         color_mode="rgb",
                                         save_to_dir=save_directory,
                                         save_prefix='c_',
                                         save_format='png'):
    i += 1
    if i > 6:
        break