import sys
import base64
import os

def convert_to_base64(file_path):
    with open(file_path, 'rb') as f_in:
        encoded = base64.b64encode(f_in.read())
    
    new_file_path = os.path.splitext(file_path)[0] + '64.txt'
    with open(new_file_path, 'wb') as f_out:
        f_out.write(encoded)

    print(f'converted at {new_file_path}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('no file')
        sys.exit(1)

    convert_to_base64(sys.argv[1])
