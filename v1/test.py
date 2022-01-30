# # import sys

# # for arg in sys.argv: 
# #     print (arg)
# from PIL import Image
# import numpy as np
# print('========== Image p loading ===========')
# img = Image.open('.\data\Tubingen_resized.png')
# p = np.array(img)
# print('Avant reshape : ' + str(p.shape))
# p = np.reshape(p,(512,512,3))
# print('Après reshape p : ' + str(p.shape))

# print('========== Image a loading ===========')
# img = Image.open('.\data\Derschrei_resized.png')
# a = np.array(img)
# print('Avant reshape : ' + str(a.shape))
# a = np.reshape(a,(1,512,512,3))
# print('Après reshape a : ' + str(a.shape))

# print('========== Image x loading ===========')
# iimg = Image.open('.\data\img_white_noise.png')
# x = np.array(img)
# print('shape x : ' + str(x.shape))
# import tensorflow as tf
# from matplotlib import pyplot as plt
# # years = [1950,1960,1970]
# # gdp = [300.2,543.3,1075.9]
# # plt.plot(years, gdp, color='green', linestyle='solid')
# # plt.title("Valeur de gdp")
# # plt.ylabel("Millards de dollars")
# # plt.show()
# content_image = tf.image.decode_jpeg(tf.io.read_file('.\data\Tubingen.jpg'))
# plt.imshow(content_image)
# plt.show()


# import tensorflow as tf
# m0 = tf.random.normal(shape=[2, 3])
# m1 = tf.random.normal(shape=[3, 5])
# e = tf.einsum('ij,jk->ik', m0, m1)
# # output[i,k] = sum_j m0[i,j] * m1[j, k]
# print(e.shape)

# import tensorflow as tf
# import tensorflow_hub as hub
# from functions import *
# import os
# os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
# hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
# hub_module = hub.load(hub_handle)
# content_image = load_img('.\..\data\portrait1.jpg',[224, 224])
# style_image = load_img('.\..\data\picasso.jpg', [224, 224])
# stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
# tensor_to_image(stylized_image)

import PIL.Image

# Création d'une animation
List= []
epochs = 51
for n in range(epochs) :
    fname = ".\..\data\output\_image_generée_iteration_%d.jpg" % n
    img = PIL.Image.open(fname)
    fname = ".\..\data\output\gif\_image_generée_iteration_%d.gif" % n
    img.save(fname)
    print("Image: {}".format(n))
    img = PIL.Image.open(fname)
    List.append(img)
List[0].save('.\..\data\output\gif\style_transfert.gif',save_all=True, append_images=List[1:], optimize=False, duration=100, loop=0)


from PIL import Image, ImageDraw

images = []

width = 200
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center * 1.5)
step = 8

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_1)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
    images.append(im)

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
    images.append(im)

images[0].save('.\..\data\output\pillow_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)