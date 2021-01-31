from contextlib import contextmanager
import subprocess
import psutil
from time import sleep

import test


@contextmanager
def tidy_process(*args, **kwargs):
    proc = subprocess.Popen(*args, **kwargs)
    try:
        yield proc
    finally:
        for child in psutil.Process(proc.pid).children(recursive=True):
            child.kill()
        proc.kill()


class ProtoDriver:

    def run(self):
        with open('out.log', 'w') as out, open('err.log', 'w') as err:
            command = ['python', 'pdapi.py']
            with tidy_process(command, stdout=out, stderr=err) as proc:
                sleep(1)
                test.run_tests()
                while True:
                    pass


if __name__ == "__main__":
    app = ProtoDriver()
    app.run()
