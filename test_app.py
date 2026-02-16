import sys
from app import run


def test_echo_command():
    result = run(f"{sys.executable} -c \"print('hello')\"")
    assert "hello" in result
