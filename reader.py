"""Read and extract an input file."""
import multiprocessing
MANAGER = multiprocessing.Manager()


class Reader:
    """
    Read and extract an input file.

    Keyword Arguments:
        input_file {str} -- The input file (default: {None})

    Returns:
        tuple -- variables used by the program
        (n, mowers_movements, grid, grid_size)
    """

    def __call__(self, input_file=None):
        lines = open(input_file).readlines()
        if len(lines) % 2 == 0:
            raise ValueError("input file should have an odd number of lines")

        grid_size = lines[0].split()
        if len(grid_size) != 2:
            raise ValueError("1st line of input file should have 2 numbers")

        try:
            grid_size = tuple([int(x) for x in grid_size])
        except ValueError:
            raise ValueError("1st line of input file should be integers")

        mowers_movements = {}
        grid = {}
        for i in range(1, len(lines), 2):
            mowers_movements[i//2] = lines[i+1].strip()
            _pos = lines[i].split()
            if len(_pos) != 3:
                raise ValueError("position of mower should be X Y O")
            try:
                _pos[0], _pos[1] = int(_pos[0]), int(_pos[1])
            except ValueError:
                raise ValueError("position coordinates should be integers")

            grid[i//2] = tuple(_pos)

        n = (len(lines) - 1) // 2
        grid = MANAGER.dict(grid)
        return n, mowers_movements, grid, grid_size
