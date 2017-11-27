from os import path, makedirs
from shutil import copyfile, move


class ImageCopier:
    def __init__(self, args, img_list):
        dir_input = args.in_dir
        dir_output = args.out_dir

        # stop if input dir not exist
        if not path.exists(dir_input):
            print("Input directory " + dir_input + " does not exist.")
            return

        # create output dir if not exist
        if not path.exists(dir_output):
            makedirs(dir_output)

        count = 0
        total = len(img_list)
        for img in img_list:
            # attach filename to input/output paths
            i_from = '/'.join((dir_input, img))
            i_to = '/'.join((dir_output, img))

            # move file if removing from original dir,
            # else copy it over instead
            if args.remove_original:
                move(i_from, i_to)
            else:
                copyfile(i_from, i_to)

            # print progress
            count += 1
            print("\r" + str(count) + "/" + str(total), end="", flush=True)

        print()
