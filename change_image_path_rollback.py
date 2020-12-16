import os
import glob


def printLazyLink(file_list):
    for file_path in file_list:
        ff = open(file_path, 'r')
        output_file_name = file_path + '_output'
        ff_output = open(output_file_name, 'w')
        for a in ff:
            if 'include lazyload.html image_src="' in a:
                src = a.split('image_src="')[1].split('" image_alt="')
                b = '![{}]({})\n\n'.format(src[1].replace(
                    '" %}', '').replace('\n', ''), src[0]).replace('{% include lazyload.html', '')
                ff_output.write(a.replace(a, b))
            else:
                ff_output.write(a)
        os.remove(file_path)
        os.rename(output_file_name, file_path)


printLazyLink(glob.glob("./_posts/**/**/*.md"))
printLazyLink(glob.glob("./_posts/**/**/**/*.md"))
