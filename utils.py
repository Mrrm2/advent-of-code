def read_file_to_array(file_name: str) -> list:
    with open(file_name) as f:
        text = f.read().splitlines()
    return text