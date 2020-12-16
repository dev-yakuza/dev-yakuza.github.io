import os
import glob


def printLazyLink(file_list):
    for file_path in file_list:
        ff = open(file_path, 'r')
        output_file_name = file_path + '_output'
        ff_output = open(output_file_name, 'w')
        for a in ff:
            ff_output.write(a.replace('href=" https', 'href="https'))
        os.remove(file_path)
        os.rename(output_file_name, file_path)


printLazyLink(glob.glob("./_site/**/*.html", recursive=True))
