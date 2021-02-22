#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 2
day = 22

def test_code():
    assert main.doubleLast([1,2,3,4,5]) == [1, 2, 3, 4, 5, 5], "doubleLast([1,2,3,4,5]) == [1, 2, 3, 4, 5, 5] failed"
    assert main.doubleLast([0,0,0,0,0,0,0,0,0,0,0,0,1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], "doubleLast([0,0,0,0,0,0,0,0,0,0,0,0,1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1] failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
