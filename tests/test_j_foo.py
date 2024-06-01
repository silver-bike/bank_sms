from src.j_foo import data_from_json

def test_data_from_json():
    assert data_from_json("../test.json") == [{'id': 1001, 'group': 'Cure', 'song': 'Friday'}, {'id': 1002, 'group': 'Doors', 'song': 'Fire'}]