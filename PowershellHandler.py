import subprocess


def create_directory(project_name: str, file_path: str = None) -> bool:
    """Creates a directory with the name project_name

    Args:
        file_path (str, optional): File path to create the new directory at. Defaults to current directory.

    Returns:
        bool: True if directory was created successfully, false otherwise.
    """


def run(cmd: str) -> subprocess.CompletedProcess:
    """Basic function to run any given powershell command. Dangerous!

    Args:
        cmd (str): Command to run

    Returns:
        subprocess.CompletedProcess: Returns a CompletedProcess object.
    """
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)

    return completed
