import os

# I know this is a security risk but I'm not worried about it and this is easier than setting up a config file on every machine
kaggle_json = '{"username":"ryangrayson","key":"ff71ca5843ee7c2766618b7faee5e6f9"}'

with open(os.path.expanduser('~/.kaggle/kaggle.json'), 'w') as f:
    f.write(kaggle_json)

import kaggle
kaggle.api.authenticate()
dataset = 'kyanyoga/sample-sales-data'
# fetch data via kaggle api
kaggle.api.dataset_download_files(dataset, path='./', unzip=True)
