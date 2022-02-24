import black
import quicktions


def _flatten(lst):
    out = []
    for i in lst:
        if isinstance(i, (list, tuple)):
            out.extend(_flatten(i))
        else:
            out.append(i)
    return out


class PitchClassSet:
    """
    Pitch Class Set.

    >>> from abjadext import microtones
    >>> import quicktions

    """

    def __init__(self, pitch_classes):
        """
        Can be initialized with list, tuple, or mixed contents.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 1, 6])
            {0, 1, 6}
            <BLANKLINE>

            >>> microtones.PitchClassSet((0, 1, 6))
            {0, 1, 6}
            <BLANKLINE>

            >>> microtones.PitchClassSet([0, (1, 6)])
            {0, 1, 6}
            <BLANKLINE>

        """
        pitch_classes = _flatten(pitch_classes)
        temp = [quicktions.Fraction(pitch) % 12 for pitch in pitch_classes]
        self.pitch_classes = []
        for pitch in temp:
            if pitch not in self.pitch_classes:
                self.pitch_classes.append(pitch)

    def __getitem__(self, index):
        """
        Gets value at index

        ..  container:: example

            >>> microtones.PitchClassSet([0, 1, 6])[0]
            Fraction(0, 1)

        """
        return self.pitch_classes[index]

    def __iter__(self):
        """
        Iterates contents.

        ..  container:: example

            >>> pc_set = microtones.PitchClassSet([0, 1, 2])
            >>> for item in pc_set:
            ...     item
            Fraction(0, 1)
            Fraction(1, 1)
            Fraction(2, 1)

            >>> for x in microtones.PitchClassSet(["31/2", "10", "33/4", "-5", "36/10", "113/10"]).prime_form():
            ...     print(x)
            0
            1/10
            7/2
            19/4
            13/2
            39/5

        """
        for pitch in self.pitch_classes:
            yield pitch

    def __len__(self):
        """
        Gets length of contents.

        ..  container:: example

            >>> len(microtones.PitchClassSet([0, 1, 2]))
            3

        """
        return len(self.pitch_classes)

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 1, 6])
            {0, 1, 6}
            <BLANKLINE>

        """
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string

    def __str__(self):
        """
        Gets string representation.

        ..  container:: example

            >>> str(microtones.PitchClassSet([0, 1, 6]))
            '{0, 1, 6}'

        """
        output = "{"
        for i, pitch in enumerate(self.pitch_classes):
            output += f"{pitch}"
            if i != len(self.pitch_classes) - 1:
                output += ", "
        output += "}"
        return output

    def __add__(self, argument):
        """
        Concatenates Pitch Class Set with iterable.

        ..  container:: example

            >>> pc_set = microtones.PitchClassSet(["0", "1/2", "5/4"])
            >>> pc_set += [0, quicktions.Fraction(11, 6), quicktions.Fraction(27, 2)]
            >>> pc_set
            {0, 1 / 2, 5 / 4, 11 / 6, 3 / 2}
            <BLANKLINE>

        """
        argument = type(self)(argument)
        items = self.pitch_classes + argument.pitch_classes
        return type(self)(items)

    def __contains__(self, argument):
        """
        Returns boolean

        ..  container::

            >>> pc_set = microtones.PitchClassSet([0, 1, 6])
            >>> 6 in pc_set
            True

            >>> 18 in pc_set
            False

            >>> pc_set = microtones.PitchClassSet([0, 1, 18])
            >>> 6 in pc_set
            True

            >>> 18 in pc_set
            False

        """
        return argument in self.pitch_classes

    def _rotate(self, n):
        copied_list = [i for i in self.pitch_classes]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return type(self)(copied_list_)

    def _transpose_to_zero(self):
        return self.transpose(-self.pitch_classes[0])

    @staticmethod
    def _binary_value(i):
        value = 0
        for bit in i:
            value += 2**bit
        return value

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_set = microtones.PitchClassSet([0, 1, 2])
            >>> input_scale = [i for i in range(12)]
            >>> pc_set.complement(input_scale)
            {3, 4, 5, 6, 7, 8, 9, 10, 11}
            <BLANKLINE>

        """
        complements = []
        for pitch in scale:
            if pitch not in self.pitch_classes:
                complements.append(pitch)
        return type(self)(complements)

    def invert(self, axis=0):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 1, 3]).invert()
            {0, 11, 9}
            <BLANKLINE>

            >>> microtones.PitchClassSet([0, 1, 3]).invert(3)
            {6, 5, 3}
            <BLANKLINE>

        """
        axis = quicktions.Fraction(axis)
        intervals = [axis - i for i in self.pitch_classes]
        inverse = [axis + interval for interval in intervals]
        return type(self)(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 1, 3]).multiply(2)
            {0, 2, 6}
            <BLANKLINE>

        """
        multiplied_pitch_classes = [
            quicktions.Fraction(n) * pitch for pitch in self.pitch_classes
        ]
        return type(self)(multiplied_pitch_classes)

    def normal_order(self):
        """
        Gets normal order.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 2, 1]).normal_order()
            {0, 1, 2}
            <BLANKLINE>

        """
        size = len(self.pitch_classes)
        if size < 2:
            return type(self)(self.pitch_classes)
        original = self.sorted()
        rotations = [original._rotate(n) for n in range(size)]
        candidate = rotations.pop()
        candidate_binary_value = self._binary_value(candidate._transpose_to_zero())
        for rotation in rotations:
            alternative_candidate_binary_value = self._binary_value(
                rotation._transpose_to_zero()
            )
            if alternative_candidate_binary_value < candidate_binary_value:
                candidate = rotation
                candidate_binary_value = alternative_candidate_binary_value
        return candidate

    def prime_form(self):
        """
        Gets prime form.

        ..  container:: example

            >>> microtones.PitchClassSet([1, 3, 2]).prime_form()
            {0, 1, 2}
            <BLANKLINE>

        """
        original = self.normal_order()._transpose_to_zero()
        inverted = self.invert().normal_order()._transpose_to_zero()
        if self._binary_value(original) < self._binary_value(inverted):
            return original
        else:
            return inverted

    def sorted(self):
        """
        Gets Pitch Class Set sorted in ascending order.

        ..  container:: example

            >>> microtones.PitchClassSet([2, 1, 0]).sorted()
            {0, 1, 2}
            <BLANKLINE>

        """
        return type(self)(sorted(self.pitch_classes))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 1, 2]).transpose(2)
            {2, 3, 4}
            <BLANKLINE>

            >>> microtones.PitchClassSet([0, 1, 3, 4, 5]).invert().transpose(1+3)
            {4, 3, 1, 0, 11}
            <BLANKLINE>

        """
        transposed = [pitch + n for pitch in self.pitch_classes]
        return type(self)(transposed)


class PitchSet:
    """
    Pitch Set.

    >>> from abjadext import microtones

    """

    def __init__(self, pitches):
        """
        Can be initialized with list, tuple, or mixed contents.

        ..  container:: example

            >>> microtones.PitchSet([0, 1, 6])
            {0, 1, 6}
            <BLANKLINE>

            >>> microtones.PitchSet((0, 1, 6))
            {0, 1, 6}
            <BLANKLINE>

            >>> microtones.PitchSet([0, (1, 6)])
            {0, 1, 6}
            <BLANKLINE>

        """
        pitches = _flatten(pitches)
        temp = [quicktions.Fraction(pitch) for pitch in pitches]
        self.pitches = []
        for pitch in temp:
            if pitch not in self.pitches:
                self.pitches.append(pitch)

    def __getitem__(self, index):
        """
        Gets value at index

        ..  container:: example

            >>> microtones.PitchSet([0, 1, 6])[0]
            Fraction(0, 1)

        """
        return self.pitches[index]

    def __iter__(self):
        """
        Iterates contents.

        ..  container:: example

            >>> pc_set = microtones.PitchSet([0, 1, 2])
            >>> for item in pc_set:
            ...     item
            Fraction(0, 1)
            Fraction(1, 1)
            Fraction(2, 1)

        """
        for pitch in self.pitches:
            yield pitch

    def __len__(self):
        """
        Gets length of contents.

        ..  container:: example

            >>> len(microtones.PitchSet([0, 1, 2]))
            3

        """
        return len(self.pitches)

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.PitchSet([0, 1, 2])
            {0, 1, 2}
            <BLANKLINE>

        """
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string

    def __str__(self):
        """
        Gets string representation.

        ..  container:: example

            >>> str(microtones.PitchSet([0, 1, 2]))
            '{0, 1, 2}'

        """
        output = "{"
        for i, pitch in enumerate(self.pitches):
            output += f"{pitch}"
            if i != len(self.pitches) - 1:
                output += ", "
        output += "}"
        return output

    def __add__(self, argument):
        """
        Concatenates Pitch Set with iterable.

        ..  container:: example

            >>> p_set = microtones.PitchSet(["0", "1/2", "5/4"])
            >>> p_set += [0, quicktions.Fraction(11, 6), quicktions.Fraction(27, 2)]
            >>> p_set
            {0, 1 / 2, 5 / 4, 11 / 6, 27 / 2}
            <BLANKLINE>

        """
        argument = type(self)(argument)
        items = self.pitches + argument.pitches
        return type(self)(items)

    def __contains__(self, argument):
        """
        Returns boolean

        ..  container::

            >>> p_set = microtones.PitchSet([0, 1, 6])
            >>> 6 in p_set
            True

            >>> 18 in p_set
            False

            >>> p_set = microtones.PitchSet([0, 1, 18])
            >>> 6 in p_set
            False

            >>> 18 in p_set
            True

        """
        return argument in self.pitches

    def _rotate(self, n):
        copied_list = [i for i in self.pitches]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return type(self)(copied_list_)

    def _transpose_to_zero(self):
        return self.transpose(-self.pitches[0])

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_set = microtones.PitchSet([0, 1, 2])
            >>> input_scale = [i for i in range(12)]
            >>> pc_set.complement(input_scale)
            {3, 4, 5, 6, 7, 8, 9, 10, 11}
            <BLANKLINE>

        """
        complements = []
        for pitch in scale:
            if pitch not in self.pitches:
                complements.append(pitch)
        return type(self)(complements)

    def invert(self, axis=0):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.PitchSet([0, 1, 3]).invert()
            {0, -1, -3}
            <BLANKLINE>

            >>> microtones.PitchSet([0, 1, 3]).invert(2)
            {4, 3, 1}
            <BLANKLINE>

        """
        axis = quicktions.Fraction(axis)
        intervals = [axis - i for i in self.pitches]
        inverse = [axis + interval for interval in intervals]
        return type(self)(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.PitchSet([0, 1, 3]).multiply(2)
            {0, 2, 6}
            <BLANKLINE>

        """
        multiplied_pitches = [quicktions.Fraction(n) * pitch for pitch in self.pitches]
        return type(self)(multiplied_pitches)

    def sorted(self):
        """
        Gets Pitch Set sorted in ascending order.

        ..  container:: example

            >>> microtones.PitchSet([2, 1, 0]).sorted()
            {0, 1, 2}
            <BLANKLINE>

        """
        return type(self)(sorted(self.pitches))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.PitchSet([0, 1, 2]).transpose(2)
            {2, 3, 4}
            <BLANKLINE>

            >>> microtones.PitchSet([0, 1, 3, 4, 5]).invert().transpose(1+3)
            {4, 3, 1, 0, -1}
            <BLANKLINE>

        """
        transposed = [pitch + n for pitch in self.pitches]
        return type(self)(transposed)


class PitchClassSegment:
    """
    Pitch Class Segment.

    >>> from abjadext import microtones

    """

    def __init__(self, pitch_classes):
        """
        Can be initialized with list, tuple, or mixed contents.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 6])
            (0, 1, 6)
            <BLANKLINE>

            >>> microtones.PitchClassSegment((0, 1, 6))
            (0, 1, 6)
            <BLANKLINE>

            >>> microtones.PitchClassSegment([0, (1, 6)])
            (0, 1, 6)
            <BLANKLINE>

        """
        pitch_classes = _flatten(pitch_classes)
        self.pitch_classes = [
            quicktions.Fraction(pitch) % 12 for pitch in pitch_classes
        ]

    def __getitem__(self, index):
        """
        Gets value at index

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 6])[0]
            Fraction(0, 1)

        """
        return self.pitch_classes[index]

    def __iter__(self):
        """
        Iterates contents.

        ..  container:: example

            >>> pc_set = microtones.PitchClassSegment([0, 1, 2])
            >>> for item in pc_set:
            ...     item
            Fraction(0, 1)
            Fraction(1, 1)
            Fraction(2, 1)

        """
        for pitch in self.pitch_classes:
            yield pitch

    def __len__(self):
        """
        Gets length of contents.

        ..  container:: example

            >>> len(microtones.PitchClassSegment([0, 1, 2]))
            3

        """
        return len(self.pitch_classes)

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 2])
            (0, 1, 2)
            <BLANKLINE>

        """
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string

    def __str__(self):
        """
        Gets string representation.

        ..  container:: example

            >>> str(microtones.PitchClassSegment([0, 1, 2]))
            '(0, 1, 2)'

        """
        output = "("
        for i, pitch in enumerate(self.pitch_classes):
            output += f"{pitch}"
            if i != len(self.pitch_classes) - 1:
                output += ", "
        output += ")"
        return output

    def __add__(self, argument):
        """
        Concatenates Pitch Class Segment with iterable.

        ..  container:: example

            >>> pc_segment = microtones.PitchClassSegment(["0", "1/2", "5/4"])
            >>> pc_segment += [0, quicktions.Fraction(11, 6), quicktions.Fraction(27, 2)]
            >>> pc_segment
            (0, 1 / 2, 5 / 4, 0, 11 / 6, 3 / 2)
            <BLANKLINE>

        """
        argument = type(self)(argument)
        items = self.pitch_classes + argument.pitch_classes
        return type(self)(items)

    def __contains__(self, argument):
        """
        Returns boolean

        ..  container::

            >>> pc_segment = microtones.PitchClassSegment([0, 1, 6])
            >>> 6 in pc_segment
            True

            >>> 18 in pc_segment
            False

            >>> pc_segment = microtones.PitchClassSegment([0, 1, 18])
            >>> 6 in pc_segment
            True

            >>> 18 in pc_segment
            False

        """
        return argument in self.pitch_classes

    def _transpose_to_zero(self):
        return self.transpose(-self.pitch_classes[0])

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_set = microtones.PitchClassSegment([0, 1, 2])
            >>> input_scale = [i for i in range(12)]
            >>> pc_set.complement(input_scale)
            (3, 4, 5, 6, 7, 8, 9, 10, 11)
            <BLANKLINE>

        """
        complements = []
        for pitch in scale:
            if pitch not in self.pitch_classes:
                complements.append(pitch)
        return type(self)(complements)

    def invert(self, axis=0):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 3]).invert()
            (0, 11, 9)
            <BLANKLINE>

            >>> microtones.PitchClassSegment([0, 1, 3]).invert(2)
            (4, 3, 1)
            <BLANKLINE>

        """
        axis = quicktions.Fraction(axis)
        intervals = [axis - i for i in self.pitch_classes]
        inverse = [axis + interval for interval in intervals]
        return type(self)(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 3]).multiply(2)
            (0, 2, 6)
            <BLANKLINE>

        """
        multiplied_pitch_classes = [
            quicktions.Fraction(n) * pitch for pitch in self.pitch_classes
        ]
        return type(self)(multiplied_pitch_classes)

    def retrograde(self):
        """
        Gets retrograde.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 2]).retrograde()
            (2, 1, 0)
            <BLANKLINE>

        """
        return type(self)(reversed(self.pitch_classes))

    def rotate(self, n):
        """
        Gets rotation.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 2]).rotate(1)
            (1, 2, 0)
            <BLANKLINE>

        """
        copied_list = [i for i in self.pitch_classes]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return type(self)(copied_list_)

    def sorted(self):
        """
        Gets Pitch Class Segment sorted in ascending order.

        ..  container:: example

            >>> microtones.PitchClassSegment([2, 1, 0]).sorted()
            (0, 1, 2)
            <BLANKLINE>

        """
        return type(self)(sorted(self.pitch_classes))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 2]).transpose(2)
            (2, 3, 4)
            <BLANKLINE>

            >>> microtones.PitchClassSegment([0, 1, 3, 4, 5]).invert().transpose(1+3)
            (4, 3, 1, 0, 11)
            <BLANKLINE>

        """
        transposed = [pitch + n for pitch in self.pitch_classes]
        return type(self)(transposed)


class PitchSegment:
    """
    Pitch Segment.

    >>> from abjadext import microtones

    """

    def __init__(self, pitches):
        """
        Can be initialized with list, tuple, or mixed contents.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 6])
            (0, 1, 6)
            <BLANKLINE>

            >>> microtones.PitchSegment((0, 1, 6))
            (0, 1, 6)
            <BLANKLINE>

            >>> microtones.PitchSegment([0, (1, 6)])
            (0, 1, 6)
            <BLANKLINE>

        """
        pitches = _flatten(pitches)
        self.pitches = [quicktions.Fraction(pitch) for pitch in pitches]

    def __getitem__(self, index):
        """
        Gets value at index

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 6])[0]
            Fraction(0, 1)

        """
        return self.pitches[index]

    def __setitem__(self, index, data):
        """
        Sets value at index

        ..  container:: example

            >>> s = microtones.PitchSegment([0, 1, 6])
            >>> s[0] = 5
            >>> s
            (5, 1, 6)
            <BLANKLINE>

        """
        self.pitches[index] = quicktions.Fraction(data)

    def __iter__(self):
        """
        Iterates contents.

        ..  container:: example

            >>> pc_set = microtones.PitchSegment([0, 1, 2])
            >>> for item in pc_set:
            ...     item
            Fraction(0, 1)
            Fraction(1, 1)
            Fraction(2, 1)

        """
        for pitch in self.pitches:
            yield pitch

    def __len__(self):
        """
        Gets length of contents.

        ..  container:: example

            >>> len(microtones.PitchSegment([0, 1, 2]))
            3

        """
        return len(self.pitches)

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 2])
            (0, 1, 2)
            <BLANKLINE>

        """
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string

    def __str__(self):
        """
        Gets string representation.

        ..  container:: example

            >>> str(microtones.PitchSegment([0, 1, 2]))
            '(0, 1, 2)'

        """
        output = "("
        for i, pitch in enumerate(self.pitches):
            output += f"{pitch}"
            if i != len(self.pitches) - 1:
                output += ", "
        output += ")"
        return output

    def __add__(self, argument):
        """
        Concatenates Pitch Segment with iterable.

        ..  container:: example

            >>> p_segment = microtones.PitchSegment(["0", "1/2", "5/4"])
            >>> p_segment += [0, quicktions.Fraction(11, 6), quicktions.Fraction(27, 2)]
            >>> p_segment
            (0, 1 / 2, 5 / 4, 0, 11 / 6, 27 / 2)
            <BLANKLINE>

        """
        argument = type(self)(argument)
        items = self.pitches + argument.pitches
        return type(self)(items)

    def __contains__(self, argument):
        """
        Returns boolean

        ..  container::

            >>> p_segment = microtones.PitchSegment([0, 1, 6])
            >>> 6 in p_segment
            True

            >>> 18 in p_segment
            False

            >>> p_segment = microtones.PitchSegment([0, 1, 18])
            >>> 6 in p_segment
            False

            >>> 18 in p_segment
            True

        """
        return argument in self.pitches

    def _transpose_to_zero(self):
        return self.transpose(-self.pitches[0])

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_set = microtones.PitchSegment([0, 1, 2])
            >>> input_scale = [i for i in range(12)]
            >>> pc_set.complement(input_scale)
            (3, 4, 5, 6, 7, 8, 9, 10, 11)
            <BLANKLINE>

        """
        complements = []
        for pitch in scale:
            if pitch not in self.pitches:
                complements.append(pitch)
        return type(self)(complements)

    def invert(self, axis=0):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 3]).invert()
            (0, -1, -3)
            <BLANKLINE>

            >>> microtones.PitchSegment([0, 1, 3]).invert(2)
            (4, 3, 1)
            <BLANKLINE>

        """
        axis = quicktions.Fraction(axis)
        intervals = [axis - i for i in self.pitches]
        inverse = [axis + interval for interval in intervals]
        return type(self)(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 3]).multiply(2)
            (0, 2, 6)
            <BLANKLINE>

        """
        multiplied_pitches = [quicktions.Fraction(n) * pitch for pitch in self.pitches]
        return type(self)(multiplied_pitches)

    def retrograde(self):
        """
        Gets retrograde.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 2]).retrograde()
            (2, 1, 0)
            <BLANKLINE>

        """
        return type(self)(reversed(self.pitches))

    def rotate(self, n):
        """
        Gets rotation.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 2]).rotate(1)
            (1, 2, 0)
            <BLANKLINE>

        """
        copied_list = [i for i in self.pitches]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return type(self)(copied_list_)

    def sorted(self):
        """
        Gets Pitch Segment sorted in ascending order.

        ..  container:: example

            >>> microtones.PitchSegment([2, 1, 0]).sorted()
            (0, 1, 2)
            <BLANKLINE>

        """
        return type(self)(sorted(self.pitches))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 2]).transpose(2)
            (2, 3, 4)
            <BLANKLINE>

            >>> microtones.PitchSegment([0, 1, 3, 4, 5]).invert().transpose(1+3)
            (4, 3, 1, 0, -1)
            <BLANKLINE>

        """
        transposed = [pitch + n for pitch in self.pitches]
        return type(self)(transposed)


class RatioClassSet:
    """
    Ratio Class Set.

    >>> from abjadext import microtones
    >>> import quicktions

    """

    def __init__(self, ratio_classes):
        """
        Can be initialized with list, tuple, or mixed contents

        ..  container:: example

            >>> microtones.RatioClassSet([1, 2, 3])
            {1, 2, 3 / 2}
            <BLANKLINE>

            >>> microtones.RatioClassSet((1, 2, 3))
            {1, 2, 3 / 2}
            <BLANKLINE>

            >>> microtones.RatioClassSet([1, (2, 3)])
            {1, 2, 3 / 2}
            <BLANKLINE>

        """
        ratio_classes = _flatten(ratio_classes)
        self.ratio_classes = []
        for ratio in ratio_classes:
            ratio = quicktions.Fraction(ratio)
            assert 0 < ratio
            while 2 < ratio:
                ratio /= 2
            while ratio < 1:
                ratio *= 2
            if ratio not in self.ratio_classes:
                self.ratio_classes.append(ratio)

    def __getitem__(self, index):
        """
        Gets item at index

        ..  container:: example

            >>> microtones.RatioClassSet([1, 2, 3])[0]
            Fraction(1, 1)

        """
        return self.ratio_classes[index]

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
            {1, 2, 3 / 2}
            <BLANKLINE>

        """
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string

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
        """
        Concatenates Ratio Class Set with iterable.

        ..  container:: example

            >>> rc_set = microtones.RatioClassSet(["1", "1/2", "5/4"])
            >>> rc_set += [1, quicktions.Fraction(11, 6), quicktions.Fraction(27, 2)]
            >>> rc_set
            {1, 5 / 4, 11 / 6, 27 / 16}
            <BLANKLINE>

        """
        argument = type(self)(argument)
        items = self.ratio_classes + argument.ratio_classes
        return type(self)(items)

    def __contains__(self, argument):
        """
        Returns boolean

        ..  container::

            >>> rc_set = microtones.RatioClassSet([1, 2, 6])
            >>> 1 in rc_set
            True

        """
        return argument in self.ratio_classes

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> rc_set = microtones.RatioClassSet([1, 2, 3])
            >>> input_scale = [i + 1 for i in range(11)]
            >>> s = rc_set.complement(input_scale)
            >>> s
            {3 / 2, 2, 5 / 4, 7 / 4, 9 / 8, 11 / 8}
            <BLANKLINE>

        """
        complements = []
        for ratio in scale:
            if ratio not in self.ratio_classes:
                complements.append(ratio)
        return type(self)(complements)

    def invert(self, axis=1):
        """
        Gets inversion.

        ..  container:: example

            >>> s = microtones.RatioClassSet([2, 4, 3]).invert()
            >>> s
            {1, 4 / 3}
            <BLANKLINE>

            >>> s = microtones.RatioClassSet([2, 4, 3]).invert(3)
            >>> s
            {9 / 8, 3 / 2}
            <BLANKLINE>

        """
        axis = quicktions.Fraction(axis)
        assert 0 < axis
        inverse = [axis / i for i in self.ratio_classes]
        inverse = [axis * ratio for ratio in inverse]
        return type(self)(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> s = microtones.RatioClassSet([1, 2, 3]).multiply(2)
            >>> s
            {2, 3 / 2}
            <BLANKLINE>

        """
        multiplied_pitch_classes = [
            quicktions.Fraction(n) * ratio for ratio in self.ratio_classes
        ]
        return type(self)(multiplied_pitch_classes)

    def sorted(self):
        """
        Gets Ratio Class Set sorted in ascending order.

        ..  container:: example

            >>> s = microtones.RatioClassSet([5, 2, 3, "1/2", 1, "1/5"]).sorted()
            >>> s
            {1, 5 / 4, 3 / 2, 8 / 5, 2}
            <BLANKLINE>

        """
        return type(self)(sorted(self.ratio_classes))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> s = microtones.RatioClassSet([1, 2, 3]).transpose(2)
            >>> s
            {3 / 2, 2, 7 / 4}
            <BLANKLINE>

            >>> s = microtones.RatioClassSet([1, 2, 4, 5, 6]).invert().transpose(1+3)
            >>> s
            {5 / 4, 7 / 5, 4 / 3}
            <BLANKLINE>

        """
        transposed = [ratio + quicktions.Fraction(n) for ratio in self.ratio_classes]
        return type(self)(transposed)


class RatioSet:
    """
    Ratio Set.

    >>> from abjadext import microtones

    """

    def __init__(self, ratios):
        """
        Can be initialized with list, tuple, or mixed contents

        ..  container:: example

            >>> microtones.RatioSet([1, 2, 3])
            {1, 2, 3}
            <BLANKLINE>

            >>> microtones.RatioSet((1, 2, 3))
            {1, 2, 3}
            <BLANKLINE>

            >>> microtones.RatioSet([1, (2, 3)])
            {1, 2, 3}
            <BLANKLINE>

        """
        ratios = _flatten(ratios)
        self.ratios = []
        for ratio in ratios:
            ratio = quicktions.Fraction(ratio)
            assert 0 < ratio
            if ratio not in self.ratios:
                self.ratios.append(ratio)

    def __getitem__(self, index):
        """
        Gets item at index

        ..  container:: example

            >>> microtones.RatioSet([1, 2, 3])[0]
            Fraction(1, 1)

        """
        return self.ratios[index]

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
            {1, 2, 3}
            <BLANKLINE>

        """
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string

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
        """
        Concatenates Ratio Set with iterable.

        ..  container:: example

            >>> r_set = microtones.RatioSet(["1", "1/2", "5/4"])
            >>> r_set += [1, quicktions.Fraction(11, 6), quicktions.Fraction(27, 2)]
            >>> s = r_set
            >>> s
            {1, 1 / 2, 5 / 4, 11 / 6, 27 / 2}
            <BLANKLINE>

        """
        argument = type(self)(argument)
        items = self.ratios + argument.ratios
        return type(self)(items)

    def __contains__(self, argument):
        """
        Returns boolean

        ..  container::

            >>> r_set = microtones.RatioSet([1, 2, 6])
            >>> 1 in r_set
            True

        """
        return argument in self.ratios

    def constrain_to_octave(self):
        """
        Gets Ratio Set constrained within an octave.

        ..  container:: example

            >>> str(microtones.RatioSet([1, 3, "1/5"]).constrain_to_octave())
            '{1, 3/2, 4/5}'

        """
        constrained = []
        for ratio in self.ratios:
            while 2 <= ratio:
                ratio /= 2
            while ratio < quicktions.Fraction(1, 2):
                ratio *= 2
            constrained.append(ratio)
        return type(self)(constrained)

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> r_set = microtones.RatioSet([1, 2, 3])
            >>> input_scale = [i + 1 for i in range(11)]
            >>> s = r_set.complement(input_scale)
            >>> s
            {4, 5, 6, 7, 8, 9, 10, 11}
            <BLANKLINE>

        """
        complements = []
        for ratio in scale:
            if ratio not in self.ratios:
                complements.append(ratio)
        return type(self)(complements)

    def invert(self, axis=1):
        """
        Gets inversion.

        ..  container:: example

            >>> s = microtones.RatioSet([2, 4, 3]).invert()
            >>> s
            {1 / 2, 1 / 4, 1 / 3}
            <BLANKLINE>

            >>> s = microtones.RatioSet([2, 4, 3]).invert(3)
            >>> s
            {9 / 2, 9 / 4, 3}
            <BLANKLINE>

        """
        axis = quicktions.Fraction(axis)
        assert 0 < axis
        inverse = [axis / i for i in self.ratios]
        inverse = [axis * ratio for ratio in inverse]
        return type(self)(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> s = microtones.RatioSet([1, 2, 3]).multiply(2)
            >>> s
            {2, 4, 6}
            <BLANKLINE>

        """
        multiplied_pitch_classes = [
            quicktions.Fraction(n) * ratio for ratio in self.ratios
        ]
        return type(self)(multiplied_pitch_classes)

    def sorted(self):
        """
        Gets Ratio Class Set sorted in ascending order.

        ..  container:: example

            >>> s = microtones.RatioSet([5, 2, 3]).sorted()
            >>> s
            {2, 3, 5}
            <BLANKLINE>

        """
        return type(self)(sorted(self.ratios))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> s = microtones.RatioSet([1, 2, 3]).transpose(2)
            >>> s
            {3, 4, 5}
            <BLANKLINE>

            >>> s = microtones.RatioSet([1, 2, 4, 5, 6]).invert().transpose(1+3)
            >>> s
            {5, 9 / 2, 17 / 4, 21 / 5, 25 / 6}
            <BLANKLINE>

        """
        transposed = [ratio + quicktions.Fraction(n) for ratio in self.ratios]
        return type(self)(transposed)


class RatioClassSegment:
    """
    Ratio Class Segment.

    >>> from abjadext import microtones

    """

    def __init__(self, ratio_classes):
        """
        Can be initialized with list, tuple, or mixed contents

        ..  container:: example

            >>> microtones.RatioClassSegment([1, 2, 3])
            (1, 2, 3 / 2)
            <BLANKLINE>

            >>> microtones.RatioClassSegment((1, 2, 3))
            (1, 2, 3 / 2)
            <BLANKLINE>

            >>> microtones.RatioClassSegment([1, (2, 3)])
            (1, 2, 3 / 2)
            <BLANKLINE>

        """
        ratio_classes = _flatten(ratio_classes)
        self.ratio_classes = []
        for ratio in ratio_classes:
            ratio = quicktions.Fraction(ratio)
            assert 0 < ratio
            while 2 < ratio:
                ratio /= 2
            while ratio < 1:
                ratio *= 2
            self.ratio_classes.append(ratio)

    def __getitem__(self, index):
        """
        Gets item at index

        ..  container:: example

            >>> microtones.RatioClassSegment([1, 2, 3])[0]
            Fraction(1, 1)

        """
        return self.ratio_classes[index]

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
            (1, 2, 3 / 2)
            <BLANKLINE>

        """
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string

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
        """
        Concatenates Ratio Class Segment with iterable.

        ..  container:: example

            >>> rc_segment = microtones.RatioClassSegment(["1", "1/2", "5/4"])
            >>> rc_segment += [1, quicktions.Fraction(11, 6), quicktions.Fraction(27, 2)]
            >>> s = rc_segment
            >>> s
            (1, 1, 5 / 4, 1, 11 / 6, 27 / 16)
            <BLANKLINE>

        """
        argument = type(self)(argument)
        items = self.ratio_classes + argument.ratio_classes
        return type(self)(items)

    def __contains__(self, argument):
        """
        Returns boolean

        ..  container::

            >>> rc_segment = microtones.RatioClassSegment([1, 2, 6])
            >>> 1 in rc_segment
            True

        """
        return argument in self.ratio_classes

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_segment = microtones.RatioClassSegment([1, 2, 3])
            >>> input_scale = [i + 1 for i in range(11)]
            >>> s = pc_segment.complement(input_scale)
            >>> s
            (3 / 2, 2, 5 / 4, 3 / 2, 7 / 4, 2, 9 / 8, 5 / 4, 11 / 8)
            <BLANKLINE>

        """
        complements = []
        for ratio in scale:
            if ratio not in self.ratio_classes:
                complements.append(ratio)
        return type(self)(complements)

    def invert(self, axis=1):
        """
        Gets inversion.

        ..  container:: example

            >>> s = microtones.RatioClassSegment([2, 4, 3]).invert()
            >>> s
            (1, 1, 4 / 3)
            <BLANKLINE>

            >>> s = microtones.RatioClassSegment([2, 4, 3]).invert(3)
            >>> s
            (9 / 8, 9 / 8, 3 / 2)
            <BLANKLINE>

        """
        axis = quicktions.Fraction(axis)
        assert 0 < axis
        inverse = [axis / i for i in self.ratio_classes]
        inverse = [axis * ratio for ratio in inverse]
        return type(self)(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> s = microtones.RatioClassSegment([1, 2, 3]).multiply(2)
            >>> s
            (2, 2, 3 / 2)
            <BLANKLINE>

        """
        multiplied_pitch_classes = [
            quicktions.Fraction(n) * ratio for ratio in self.ratio_classes
        ]
        return type(self)(multiplied_pitch_classes)

    def retrograde(self):
        """
        Gets retrograde.

        ..  container:: example

            >>> s = microtones.RatioClassSegment([1, 2, 3, 3]).retrograde()
            >>> s
            (3 / 2, 3 / 2, 2, 1)
            <BLANKLINE>

        """
        return type(self)(reversed(self.ratio_classes))

    def rotate(self, n):
        """
        Gets rotation.

        ..  container:: example

            >>> s = microtones.RatioClassSegment([1, 2, 3]).rotate(1)
            >>> s
            (2, 3 / 2, 1)
            <BLANKLINE>

        """
        copied_list = [i for i in self.ratio_classes]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return type(self)(copied_list_)

    def sorted(self):
        """
        Gets Ratio Class Segment sorted in ascending order.

        ..  container:: example

            >>> s = microtones.RatioClassSegment([5, 2, 3, "1/2", 1, "1/5"]).sorted()
            >>> s
            (1, 1, 5 / 4, 3 / 2, 8 / 5, 2)
            <BLANKLINE>

        """
        return type(self)(sorted(self.ratio_classes))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> s = microtones.RatioClassSegment([1, 2, 3]).transpose(2)
            >>> s
            (3 / 2, 2, 7 / 4)
            <BLANKLINE>

            >>> s = microtones.RatioClassSegment([1, 2, 4, 5, 6]).invert().transpose(1+3)
            >>> s
            (5 / 4, 5 / 4, 5 / 4, 7 / 5, 4 / 3)
            <BLANKLINE>

        """
        transposed = [ratio + quicktions.Fraction(n) for ratio in self.ratio_classes]
        return type(self)(transposed)


class RatioSegment:
    """
    Ratio Segment.

    >>> from abjadext import microtones

    """

    def __init__(self, ratios):
        """
        Can be initialized with list, tuple, or mixed contents

        ..  container:: example

            >>> microtones.RatioSegment([1, 2, "3/2"])
            (1, 2, 3 / 2)
            <BLANKLINE>

            >>> microtones.RatioSegment((1, 2, "3/2"))
            (1, 2, 3 / 2)
            <BLANKLINE>

            >>> microtones.RatioSegment([1, [2, "3/2"], (4, 5)])
            (1, 2, 3 / 2, 4, 5)
            <BLANKLINE>

        """
        ratios = _flatten(ratios)
        self.ratios = []
        for ratio in ratios:
            ratio = quicktions.Fraction(ratio)
            assert 0 < ratio
            self.ratios.append(ratio)

    def __getitem__(self, index):
        """
        Gets item at index

        ..  container:: example

            >>> microtones.RatioSegment([1, 2, 3])[0]
            Fraction(1, 1)

        """
        return self.ratios[index]

    def __setitem__(self, index, data):
        """
        Sets item at index

        ..  container:: example

            >>> s = microtones.RatioSegment([1, 2, 3])
            >>> s[1] = 5
            >>> s
            (1, 5, 3)
            <BLANKLINE>

        """
        self.ratios[index] = quicktions.Fraction(data)

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
            (1, 2, 3)
            <BLANKLINE>

        """
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string

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
        """
        Concatenates Ratio Segment with iterable.

        ..  container:: example

            >>> r_segment = microtones.RatioSegment(["1", "1/2", "5/4"])
            >>> r_segment += [1, quicktions.Fraction(11, 6), quicktions.Fraction(27, 2)]
            >>> s = r_segment
            >>> s
            (1, 1 / 2, 5 / 4, 1, 11 / 6, 27 / 2)
            <BLANKLINE>

        """
        argument = type(self)(argument)
        items = self.ratios + argument.ratios
        return type(self)(items)

    def __contains__(self, argument):
        """
        Returns boolean

        ..  container::

            >>> r_segment = microtones.RatioSegment([1, 2, 6])
            >>> 1 in r_segment
            True

        """
        return argument in self.ratios

    def constrain_to_octave(self):
        """
        Gets Ratio Segment constrained within an octave.

        ..  container:: example

            >>> str(microtones.RatioSegment([1, 3, "1/5"]).constrain_to_octave())
            '(1, 3/2, 4/5)'

        """
        constrained = []
        for ratio in self.ratios:
            while 2 <= ratio:
                ratio /= 2
            while ratio < quicktions.Fraction(1, 2):
                ratio *= 2
            constrained.append(ratio)
        return type(self)(constrained)

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_segment = microtones.RatioSegment([1, 2, 3])
            >>> input_scale = [i + 1 for i in range(11)]
            >>> s = pc_segment.complement(input_scale)
            >>> s
            (4, 5, 6, 7, 8, 9, 10, 11)
            <BLANKLINE>

        """
        complements = []
        for ratio in scale:
            if ratio not in self.ratios:
                complements.append(ratio)
        return type(self)(complements)

    def invert(self, axis=1):
        """
        Gets inversion.

        ..  container:: example

            >>> s = microtones.RatioSegment([2, 4, 3]).invert()
            >>> s
            (1 / 2, 1 / 4, 1 / 3)
            <BLANKLINE>

            >>> s = microtones.RatioSegment([2, 4, 3]).invert(3)
            >>> s
            (9 / 2, 9 / 4, 3)
            <BLANKLINE>

        """
        axis = quicktions.Fraction(axis)
        assert 0 < axis
        inverse = [axis / i for i in self.ratios]
        inverse = [axis * ratio for ratio in inverse]
        return type(self)(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> s = microtones.RatioSegment([1, 2, 3]).multiply(2)
            >>> s
            (2, 4, 6)
            <BLANKLINE>

        """
        multiplied_pitch_classes = [
            quicktions.Fraction(n) * ratio for ratio in self.ratios
        ]
        return type(self)(multiplied_pitch_classes)

    def retrograde(self):
        """
        Gets retrograde.

        ..  container:: example

            >>> s = microtones.RatioSegment([1, 2, 3, 3]).retrograde()
            >>> s
            (3, 3, 2, 1)
            <BLANKLINE>

        """
        return type(self)(reversed(self.ratios))

    def rotate(self, n):
        """
        Gets rotation.

        ..  container:: example

            >>> s = microtones.RatioSegment([1, 2, 3]).rotate(1)
            >>> s
            (2, 3, 1)
            <BLANKLINE>

        """
        copied_list = [i for i in self.ratios]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return type(self)(copied_list_)

    def sorted(self):
        """
        Gets Ratio Segment sorted in ascending order.

        ..  container:: example

            >>> s = microtones.RatioSegment([5, 2, 3, "1/2", 1, "1/5"]).sorted()
            >>> s
            (1 / 5, 1 / 2, 1, 2, 3, 5)
            <BLANKLINE>

        """
        return type(self)(sorted(self.ratios))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> s = microtones.RatioSegment([1, 2, 3]).transpose(2)
            >>> s
            (3, 4, 5)
            <BLANKLINE>

            >>> s = microtones.RatioSegment([1, 2, 4, 5, 6]).invert().transpose(1+3)
            >>> s
            (5, 9 / 2, 17 / 4, 21 / 5, 25 / 6)
            <BLANKLINE>

        """
        transposed = [ratio + quicktions.Fraction(n) for ratio in self.ratios]
        return type(self)(transposed)
