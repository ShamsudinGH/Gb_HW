import os


def batch_rename(new_name, digits=3, source_ext='.txt', dest_ext='.txt', range_name: list = None, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(source_ext):
            old_name = os.path.splitext(filename)[0]
            old_name_substring = old_name[range_name[0]:range_name[1]] if range_name else ""
            new_filename = f"{old_name_substring}{new_name}{str(counter).zfill(digits)}{dest_ext}"
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            counter += 1

batch_rename('new_file', 2, '.md', '.txt', [0, 0], './output')