"""
TDD example

Make a test list
* Is initialized to an empty list
* Number of points attribute is zero on initialization
* Test adding a datapoint when empty
* Test adding a datapoint when partially full
* Test removing the oldest datapoint
* Test adding a datapoint when full
* Returns correct average for 1 data point
* Returns correct average for n-1 data points
* Returns correct average for n data points
* Returns correct average for n+1 data points
* Returns correct average after 2n data points
"""
import pytest

from running_avg.running_avg import Averager


def test_is_list_initialized_to_empty():
    """Test if the data list is empty after initialization."""
    # Setup
    avg = Averager()

    # Exercise/Verify
    assert avg.data == []

    # Teardown - none


def test_number_of_points_is_zero_on_initialization():
    """Test that the number of data points is zero on initialization."""
    # Setup
    avg = Averager()

    # Exercise/Verify
    assert avg.number_of_data_points == 0

    # Teardown - none

def test_adding_datapoint_to_empty():
    """Test adding a datapoint to an empty instance."""
    # Setup
    avg = Averager()

    # Exercise
    avg.add_data(1)

    # Verify
    assert avg.data == [1]
    assert avg.number_of_data_points == 1

    # Teardown - none


def test_adding_datapoint_to_partially_full():
    """Test adding a datapoint to a partially full instance."""
    # Setup
    avg = Averager()

    # Exercise
    avg.add_data(1)
    avg.add_data(2)
    avg.add_data(3)

    # Verify
    assert avg.data == [1, 2, 3]
    assert avg.number_of_data_points == 3

    # Teardown - none


def test_remove_first_point():
    """Test removing the first point from the list."""
    # Setup
    avg = Averager()

    # Exercise
    avg.add_data(1)
    avg.add_data(2)
    avg.add_data(3)

    avg.remove_first_point()

    # Verify
    assert avg.data == [2, 3]
    assert avg.number_of_data_points == 2

    # Teardown - none


def test_adding_datapoint_to_full():
    """Test adding data point to full list"""
    # Setup
    avg = Averager()

    # Exercise
    for i in range(1, 5):
        avg.add_data(i)

    # Verify
    assert avg.data == [2, 3, 4]
    assert avg.number_of_data_points == 3

    # Teardown - none


def test_average_for_one_data_point():
    """Test calculating average for one data point"""
    # Setup
    avg = Averager(3)

    # Exercise
    avg.add_data(5)
    average = avg.running_mean()

    # Verify
    assert average == 5

    # Teardown - none


def test_average_for_n_minus_one_data_points():
    """Test calculating average for n -1 data point"""
    # Setup
    avg = Averager(3)

    # Exercise
    avg.add_data(5)
    avg.add_data(7)
    average = avg.running_mean()

    # Verify
    assert average == 6

    # Teardown - none


def test_average_for_n_data_points():
    """Test calculating average for n data point"""
    # Setup
    avg = Averager(3)

    # Exercise
    avg.add_data(5)
    avg.add_data(7)
    avg.add_data(9)
    average = avg.running_mean()

    # Verify
    assert average == 7

    # Teardown - none


def test_average_for_n_plus_one_data_points():
    """Test calculating average for n + 1 data point"""
    # Setup
    avg = Averager(3)

    # Exercise
    avg.add_data(5)
    avg.add_data(7)
    avg.add_data(9)
    avg.add_data(11)
    average = avg.running_mean()

    # Verify
    assert average == 9

    # Teardown - none


def test_average_for_2n_data_points():
    """Test calculating average for 2n data point"""
    # Setup
    avg = Averager(3)

    # Exercise
    for i in range(1, 7):
        avg.add_data(i)
    average = avg.running_mean()

    # Verify
    assert average == 5

    # Teardown - none


def test_remove_from_empty_list():
    """
    Test to see if it raises an exception
    when trying to remove data form a zero length dataset
    """
    # Setup
    avg = Averager(3)

    # Exercise/Verify
    with pytest.raises(IndexError):
        avg.remove_first_point()

    # Teardown - none


def test_calculate_average_from_empty_list():
    """
    Test to see if it raises an exception
    when trying to calculate average form a zero length dataset
    """
    # Setup
    avg = Averager(3)

    # Exercise/Verify
    with pytest.raises(IndexError):
        avg.running_mean()

    # Teardown - none
