import pytest


@pytest.fixture(scope="session")
def dummy_data():
    dummy_data = """5 5
        1 2 N
        LFLFLFLFF
        3 3 E
        FFRFFRFRRF"""
    yield dummy_data


@pytest.fixture(scope="function")
def dummy_data_path(dummy_data, tmpdir):
    data_path = str(tmpdir.join("test.txt"))
    with open(data_path, "w") as f:
        f.writelines(dummy_data)

    return data_path
