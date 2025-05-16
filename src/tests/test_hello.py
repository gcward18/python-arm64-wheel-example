import io
import sys
from helloworldpkg import print_hello_world

def test_print_hello_world(capsys):
    print_hello_world()
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello world"
