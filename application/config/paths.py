from pathlib import Path
from typing import Final


ROOT_PATH: Final[Path] = Path(__file__).parents[2]
FILES_INPUT: Final[Path] = ROOT_PATH.joinpath("files_input", "text.txt")
FILES_INPUT_CSV: Final[Path] = ROOT_PATH.joinpath("files_input", "people.csv")
