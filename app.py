import subprocess
from fastapi import FastAPI

app = FastAPI()

def run(cmd: str):
    return subprocess.run(
        cmd,
        shell=True,
        capture_output=True
    ).stdout
