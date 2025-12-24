import os
import shutil

image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff"]
document_extensions = [".txt", ".pdf", ".docx", ".xlsx", ".doc", ".ppt", ".pptx", ".xls", ".csv"]
video_extensions = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"]
audio_extensions = [".mp3", ".wav", ".aac", ".flac", ".ogg"]
archieves_extensions = [".zip", ".rar", ".7z", ".tar", ".gz"]
path = input("Enter the path:")
folder_path = path.strip()
list_of_items = os.listdir(folder_path)



images_path = os.path.join(folder_path, "Images")
documents_path = os.path.join(folder_path, "Documents")
videos_path = os.path.join(folder_path, "Videos")
audios_path = os.path.join(folder_path, "Audios")
archieves_path = os.path.join(folder_path, "Archieves")
others_path = os.path.join(folder_path, "Others")

os.makedirs(images_path , exist_ok = True)     # if the folder already exist then it will not return any error
os.makedirs(documents_path , exist_ok = True)
os.makedirs(videos_path , exist_ok = True)
os.makedirs(audios_path , exist_ok = True)
os.makedirs(archieves_path , exist_ok = True)
os.makedirs(others_path , exist_ok = True)

for item in list_of_items:
    full_path = os.path.join(folder_path, item)

    # working only with files not with folders
    if os.path.isfile(full_path):
        name, extension = os.path.splitext(item)
        extension = extension.lower()

        if extension in image_extensions:
            destination_file = os.path.join(images_path, item)
            if os.path.exists(destination_file):
                print("Skipped (already exists): ", item)
            else:
                shutil.move(full_path, images_path)
        elif extension in document_extensions:
            destination_file = os.path.join(documents_path, item)
            if os.path.exists(destination_file):
                print("Skipped (already exists): ", item)
            else:
                shutil.move(full_path, documents_path)
        elif extension in video_extensions:
            destination_file = os.path.join(videos_path, item)
            if os.path.exists(destination_file):
                print("Skipped (already exists): ", item)
            else:
                shutil.move(full_path, videos_path)
        elif extension in audio_extensions:
            destination_file = os.path.join(audios_path, item)
            if os.path.exists(destination_file):
                print("Skipped (already exists): ", item)
            else:
                shutil.move(full_path, audios_path)
        elif extension in video_extensions:
            destination_file = os.path.join(videos_path, item)
            if os.path.exists(destination_file):
                print("Skipped (already exists): ", item)
            else:
                shutil.move(full_path, videos_path)
        elif extension in archieves_extensions:
            destination_file = os.path.join(archieves_path, item)
            if os.path.exists(destination_file):
                print("Skipped (already exists): ", item)
            else:
                shutil.move(full_path, archieves_path)
        else:
            destination_file = os.path.join(others_path, item)
            if os.path.exists(destination_file):
                print("Skipped (already exists): ", item)
            else:
                shutil.move(full_path, others_path)
    else:
        print("It is a folder: ", item)
