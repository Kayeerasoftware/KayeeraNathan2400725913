#file automation
#get the file path downlod
#file path
import os
from pathlib import Path
import shutil
from datetime import datetime
from dataclasses import dataclass


        #old way using the os.path
file_path = os.path.join("os.path.expanduse("~"), "Downloads", "report.pdf")

        #new way using pathlib
file_path = Path.home() / "Downloads" / "report.pdf"

        #file organisation
        #Real we can automatically organise a downlod folder by the file  type

@dataclass(frozen=True):
class config:
    source_folder: Path = Path.home() / "Downloads"
    destination_folder: Path = Path.home() / "Documents" / "Organized_Files"
    dry_run: bool = True  

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".cs"],
}:
#ASSIGNMENT:  Write a python script that automatically organizes files in the Downloads folder based on their file types. The script should create subfolders for each file type (e.g., Images, Documents, Videos, etc.) and move the corresponding files into their respective folders. Additionally, implement a dry run mode that allows users to see what changes would be made without actually moving any files.
#code logic for file automation
def get_target_category(filepath: path) -> str: