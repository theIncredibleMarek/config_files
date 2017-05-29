from os import listdir
from os.path import isfile, join

my_path = "./"
only_nonhidden_folders = [f for f in listdir(my_path) if not(
    isfile(join(my_path, f))) and f[0] != "."]
print(only_nonhidden_folders)

readme = open("./README.md", "w")
readme.seek(0)
readme.write("# Configuration files for:\n")
for f in only_nonhidden_folders:
    f[0].capitalize()
    readme.write("* {}{}\n".format(f[0].capitalize(), f[1:]))
readme.close()
