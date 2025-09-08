# tests/conftest.py
import pytest
from apps.calculator import Calculator

@pytest.fixture(scope = "module")
def calcurator_instance():
    print("\n계산기 인스턴스 생성")
    c = Calculator()
    return c