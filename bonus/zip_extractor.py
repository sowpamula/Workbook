import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/Users/sowjanya/PycharmProjects/pythonProject_U/bonus/compressed.zip","/Users/sowjanya/PycharmProjects/pythonProject_U/bonus/files")