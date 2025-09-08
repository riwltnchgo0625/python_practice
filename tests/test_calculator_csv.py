# tests/test_calculator_csv.py

import csv
import pytest

def load_cases(path):
    cases = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            a = row['a']
            b = row['b']
            expected = row['expected_result']
            cases.append( (a, b, expected) )
    return cases
        

ADD_CASES = load_cases("tests/data/add.csv")
print(ADD_CASES)

def trans(s):
    if s == "":
        return None
    try:
        return int(s)
    except ValueError:
        return s        #숫자로 못바꾸면 그대로 문자열쓰겠다


@pytest.mark.parametrize("a,b,expected", ADD_CASES)
def test_add_from_csv(calcurator_instance, a,b,expected):
    a = trans(a)
    b = trans(b)
    expected = trans(expected) #if expected is not None else None

    if expected == "TypeError":
        with pytest.raises(TypeError):
            calcurator_instance.add(a,b)
    else:
        assert calcurator_instance.add(a,b) == expected
