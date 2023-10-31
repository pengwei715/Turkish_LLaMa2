import subprocess
from pathlib import Path

def download_file_with_wget(url, filename=None):
    """
    Download a file using wget.
    
    Parameters:
    - url (str): URL of the file to download
    - filename (str, optional): Name of the file to save the downloaded content to.
                                If not provided, wget will use the original filename.
    """
    cmd = ["wget", url]
    
    if filename:
        cmd.extend(["-O", filename])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"File successfully downloaded from {url}")
        if filename:
            print(f"Saved as {filename}")
    else:
        print(f"Error downloading file from {url}")
        print(result.stderr)

    return Path(filename)

# Example usage:
# download_file_with_wget('https://example.com/path/to/file', 'local_filename.txt')
