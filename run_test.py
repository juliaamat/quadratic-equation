#!/usr/bin/env python3
# coding: utf8
env = globals().copy()

import sys
import os
import unittest

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def runfile(name, skip=16, **kwargs):
    filename = name + '.py'
    with open(filename, encoding='utf8') as file:
        source = file.read()
    if source[0] == '\ufeff':
        source = source[1:]
    source = "\n".join([""] * skip + source.splitlines()[skip:]) + "\n"
    code = compile(source, filename, 'exec')
    vars = kwargs.copy()
    vars['solutions'] = ()
    exec(code, env, vars)
    return vars.get('solutions')


########################################################################################################################


class TestRoots(unittest.TestCase):
    def assert_roots(self, solutions, *ref):
        solutions = sorted(solutions)
        self.assertEqual(len(solutions), len(ref), "Wrong number of results")
        for x, r in zip(solutions, ref):
            self.assertAlmostEqual(x, r)

    def test_sample0(self):
        solutions = runfile('exercise1', a=1, b=2, c=3)
        self.assert_roots(solutions)

    def test_sample1(self):
        solutions = runfile('exercise1', a=1, b=-2, c=1)
        self.assert_roots(solutions, 1.)

    def test_sample2(self):
        solutions = runfile('exercise1', a=3, b=-2, c=-1)
        self.assert_roots(solutions, -0.33333333333333, 1.)

    def test_sampleL(self):
        solutions = runfile('exercise1', a=0, b=-2, c=1)
        self.assert_roots(solutions, 0.5)


if __name__ == '__main__':
    test = unittest.main(exit=False)
    sys.exit(not test.result.wasSuccessful())
