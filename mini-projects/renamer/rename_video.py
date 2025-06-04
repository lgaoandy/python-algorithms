import os

def rename_videos(folder_path):
    # Supported video extensions (modify as needed)
    video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv']

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip directories and non-video files
        if os.path.isdir(file_path):
            continue
        
        # Check if file is a video
        ext = os.path.splitext(filename)[1].lower()
        if ext not in video_extensions:
            continue
        
        # Check if filename starts with "VID" (case-insensitive)
        if filename.upper().startswith("VID"):
            # Remove "VID" prefix and add "-VID" suffix
            new_name = "IMG" + filename[3:]  # Replace "VID" with "IMG"
            new_name = os.path.splitext(new_name)[0] + "-VID" + ext  # Add "-VID" before extension
            new_path = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(file_path, new_path)
            print(f"Renamed: {filename} → {new_name}")
        else:
            print(f"Skipped (no 'VID' prefix): {filename}")

if __name__ == "__main__":
    folder_path = r"C:\Users\Andy\Downloads\Photos-1-001"  # Hardcoded path
    if os.path.exists(folder_path):
        rename_videos(folder_path)
        print("Renaming complete!")
    else:
        print(f"Error: Folder not found at {folder_path}")