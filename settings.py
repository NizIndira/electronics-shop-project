from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_FILE = 'items.csv'
SRC_PATH = Path.joinpath(ROOT_PATH, 'src')
PATH_CSV_ITEMS = Path.joinpath(SRC_PATH, DATA_FILE)
