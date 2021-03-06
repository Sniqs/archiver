import os
import shutil
import subprocess
import sys


def main():
    ARCHIVE_FOLDER = "D:\\Home\\Desktop\\New archive\\"

    item_name = os.path.basename(sys.argv[1])
    extension = os.path.splitext(item_name)[1]

    if extension.lower() == ".zip":
        move_to_archive(ARCHIVE_FOLDER, item_name)

    elif extension == "":
        zip_to_file(item_name)
        item_name += ".zip"
        sys.argv[1] += ".zip"
        move_to_archive(ARCHIVE_FOLDER, item_name)

    else:
        subprocess.run("cls", shell=True)
        print("Incorrect file. Operation aborted.")


def zip_to_file(item_name):
    """Zips a folder to a .zip file and deletes the folder.

    Args:
        item_name (str): The name of the folder to zip.
    """

    try:
        subprocess.run('7z a "' + sys.argv[1] + '.zip" "' + sys.argv[1] + '"')
    except Exception as e:
        print(f"A problem occured when zipping the folder: {e}")
        sys.exit()
    else:
        try:
            shutil.rmtree(sys.argv[1])
        except OSError as e:
            print(f"Error: {e.strerror}")


def move_to_archive(ARCHIVE_FOLDER, item_name):
    """Moves a .zip file into the archive folder.

    Args:
        ARCHIVE_FOLDER (str): The folder where the file is to be archived.
        item_name (str): The name of the zip file to archive.
    """

    subprocess.run("cls", shell=True)
    if os.path.isdir(ARCHIVE_FOLDER):
        try:
            shutil.move(sys.argv[1], ARCHIVE_FOLDER)
        except FileExistsError:
            print(f'File "{item_name}" already exists.')
        else:
            print(
                f'File "{item_name}" successfully moved to the archive folder "{ARCHIVE_FOLDER}".'
            )
        finally:
            print("All done.")
    else:
        print(f'Target folder: "{ARCHIVE_FOLDER}" doesn\'t exist.')


if __name__ == "__main__":
    main()
