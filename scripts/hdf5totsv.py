import numpy as np
import h5py
np.savetxt('graffiti_data.tsv', h5py.File('../assets/hdf5/graffiti-data.h5')['dataset_1'], '%g', '\t')
