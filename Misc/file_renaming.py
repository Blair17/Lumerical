import os

directory = '/Users/samblair/Desktop/Code/Projects/Lumerical/test_code/'

# List all files in the directory
files = os.listdir(directory)

# Iterate through the files
for file in files:
    if file.startswith('reflection'):
        parts = file.split('_')
        if len(parts) == 2:
            prefix, number_with_ext = parts
        else:
            # If there is no underscore, consider the entire filename as the number_with_ext
            prefix = ''
            number_with_ext = file

        if '.' in number_with_ext:
            number, ext = number_with_ext.rsplit('.', 1)  # Split from the right to handle multiple dots
            if len(number) == 3:
                new_number = f'{int(number):04d}'  # Add leading zeros to make it four digits
                new_filename = f'{prefix}_{new_number}.{ext}' if prefix else f'{new_number}.{ext}'
                os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
                print(f'Renamed {file} to {new_filename}')





                    
