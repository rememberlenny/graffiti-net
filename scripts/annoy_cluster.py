from annoy import AnnoyIndex
import numpy as np
import h5py

file_name = '../graffiti-data.h5'
hf = h5py.File(file_name, 'r')
image_array = hf.get('dataset_1')
np_image_array = np.array(image_array)

d = np_image_array.shape[1]
t = AnnoyIndex(d)

for i, v in enumerate(np_image_array.tolist()):
    t.add_item(i, v)
    print(v)
t.build(10) # 10 trees
t.save('graffiti_data.ann')

