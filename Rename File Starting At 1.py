import os

directory = input("Enter the absolute directory path containing the files: ")

additional_string = input("What would you like the files to be called?")

def rename_files(directory):
    files = os.listdir(directory)
    # Sort files alphabetically
    files.sort()
    
    count = 1
    
    for filename in files:
        # Get the current file's extension
        _, extension = os.path.splitext(filename)
        # Construct the new filename with additional string
        new_filename = additional_string + " " + str(count) + extension
        # Construct the full paths to the old and new files
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Check if the new filename already exists
        while os.path.exists(new_path):
            # Append "_copy" to the filename
            new_filename = str(count) + ' ' + additional_string + '_copy' + extension
            new_path = os.path.join(directory, new_filename)
            count += 1
        
        # Rename the file
        os.rename(old_path, new_path)
        
        count += 1

rename_files(directory)
