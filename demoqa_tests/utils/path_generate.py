from pathlib import Path


def generate_path(file_name):
    return str(Path(__file__).parent.parent.parent.joinpath(f'resources/{file_name}'))
