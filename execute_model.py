import subprocess

def extract_objects(ids, csv_path, save_dir):
    command = ["python", "extract_objects.py", "--ids", ",".join(ids), "--csv", csv_path, "--dir", save_dir]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("Object extraction successful!")
    else:
        print(f"Error: {result.stderr}")

# Example usage
ids = ["id1", "id2", "id3"]
extract_objects(ids, "data/sample.csv", "outputs/")
