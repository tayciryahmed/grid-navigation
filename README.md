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
  * Optimize the navigation for when the mower is turned in directions that cancel each other such as RL or LLLL/RRRR. 
