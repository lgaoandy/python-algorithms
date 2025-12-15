import os
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
import ffmpeg
from datetime import datetime
import re

def sanitize_filename(name):
    """Remove invalid characters from filename"""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def get_date_taken(file_path):
    """Extract actual date taken from media metadata"""
    file_path = Path(file_path)
    file_ext = file_path.suffix.lower()
    
    # Image files - try to get EXIF DateTimeOriginal
    if file_ext in {'.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.heic', '.webp'}:
        try:
            with Image.open(file_path) as img:
                exif_data = img._getexif()
                if exif_data:
                    # Priority order for date tags
                    date_tags = ['DateTimeOriginal', 'DateTimeDigitized', 'DateTime']
                    
                    for tag_name in date_tags:
                        for tag_id, value in exif_data.items():
                            tag = TAGS.get(tag_id, tag_id)
                            if tag == tag_name and value:
                                try:
                                    # Convert EXIF date string to datetime object
                                    return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                                except ValueError:
                                    try:
                                        return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                                    except ValueError:
                                        continue
        except Exception as e:
            print(f"Error reading image EXIF data: {e}")
    
    # Video files - try to get creation_time from metadata
    elif file_ext in {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.m4v'}:
        try:
            probe = ffmpeg.probe(str(file_path))
            format_info = probe.get('format', {})
            tags = format_info.get('tags', {})
            
            # Priority order for video date tags
            video_date_tags = ['creation_time', 'date', 'DATE', 'DateTimeOriginal']
            
            for tag in video_date_tags:
                if tag in tags and tags[tag]:
                    time_str = tags[tag]
                    try:
                        # Handle ISO format (common in videos)
                        if 'T' in time_str:
                            return datetime.fromisoformat(time_str.replace('Z', '+00:00'))
                        # Handle other common formats
                        elif ':' in time_str and '-' in time_str:
                            return datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
                        elif ':' in time_str:
                            return datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
                    except ValueError as e:
                        print(f"Error parsing video date {tag}: {time_str} - {e}")
                        continue
                        
        except Exception as e:
            print(f"Error reading video metadata: {e}")
    
    # If no date taken found, return None instead of falling back to file time
    return None

def rename_file_to_date_taken(file_path, dry_run=True):
    """Rename file to its actual date taken from metadata"""
    file_path = Path(file_path)
    
    try:
        date_taken = get_date_taken(file_path)
        
        if date_taken is None:
            print(f"SKIPPED: {file_path.name} - No date taken metadata found")
            return None
        
        # Format the timestamp for filename (YYYY-MM-DD_HH-MM-SS)
        timestamp_str = date_taken.strftime('%Y-%m-%d_%H-%M-%S')
        
        # Get original file extension
        file_ext = file_path.suffix
        
        # Create new filename
        new_filename = f"{timestamp_str}{file_ext}"
        new_file_path = file_path.parent / new_filename
        
        # Handle duplicate names by adding counter
        counter = 1
        original_new_path = new_file_path
        while new_file_path.exists():
            new_filename = f"{timestamp_str}_{counter:02d}{file_ext}"
            new_file_path = file_path.parent / new_filename
            counter += 1
        
        if dry_run:
            print(f"WOULD RENAME: {file_path.name}")
            print(f"         TO: {new_file_path.name}")
            print(f"  DATE TAKEN: {date_taken.strftime('%Y-%m-%d %H:%M:%S')}")
            return None
        else:
            file_path.rename(new_file_path)
            print(f"RENAMED: {file_path.name} -> {new_file_path.name}")
            print(f"DATE TAKEN: {date_taken.strftime('%Y-%m-%d %H:%M:%S')}")
            return new_file_path
            
    except Exception as e:
        print(f"Error processing {file_path.name}: {e}")
        return None

def process_folder_by_date_taken(folder_path, dry_run=True):
    """Process all media files in folder and rename them to date taken"""
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Folder {folder_path} does not exist!")
        return
    
    # Supported media extensions
    media_extensions = {
        '.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.heic', '.webp',
        '.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.m4v'
    }
    
    media_files = [f for f in folder.iterdir() 
                  if f.is_file() and f.suffix.lower() in media_extensions]
    
    if not media_files:
        print("No media files found!")
        return
    
    print(f"Found {len(media_files)} media files")
    print("DRY RUN MODE" if dry_run else "LIVE RENAME MODE")
    print("=" * 60)
    
    renamed_count = 0
    skipped_count = 0
    
    for file_path in media_files:
        result = rename_file_to_date_taken(file_path, dry_run=dry_run)
        if result:
            renamed_count += 1
        else:
            # Check if it was skipped due to no date taken
            date_taken = get_date_taken(file_path)
            if date_taken is None:
                skipped_count += 1
        print("-" * 40)
    
    print(f"\nSummary:")
    print(f"Total files processed: {len(media_files)}")
    print(f"Files with date taken metadata: {renamed_count}")
    print(f"Files without date taken metadata: {skipped_count}")
    
    if not dry_run:
        print(f"Successfully renamed {renamed_count} files")


if __name__ == "__main__":
    folder_path = input("Enter folder path: ").strip('"')
    
    # First, do a dry run to see what would happen
    print("=== DRY RUN (no changes will be made) ===")
    process_folder_by_date_taken(folder_path, dry_run=True)
    
    # Uncomment the line below to actually rename files
    # print("\n=== LIVE RUN (files will be renamed) ===")
    # process_folder_by_date_taken(folder_path, dry_run=False)