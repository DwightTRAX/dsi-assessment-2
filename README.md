# Week 2 Assessment

Welcome to the second week of Zipfian!

* Time: 60 minutes
* Open book
* Individual

## Assignment

The goal of this assignment is to fill in each function stub in `assessment.py` according to its docstring and make the associated test pass. The repository structure is below for reference. `assessment.py` is under `src` directory.

There are 10 questions in `assessment.py` over these topics in this order:

* general Python (4 questions)
* pandas (3 questions)
* SQL (3 questions)

We recommend skimming over all the questions and solving the ones that you are most confident about first.

 * **Running Unit Tests**

 * You can run the tests with this command from the root directory (assessment-2/):    

    `make test`

 * If you do not have unittest2 or py.test, you may see Import errors. Run the following commands in case you see such errors:    

    * `pip install unittest2`    
    * `pip install pytest`     

 * `.` refers to passing test, `E` is an error in the code and `F` is a failure. So something that looks like this: `....EFFFFFF` means 4 tests passed, one has an error and 6-11 fail.
 * It can be helpful to press enter a bunch of times between each time you run the test so that it's easy to find the beginning of your most recent results.    

## Repository Structure

The repository has the following folder structure:

        assessment-2
        ├── Makefile
        ├── README.md
        ├── src
        │   ├── __init__.py
        │   ├── assessment.py
        ├── data
        │   ├── people.txt
        │   ├── housing.sql
        |   |-- buy.csv
        |   |-- rent.csv
        ├── test
            ├── __init__.py
            └── unittests.py


* At the end of 60 minutes, don't forget to submit a pull request.

**Feel free to use any online resources like python documentation and tutorials, your notes, readings and exercises.**

Good luck!
