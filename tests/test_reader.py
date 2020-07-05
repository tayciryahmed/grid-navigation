from reader import Reader


def test_reader(dummy_data_path):
    reader = Reader()
    n, mowers_movements, grid, grid_size = reader(dummy_data_path)
    assert n == 2
    assert mowers_movements == {0: 'LFLFLFLFF', 1: 'FFRFFRFRRF'}
    assert grid_size == (5, 5)
    assert dict(grid) == {0: (1, 2, 'N'), 1: (3, 3, 'E')}
