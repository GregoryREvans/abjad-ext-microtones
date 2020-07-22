import fractions

import abjad


class PitchClassSet(object):
    """
    Pitch Class Set.

    >>> from abjadext import microtones
    >>> import fractions

    """

    def __init__(self, pitch_classes):
        temp = [fractions.Fraction(pitch) % 12 for pitch in pitch_classes]
        self.pitch_classes = []
        for pitch in temp:
            if pitch not in self.pitch_classes:
                self.pitch_classes.append(pitch)

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

            >>> microtones.PitchClassSet([0, 1, 2])
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

        """
        return abjad.storage(self)

    def __str__(self):
        """
        Gets string representation.

        ..  container:: example

            >>> str(microtones.PitchClassSet([0, 1, 2]))
            '{0, 1, 2}'

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
            >>> pc_set += [0, fractions.Fraction(11, 6), fractions.Fraction(27, 2)]
            >>> pc_set
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(0, 1),
                    Fraction(1, 2),
                    Fraction(5, 4),
                    Fraction(11, 6),
                    Fraction(3, 2),
                    ]
                )

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
        return PitchClassSet(copied_list_)

    def _transpose_to_zero(self):
        return self.transpose(-self.pitch_classes[0])

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

            >>> pc_set = microtones.PitchClassSet([0, 1, 2])
            >>> input_scale = [i for i in range(12)]
            >>> pc_set.complement(input_scale)
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(3, 1),
                    Fraction(4, 1),
                    Fraction(5, 1),
                    Fraction(6, 1),
                    Fraction(7, 1),
                    Fraction(8, 1),
                    Fraction(9, 1),
                    Fraction(10, 1),
                    Fraction(11, 1),
                    ]
                )

        """
        complements = []
        for pitch in scale:
            if pitch not in self.pitch_classes:
                complements.append(pitch)
        return PitchClassSet(complements)

    def invert(self, axis=0):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 1, 3]).invert()
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(0, 1),
                    Fraction(11, 1),
                    Fraction(9, 1),
                    ]
                )

            >>> microtones.PitchClassSet([0, 1, 3]).invert(3)
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(6, 1),
                    Fraction(5, 1),
                    Fraction(3, 1),
                    ]
                )

        """
        intervals = [axis - i for i in self.pitch_classes]
        inverse = [axis + interval for interval in intervals]
        return PitchClassSet(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 1, 3]).multiply(2)
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(0, 1),
                    Fraction(2, 1),
                    Fraction(6, 1),
                    ]
                )

        """
        multiplied_pitch_classes = [n * pitch for pitch in self.pitch_classes]
        return PitchClassSet(multiplied_pitch_classes)

    def normal_order(self):
        """
        Gets normal order.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 2, 1]).normal_order()
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

        """
        size = len(self.pitch_classes)
        if size < 2:
            return PitchClassSet(self.pitch_classes)
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
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

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
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

        """
        return PitchClassSet(sorted(self.pitch_classes))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.PitchClassSet([0, 1, 2]).transpose(2)
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(2, 1),
                    Fraction(3, 1),
                    Fraction(4, 1),
                    ]
                )

            >>> microtones.PitchClassSet([0, 1, 3, 4, 5]).invert().transpose(1+3)
            abjadext.et_utilities.PitchClassSet(
                [
                    Fraction(4, 1),
                    Fraction(3, 1),
                    Fraction(1, 1),
                    Fraction(0, 1),
                    Fraction(11, 1),
                    ]
                )

        """
        transposed = [pitch + n for pitch in self.pitch_classes]
        return PitchClassSet(transposed)


class PitchSet(object):
    """
    Pitch Set.

    >>> from abjadext import microtones

    """

    def __init__(self, pitches):
        temp = [fractions.Fraction(pitch) for pitch in pitches]
        self.pitches = []
        for pitch in temp:
            if pitch not in self.pitches:
                self.pitches.append(pitch)

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
            abjadext.et_utilities.PitchSet(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

        """
        return abjad.storage(self)

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
            >>> p_set += [0, fractions.Fraction(11, 6), fractions.Fraction(27, 2)]
            >>> p_set
            abjadext.et_utilities.PitchSet(
                [
                    Fraction(0, 1),
                    Fraction(1, 2),
                    Fraction(5, 4),
                    Fraction(11, 6),
                    Fraction(27, 2),
                    ]
                )

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
        return PitchSet(copied_list_)

    def _transpose_to_zero(self):
        return self.transpose(-self.pitches[0])

    def complement(self, scale):
        """
        Gets complement in scale.

        ..  container:: example

            >>> pc_set = microtones.PitchSet([0, 1, 2])
            >>> input_scale = [i for i in range(12)]
            >>> pc_set.complement(input_scale)
            abjadext.et_utilities.PitchSet(
                [
                    Fraction(3, 1),
                    Fraction(4, 1),
                    Fraction(5, 1),
                    Fraction(6, 1),
                    Fraction(7, 1),
                    Fraction(8, 1),
                    Fraction(9, 1),
                    Fraction(10, 1),
                    Fraction(11, 1),
                    ]
                )

        """
        complements = []
        for pitch in scale:
            if pitch not in self.pitches:
                complements.append(pitch)
        return PitchSet(complements)

    def invert(self, axis=0):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.PitchSet([0, 1, 3]).invert()
            abjadext.et_utilities.PitchSet(
                [
                    Fraction(0, 1),
                    Fraction(-1, 1),
                    Fraction(-3, 1),
                    ]
                )

            >>> microtones.PitchSet([0, 1, 3]).invert(2)
            abjadext.et_utilities.PitchSet(
                [
                    Fraction(4, 1),
                    Fraction(3, 1),
                    Fraction(1, 1),
                    ]
                )

        """
        intervals = [axis - i for i in self.pitches]
        inverse = [axis + interval for interval in intervals]
        return PitchSet(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.PitchSet([0, 1, 3]).multiply(2)
            abjadext.et_utilities.PitchSet(
                [
                    Fraction(0, 1),
                    Fraction(2, 1),
                    Fraction(6, 1),
                    ]
                )

        """
        multiplied_pitches = [n * pitch for pitch in self.pitches]
        return PitchSet(multiplied_pitches)

    def sorted(self):
        """
        Gets Pitch Set sorted in ascending order.

        ..  container:: example

            >>> microtones.PitchSet([2, 1, 0]).sorted()
            abjadext.et_utilities.PitchSet(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

        """
        return PitchSet(sorted(self.pitches))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.PitchSet([0, 1, 2]).transpose(2)
            abjadext.et_utilities.PitchSet(
                [
                    Fraction(2, 1),
                    Fraction(3, 1),
                    Fraction(4, 1),
                    ]
                )

            >>> microtones.PitchSet([0, 1, 3, 4, 5]).invert().transpose(1+3)
            abjadext.et_utilities.PitchSet(
                [
                    Fraction(4, 1),
                    Fraction(3, 1),
                    Fraction(1, 1),
                    Fraction(0, 1),
                    Fraction(-1, 1),
                    ]
                )

        """
        transposed = [pitch + n for pitch in self.pitches]
        return PitchSet(transposed)


class PitchClassSegment(object):
    """
    Pitch Class Segment.

    >>> from abjadext import microtones

    """

    def __init__(self, pitch_classes):
        self.pitch_classes = [fractions.Fraction(pitch) % 12 for pitch in pitch_classes]

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
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

        """
        return abjad.storage(self)

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
            >>> pc_segment += [0, fractions.Fraction(11, 6), fractions.Fraction(27, 2)]
            >>> pc_segment
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(0, 1),
                    Fraction(1, 2),
                    Fraction(5, 4),
                    Fraction(0, 1),
                    Fraction(11, 6),
                    Fraction(3, 2),
                    ]
                )

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
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(3, 1),
                    Fraction(4, 1),
                    Fraction(5, 1),
                    Fraction(6, 1),
                    Fraction(7, 1),
                    Fraction(8, 1),
                    Fraction(9, 1),
                    Fraction(10, 1),
                    Fraction(11, 1),
                    ]
                )

        """
        complements = []
        for pitch in scale:
            if pitch not in self.pitch_classes:
                complements.append(pitch)
        return PitchClassSegment(complements)

    def invert(self, axis=0):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 3]).invert()
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(0, 1),
                    Fraction(11, 1),
                    Fraction(9, 1),
                    ]
                )

            >>> microtones.PitchClassSegment([0, 1, 3]).invert(2)
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(4, 1),
                    Fraction(3, 1),
                    Fraction(1, 1),
                    ]
                )

        """
        intervals = [axis - i for i in self.pitch_classes]
        inverse = [axis + interval for interval in intervals]
        return PitchClassSegment(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 3]).multiply(2)
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(0, 1),
                    Fraction(2, 1),
                    Fraction(6, 1),
                    ]
                )

        """
        multiplied_pitch_classes = [n * pitch for pitch in self.pitch_classes]
        return PitchClassSegment(multiplied_pitch_classes)

    def retrograde(self):
        """
        Gets retrograde.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 2]).retrograde()
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(2, 1),
                    Fraction(1, 1),
                    Fraction(0, 1),
                    ]
                )

        """
        return PitchClassSegment(reversed(self.pitch_classes))

    def rotate(self, n):
        """
        Gets rotation.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 2]).rotate(1)
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(1, 1),
                    Fraction(2, 1),
                    Fraction(0, 1),
                    ]
                )

        """
        copied_list = [i for i in self.pitch_classes]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return PitchClassSegment(copied_list_)

    def sorted(self):
        """
        Gets Pitch Class Segment sorted in ascending order.

        ..  container:: example

            >>> microtones.PitchClassSegment([2, 1, 0]).sorted()
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

        """
        return PitchClassSegment(sorted(self.pitch_classes))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.PitchClassSegment([0, 1, 2]).transpose(2)
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(2, 1),
                    Fraction(3, 1),
                    Fraction(4, 1),
                    ]
                )

            >>> microtones.PitchClassSegment([0, 1, 3, 4, 5]).invert().transpose(1+3)
            abjadext.et_utilities.PitchClassSegment(
                [
                    Fraction(4, 1),
                    Fraction(3, 1),
                    Fraction(1, 1),
                    Fraction(0, 1),
                    Fraction(11, 1),
                    ]
                )

        """
        transposed = [pitch + n for pitch in self.pitch_classes]
        return PitchClassSegment(transposed)


class PitchSegment(object):
    """
    Pitch Segment.

    >>> from abjadext import microtones

    """

    def __init__(self, pitches):
        self.pitches = [fractions.Fraction(pitch) for pitch in pitches]

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
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

        """
        return abjad.storage(self)

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
            >>> p_segment += [0, fractions.Fraction(11, 6), fractions.Fraction(27, 2)]
            >>> p_segment
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(0, 1),
                    Fraction(1, 2),
                    Fraction(5, 4),
                    Fraction(0, 1),
                    Fraction(11, 6),
                    Fraction(27, 2),
                    ]
                )

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
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(3, 1),
                    Fraction(4, 1),
                    Fraction(5, 1),
                    Fraction(6, 1),
                    Fraction(7, 1),
                    Fraction(8, 1),
                    Fraction(9, 1),
                    Fraction(10, 1),
                    Fraction(11, 1),
                    ]
                )

        """
        complements = []
        for pitch in scale:
            if pitch not in self.pitches:
                complements.append(pitch)
        return PitchSegment(complements)

    def invert(self, axis=0):
        """
        Gets inversion.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 3]).invert()
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(0, 1),
                    Fraction(-1, 1),
                    Fraction(-3, 1),
                    ]
                )

            >>> microtones.PitchSegment([0, 1, 3]).invert(2)
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(4, 1),
                    Fraction(3, 1),
                    Fraction(1, 1),
                    ]
                )

        """
        intervals = [axis - i for i in self.pitches]
        inverse = [axis + interval for interval in intervals]
        return PitchSegment(inverse)

    def multiply(self, n):
        """
        Gets multiplication.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 3]).multiply(2)
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(0, 1),
                    Fraction(2, 1),
                    Fraction(6, 1),
                    ]
                )

        """
        multiplied_pitches = [n * pitch for pitch in self.pitches]
        return PitchSegment(multiplied_pitches)

    def retrograde(self):
        """
        Gets retrograde.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 2]).retrograde()
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(2, 1),
                    Fraction(1, 1),
                    Fraction(0, 1),
                    ]
                )

        """
        return PitchSegment(reversed(self.pitches))

    def rotate(self, n):
        """
        Gets rotation.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 2]).rotate(1)
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(1, 1),
                    Fraction(2, 1),
                    Fraction(0, 1),
                    ]
                )

        """
        copied_list = [i for i in self.pitches]
        steps = int(n) % len(copied_list)
        copied_list_ = copied_list[steps:] + copied_list[:steps]
        return PitchSegment(copied_list_)

    def sorted(self):
        """
        Gets Pitch Segment sorted in ascending order.

        ..  container:: example

            >>> microtones.PitchSegment([2, 1, 0]).sorted()
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(0, 1),
                    Fraction(1, 1),
                    Fraction(2, 1),
                    ]
                )

        """
        return PitchSegment(sorted(self.pitches))

    def transpose(self, n):
        """
        Gets transposition.

        ..  container:: example

            >>> microtones.PitchSegment([0, 1, 2]).transpose(2)
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(2, 1),
                    Fraction(3, 1),
                    Fraction(4, 1),
                    ]
                )

            >>> microtones.PitchSegment([0, 1, 3, 4, 5]).invert().transpose(1+3)
            abjadext.et_utilities.PitchSegment(
                [
                    Fraction(4, 1),
                    Fraction(3, 1),
                    Fraction(1, 1),
                    Fraction(0, 1),
                    Fraction(-1, 1),
                    ]
                )

        """
        transposed = [pitch + n for pitch in self.pitches]
        return PitchSegment(transposed)
