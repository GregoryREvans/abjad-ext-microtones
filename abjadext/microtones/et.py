import fractions
import math

import abjad


class ETBundle:
    """
    ET bundle.

    >>> from abjadext import microtones

    """

    def __init__(self, pitch="c'", accidental_string=None):
        self.pitch = pitch
        self.accidental_string = accidental_string

    def __repr__(self):
        """
        Gets interpreter representation.

        ..  container:: example

            >>> microtones.ETBundle()
            ETBundle(pitch="c'", accidental_string=None)

        """
        if self.accidental_string is None:
            return f"""{self.__class__.__name__}(pitch="{self.pitch}", accidental_string={self.accidental_string})"""
        else:
            return f"""{self.__class__.__name__}(pitch="{self.pitch}", accidental_string="{self.accidental_string}")"""


_accidental_to_value = {
    "double sharp": 2,
    "three-quarters sharp": fractions.Fraction(3 / 2),
    "sharp": 1,
    "quarter sharp": fractions.Fraction(1 / 2),
    "natural": 0,
    "quarter flat": fractions.Fraction(-1 / 2),
    "flat": -1,
    "three-quarters flat": fractions.Fraction(-3 / 2),
    "double flat": -2,
}

_value_to_accidental = {
    "2": r"\double-sharp",
    "11/6": r"\eleven-twelfths-sharp",
    "7/4": r"\seven-eighths-sharp",
    "5/3": r"\five-sixths-sharp",
    "8/5": r"\four-fifths-sharp",
    "3/2": r"\three-quarters-sharp",
    "7/5": r"\seven-tenths-sharp",
    "4/3": r"\two-thirds-sharp",
    "5/4": r"\five-eighths-sharp",
    "6/5": r"\three-fifths-sharp",
    "7/6": r"\seven-twelfths-sharp",
    "1": r"\sharp",
    "5/6": r"\five-twelfths-sharp",
    "4/5": r"\two-fifths-sharp",
    "3/4": r"\three-eighths-sharp",
    "2/3": r"\one-third-sharp",
    "3/5": r"\three-tenths-sharp",
    "1/2": r"\one-quarter-sharp",
    "2/5": r"\one-fifth-sharp",
    "1/3": r"\one-sixth-sharp",
    "1/4": r"\one-eighth-sharp",
    "1/5": r"\one-tenth-sharp",
    "1/6": r"\one-twelfth-sharp",
    "0": r"\natural",
    "-1/6": r"\one-twelfth-flat",
    "-1/5": r"\one-tenth-flat",
    "-1/4": r"\one-eighth-flat",
    "-1/3": r"\one-sixth-flat",
    "-2/5": r"\one-fifth-flat",
    "-1/2": r"\one-quarter-flat",
    "-3/5": r"\three-tenths-flat",
    "-2/3": r"\one-third-flat",
    "-3/4": r"\three-eighths-flat",
    "-4/5": r"\two-fifths-flat",
    "-5/6": r"\five-twelfths-flat",
    "-1": r"\flat",
    "-7/6": r"\seven-twelfths-flat",
    "-6/5": r"\three-fifths-flat",
    "-5/4": r"\five-eighths-flat",
    "-4/3": r"\two-thirds-flat",
    "-7/5": r"\seven-tenths-flat",
    "-3/2": r"\three-quarters-flat",
    "-8/5": r"\four-fifths-flat",
    "-5/3": r"\five-sixths-flat",
    "-7/4": r"\seven-eighths-flat",
    "-11/6": r"\eleven-twelfths-flat",
    "-2": r"\double-flat",
}

_reversed_value_to_accidental = {
    r"\double-sharp-markup": "2/1",
    r"\eleven-twelfths-sharp-markup": "11/6",
    r"\seven-eighths-sharp-markup": "7/4",
    r"\five-sixths-sharp-markup": "5/3",
    r"\four-fifths-sharp-markup": "8/5",
    r"\three-quarters-sharp-markup": "3/2",
    r"\two-thirds-sharp-markup": "4/3",
    r"\five-eighths-sharp-markup": "5/4",
    r"\three-fifths-sharp-markup": "6/5",
    r"\seven-twelfths-sharp-markup": "7/6",
    r"\sharp-markup": "1/1",
    r"\five-twelfths-sharp-markup": "5/6",
    r"\two-fifths-sharp-markup": "4/5",
    r"\three-eighths-sharp-markup": "3/4",
    r"\one-third-sharp-markup": "2/3",
    r"\one-quarter-sharp-markup": "1/2",
    r"\one-fifth-sharp-markup": "2/5",
    r"\one-sixth-sharp-markup": "1/3",
    r"\one-eighth-sharp-markup": "1/4",
    r"\one-twelfth-sharp-markup": "1/6",
    r"\natural-markup": "0",
    r"\one-twelfth-flat-markup": "-1/6",
    r"\one-eighth-flat-markup": "-1/4",
    r"\one-sixth-flat-markup": "-1/3",
    r"\one-fifth-flat-markup": "-2/5",
    r"\one-quarter-flat-markup": "-1/2",
    r"\one-third-flat-markup": "-2/3",
    r"\three-eighths-flat-markup": "-3/4",
    r"\two-fifths-flat-markup": "-4/5",
    r"\five-twelfths-flat-markup": "-5/6",
    r"\flat-markup": "-1/1",
    r"\seven-twelfths-flat-markup": "-7/6",
    r"\three-fifths-flat-markup": "-6/5",
    r"\five-eighths-flat-markup": "-5/4",
    r"\two-thirds-flat-markup": "-4/3",
    r"\three-quarters-flat-markup": "-3/2",
    r"\four-fifths-flat-markup": "-8/5",
    r"\five-sixths-flat-markup": "-5/3",
    r"\seven-eighths-flat-markup": "-7/4",
    r"\eleven-twelfths-flat-markup": "-11/6",
    r"\double-flat-markup": "-2/1",
}


def get_accidental_value(pitch):
    """
    Gets accidental value.

    ..  container:: example

        >>> pitch = abjad.NamedPitch("cs'")
        >>> microtones.get_accidental_value(pitch)
        1

    """
    accidental = pitch.accidental.name
    accidental_value = _accidental_to_value[f"{accidental}"]
    return accidental_value


def get_value_sum(pitch, value):
    """
    Gets value sum.

    ..  container:: example

        >>> pitch = abjad.NamedPitch("cs'")
        >>> microtones.get_value_sum(pitch, "3/4")
        Fraction(7, 4)

    """
    value = fractions.Fraction(value)
    return get_accidental_value(pitch) + value


def get_alteration(pitch, value):
    r"""
    Gets alteration.

    ..  container:: example

        >>> pitch = abjad.NumberedPitch(0)
        >>> bundle = microtones.get_alteration(pitch, "2/1")
        >>> bundle.pitch
        NumberedPitch(2)

        >>> bundle.accidental_string
        '\\natural-markup'

    ..  container:: example

        >>> pitch = abjad.NumberedPitch(0)
        >>> bundle = microtones.get_alteration(pitch, "1/1")
        >>> bundle.pitch
        NumberedPitch(1)

        >>> bundle.accidental_string
        '\\sharp-markup'

    """
    value = fractions.Fraction(value)
    semitones = int(math.modf(value)[1])
    remainder = fractions.Fraction(value - int(math.modf(value)[1]))
    if semitones != 0:
        pitch = abjad.NumberedInterval(semitones).transpose(pitch)
    transposed_accidental_value = get_value_sum(pitch, remainder)
    key = str(transposed_accidental_value)
    new_accidental = _value_to_accidental[key] + "-markup"
    return ETBundle(pitch, new_accidental)


def apply_alteration(note_head, value):
    r"""
    Applies alteration.

    ..  container:: example

        >>> from fractions import Fraction
        >>> steps = [0, "1/12", "1/10", "1/8", "1/6", "1/5", "1/4", "3/10", "1/3", "3/8", "2/5", "5/12", "1/2", "7/12", "3/5", "5/8", "2/3", "7/10", "3/4", "4/5", "5/6", "7/8", "11/12", 1]
        >>> steps = [Fraction(step) * 2 for step in steps]
        >>> reverse_steps = [0 - step for step in steps]
        >>> reverse_steps.reverse()
        >>> total_steps = []
        >>> total_steps.extend(reverse_steps)
        >>> total_steps.extend(steps)
        >>> final_steps = sorted(list(set(total_steps)))
        >>> notes = [abjad.Note() for step in final_steps]
        >>> for note, step in zip(notes, final_steps):
        ...     microtones.apply_alteration(note.note_head, step)
        ...
        >>> staff = abjad.Staff(notes)
        >>> markup_fractions = [fraction / 2 for fraction in final_steps]
        >>> pairs = [(abs(fraction.numerator), abs(fraction.denominator)) for fraction in markup_fractions]
        >>> markups = [abjad.Markup(abjad.Markup.fraction(pair[0], pair[1]), direction=abjad.Up) for pair in pairs]
        >>> for markup, note in zip(markups, abjad.select(staff).leaves()):
        ...     abjad.attach(markup, note)
        ...
        >>> abjad.attach(abjad.TimeSignature((6, 4)), abjad.select(staff).leaves()[0])
        >>> abjad.attach(abjad.TimeSignature((5, 4)), abjad.select(staff).leaves()[18])
        >>> abjad.attach(abjad.TimeSignature((1, 4)), abjad.select(staff).leaves()[23])
        >>> abjad.attach(abjad.TimeSignature((5, 4)), abjad.select(staff).leaves()[24])
        >>> abjad.attach(abjad.TimeSignature((6, 4)), abjad.select(staff).leaves()[29])
        >>> break_points = [5, 11, 17, 22, 23, 28, 34, 40]
        >>> for point in break_points:
        ...     abjad.attach(abjad.LilyPondLiteral(r"\break", format_slot="after"), abjad.select(staff).leaves()[point])
        ...
        >>> lilypond_file = abjad.LilyPondFile.new(
        ...     staff,
        ...     includes=[
        ...         "default.ily",
        ...         "ekmelos-edo-accidental-markups.ily",
        ...         "all-edo-markups-example.ily",
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file.layout_block.items.append(fr"\accidentalStyle {style}")
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                \time 6/4
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \flat-markup
                bf4
                ^ \markup {
                    \fraction
                        1
                        1
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \five-twelfths-flat-markup
                b4
                ^ \markup {
                    \fraction
                        11
                        12
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \three-eighths-flat-markup
                b4
                ^ \markup {
                    \fraction
                        7
                        8
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-third-flat-markup
                b4
                ^ \markup {
                    \fraction
                        5
                        6
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \three-tenths-flat-markup
                b4
                ^ \markup {
                    \fraction
                        4
                        5
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-quarter-flat-markup
                b4
                ^ \markup {
                    \fraction
                        3
                        4
                    }
                \break
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-fifth-flat-markup
                b4
                ^ \markup {
                    \fraction
                        7
                        10
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-sixth-flat-markup
                b4
                ^ \markup {
                    \fraction
                        2
                        3
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-eighth-flat-markup
                b4
                ^ \markup {
                    \fraction
                        5
                        8
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-tenth-flat-markup
                b4
                ^ \markup {
                    \fraction
                        3
                        5
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-twelfth-flat-markup
                b4
                ^ \markup {
                    \fraction
                        7
                        12
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \natural-markup
                b4
                ^ \markup {
                    \fraction
                        1
                        2
                    }
                \break
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \five-twelfths-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        5
                        12
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \two-fifths-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        2
                        5
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \three-eighths-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        3
                        8
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-third-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        3
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \three-tenths-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        3
                        10
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-quarter-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        4
                    }
                \break
                \time 5/4
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-fifth-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        5
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-sixth-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        6
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-eighth-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        8
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-tenth-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        10
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-twelfth-flat-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        12
                    }
                \break
                \time 1/4
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \natural-markup
                c'4
                ^ \markup {
                    \fraction
                        0
                        1
                    }
                \break
                \time 5/4
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-twelfth-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        12
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-tenth-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        10
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-eighth-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        8
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-sixth-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        6
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-fifth-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        5
                    }
                \break
                \time 6/4
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-quarter-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        4
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \three-tenths-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        3
                        10
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-third-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        1
                        3
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \three-eighths-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        3
                        8
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \two-fifths-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        2
                        5
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \five-twelfths-sharp-markup
                c'4
                ^ \markup {
                    \fraction
                        5
                        12
                    }
                \break
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \flat-markup
                df'4
                ^ \markup {
                    \fraction
                        1
                        2
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \five-twelfths-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        7
                        12
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \two-fifths-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        3
                        5
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \three-eighths-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        5
                        8
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-third-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        2
                        3
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \three-tenths-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        7
                        10
                    }
                \break
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-quarter-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        3
                        4
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-fifth-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        4
                        5
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-sixth-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        5
                        6
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-eighth-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        7
                        8
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-twelfth-flat-markup
                df'4
                ^ \markup {
                    \fraction
                        11
                        12
                    }
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \natural-markup
                d'4
                ^ \markup {
                    \fraction
                        1
                        1
                    }
            }

    ..  container:: example

        >>> note = abjad.Note("c'4")
        >>> microtones.apply_alteration(note.note_head, "5/4")
        >>> staff = abjad.Staff([note])
        >>> lilypond_file = abjad.LilyPondFile.new(
        ...     staff, includes=["default.ily", "ekmelos-edo-accidental-markups.ily"],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file.layout_block.items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(note)
            \tweak Accidental.stencil #ly:text-interface::print
            \tweak Accidental.text \three-eighths-flat-markup
            df'4

    ..  container:: example

        >>> note = abjad.Note("c'4")
        >>> microtones.apply_alteration(note.note_head, "5/4")
        >>> staff = abjad.Staff([note])
        >>> lilypond_file = abjad.LilyPondFile.new(
        ...     staff, includes=["default.ily", "default-edo-accidental-markups.ily"],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file.layout_block.items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

    ..  container:: example

        >>> note = abjad.Note("c'4")
        >>> microtones.apply_alteration(note.note_head, "4/5")
        >>> staff = abjad.Staff([note])
        >>> lilypond_file = abjad.LilyPondFile.new(
        ...     staff, includes=["default.ily", "ekmelos-edo-accidental-markups.ily"],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file.layout_block.items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(note)
            \tweak Accidental.stencil #ly:text-interface::print
            \tweak Accidental.text \two-fifths-sharp-markup
            c'4

    ..  container:: example

        >>> note = abjad.Note("c'4")
        >>> microtones.apply_alteration(note.note_head, "4/5")
        >>> staff = abjad.Staff([note])
        >>> lilypond_file = abjad.LilyPondFile.new(
        ...     staff, includes=["default.ily", "default-edo-accidental-markups.ily"],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file.layout_block.items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

    ..  container:: example

        >>> note = abjad.Note("c''4")
        >>> microtones.apply_alteration(note.note_head, "11/6")
        >>> staff = abjad.Staff([note])
        >>> lilypond_file = abjad.LilyPondFile.new(
        ...     staff, includes=["default.ily", "ekmelos-edo-accidental-markups.ily"],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file.layout_block.items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(note)
            \tweak Accidental.stencil #ly:text-interface::print
            \tweak Accidental.text \one-twelfth-flat-markup
            df''4

    ..  container:: example

        >>> note = abjad.Note("c''4")
        >>> microtones.apply_alteration(note.note_head, "11/6")
        >>> staff = abjad.Staff([note])
        >>> lilypond_file = abjad.LilyPondFile.new(
        ...     staff, includes=["default.ily", "default-edo-accidental-markups.ily"],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file.layout_block.items.append(fr"\accidentalStyle {style}" )
        >>> abjad.show(lilypond_file) # doctest: +SKIP

    """
    value = fractions.Fraction(value)
    pitch = note_head.written_pitch
    bundle = get_alteration(pitch, value)
    note_head.written_pitch = bundle.pitch
    string = r"#ly:text-interface::print"
    abjad.tweak(note_head, literal=True).Accidental.stencil = string
    abjad.tweak(note_head, literal=True).Accidental.text = bundle.accidental_string
