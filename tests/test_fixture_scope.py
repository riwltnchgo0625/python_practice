# tests/ test_fixture_scope.py

import pytest

@pytest.fixture(scope="class")
def sample_data():
    print("\n데이터생성")
    return {"id":1, "name":"henry"}

class TestSample:
    def test_id(self, calcurator_instance):
        assert calcurator_instance.add(3,4)==7
        
    def test_name(self, sample_data):
        assert sample_data["name"]=="henry"

class TestGuest:
    def test_empty(self, sample_data):
        assert sample_data["id"]==1


def test_id(sample_data):
    assert sample_data["id"]==1
def test_id2(sample_data):
    assert sample_data["id"]==1    
    