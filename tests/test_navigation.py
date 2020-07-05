import subprocess
import navigation


def test_worker():
    navigation.GRID = {0: (1, 2, 'N')}
    instructions = 'LFLFLFLFF'
    navigation.worker(instructions, 0, (5, 5))
    assert navigation.GRID[0] == (1, 3, 'N')


def test_worker_2():
    navigation.GRID = {0: (1, 2, 'N')}
    instructions = 'RFF'
    navigation.worker(instructions, 0, (5, 5))
    assert navigation.GRID[0] == (3, 2, 'E')


def test_worker_3():
    navigation.GRID = {0: (1, 2, 'N'), 1: (3, 3, 'E')}
    instructions = 'LFLFLFLFF'
    navigation.worker(instructions, 0, (5, 5))
    assert navigation.GRID[1] == (3, 3, 'E')


def test_worker_4():
    navigation.GRID = {0: (1, 4, 'N')}
    instructions = 'FF'
    navigation.worker(instructions, 0, (5, 5))
    assert navigation.GRID[0] == (1, 5, 'N')


def test_worker_5():
    navigation.GRID = {0: (1, 4, 'N')}
    instructions = 'FFRFLFLF'
    navigation.worker(instructions, 0, (5, 5))
    assert navigation.GRID[0] == (1, 5, 'W')


def test_worker_6():
    navigation.GRID = {0: (1, 4, 'S')}
    instructions = 'FFFFFFRFFFF'
    navigation.worker(instructions, 0, (5, 5))
    assert navigation.GRID[0] == (0, 0, 'W')


def test_navigation(dummy_data_path):
    result = subprocess.run([
        'python', './navigation.py',
        dummy_data_path
    ], capture_output=True, check=True)
    assert result.returncode == 0


def test_navigation_2(dummy_data_path):
    result = subprocess.check_output([
        'python', './navigation.py',
        dummy_data_path
    ])
    print(result)
    assert result == b'1 3 N\n5 1 E\n'
