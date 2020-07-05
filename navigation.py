"""Navigation script through the grid (lawn)."""
import functools
import multiprocessing
import argparse
from reader import Reader
from utils import (orientations, movements)


def worker(instructions, m_id, grid_size):
    """
    Perform the grid updates given a mower.

    Arguments:
        instructions {str} -- string of instructions with chars R/L/F.
        m_id {int} -- id of the mower
        grid_size {tuple} -- grid (lawn) max X and max Y.
    """
    orientation = GRID[m_id][2]
    for instruction in instructions:
        if instruction in ['R', 'L']:
            orientation = orientations[(orientation, instruction)]
            c_ind = GRID[m_id]
            GRID[m_id] = (c_ind[0], c_ind[1], orientation)
        elif instruction == 'F':
            mov = movements[orientation]
            c_ind = GRID[m_id]
            new_pos = (c_ind[0]+mov[0], c_ind[1]+mov[1])
            if (new_pos not in GRID.values()) and (
                    0 <= new_pos[0] <= grid_size[0]) and (
                    0 <= new_pos[1] <= grid_size[1]):
                GRID[m_id] = (c_ind[0] + mov[0], c_ind[1] + mov[1], orientation)
        else:
            raise ValueError("instructions should be R/L/F.")


if __name__ == "__main__":
    # get path to input file
    PARSER = argparse.ArgumentParser(description='Mower navigation.')
    PARSER.add_argument('input_file', type=str,
                        help='File with the input specifications')
    ARGS = PARSER.parse_args()

    # read inputs
    READER = Reader()
    n, MOWERS_MOVEMENTS, GRID, GRID_SIZE = READER(ARGS.input_file)

    # start processing
    PROCESSES = []
    for i in range(n):
        PROCESSES.append(multiprocessing.Process(
            target=functools.partial(worker, m_id=i,
                                     grid_size=GRID_SIZE),
            args=[MOWERS_MOVEMENTS[i]]))

    for i in range(n):
        PROCESSES[i].start()

    for i in range(n):
        PROCESSES[i].join()
    
    # grid has a sparse representation: {'mower_id': (X, Y, O)} 
    for mower in GRID.values():
        print(str(mower[0]) + " " + str(mower[1]) + " " + mower[2])
