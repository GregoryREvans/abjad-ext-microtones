from fractions import Fraction
from math import modf

import abjad


class EDOBundle:
    def __init__(self, pitch="c'", accidental_string=None):
        self.pitch = pitch
        self.accidental_string = accidental_string

    def __repr__(self):
        return "EDOBundle()"

    def __str__(self):
        return f"{self.pitch} + {self.accidental_string}"


accidental_to_value = {
    "double sharp": 2,
    "three-quarters sharp": Fraction(3 / 2),
    "sharp": 1,
    "quarter sharp": Fraction(1 / 2),
    "natural": 0,
    "quarter flat": Fraction(-1 / 2),
    "flat": -1,
    "three-quarters flat": Fraction(-3 / 2),
    "double flat": -2,
}

value_to_accidental = {
    "2/1": r"\double-sharp",
    "11/6": r"\eleven-twelfths-sharp",
    "7/4": r"\seven-eighths-sharp",
    "5/3": r"\five-sixths-sharp",
    "3/2": r"\three-quarters-sharp",
    "4/3": r"\two-thirds-sharp",
    "5/4": r"\five-eighths-sharp",
    "7/6": r"\seven-twelfths-sharp",
    "1/1": r"\forced-sharp",
    "5/6": r"\five-twelfths-sharp",
    "3/4": r"\three-eighths-sharp",
    "2/3": r"\one-third-sharp",
    "1/2": r"\quarter-sharp",
    "1/3": r"\one-sixth-sharp",
    "1/4": r"\eighth-sharp",
    "1/6": r"\one-twelfth-sharp",
    "0": r"\forced-natural",
    "-1/6": r"\one-twelfth-flat",
    "-1/4": r"\eighth-flat",
    "-1/3": r"\one-sixth-flat",
    "-1/2": r"\quarter-flat",
    "-2/3": r"\one-third-flat",
    "-3/4": r"\three-eighths-flat",
    "-5/6": r"\five-twelfths-flat",
    "-1/1": r"\forced-flat",
    "-7/6": r"\seven-twelfths-flat",
    "-5/4": r"\five-eighths-flat",
    "-4/3": r"\two-thirds-flat",
    "-3/2": r"\three-quarters-flat",
    "-5/3": r"\five-sixths-flat",
    "-7/4": r"\seven-eighths-flat",
    "-11/6": r"\eleven-twelfths-flat",
    "-2/1": r"\double-flat",
}

reversed_value_to_accidental = {
    r"\double-sharp-markup": "2/1",
    r"\eleven-twelfths-sharp-markup": "11/6",
    r"\seven-eighths-sharp-markup": "7/4",
    r"\five-sixths-sharp-markup": "5/3",
    r"\three-quarters-sharp-markup": "3/2",
    r"\two-thirds-sharp-markup": "4/3",
    r"\five-eighths-sharp-markup": "5/4",
    r"\seven-twelfths-sharp-markup": "7/6",
    r"\forced-sharp-markup": "1/1",
    r"\five-twelfths-sharp-markup": "5/6",
    r"\three-eighths-sharp-markup": "3/4",
    r"\one-third-sharp-markup": "2/3",
    r"\quarter-sharp-markup": "1/2",
    r"\one-sixth-sharp-markup": "1/3",
    r"\eighth-sharp-markup": "1/4",
    r"\one-twelfth-sharp-markup": "1/6",
    r"\forced-natural": "0",
    r"\one-twelfth-flat-markup": "-1/6",
    r"\eighth-flat-markup": "-1/4",
    r"\one-sixth-flat-markup": "-1/3",
    r"\quarter-flat-markup": "-1/2",
    r"\one-third-flat-markup": "-2/3",
    r"\three-eighths-flat-markup": "-3/4",
    r"\five-twelfths-flat-markup": "-5/6",
    r"\forced-flat-markup": "-1/1",
    r"\seven-twelfths-flat-markup": "-7/6",
    r"\five-eighths-flat-markup": "-5/4",
    r"\two-thirds-flat-markup": "-4/3",
    r"\three-quarters-flat-markup": "-3/2",
    r"\five-sixths-flat-markup": "-5/3",
    r"\seven-eighths-flat-markup": "-7/4",
    r"\eleven-twelfths-flat-markup": "-11/6",
    r"\double-flat-markup": "-2/1",
}


def get_accidental_value(pitch):
    r"""
    >>> import abjad
    >>> from abjadext import microtones
    >>> pitch = abjad.NamedPitch("cs'")
    >>> print(microtones.get_accidental_value(pitch))
    1

    """

    accidental = pitch.accidental.name
    accidental_value = accidental_to_value[f"{accidental}"]
    return accidental_value


def get_value_sum(pitch, value):
    r"""
    >>> pitch = abjad.NamedPitch("cs'")
    >>> print(microtones.get_value_sum(pitch, "3/4"))
    7/4

    """

    value = Fraction(value)
    return get_accidental_value(pitch) + value


def get_alteration(pitch, value):
    r"""
    >>> pitch = abjad.NamedPitch("cs'")
    >>> print(microtones.get_alteration(pitch, "3/4").pitch)
    d'

    >>> print(microtones.get_alteration(pitch, "3/4").accidental_string)
    \quarter-sharp-markup

    """

    value = Fraction(value) * 2
    semitones = int(modf(value)[1])
    remainder = Fraction(value - int(modf(value)[1]))
    if semitones != 0:
        pitch = abjad.NumberedInterval(semitones).transpose(pitch)
    transposed_accidental_value = get_value_sum(pitch, remainder)
    new_accidental = (
        value_to_accidental[str(transposed_accidental_value)] + "-markup"
    )  # temporary markup
    return EDOBundle(pitch, new_accidental)


def apply_alteration(note_head, value):
    r"""
    >>> note = abjad.Note("c'4")
    >>> microtones.apply_alteration(note.note_head, "3/4")
    >>> abjad.f(note)
    dqf'4

    >>> note = abjad.Note("c'4")
    >>> microtones.apply_alteration(note.note_head, "11/12")
    >>> abjad.f(note)
    \tweak Accidental.stencil #ly::text-interface:print
    \tweak Accidental.text \one-twelfth-flat-markup
    df'4

    """

    value = Fraction(value)
    pitch = note_head.written_pitch
    bundle = get_alteration(pitch, value)
    if (
        Fraction(reversed_value_to_accidental[fr"{bundle.accidental_string}"])
        % Fraction(1, 2)
        == 0
    ):
        step = -Fraction(reversed_value_to_accidental[fr"{bundle.accidental_string}"])
        bundle.pitch = abjad.NumberedInterval(step).transpose(bundle.pitch)
        note_head.written_pitch = bundle.pitch
    else:
        # literal = abjad.LilyPondLiteral(bundle.accidental_string, format_slot="before")
        note_head.written_pitch = bundle.pitch
        abjad.tweak(
            note_head, literal=True
        ).Accidental.stencil = r"#ly::text-interface:print"
        abjad.tweak(note_head, literal=True).Accidental.text = bundle.accidental_string
        # abjad.attach(literal, note_head)


# ### NOTES ###
# cannot attach to note-head
# can only tweak note-head
# can only attach leaf
