import pickle
import csv
import numpy

file_names = pickle.load(open('../assets/pickle/graffiti_file_names.pkl', 'rb'))

file_list = []

for file_name in file_names:
    file_without_path = file_name.split('/home/lkbgift/Spaceship/graffiti-net/images/')
    file_without_path_stub = file_without_path[1]
    file_remain = file_without_path_stub.split('/')
    print(file_remain[0])
    file_list.append(file_remain[0])

a = numpy.array(file_list)

print(a)

numpy.savetxt("graffiti_file_names.tsv", a, delimiter="\t", fmt="%s")

