import fractions


class RatioClassSet(object):
    """
    Ratio Class Set.

    >>> from abjadext import microtones

    """

    def __init__(self, ratio_classes):
        self.ratio_classes = []
        for ratio in ratio_classes:
            ratio = fractions.Fraction(ratio)
            assert 0 < ratio
            if ratio < 1:
                ratio = fractions.Fraction(ratio.denominator, ratio.numerator)
            while 2 < ratio:
                ratio /= 2
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

            >>> for x in microtones.RatioClassSet(["31/2", "10", "33/4", "36/10", "113/10"]):
            ...     print(x)
            31/16
            5/4
            33/32
            9/5
            113/80

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

    def __add__(self, argument):
        argument = type(self)(argument)
        items = self.ratio_classes + argument.ratio_classes
        return type(self)(items)

    def __contains__(self, argument):
        return super().__contains__(argument)

    def __getitem__(self, argument):
        return super().__getitem__(argument)

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
            RatioClassSet([Fraction(2, 1), Fraction(3, 2)])

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

    def sorted(self):
        """
        Gets Ratio Class Set sorted in ascending order.

        ..  container:: example

            >>> microtones.RatioClassSet([5, 2, 3, "1/2", 1, "1/5"]).sorted()
            RatioClassSet([Fraction(1, 1), Fraction(5, 4), Fraction(3, 2), Fraction(2, 1)])

        """
        return RatioClassSet(sorted(self.ratio_classes))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.RatioClassSet([1, 2, 3]).transpose(2)
            RatioClassSet([Fraction(3, 2), Fraction(2, 1), Fraction(7, 4)])

            >>> microtones.RatioClassSet([1, 2, 4, 5, 6]).invert().transpose(1+3)
            RatioClassSet([Fraction(5, 4), Fraction(3, 2), Fraction(21, 16), Fraction(11, 8)])

        """
        transposed = [ratio + n for ratio in self.ratio_classes]
        return RatioClassSet(transposed)


class RatioSet(object):
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

    def __add__(self, argument):
        argument = type(self)(argument)
        items = self.ratios + argument.ratios
        return type(self)(items)

    def __contains__(self, argument):
        return super().__contains__(argument)

    def __getitem__(self, argument):
        return super().__getitem__(argument)

    def constrain_to_octave(self):
        """
        Gets Ratio Set constrained within an octave.

        ..  container:: example

            >>> str(microtones.RatioSet([1, 3, "1/5"]).constrain_to_octave())
            '{1, 3/2, 4/5}'

        """
        constrained = []
        for ratio in self.ratios:
            while 2 < ratio:
                ratio /= 2
            while ratio < fractions.Fraction(1, 2):
                ratio *= 2
            constrained.append(ratio)
        return RatioSet(constrained)

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


class RatioClassSegment(object):
    """
    Ratio Class Segment.

    >>> from abjadext import microtones

    """

    def __init__(self, ratio_classes):
        self.ratio_classes = []
        for ratio in ratio_classes:
            ratio = fractions.Fraction(ratio)
            assert 0 < ratio
            if ratio < 1:
                ratio = fractions.Fraction(ratio.denominator, ratio.numerator)
            while 2 < ratio:
                ratio /= 2
            self.ratio_classes.append(ratio)

    def __iter__(self):
        """
        Iterates contents.

        ..  container:: example

            >>> pc_segment = microtones.RatioClassSegment([1, 2, 3, 3])
            >>> for item in pc_segment:
            ...     item
            Fraction(1, 1)
            Fraction(2, 1)
            Fraction(3, 2)
            Fraction(3, 2)

            >>> for x in microtones.RatioClassSegment(["31/2", "10", "33/4", "36/10", "113/10"]):
            ...     print(x)
            31/16
            5/4
            33/32
            9/5
            113/80

        """
        for ratio in self.ratio_classes:
            yield ratio

    def __len__(self):
        """
        Gets length of contents.

        ..  container:: example

            >>> len(microtones.RatioClassSegment([1, 2, 3]))
            3

        """
        return len(self.ratio_classes)

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.RatioClassSegment([1, 2, 3])
            RatioClassSegment([Fraction(1, 1), Fraction(2, 1), Fraction(3, 2)])

        """
        return f"{self.__class__.__name__}({self.ratio_classes})"

    def __str__(self):
        """
        Gets string representation.

        ..  container:: example

            >>> str(microtones.RatioClassSegment([1, 2, 3]))
            '(1, 2, 3/2)'

        """
        output = "("
        for i, ratio in enumerate(self.ratio_classes):
            output += f"{ratio}"
            if i != len(self.ratio_classes) - 1:
                output += ", "
        output += ")"
        return output

    def __add__(self, argument):
        argument = type(self)(argument)
        items = self.ratio_classes + argument.ratio_classes
        return type(self)(items)

    def __contains__(self, argument):
        return super().__contains__(argument)

    def __getitem__(self, argument):
        return super().__getitem__(argument)

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_segment = microtones.RatioClassSegment([1, 2, 3])
            >>> input_scale = [i + 1 for i in range(11)]
            >>> pc_segment.complement(input_scale)
            RatioClassSegment([Fraction(3, 2), Fraction(2, 1), Fraction(5, 4), Fraction(3, 2), Fraction(7, 4), Fraction(2, 1), Fraction(9, 8), Fraction(5, 4), Fraction(11, 8)])

        """
        complements = []
        for ratio in scale:
            if ratio not in self.ratio_classes:
                complements.append(ratio)
        return RatioClassSegment(complements)

    def invert(self, axis=1):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.RatioClassSegment([2, 4, 3]).invert()
            RatioClassSegment([Fraction(2, 1), Fraction(2, 1), Fraction(3, 2)])

            >>> microtones.RatioClassSegment([2, 4, 3]).invert(3)
            RatioClassSegment([Fraction(3, 2), Fraction(3, 2), Fraction(2, 1)])

        """
        assert 0 < axis
        inverse = [axis / i for i in self.ratio_classes]
        return RatioClassSegment(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.RatioClassSegment([1, 2, 3]).multiply(2)
            RatioClassSegment([Fraction(2, 1), Fraction(2, 1), Fraction(3, 2)])

        """
        multiplied_pitch_classes = [n * ratio for ratio in self.ratio_classes]
        return RatioClassSegment(multiplied_pitch_classes)

    def retrograde(self):
        """
        Gets retrograde.

        ..  container:: example

            >>> microtones.RatioClassSegment([1, 2, 3, 3]).retrograde()
            RatioClassSegment([Fraction(3, 2), Fraction(3, 2), Fraction(2, 1), Fraction(1, 1)])

        """
        return RatioClassSegment(reversed(self.ratio_classes))

    def rotate(self, n):
        """
        Gets rotation.

        ..  container:: example

            >>> microtones.RatioClassSegment([1, 2, 3]).rotate(1)
            RatioClassSegment([Fraction(2, 1), Fraction(3, 2), Fraction(1, 1)])

        """
        copied_list = [i for i in self.ratio_classes]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return RatioClassSegment(copied_list_)

    def sorted(self):
        """
        Gets Ratio Class Segment sorted in ascending order.

        ..  container:: example

            >>> microtones.RatioClassSegment([5, 2, 3, "1/2", 1, "1/5"]).sorted()
            RatioClassSegment([Fraction(1, 1), Fraction(5, 4), Fraction(5, 4), Fraction(3, 2), Fraction(2, 1), Fraction(2, 1)])

        """
        return RatioClassSegment(sorted(self.ratio_classes))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.RatioClassSegment([1, 2, 3]).transpose(2)
            RatioClassSegment([Fraction(3, 2), Fraction(2, 1), Fraction(7, 4)])

            >>> microtones.RatioClassSegment([1, 2, 4, 5, 6]).invert().transpose(1+3)
            RatioClassSegment([Fraction(5, 4), Fraction(3, 2), Fraction(3, 2), Fraction(21, 16), Fraction(11, 8)])

        """
        transposed = [ratio + n for ratio in self.ratio_classes]
        return RatioClassSegment(transposed)


class RatioSegment(object):
    """
    Ratio Segment.

    >>> from abjadext import microtones

    """

    def __init__(self, ratios):
        self.ratios = []
        for ratio in ratios:
            ratio = fractions.Fraction(ratio)
            assert 0 < ratio
            self.ratios.append(ratio)

    def __iter__(self):
        """
        Iterates contents.

        ..  container:: example

            >>> pc_segment = microtones.RatioSegment([1, 2, 3, 3])
            >>> for item in pc_segment:
            ...     item
            Fraction(1, 1)
            Fraction(2, 1)
            Fraction(3, 1)
            Fraction(3, 1)

            >>> for x in microtones.RatioSegment(["31/2", "10", "33/4", "36/10", "113/10"]):
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

            >>> len(microtones.RatioSegment([1, 2, 3]))
            3

        """
        return len(self.ratios)

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.RatioSegment([1, 2, 3])
            RatioSegment([Fraction(1, 1), Fraction(2, 1), Fraction(3, 1)])

        """
        return f"{self.__class__.__name__}({self.ratios})"

    def __str__(self):
        """
        Gets string representation.

        ..  container:: example

            >>> str(microtones.RatioSegment([1, 2, 3]))
            '(1, 2, 3)'

        """
        output = "("
        for i, ratio in enumerate(self.ratios):
            output += f"{ratio}"
            if i != len(self.ratios) - 1:
                output += ", "
        output += ")"
        return output

    def __add__(self, argument):
        argument = type(self)(argument)
        items = self.ratios + argument.ratios
        return type(self)(items)

    def __contains__(self, argument):
        return super().__contains__(argument)

    def __getitem__(self, argument):
        return super().__getitem__(argument)

    def constrain_to_octave(self):
        """
        Gets Ratio Segment constrained within an octave.

        ..  container:: example

            >>> str(microtones.RatioSegment([1, 3, "1/5"]).constrain_to_octave())
            '(1, 3/2, 4/5)'

        """
        constrained = []
        for ratio in self.ratios:
            while 2 < ratio:
                ratio /= 2
            while ratio < fractions.Fraction(1, 2):
                ratio *= 2
            constrained.append(ratio)
        return RatioSegment(constrained)

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_segment = microtones.RatioSegment([1, 2, 3])
            >>> input_scale = [i + 1 for i in range(11)]
            >>> pc_segment.complement(input_scale)
            RatioSegment([Fraction(4, 1), Fraction(5, 1), Fraction(6, 1), Fraction(7, 1), Fraction(8, 1), Fraction(9, 1), Fraction(10, 1), Fraction(11, 1)])

        """
        complements = []
        for ratio in scale:
            if ratio not in self.ratios:
                complements.append(ratio)
        return RatioSegment(complements)

    def invert(self, axis=1):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.RatioSegment([2, 4, 3]).invert()
            RatioSegment([Fraction(1, 2), Fraction(1, 4), Fraction(1, 3)])

            >>> microtones.RatioSegment([2, 4, 3]).invert(3)
            RatioSegment([Fraction(3, 2), Fraction(3, 4), Fraction(1, 1)])

        """
        assert 0 < axis
        inverse = [axis / i for i in self.ratios]
        return RatioSegment(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.RatioSegment([1, 2, 3]).multiply(2)
            RatioSegment([Fraction(2, 1), Fraction(4, 1), Fraction(6, 1)])

        """
        multiplied_pitch_classes = [n * ratio for ratio in self.ratios]
        return RatioSegment(multiplied_pitch_classes)

    def retrograde(self):
        """
        Gets retrograde.

        ..  container:: example

            >>> microtones.RatioSegment([1, 2, 3, 3]).retrograde()
            RatioSegment([Fraction(3, 1), Fraction(3, 1), Fraction(2, 1), Fraction(1, 1)])

        """
        return RatioSegment(reversed(self.ratios))

    def rotate(self, n):
        """
        Gets rotation.

        ..  container:: example

            >>> microtones.RatioSegment([1, 2, 3]).rotate(1)
            RatioSegment([Fraction(2, 1), Fraction(3, 1), Fraction(1, 1)])

        """
        copied_list = [i for i in self.ratios]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return RatioSegment(copied_list_)

    def sorted(self):
        """
        Gets Ratio Segment sorted in ascending order.

        ..  container:: example

            >>> microtones.RatioSegment([5, 2, 3, "1/2", 1, "1/5"]).sorted()
            RatioSegment([Fraction(1, 5), Fraction(1, 2), Fraction(1, 1), Fraction(2, 1), Fraction(3, 1), Fraction(5, 1)])

        """
        return RatioSegment(sorted(self.ratios))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.RatioSegment([1, 2, 3]).transpose(2)
            RatioSegment([Fraction(3, 1), Fraction(4, 1), Fraction(5, 1)])

            >>> microtones.RatioSegment([1, 2, 4, 5, 6]).invert().transpose(1+3)
            RatioSegment([Fraction(5, 1), Fraction(9, 2), Fraction(17, 4), Fraction(21, 5), Fraction(25, 6)])

        """
        transposed = [ratio + n for ratio in self.ratios]
        return RatioSegment(transposed)
