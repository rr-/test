# Description

Given a list of numbers, the project prints pairs with equal sums.

# Installation

Minimum Python version: 3.13.

To be able to run unit tests:
```
python3 -m pip install -r requirements.dev.txt
```

# Usage

To run interactively:

```
$ python3 -m task
Enter numbers to analyze.
1 2 3 4 5 6
Pairs : ( 1, 4) ( 2, 3) have sum : 5
Pairs : ( 1, 5) ( 2, 4) have sum : 6
Pairs : ( 1, 6) ( 2, 5) ( 3, 4) have sum : 7
Pairs : ( 2, 6) ( 3, 5) have sum : 8
Pairs : ( 3, 6) ( 4, 5) have sum : 9
1 2 3
No pairs
$
```

To run on a specific file:

```
$ echo '1 2 3 4 5 6'| python3 -m task -f /dev/stdin
Pairs : ( 1, 4) ( 2, 3) have sum : 5
Pairs : ( 1, 5) ( 2, 4) have sum : 6
Pairs : ( 1, 6) ( 2, 5) ( 3, 4) have sum : 7
Pairs : ( 2, 6) ( 3, 5) have sum : 8
Pairs : ( 3, 6) ( 4, 5) have sum : 9
```

Results are printed to standard output.
Errors are printed to standard error output.

# Notes to readers

For a bigger app I'd include a Docker setup, but I believe it goes slightly out
of scope for this task. I also didn't include lock files and such for the sake
of simplicity, but I have worked with pip, poetry and uv before.

I used ruff, mypy and black to format / lint the code, but haven't included the
scaffolding around it.
