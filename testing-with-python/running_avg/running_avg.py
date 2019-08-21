"""
TDD example

Requirements
* Must compute the average of n datapoints with our most recent observation as the last point. (i.e. a 10 point average would use the most recent observation and the previous 9.)
* Have a method to provide a new data point one point at a time.
* Have a method to calculate the average
* When starting from a fresh start with no prior data, return the average of all data until we have at least n points.
"""


class Averager(object):
    """Calculating running average"""
    def __init__(self, npts_average=3):
        self.data = []
        self.number_of_data_points = 0
        self.npts_average = npts_average

    def add_data(self, datapoint):
        self.data.append(datapoint)
        self.number_of_data_points += 1

        if self.number_of_data_points > self.npts_average:
            self.remove_first_point()

    def remove_first_point(self):
        if self.data:
            self.data.pop(0)
            self.number_of_data_points -= 1
        else:
            raise IndexError

    def running_mean(self):
        if self.data:
            return sum(self.data) / self.number_of_data_points
        else:
            raise IndexError
