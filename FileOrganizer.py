import os
import shutil

path = r'C:\Users\adham\Downloads'

# Create destination folders outside the loop
media_folder = os.path.join(path, 'Media')
pdf_folder = os.path.join(path, 'PDFs')
compressed_folder = os.path.join(path, 'Compressed')
documents_folder = os.path.join(path, 'Documents')
misc_folder = os.path.join(path, 'Miscellaneous')

for folder in (media_folder, pdf_folder, compressed_folder, documents_folder, misc_folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

files = os.listdir(path)

for file in files:
    if os.path.isdir(os.path.join(path, file)):
        continue

    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if extension in ('mp4', 'mkv', 'avi', 'mov', 'jpg', 'jpeg', 'png', 'bmp'):
        shutil.move(os.path.join(path, file), os.path.join(media_folder, file))
    elif extension == 'pdf':
        shutil.move(os.path.join(path, file), os.path.join(pdf_folder, file))
    elif extension in ('zip', 'rar', '7z'):
        shutil.move(os.path.join(path, file), os.path.join(compressed_folder, file))
    elif extension in ('docx', 'txt', 'log'):
        shutil.move(os.path.join(path, file), os.path.join(documents_folder, file))
    else:
        shutil.move(os.path.join(path, file), os.path.join(misc_folder, file))
