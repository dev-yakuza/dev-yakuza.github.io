import os
import glob


def printLazyLink(file_list):
    for file_path in file_list:
        ff = open(file_path, 'r')
        output_file_name = file_path + '_output'
        ff_output = open(output_file_name, 'w')
        for a in ff:
            if a[0:2] == '![':
                source = a[2:].split(']')
                alt = source[0]
                if('/assets/images/' in source[1]):
                    src = source[1].split('{')[0].replace(
                        '(', '').replace(')', '').strip()
                    b = '{}{} include lazyload.html image_src="{}" image_alt="{}" {}{}'.format(
                        '{', '%', src, alt, '%', '}')
                    ff_output.write(a.replace(a, b))
                else:
                    ff_output.write(a)
            else:
                ff_output.write(a)
        os.remove(file_path)
        os.rename(output_file_name, file_path)


printLazyLink(glob.glob("./_posts/**/**/*.md"))
printLazyLink(glob.glob("./_posts/**/**/**/*.md"))
