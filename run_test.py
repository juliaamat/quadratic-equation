#!/usr/bin/env python3
# coding: utf8
import sys
from io import StringIO
from unittest.mock import patch
import unittest
env = globals().copy()


def runfile(name, skip=0, **kwargs):
    filename = name + '.py'
    with open(filename, encoding='utf8') as file:
        source = file.read()
    if source[0] == '\ufeff':
        source = source[1:]
    source = "\n".join([""] * skip + source.splitlines()[skip:]) + "\n"
    code = compile(source, filename, 'exec')
    exec(code, env, kwargs)


def patchio():
    return lambda meth: patch('sys.stdout', new_callable=StringIO)(meth)

########################################################################################################################


class TestRoots(unittest.TestCase):

    def assert_roots(self, stdout, res1, res2):
        out = stdout.getvalue()
        if not out:
            raise ValueError("Nothing printed")
        x1, x2 = out.split()
        x1 = complex(x1)
        x2 = complex(x2)
        if x2.real < x1.real or (x1.real == x2.real and x2.imag < x1.imag):
            x1, x2 = x2, x1
        self.assertAlmostEqual(x1, res1)
        self.assertAlmostEqual(x2, res2)

    @patchio()
    def test_default(self, stdout):
        runfile('exercise1')
        self.assert_roots(stdout, (-1-1.4142135623730951j), (-1+1.4142135623730951j))

    @patchio()
    def test_sample1(self, stdout):
        runfile('exercise1', 15, a=1, b=-2, c=1)
        self.assert_roots(stdout, 1., 1.)

    @patchio()
    def test_sample2(self, stdout):
        runfile('exercise1', 15, a=3, b=-2, c=-1)
        self.assert_roots(stdout, -0.33333333333333, 1.)


if __name__ == '__main__':
    test = unittest.main(exit=False)
    sys.exit(not test.result.wasSuccessful())
