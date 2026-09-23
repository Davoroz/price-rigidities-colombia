"""Project paths.

All notebooks import their folders from here, so the project runs from any
location once the repository is cloned. Paths are exposed both as
``pathlib.Path`` objects and as the legacy string variables (``wd_dp``,
``wd_db``...) used throughout the notebooks.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "data"
DATA_RAW = DATA / "raw"              # scraped files, one per store (<store>_raw.csv; not published)
DATA_INTERIM = DATA / "interim"      # cleaned per-store files (<store>_clean.csv) and Retailer_data.csv
DATA_PROCESSED = DATA / "processed"  # filtered panels with regular/reference prices

RESULTS = ROOT / "results"
RESULTS_ESTIMATIONS = RESULTS / "estimations"  # product-level statistics and transition matrices
RESULTS_FIGURES = RESULTS / "figures"
RESULTS_TABLES = RESULTS / "tables"

for _folder in (DATA_RAW, DATA_INTERIM, DATA_PROCESSED,
                RESULTS_ESTIMATIONS, RESULTS_FIGURES, RESULTS_TABLES):
    _folder.mkdir(parents=True, exist_ok=True)


def _s(path: Path) -> str:
    """String version with a trailing slash, so `wd_x + "file.csv"` keeps working."""
    return path.as_posix() + "/"


# Legacy names used in the notebooks
wd = _s(ROOT)
wd_data = _s(DATA)
wd_dp = _s(DATA_RAW)
wd_db = _s(DATA_INTERIM)
wd_d = _s(DATA_INTERIM)
wd_dpr = _s(DATA_PROCESSED)
wd_r = _s(RESULTS)
wd_re = _s(RESULTS_ESTIMATIONS)
wd_rp = _s(RESULTS_FIGURES)
wd_rt = _s(RESULTS_TABLES)
wd_rdb = _s(RESULTS_ESTIMATIONS)
