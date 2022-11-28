import argparse
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable


def path_type(exists: bool = True) -> "Callable[[str], Path]":
    """Path type for use with argparse

    Args:
        exists (bool, optional): whether or not path should exist. Defaults to True.
    """

    def to_path(pathname: str) -> Path:
        path = Path(pathname)
        if exists != path.exists():
            raise argparse.ArgumentTypeError(
                f"{path} should {'exist' if exists else 'not exist'}."
            )
        return path

    return to_path
