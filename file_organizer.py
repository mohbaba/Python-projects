import os
import shutil


def organize(path_name):
    os.chdir(path_name)
    directory = os.listdir(path_name)
    extensions = {
        '.txt': 'Text Files',
        '.pdf': 'PDFs',
        '.jpg': 'Images',
        '.png': 'Images',
        '.xlsx': 'Spreadsheets',
        '.docx': 'Documents',
        '.mp3': 'Music',
        '.mp4': 'Videos',
        '.mkv':'Videos',
        '.zip' : 'Zip Files',
        '.exe' : 'Software Setups',
        '.srt':'Videos'
        # Add more file extensions and folder names as needed
    }
    split_files = []
    ext= []
    filename = []
    # splits the files into their filenames and extensions
    for filename in os.listdir(path_name):
        file = os.path.join(path_name , filename)
        
        if os.path.isfile(file):
            _,file_ext = os.path.splitext(filename)
            
            if file_ext.lower() in extensions:
                new_directory = os.path.join(path_name, extensions[file_ext.lower()])
                os.makedirs(new_directory,exist_ok=True)
                
                shutil.move(filename, os.path.join(new_directory, filename))
                print(f"Moved {filename} to {new_directory}")
        


p= organize(r'C:\Users\hp\Downloads\New folder\New folder')

