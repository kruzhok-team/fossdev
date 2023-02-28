import pytest

from my_math.series import (get_series,
                            get_even_series,
                            get_odd_series)

class TestSeries:
    def test_series(self):
        assert get_series(5) == [0, 1, 2, 3, 4]

    def test_even_series(self):
        assert get_even_series(5) == [0, 2, 4, 6, 8]

    def test_odd_series(self):
        assert get_odd_series(5) == [1, 3, 5, 7, 9]

    # test include the same code as in the function implementation
    def test_even_series_bad(self):
        n = 5
        even_series = [i * 2 for i in get_series(n)]
        assert get_even_series(n) == even_series
    
    # test include several functions that can be tested separetely
    def test_all_series_bad(self):
        n = 5
        assert get_series(n) == [0, 1, 2, 3, 4]
        assert get_even_series(n) == [0, 2, 4, 6, 8]
        assert get_odd_series(n) == [1, 3, 5, 7, 9]
        
    # might be a good test
    def test_series_full(self):
        series = get_even_series(5) + get_odd_series(5)
        series.sort()
        assert get_series(10) == series
        
    def test_series_parametrized(self, max_number):
        i = 0
        series = list()
        while i < max_number: 
            series.append(i)
            i = i + 1
        assert get_series(max_number) == series
