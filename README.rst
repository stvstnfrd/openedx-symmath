openedx-symmath
===============

A helper library for symbolic math expressions,
used by the `edx-platform`_.

This code originally lived in the `edx-platform`_ repo,
but now exists here independently.


Background
----------

At a high level, the main challenges of checking symbolic math expressions are:

1. making sure the expression is mathematically legal, and
2. simplifying the expression for comparison with what is expected.

1. Generation (and testing) of legal input is done by using MathJax to provide
input math in an XML format known as Presentation MathML (PMathML). Such
expressions typeset correctly, but may not be mathematically legal, like "5 /
(1 = 2)". The PMathML is converted into "Content MathML" (CMathML), which is
by definition mathematically legal, using an XSLT 2.0 stylesheet, via a module
in `SnuggleTeX`_. CMathML is then converted into a `SymPy`_ expression.
This work is all done in ``symmath/formula.py``.
See: `MathML`_.

2. Simplifying the expression and checking against what is expected is done by
using `SymPy`_, and a set of heuristics based on options flags provided by the
problem author. For example, the problem author may specify that the expected
expression is a matrix, in which case the dimensionality of the input
expression is checked. Other options include specifying that the comparison be
checked numerically in addition to symbolically. The checking is done in
stages, first with no simplification, then with increasing levels of testing;
if a match is found at any stage, then an "ok" is returned. Helpful messages
are also returned, eg if the input expression is of a different type than the
expected. This work is all done in ``symmath/symmath_check.py``.

License
-------

The code in this repository is licensed under version 3 of the AGPL
unless otherwise noted. Please see the `LICENSE`_ file for details.


.. _edx-platform: https://github.com/edx/edx-platform
.. _LICENSE: https://github.com/edx/openedx-symmath/blob/master/LICENSE
.. _MathML: http://www.w3.org/TR/MathML2/overview.html
.. _SnuggleTeX: http://www2.ph.ed.ac.uk/snuggletex/documentation/overview-and-features.html
.. _SymPy: http://sympy.org/en/index.html
