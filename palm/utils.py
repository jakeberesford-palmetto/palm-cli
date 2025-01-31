from typing import Optional, Tuple
import subprocess
from sys import version_info


class UnsupportedVersion(Exception):
    pass


def is_cmd_file(filename: str) -> bool:
    return filename.endswith(".py") and filename.startswith("cmd")


def cmd_name_from_file(filename: str) -> str:
    return filename[4:-3]


def run_on_host(
    cmd: str, bubble_error: Optional[bool] = False
) -> Tuple[int, str, str]:
    """A simplifed, platform-and-version agnostic interface
        for subprocess.
        By default run_on_host makes some strong
        conventional choices: 
         - calls are run as a shell
         - calls are blocking
         - errors in the shell are NOT bubbled up by default
        Args:
            cmd: the command to run.
            bubble_error: if True raise a `CalledProcessError<https://docs.python.org/3.6/library/subprocess.html#subprocess.CalledProcessError>`_
        Returns:
            Tuple: status code, stdout, stderr
    """
    major, minor, patch, _, _ = version_info
    kwargs = dict(shell=True, check=bubble_error)
    if major < 3 or minor < 5:
        raise UnsupportedVersion(f"Python version {major}.{minor} is not supported.")
    if minor < 7:
        from subprocess import PIPE

        kwargs.update(dict(stdout=PIPE, stderr=PIPE))
    else:
        kwargs.update(dict(capture_output=True))
    completed = subprocess.run(cmd, **kwargs)
    return (
        completed.returncode,
        completed.stdout.decode("utf-8"),
        completed.stderr.decode("utf-8"),
    )
