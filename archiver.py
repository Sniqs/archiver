# Check if the clicked thing is a zip file or a folder
# If it's a zip: try to move it to the target directory
# If it's a folder: zip it and try to move it to the target directory

import os

import sys


def main():
    ARCHIVE_FOLDER = "D:\\Home\\Desktop\\Archiwum zleceń\\"

    item_name = os.path.basename(sys.argv[1])
    extension = os.path.splitext(item_name)[1]

    if extension.lower() == ".zip":
        move_to_archive(ARCHIVE_FOLDER, item_name)

    elif extension == "":
        zip_to_file(item_name)
        item_name += ".zip"
        # move_to_archive(ARCHIVE_FOLDER, item_name)

    else:
        os.system("cls")
        print("Incorrect file. Operation aborted.")


def zip_to_file(item_name):
    """Zips a folder to a .zip file."""

    command = '7z a "' + item_name + '.zip" "' + item_name + '"'
    os.system(command)


def move_to_archive(ARCHIVE_FOLDER, item_name):
    """Moves a .zip file into the archive folder."""

    # os.system("cls")
    try:
        os.rename(sys.argv[1], ARCHIVE_FOLDER + item_name)
        print(f"File {item_name} successfully moved to the archive.")
    except FileExistsError:
        print(f"File {item_name} already exists.")


if __name__ == "__main__":
    main()
