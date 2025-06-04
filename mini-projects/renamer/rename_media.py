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
    # Check if filename starts with a number
    if re.match(r'^\d', filename):
        return f"IMG_{filename}"
    
    # Find where the first number occurs in the filename
    match = re.search(r'\d', filename)
    if match:
        first_num_pos = match.start()
        prefix = filename[:first_num_pos]
        rest = filename[first_num_pos:]
        return f"IMG_{rest}-{prefix.strip('_')}"
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
        
        # Add -VID suffix for videos
        if is_video(filename):
            new_name += "-VID"
        
        new_filename = f"{new_name}{ext}"
        new_path = os.path.join(folder_path, new_filename)
        
        # Handle potential name collisions
        counter = 1
        while os.path.exists(new_path):
            new_filename = f"{new_name}_{counter}{ext}"
            new_path = os.path.join(folder_path, new_filename)
            counter += 1
        
        os.rename(file_path, new_path)
        print(f"Renamed: {filename} → {new_filename}")

if __name__ == "__main__":
    folder_path = input("Enter folder path: ").strip('"')  # Change this to your target folder
    if os.path.exists(folder_path):
        rename_media_files(folder_path)
        print("Renaming complete!")
    else:
        print(f"Error: Folder not found at {folder_path}")