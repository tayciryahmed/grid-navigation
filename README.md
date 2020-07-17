# grid-navigation

[![Build Status](https://travis-ci.org/tayciryahmed/grid-navigation.svg?branch=master)](https://travis-ci.org/tayciryahmed/grid-navigation)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8bb6f8af62004bb9b9179ac840cf702b)](https://app.codacy.com/manual/tayciryahmed/grid-navigation?utm_source=github.com&utm_medium=referral&utm_content=tayciryahmed/grid-navigation&utm_campaign=Badge_Grade_Dashboard)
[![codecov](https://codecov.io/gh/tayciryahmed/grid-navigation/branch/master/graph/badge.svg)](https://codecov.io/gh/tayciryahmed/grid-navigation)

Grid navigation for multiple mowers.

## Requirements 

Python 3.7

## To execute on a file

```bash
python navigation.py <input_file>
```

## To run the tests

```bash
python -m pytest tests
```

## Further improvements

  * Console entry point for `navigation.py`.
  * Further improve the pylint score (current score 9.37/10).
  * Change the reader the be an interator to manage big files and not read all lines in memory. Use of `next` to read mowers information inside the `worker`. The max number of processes (in the loop) would be the resources (processors) we have available.
  * Optimize the navigation for when the mower is turned in directions that cancel each other such as RL or LLLL/RRRR. 
  * Manage the case many mowers are in the same position initially.
  * The check to ovoid overlapping mowers in [navigation.py#L28](https://github.com/tayciryahmed/grid-navigation/blob/master/navigation.py#L28) is not correct because considers the orientation, while comparing a 2-element tuple to a 3-element tuple.
  * Change all 'R', 'L', 'F' strings in string with an enum class in utils.py and or simply a dict (e.g. for multilingual input).
