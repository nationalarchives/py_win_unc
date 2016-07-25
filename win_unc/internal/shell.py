from time import sleep
from subprocess import Popen, PIPE

from win_unc.errors import ShellCommandError
from win_unc.internal.loggers import no_logging


RETURN_CODE_SUCCESS = 0


def run(command, logger=no_logging):
    """
    Executes `command` in the shell and returns `stdout` and `stderr` as a
    tuple in that order.

    `logger` may be a function that takes a string for custom logging purposes.
    It defaults to a no-op.
    """
    process = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    while True:
        try:
            sleep(0.1)
            if process.poll() is not None:
                break

            # Write new lines in case the command prompts the us for some
            # input.
            process.stdin.write(b'\n')
        except IOError:
            pass

    stdout = process.stdout.read().decode('utf-8')
    stderr = process.stderr.read().decode('utf-8')

    # it seems that in py3k if you try to write to a windows process that
    # doesn't read its stdin, and then close that stdin, you get 1 free OSError
    try:
        process.stdin.close()
    except OSError:
        pass

    process.stdout.close()
    process.stderr.close()

    if process.returncode == RETURN_CODE_SUCCESS:
        return stdout, stderr
    else:
        raise ShellCommandError(command, process.returncode)
