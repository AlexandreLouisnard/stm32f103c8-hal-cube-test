# Try to replace each file in TARGET_DIR subdirs by the same file (name) from SOURCE_DIR subdirs

import os
import shutil
import sys

# Update these directories
# Use -r parameter to invert these two dirs
SOURCE_DIRS = ["stm32f103c8-hal-cube-test/src", "lala"]
TARGET_DIRS = ["cubemx-code-generator", "LILI"]

# Reverse ?
if (len(sys.argv) > 1 and sys.argv[1] == '-r'):
    tmp = SOURCE_DIRS
    SOURCE_DIRS = TARGET_DIRS
    TARGET_DIRS = tmp

print('Copy from SOURCE={}\ninto TARGET={}'.format(SOURCE_DIRS, TARGET_DIRS))

# Work from script dir
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)

print('Trying to replace each file in TARGET_DIRS by the same file (name) from SOURCE_DIRS')

for target_dir in TARGET_DIRS:
    if(not os.path.isdir(target_dir)):
        print('TARGET DIR {} => NOT FOUND, skipping'.format(target_dir))
        continue
    target_files = [os.path.join(dp, f) for dp, dn, fn in os.walk(
        os.path.expanduser(target_dir)) for f in fn]
    for target_file in target_files:
        # for each target file (in target dirs and subdirs)
        found = False
        target_filename = os.path.split(target_file)[1]
        for source_dir in SOURCE_DIRS:
            if(not os.path.isdir(source_dir)):
                print('SOURCE DIR {} => NOT FOUND, skipping'.format(source_dir))
                continue
            source_files = [os.path.join(dp, f) for dp, dn, fn in os.walk(
                os.path.expanduser(source_dir)) for f in fn]
            for source_file in source_files:
                # check if the same file (name) exists in source dirs and subdirs
                source_filename = os.path.split(source_file)[1]
                if (target_filename == source_filename):
                    # found ! copy it
                    found = True
                    try:
                        shutil.copyfile(source_file, target_file)
                    except shutil.SameFileError:
                        pass
                    break
            if found:
                break
        print('{0:2}'.format('X' if found else ''), end=" ")
        print(target_filename)



# exit()

# for subdir in TARGET_SUBDIRS:
#     dir = os.path.join(TARGET_DIR, subdir)
#     for filename in os.listdir(dir):
#         # For each file in TARGET_DIR subdirs
#         found = False
#         for subdir2 in SOURCE_SUBDIRS:
#             # Search for replacement in SOURCE_DIR subdirs
#             file2 = os.path.join(SOURCE_DIR, subdir2, filename)
#             if (os.path.isfile(file2)):
#                 # Found => copy !
#                 found = True
#                 try:
#                     shutil.copyfile(file2, os.path.join(dir, filename))
#                 except shutil.SameFileError:
#                     pass
#                 break
#         print('{0:2}'.format('X' if found else ''), end=" ")
#         print(filename)
