import pytest
import utils

def test_fact():
    assert utils.fact(3) == 6

def test_roots():
    assert utils.roots(1,0,0) == 0


def test_integrate():
    assert utils.integrate(1,0,1) == 1
