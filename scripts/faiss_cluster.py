import faiss_gpu as faiss                   # make faiss available
import numpy as np
import h5py

file_name = '../graffiti-data.h5'
hf = h5py.File(file_name, 'r')

image_array = hf.get('dataset_1')
d = image_array.shape[1]

index = faiss.IndexFlatL2(d)   # build the index
print(index.is_trained)
index.add(image_array)                  # add vectors to the index
print(index.ntotal)
