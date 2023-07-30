class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = self._compute_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def _compute_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def closest_ratio_to_irrational(self, irrational):
        closest_difference = float("inf")
        closest_numerator = 0
        closest_denominator = 0

        for denominator in range(1, 101):
            numerator = round(denominator * irrational)
            difference = abs(irrational - numerator / denominator)

            if difference < closest_difference:
                closest_difference = difference
                closest_numerator = numerator
                closest_denominator = denominator

        return closest_numerator, closest_denominator
