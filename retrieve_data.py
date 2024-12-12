import pyhdfs
import pandas as pd

def read_csv_from_hadoop(hdfs_host, hdfs_port, file_path):
    fs = pyhdfs.HdfsClient(hosts=f"{hdfs_host}:{hdfs_port}")
    if fs.exists(file_path):
        with fs.open(file_path) as f:
            df = pd.read_csv(f)
        return df
    else:
        raise FileNotFoundError("File not found in HDFS!")

def retrieve_fits_files(hdfs_host, hdfs_port, folder_path, ids, local_save_dir):
    fs = pyhdfs.HdfsClient(hosts=f"{hdfs_host}:{hdfs_port}")
    for file_id in ids:
        remote_path = f"{folder_path}/{file_id}.fits"
        local_path = f"{local_save_dir}/{file_id}.fits"
        if fs.exists(remote_path):
            with fs.open(remote_path) as remote_file, open(local_path, "wb") as local_file:
                local_file.write(remote_file.read())
            print(f"Downloaded: {file_id}.fits")
