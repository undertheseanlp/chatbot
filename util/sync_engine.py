from os import listdir
from shutil import copy

from os.path import dirname, join

original = "hoaian"
target = "hungcuong"

engine_folder = join(dirname(dirname(__file__)), "engine", "eg")
original_folder = join(engine_folder, original)
target_folder = join(engine_folder, target)
for file in listdir(original_folder):
    if file != "personality.rive":
        print("Sync {}".format(file))
        copy(join(original_folder, file), join(target_folder, file))