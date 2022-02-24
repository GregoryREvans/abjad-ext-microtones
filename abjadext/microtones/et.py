"""
Package for equal tempered microtones.
"""
import math

import abjad
import black
import quicktions


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
            repr not yet defined

        """
        return "repr not yet defined"

    def __str__(self):
        string = str(self)
        string = black.format_str(string, mode=black.mode.Mode())
        return string


_accidental_to_value = {
    "double sharp": 2,
    "three-quarters sharp": quicktions.Fraction(3 / 2),
    "sharp": 1,
    "quarter sharp": quicktions.Fraction(1 / 2),
    "natural": 0,
    "quarter flat": quicktions.Fraction(-1 / 2),
    "flat": -1,
    "three-quarters flat": quicktions.Fraction(-3 / 2),
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
    "1": r"\abjad-sharp",
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
    "0": r"\abjad-natural",
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
    "-1": r"\abjad-flat",
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
    r"\abjad-sharp-markup": "1/1",
    r"\five-twelfths-sharp-markup": "5/6",
    r"\two-fifths-sharp-markup": "4/5",
    r"\three-eighths-sharp-markup": "3/4",
    r"\one-third-sharp-markup": "2/3",
    r"\one-quarter-sharp-markup": "1/2",
    r"\one-fifth-sharp-markup": "2/5",
    r"\one-sixth-sharp-markup": "1/3",
    r"\one-eighth-sharp-markup": "1/4",
    r"\one-twelfth-sharp-markup": "1/6",
    r"\abjad-natural-markup": "0",
    r"\one-twelfth-flat-markup": "-1/6",
    r"\one-eighth-flat-markup": "-1/4",
    r"\one-sixth-flat-markup": "-1/3",
    r"\one-fifth-flat-markup": "-2/5",
    r"\one-quarter-flat-markup": "-1/2",
    r"\one-third-flat-markup": "-2/3",
    r"\three-eighths-flat-markup": "-3/4",
    r"\two-fifths-flat-markup": "-4/5",
    r"\five-twelfths-flat-markup": "-5/6",
    r"\abjad-flat-markup": "-1/1",
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
    value = quicktions.Fraction(value)
    return get_accidental_value(pitch) + value


def get_alteration(pitch, value, spell=None):
    r"""
    Gets alteration.

    ..  container:: example

        >>> pitch = abjad.NumberedPitch(0)
        >>> bundle = microtones.get_alteration(pitch, "2/1")
        >>> bundle.pitch
        NumberedPitch(2)

        >>> bundle.accidental_string
        '\\abjad-natural-markup'

    ..  container:: example

        >>> pitch = abjad.NumberedPitch(0)
        >>> bundle = microtones.get_alteration(pitch, "1/1")
        >>> bundle.pitch
        NumberedPitch(1)

        >>> bundle.accidental_string
        '\\abjad-sharp-markup'

    ..  container:: example

        >>> pitch = abjad.NumberedPitch(0)
        >>> bundle = microtones.get_alteration(pitch, "1/1", "flat")
        >>> bundle.pitch
        NamedPitch("df'")

        >>> bundle.accidental_string
        '\\abjad-flat-markup'

    ..  container:: example

        >>> pitch = abjad.NumberedPitch(0)
        >>> bundle = microtones.get_alteration(pitch, "3/2", "sharp")
        >>> bundle.pitch
        NumberedPitch(1)

        >>> bundle.accidental_string
        '\\three-quarters-sharp-markup'

    ..  container:: example

        >>> pitch = abjad.NumberedPitch(0)
        >>> bundle = microtones.get_alteration(pitch, "11/6", "sharp")
        >>> bundle.pitch
        NumberedPitch(1)

        >>> bundle.accidental_string
        '\\eleven-twelfths-sharp-markup'

    """
    value = quicktions.Fraction(value)
    semitones = int(math.modf(value)[1])
    remainder = quicktions.Fraction(value - int(math.modf(value)[1]))
    if semitones != 0:
        pitch = abjad.NumberedInterval(semitones).transpose(pitch)
    transposed_accidental_value = get_value_sum(pitch, remainder)
    key = str(transposed_accidental_value)
    new_accidental = _value_to_accidental[key] + "-markup"
    if spell is not None:
        if spell == "sharp":
            if quicktions.Fraction(_reversed_value_to_accidental[new_accidental]) < 0:
                # make sharp
                temp_note = abjad.Note(abjad.NamedPitch(pitch), (1, 4))
                abjad.iterpitches.respell_with_sharps([temp_note])
                pitch = temp_note.written_pitch
                transposed_accidental_value = get_value_sum(pitch, remainder)
                key = str(transposed_accidental_value)
                new_accidental = _value_to_accidental[key] + "-markup"
        if spell == "flat":
            if 0 < quicktions.Fraction(_reversed_value_to_accidental[new_accidental]):
                # make flat
                temp_note = abjad.Note(abjad.NamedPitch(pitch), (1, 4))
                abjad.iterpitches.respell_with_flats([temp_note])
                pitch = temp_note.written_pitch
                transposed_accidental_value = get_value_sum(pitch, remainder)
                key = str(transposed_accidental_value)
                new_accidental = _value_to_accidental[key] + "-markup"
    return ETBundle(pitch, new_accidental)


def apply_alteration(note_head, value, spell=None):
    r"""
    Applies alteration.

    ..  container:: example

        Eighth tone accidentals:

        >>> from quicktions import Fraction
        >>> steps = [0, "1/8", "2/8", "3/8", "4/8", "5/8", "6/8", "7/8", 1]
        >>> steps = [Fraction(step) * 2 for step in steps]
        >>> reverse_steps = [0 - step for step in steps]
        >>> reverse_steps.reverse()
        >>> total_steps = []
        >>> total_steps.extend(reverse_steps)
        >>> total_steps.extend(steps)
        >>> final_steps = sorted(list(set(total_steps)))
        >>> notes = [abjad.Note("c'4") for step in final_steps]
        >>> for note, step in zip(notes, final_steps):
        ...     microtones.apply_alteration(note.note_head, step)
        ...
        >>> staff = abjad.Staff(notes)
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/abjad.ily\'",
        ...         "\\include \'all-edo-markups-example.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}")
        >>> abjad.show(lilypond_file) # doctest: +SKIP

    ..  container:: example

        Tenth tone accidentals:

        >>> from quicktions import Fraction
        >>> steps = [0, "1/10", "2/10", "3/10", "4/10", "5/10", "6/10", "7/10", "8/10", "9/10", 1]
        >>> steps = [Fraction(step) * 2 for step in steps]
        >>> reverse_steps = [0 - step for step in steps]
        >>> reverse_steps.reverse()
        >>> total_steps = []
        >>> total_steps.extend(reverse_steps)
        >>> total_steps.extend(steps)
        >>> final_steps = sorted(list(set(total_steps)))
        >>> notes = [abjad.Note("c'4") for step in final_steps]
        >>> for note, step in zip(notes, final_steps):
        ...     microtones.apply_alteration(note.note_head, step)
        ...
        >>> staff = abjad.Staff(notes)
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/abjad.ily\'",
        ...         "\\include \'all-edo-markups-example.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}")
        >>> abjad.show(lilypond_file) # doctest: +SKIP

    ..  container:: example

        Twelfth tone accidentals:

        >>> from quicktions import Fraction
        >>> steps = [0, "1/12", "2/12", "3/12", "4/12", "5/12", "6/12", "7/12", "8/12", "9/12", "10/12", "11/12", 1]
        >>> steps = [Fraction(step) * 2 for step in steps]
        >>> reverse_steps = [0 - step for step in steps]
        >>> reverse_steps.reverse()
        >>> total_steps = []
        >>> total_steps.extend(reverse_steps)
        >>> total_steps.extend(steps)
        >>> final_steps = sorted(list(set(total_steps)))
        >>> notes = [abjad.Note("c'4") for step in final_steps]
        >>> for note, step in zip(notes, final_steps):
        ...     microtones.apply_alteration(note.note_head, step)
        ...
        >>> staff = abjad.Staff(notes)
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/abjad.ily\'",
        ...         "\\include \'all-edo-markups-example.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}")
        >>> abjad.show(lilypond_file) # doctest: +SKIP

    ..  container:: example

        Spells with sharps when ``spell="sharp"``:

        >>> step = "3/2"
        >>> note = abjad.Note("c'4")
        >>> microtones.apply_alteration(note.note_head, step, spell="sharp")
        >>> staff = abjad.Staff([note])
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/abjad.ily\'",
        ...         "\\include \'all-edo-markups-example.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}")
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> print(abjad.lilypond(staff))
            \new Staff
            {
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \three-quarters-sharp-markup
                cs'4
            }

    ..  container:: example

        Spells with flats when ``spell="flat"``:

        >>> step = "3/2"
        >>> note = abjad.Note("c'4")
        >>> microtones.apply_alteration(note.note_head, step, spell="flat")
        >>> staff = abjad.Staff([note])
        >>> score = abjad.Score([staff])
        >>> moment = "#(ly:make-moment 1 25)"
        >>> abjad.setting(score).proportional_notation_duration = moment
        >>> lilypond_file = abjad.LilyPondFile(
        ...     items=[
        ...         "#(set-default-paper-size \"a4\" \'portrait)",
        ...         r"#(set-global-staff-size 16)",
        ...         "\\include \'Users/gregoryevans/abjad/docs/source/_stylesheets/abjad.ily\'",
        ...         "\\include \'all-edo-markups-example.ily\'",
        ...         score,
        ...         abjad.Block(name="layout"),
        ...     ],
        ... )
        >>> style = '"dodecaphonic"'
        >>> lilypond_file["layout"].items.append(fr"\accidentalStyle {style}")
        >>> abjad.show(lilypond_file) # doctest: +SKIP

        ..  docs::

            >>> print(abjad.lilypond(staff))
            \new Staff
            {
                \tweak Accidental.stencil #ly:text-interface::print
                \tweak Accidental.text \one-quarter-flat-markup
                df'4
            }

    """
    value = quicktions.Fraction(value)
    pitch = note_head.written_pitch
    bundle = get_alteration(pitch, value, spell)
    note_head.written_pitch = bundle.pitch
    string = r"#ly:text-interface::print"
    abjad.tweak(note_head, literal=True).Accidental.stencil = string
    abjad.tweak(note_head, literal=True).Accidental.text = bundle.accidental_string
