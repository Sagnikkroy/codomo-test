import subprocess

def run(cmd: str):
    return subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True,
    ).stdout
