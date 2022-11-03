# Copyright 2017, Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division


class Histogram(object):
    """Representation of a single histogram.

    The purpose of this class is to store actual ack timing information
    in order to predict how long to renew leases.

    The default implementation uses the 99th percentile of previous ack
    times to implicitly lease messages; however, custom
    :class:`~.pubsub_v1.subscriber._consumer.Consumer` subclasses
    are free to use a different formula.

    The precision of data stored is to the nearest integer. Additionally,
    values outside the range of ``10 <= x <= 600`` are stored as ``10`` or
    ``600``, since these are the boundaries of leases in the actual API.
    """

    def __init__(self, data=None):
        """Instantiate the histogram.

        Args:
            data (Mapping[str, int]): The data strucure to be used to store
                the underlying data. The default is an empty dictionary.
                This can be set to a dictionary-like object if required
                (for example, if a special object is needed for
                concurrency reasons).
        """
        # The data is stored as a dictionary, with the keys being the
        # value being added and the values being the number of times that
        # value was added to the dictionary.
        #
        # This is depending on the Python interpreter's implicit ordering
        # of dictionaries, which is a bitwise sort by the key's ``hash()``
        # value. Because ``hash(int i) -> i`` and all of our keys are
        # positive integers (negatives would be a problem because the sort
        # is bitwise), we can rely on this.
        if data is None:
            data = {}
        self._data = data
        self._len = 0

    def __len__(self):
        """Return the total number of data points in this histogram.

        This is cached on a separate counter (rather than computing it using
        ``sum([v for v in self._data.values()])``) to optimize lookup.

        Returns:
            int: The total number of data points in this histogram.
        """
        return self._len

    def __contains__(self, needle):
        """Return True if needle is present in the histogram, False otherwise.

        Returns:
            bool: True or False
        """
        return needle in self._data

    def __repr__(self):
        return "<Histogram: {len} values between {min} and {max}>".format(
            len=len(self), max=self.max, min=self.min
        )

    @property
    def max(self):
        """Return the maximum value in this histogram.

        If there are no values in the histogram at all, return 600.

        Returns:
            int: The maximum value in the histogram.
        """
        if len(self._data) == 0:
            return 600
        return next(iter(reversed(sorted(self._data.keys()))))

    @property
    def min(self):
        """Return the minimum value in this histogram.

        If there are no values in the histogram at all, return 10.

        Returns:
            int: The minimum value in the histogram.
        """
        if len(self._data) == 0:
            return 10
        return next(iter(sorted(self._data.keys())))

    def add(self, value):
        """Add the value to this histogram.

        Args:
            value (int): The value. Values outside of ``10 <= x <= 600``
                will be raised to ``10`` or reduced to ``600``.
        """
        # If the value is out of bounds, bring it in bounds.
        value = int(value)
        if value < 10:
            value = 10
        if value > 600:
            value = 600

        # Add the value to the histogram's data dictionary.
        self._data.setdefault(value, 0)
        self._data[value] += 1
        self._len += 1

    def percentile(self, percent):
        """Return the value that is the Nth precentile in the histogram.

        Args:
            percent (Union[int, float]): The precentile being sought. The
                default consumer implementations use consistently use ``99``.

        Returns:
            int: The value corresponding to the requested percentile.
        """
        # Sanity check: Any value over 100 should become 100.
        if percent >= 100:
            percent = 100

        # Determine the actual target number.
        target = len(self) - len(self) * (percent / 100)

        # Iterate over the values in reverse, dropping the target by the
        # number of times each value has been seen. When the target passes
        # 0, return the value we are currently viewing.
        for k in reversed(sorted(self._data.keys())):
            target -= self._data[k]
            if target < 0:
                return k

        # The only way to get here is if there was no data.
        # In this case, just return 10 seconds.
        return 10
