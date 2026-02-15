from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/run")
def run(cmd: str):
    return subprocess.run(cmd, shell=True, capture_output=True).stdout
