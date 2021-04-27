import requests
import zipfile

# @see http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py

def download_file(url):
    filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        return filename

    return False

def zip_extract(filename):
    target_directory = './data'
    zfile = zipfile.ZipFile(filename)
    zfile.extractall(target_directory)

if __name__ == "__main__":
    url = 'https://www.rosenzu.com/~gtfs/gifu/gifu_GTFS.zip'
    filename = download_file(url)
    if filename:
        print('{} is downloaded.'.format(filename))
    zip_extract(filename)
  