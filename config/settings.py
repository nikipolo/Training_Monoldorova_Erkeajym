from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent

STORAGE_DIR: Path = BASE_DIR / 'storage'

STORAGE_BROWSER_DIR: Path = STORAGE_DIR / 'browser'

DOMAIN: str = 'https://demo.oraclesiebelcrm.com/'
