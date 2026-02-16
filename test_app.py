from app import run

def test_echo_command():
    result = run("echo hello")
    assert b"hello" in result
