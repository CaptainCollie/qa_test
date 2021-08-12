import hashlib
import os
from pathlib import Path


def check_file(input_file, check_dir):
    if os.path.exists(check_dir):
        list_of_files = os.listdir(check_dir)
    else:
        return 'Dir does not exist'

    if not os.path.exists(input_file):
        return 'Input file does not exist'

    item = ''

    with open(input_file, 'r', encoding='UTF-8') as f:
        test_list = f.readlines()

    files_to_check = [i.split()[0] for i in test_list]

    with open('./output_file.txt', 'w', encoding='UTF-8') as fw:
        for j, i in enumerate(files_to_check):
            res = ''
            if i in list_of_files:
                with open(Path(check_dir, i), 'r', encoding='UTF-8') as f:
                    item = f.readlines()
                    item = '\n'.join(item).encode()
            else:
                res = 'NOT FOUND'

            method = test_list[j].split()[1]
            input_coded = test_list[j].split()[2]
            coded_file = ''

            if method == 'md5':
                coded_file = hashlib.md5(item).hexdigest()
            if method == 'sha1':
                coded_file = hashlib.sha1(item).hexdigest()
            if method == 'sha256':
                coded_file = hashlib.sha256(item).hexdigest()

            if not res:
                res = 'YES' if coded_file == input_coded else 'FAIL'
            print(f'{i} {res}')
            fw.write(f'{i} {res}')
            fw.write('\n')
