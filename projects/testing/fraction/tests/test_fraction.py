from fraction import Fraction

def test_simplify():
    fraction = Fraction(6, 9)
    fraction.simplify()
    assert fraction.numerator == 2
    assert fraction.denominator == 3

def test_compute_gcd():
    fraction = Fraction(15, 25)
    gcd = fraction._compute_gcd(15, 25)
    assert gcd == 5

def test_closest_ratio_to_irrational():
    fraction = Fraction(7, 20)

    # Test with an irrational number of 0.3
    irrational_number = 0.3
    numerator, closest_denominator = fraction.closest_ratio_to_irrational(irrational_number)
    assert numerator == 3
    assert closest_denominator == 10

    # Test with an irrational number of 0.8
    irrational_number = 0.8
    numerator, closest_denominator = fraction.closest_ratio_to_irrational(irrational_number)
    assert numerator == 4
    assert closest_denominator == 5

    # Test with an irrational number of 0.5
    irrational_number = 0.5
    numerator, closest_denominator = fraction.closest_ratio_to_irrational(irrational_number)
    assert numerator == 1
    assert closest_denominator == 2

    # Test with an irrational number of 0.123456789
    irrational_number = 0.123456789
    numerator, closest_denominator = fraction.closest_ratio_to_irrational(irrational_number)
    assert numerator == 10
    assert closest_denominator == 81
