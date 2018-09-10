from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import h5py
import glob

hf = h5py.File('graffiti-data.h5', 'w')
model = VGG16(weights='imagenet', include_top=False)

vgg16_feature_list = []

subdir = '/home/lkbgift/Spaceship/graffiti-net/images'

for directory_name in glob.glob(subdir + '/*'):
    print(directory_name)
    for file_path in glob.glob(directory_name + '/*'):
        print(file_path)
        img = image.load_img(file_path, target_size=(224, 224))
        img_data = image.img_to_array(img)
        img_data = np.expand_dims(img_data, axis=0)
        img_data = preprocess_input(img_data)

        vgg16_feature = model.predict(img_data)
        vgg16_feature_np = np.array(vgg16_feature)
        vgg16_feature_list.append(vgg16_feature_np.flatten())

vgg16_feature_list_np = np.array(vgg16_feature_list)

hf.create_dataset('dataset_1', data=vgg16_feature_list_np)
hf.close()

kmeans = KMeans(n_clusters=2, random_state=0).fit(vgg16_feature_list_np)
