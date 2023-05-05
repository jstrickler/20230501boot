import os
from datetime import datetime

START_DIR = "."

for dir, subdirs, files in os.walk(START_DIR):
    if '.git' in subdirs:
        subdirs.remove('.git')  # remove .git from subdirs so it won't be visited
    print(dir)
    for file_name in files:
        if file_name.startswith('p'):
            file_path = os.path.join(dir, file_name)
            file_size = os.path.getsize(file_path)
            raw_timestamp = os.path.getmtime(file_path)
            file_datetime = datetime.fromtimestamp(raw_timestamp)
            print(f"    {file_size:10d} {file_datetime.strftime('%x')} {file_name}")