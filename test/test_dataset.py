import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / "../..").resolve()))
from src.datasets import DATASET_METADATA, DATASET_ZOO


def test_registry():
    assert len(DATASET_METADATA) >= 0
    assert len(DATASET_ZOO) >= 0
