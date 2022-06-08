# HOMEWORK

Try hard edition

> !!! You need python 3.8 to run this because I use the `walrus` a.k.a. `:=` operator. Because it's 2022 ffs.

## Numbers Dictionary

### Option One

The simple solution is to just run...
```bash
python Numbers_Dictionary.py
```
...and then interact with the code on the prompt.

Alternatively you can go into the file and change the `DEBUG` constant to `True`. This will then make the program run in an automated debug mode that reads input from the `TEST_RUNS` nested `tuples`.

In this mode both the standart and alt solution will be executed sequentially.

### Option Two

The over engeneered solution is to run...
```bash
python numbers_dictionary
```
...and then interact with the code on the prompt.

Alternatively...
```bash
python numbers_dictionary -h
usage: numbers_dictionary [-h] [--inputs INPUTS] [--solution SOLUTION]

Numbers Dictionary Solver

optional arguments:
  -h, --help           show this help message and exit
  --inputs INPUTS      Path to a json file holding test run inputs
  --solution SOLUTION  The solution to test. Available options are "first" and "second".
```
The `numbers_dictionary.json` file holds test data. You can pass it to the module with the `--inputs` argument. This will run the solution non-interactivley with the inputs supplied in the file. The two solutions are files in the `numbers_dictionary` module. They are called `first` and `second`. You can specify the wanted solution with the `--solution` argument.
```bash
python numbers_dictionary --solution first --inputs numbers_dictionary.json
python numbers_dictionary --solution second --inputs numbers_dictionary.json
```
This is what hapens if the homework is fucking boring.
