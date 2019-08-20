"""
* Sometimes we need to create a special test function to help us
solve a specific issue over and over. In this case, we’re going
to make a special test helper that checks if the first row of a
pandas dataframe is equal to one we specify with the caveat that
the row we are comparing to can have more columns or the columns
in a different order than our truth values.

This is helpful when the returned data may have more columns
(i.e. a certain station may have a radiation sensor and another may not).


* vcrpy
VCR.py simplifies and speeds up tests that make HTTP requests.
The first time you run code that is inside a VCR.py context manager
or decorated function, VCR.py records all HTTP interactions that
take place through the libraries it supports and serializes and
writes them to a flat file (in yaml format by default).
This flat file is called a cassette. When the relevant piece of code
is executed again, VCR.py will read the serialized requests and
responses from the aforementioned cassette file, and intercept any
HTTP requests that it recognizes from the original test run and
return the responses that corresponded to those requests.
https://vcrpy.readthedocs.io/en/latest/index.html
"""
from numpy.testing import assert_almost_equal
import vcr

def assert_dataseries_equal(actual, desired):
    """
    Intelligently compare dataseries (i.e. dictionary) for testing.
    Only compares the keys that are in desired, i.e. there can be extra keys
    in actual and the test will pass. Handles comparison of floating points
    in a more intelligent way and does not require fields to be lined up in
    the same order.
    """
    for key in desired.keys():
        # If this is a float, then check accordingly
        if 'float' in str(type(desired.get(key))):
            assert_almost_equal(actual.get(key), desired.get(key))
        else:
            assert actual.get(key) == desired.get(key)


def get_recorder(test_file_path):
    """Return an appropriate response recorder for the given path."""
    return vcr.VCR(cassette_library_dir=str(test_file_path / 'fixtures'))