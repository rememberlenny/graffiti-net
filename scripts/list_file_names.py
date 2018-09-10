import numpy as np
import glob
import pickle

file_list = []
subdir = '/home/lkbgift/Spaceship/graffiti-net/images'

for directory_name in glob.glob(subdir + '/*'):
    print(directory_name)
    for file_path in glob.glob(directory_name + '/*'):
        print(file_path)
        file_list.append(file_path)

file_list_np = np.array(file_list)

with open('graffiti_file_names.pkl', 'wb') as f:
    pickle.dump(file_list_np, f)
