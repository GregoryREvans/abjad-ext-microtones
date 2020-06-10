import fractions


class RatioClassSet:
    """
    Ratio Class Set.

    >>> from abjadext import microtones

    """

    def __init__(self, ratio_classes):
        self.ratio_classes = []
        for ratio in ratio_classes:
            ratio = fractions.Fraction(ratio)
            assert 0 < ratio
            while 2 < ratio:
                ratio /= 2
            while ratio < fractions.Fraction(1, 2):
                ratio *= 2
            if ratio not in self.ratio_classes:
                self.ratio_classes.append(ratio)

    def __iter__(self):
        """
        Iterates contents.

        ..  container:: example

            >>> pc_set = microtones.RatioClassSet([1, 2, 3])
            >>> for item in pc_set:
            ...     item
            Fraction(1, 1)
            Fraction(2, 1)
            Fraction(3, 2)

            >>> for x in microtones.RatioClassSet(["31/2", "10", "33/4", "36/10", "113/10"]).prime_form():
            ...     print(x)
            1487/1023
            1
            290/279
            4175/3503
            199/155

        """
        for ratio in self.ratio_classes:
            yield ratio

    def __len__(self):
        """
        Gets length of contents.

        ..  container:: example

            >>> len(microtones.RatioClassSet([1, 2, 3]))
            3

        """
        return len(self.ratio_classes)

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.RatioClassSet([1, 2, 3])
            RatioClassSet([Fraction(1, 1), Fraction(2, 1), Fraction(3, 2)])

        """
        return f"{self.__class__.__name__}({self.ratio_classes})"

    def __str__(self):
        """
        Gets string representation.

        ..  container:: example

            >>> str(microtones.RatioClassSet([1, 2, 3]))
            '{1, 2, 3/2}'

        """
        output = "{"
        for i, ratio in enumerate(self.ratio_classes):
            output += f"{ratio}"
            if i != len(self.ratio_classes) - 1:
                output += ", "
        output += "}"
        return output

    def _rotate(self, n):
        copied_list = [i for i in self.ratio_classes]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return RatioClassSet(copied_list_)

    def _transpose_to_one(self):
        return self.transpose(-min(self.ratio_classes) + 1)

    @staticmethod
    def _binary_value(i):
        value = 0
        for bit in i:
            value += 2 ** bit
        return value

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_set = microtones.RatioClassSet([1, 2, 3])
            >>> input_scale = [i + 1 for i in range(11)]
            >>> pc_set.complement(input_scale)
            RatioClassSet([Fraction(3, 2), Fraction(2, 1), Fraction(5, 4), Fraction(7, 4), Fraction(9, 8), Fraction(11, 8)])

        """
        complements = []
        for ratio in scale:
            if ratio not in self.ratio_classes:
                complements.append(ratio)
        return RatioClassSet(complements)

    def invert(self, axis=1):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.RatioClassSet([2, 4, 3]).invert()
            RatioClassSet([Fraction(1, 2), Fraction(2, 3)])

            >>> microtones.RatioClassSet([2, 4, 3]).invert(3)
            RatioClassSet([Fraction(3, 2), Fraction(2, 1)])

        """
        assert 0 < axis
        inverse = [axis / i for i in self.ratio_classes]
        return RatioClassSet(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.RatioClassSet([1, 2, 3]).multiply(2)
            RatioClassSet([Fraction(2, 1), Fraction(3, 2)])

        """
        multiplied_pitch_classes = [n * ratio for ratio in self.ratio_classes]
        return RatioClassSet(multiplied_pitch_classes)

    def normal_order(self):
        """
        Gets normal order.

        ..  container:: example

            >>> microtones.RatioClassSet([2, 4, 3]).normal_order()
            RatioClassSet([Fraction(2, 1), Fraction(3, 2)])

        """
        size = len(self.ratio_classes)
        if size < 2:
            return RatioClassSet(self.ratio_classes)
        original = self.sorted()
        rotations = [original._rotate(n) for n in range(size)]
        candidate = rotations.pop()
        candidate_binary_value = self._binary_value(candidate._transpose_to_one())
        for rotation in rotations:
            alternative_candidate_binary_value = self._binary_value(
                rotation._transpose_to_one()
            )
            if alternative_candidate_binary_value < candidate_binary_value:
                candidate = rotation
                candidate_binary_value = alternative_candidate_binary_value
        return candidate

    def prime_form(self):
        """
        Gets prime form.

        ..  container:: example

            >>> microtones.RatioClassSet([2, 4, 3]).prime_form()
            RatioClassSet([Fraction(7, 6), Fraction(1, 1)])

        """
        original = self.normal_order()._transpose_to_one()
        inverted = self.invert().normal_order()._transpose_to_one()
        if self._binary_value(original) < self._binary_value(inverted):
            return original
        else:
            return inverted

    def sorted(self):
        """
        Gets Ratio Class Set sorted in ascending order.

        ..  container:: example

            >>> microtones.RatioClassSet([5, 2, 3]).sorted()
            RatioClassSet([Fraction(5, 4), Fraction(3, 2), Fraction(2, 1)])

        """
        return RatioClassSet(sorted(self.ratio_classes))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.RatioClassSet([1, 2, 3]).transpose(2)
            RatioClassSet([Fraction(3, 2), Fraction(2, 1), Fraction(7, 4)])

            >>> microtones.RatioClassSet([1, 2, 4, 5, 6]).invert().transpose(1+3)
            RatioClassSet([Fraction(5, 4), Fraction(9, 8), Fraction(6, 5), Fraction(7, 6)])

        """
        transposed = [ratio + n for ratio in self.ratio_classes]
        return RatioClassSet(transposed)


class RatioSet:
    """
    Ratio Set.

    >>> from abjadext import microtones

    """

    def __init__(self, ratios):
        self.ratios = []
        for ratio in ratios:
            ratio = fractions.Fraction(ratio)
            assert 0 < ratio
            if ratio not in self.ratios:
                self.ratios.append(ratio)

    def __iter__(self):
        """
        Iterates contents.

        ..  container:: example

            >>> pc_set = microtones.RatioSet([1, 2, 3])
            >>> for item in pc_set:
            ...     item
            Fraction(1, 1)
            Fraction(2, 1)
            Fraction(3, 1)

            >>> for x in microtones.RatioSet(["31/2", "10", "33/4", "36/10", "113/10"]):
            ...     print(x)
            31/2
            10
            33/4
            18/5
            113/10

        """
        for ratio in self.ratios:
            yield ratio

    def __len__(self):
        """
        Gets length of contents.

        ..  container:: example

            >>> len(microtones.RatioSet([1, 2, 3]))
            3

        """
        return len(self.ratios)

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.RatioSet([1, 2, 3])
            RatioSet([Fraction(1, 1), Fraction(2, 1), Fraction(3, 1)])

        """
        return f"{self.__class__.__name__}({self.ratios})"

    def __str__(self):
        """
        Gets string representation.

        ..  container:: example

            >>> str(microtones.RatioSet([1, 2, 3]))
            '{1, 2, 3}'

        """
        output = "{"
        for i, ratio in enumerate(self.ratios):
            output += f"{ratio}"
            if i != len(self.ratios) - 1:
                output += ", "
        output += "}"
        return output

    def _rotate(self, n):
        copied_list = [i for i in self.ratios]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return RatioSet(copied_list_)

    def _transpose_to_one(self):
        return self.transpose(-min(self.ratios) + 1)

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_set = microtones.RatioSet([1, 2, 3])
            >>> input_scale = [i + 1 for i in range(11)]
            >>> pc_set.complement(input_scale)
            RatioSet([Fraction(4, 1), Fraction(5, 1), Fraction(6, 1), Fraction(7, 1), Fraction(8, 1), Fraction(9, 1), Fraction(10, 1), Fraction(11, 1)])

        """
        complements = []
        for ratio in scale:
            if ratio not in self.ratios:
                complements.append(ratio)
        return RatioSet(complements)

    def invert(self, axis=1):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.RatioSet([2, 4, 3]).invert()
            RatioSet([Fraction(1, 2), Fraction(1, 4), Fraction(1, 3)])

            >>> microtones.RatioSet([2, 4, 3]).invert(3)
            RatioSet([Fraction(3, 2), Fraction(3, 4), Fraction(1, 1)])

        """
        assert 0 < axis
        inverse = [axis / i for i in self.ratios]
        return RatioSet(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.RatioSet([1, 2, 3]).multiply(2)
            RatioSet([Fraction(2, 1), Fraction(4, 1), Fraction(6, 1)])

        """
        multiplied_pitch_classes = [n * ratio for ratio in self.ratios]
        return RatioSet(multiplied_pitch_classes)

    def sorted(self):
        """
        Gets Ratio Class Set sorted in ascending order.

        ..  container:: example

            >>> microtones.RatioSet([5, 2, 3]).sorted()
            RatioSet([Fraction(2, 1), Fraction(3, 1), Fraction(5, 1)])

        """
        return RatioSet(sorted(self.ratios))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.RatioSet([1, 2, 3]).transpose(2)
            RatioSet([Fraction(3, 1), Fraction(4, 1), Fraction(5, 1)])

            >>> microtones.RatioSet([1, 2, 4, 5, 6]).invert().transpose(1+3)
            RatioSet([Fraction(5, 1), Fraction(9, 2), Fraction(17, 4), Fraction(21, 5), Fraction(25, 6)])

        """
        transposed = [ratio + n for ratio in self.ratios]
        return RatioSet(transposed)
