import os

folder = "/home/muhammad-ahmed/Documents/snaptrace/data/fail"

files = os.listdir(folder)

for i, file in enumerate(files):
    old_path = os.path.join(folder, file)

    ext = file.split(".")[-1]

    new_name = f"{i:04d}.{ext}"
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)

print("Done")