import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath) # changing the filepath from string to a special pathlib object
            archive.write(filepath, arcname=filepath.name) # the dot name method provides the file name without the folder structure behind it.

if __name__ == "__main__":
    make_archive(filepaths=["file.txt"], dest_dir="dest")