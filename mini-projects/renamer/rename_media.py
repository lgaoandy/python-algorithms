import os
import re

def is_photo_or_video(filename):
    photo_ext = ['.jpg', '.jpeg', '.png', '.gif', '.heic', '.img']
    video_ext = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv']
    ext = os.path.splitext(filename)[1].lower()
    return ext in photo_ext or ext in video_ext

def is_video(filename):
    video_ext = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv']
    ext = os.path.splitext(filename)[1].lower()
    return ext in video_ext

def process_filename(filename):
    # Find where the first number occurs in the filename
    match = re.search(r'_(\d+_\d+)', filename)
    if match:
        basename = match.group(1)
        return f"IMG_{basename}"
    return filename

def rename_media_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip directories and non-media files
        if os.path.isdir(file_path) or not is_photo_or_video(filename):
            continue
        
        # Process the filename according to rules
        name, ext = os.path.splitext(filename)
        new_name = process_filename(name)
        
        if is_video(filename):
            new_name += "_VID"
        
        new_filename = f"{new_name}{ext}"
        new_path = os.path.join(folder_path, new_filename)
        
        # Handle potential name collisions
        counter = 1
        while os.path.exists(new_path):
            new_filename = f"{new_name}_{counter}{ext}"
            new_path = os.path.join(folder_path, new_filename)
            counter += 1
        
        os.rename(file_path, new_path)
        if filename == new_filename:
            print(f"Ignored: {filename}")
        else:
            print(f"Renamed: {filename} → {new_filename}")

if __name__ == "__main__":
    # Ask for folder
    folder_path = input("Enter folder path: ").strip('"')
    
    if os.path.exists(folder_path):
        rename_media_files(folder_path)
        print("Renaming complete!")
    else:
        print(f"Error: Folder not found at {folder_path}")