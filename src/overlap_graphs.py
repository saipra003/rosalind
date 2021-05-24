import os # useful for modifying the current working directory (aka cwd)

# os.chdir("..") # goes up one directory similar to cd .. in the terminal
os.chdir("rosalind_datasets/test") # goes into the test directory under the datasets directory

f = open("overlap_graphs_test.txt", "r")
raw_data_list = f.readlines()

for i in range(len(raw_data_list)):
    raw_data_list[i] = raw_data_list[i].strip("\n")
print(raw_data_list)
