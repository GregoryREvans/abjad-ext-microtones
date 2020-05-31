from math import modf
from fractions import Fraction

import abjad


class EDOBundle:
    def __init__(
        self, pitch="c'",
        accidental_string=None,
    ):
        self.pitch = pitch
        self.accidental_string = accidental_string

    def __repr__(self):
        return "EDOBundle()"

    def __str__(self):
        return f"{self.pitch} + {self.accidental_string}"

accidental_to_value = {
    "double sharp": 2,
    "three-quarters sharp": Fraction(3/2),
    "sharp": 1,
    "quarter sharp": Fraction(1/2),
    "natural": 0,
    "quarter flat": Fraction(-1/2),
    "flat": -1,
    "three-quarters flat": Fraction(-3/2),
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

def get_accidental_value(pitch):
    accidental = pitch.accidental.name
    accidental_value = accidental_to_value[f"{accidental}"]
    return accidental_value

def get_value_sum(pitch, value):
    value = Fraction(value)
    return get_accidental_value(pitch) + value

def get_alteration(pitch, value):
    print(pitch)
    value = Fraction(value)
    semitones = int(modf(value)[1])
    remainder = Fraction(f - int(modf(f)[1]))
    if semitones > 0:
        for i in range(semitones):
            pitch = abjad.NamedInterval("+m2").transpose(pitch)
    elif semitones < 0:
        for i in range(semitones):
            pitch = abjad.NamedInterval("-m2").transpose(pitch)
    print(pitch)
    transposed_accidental_value = get_value_sum(pitch, remainder)
    new_accidental = value_to_accidental[str(transposed_accidental_value)] + "-markup" # temporary markup
    return EDOBundle(pitch, new_accidental)

def apply_alteration(note_head, value):
    value = Fraction(value)
    pitch = note_head.written_pitch
    bundle = get_alteration(pitch, value)
    literal = abjad.LilyPondLiteral(
        bundle.accidental_string,
        format_slot="before",
    )
    note_head.written_pitch = bundle.pitch
    abjad.tweak(note_head, literal=True).Accidental.stencil = r"#ly::text-interface:print"
    abjad.tweak(note_head, literal=True).Accidental.text = bundle.accidental_string
    # abjad.attach(literal, note_head)

pitch = abjad.NamedPitch("cs'")
print(get_accidental_value(pitch))
print(get_value_sum(pitch, "3/4"))
get_alteration(pitch, "5/4")

note = abjad.Note("c'4")
apply_alteration(note.note_head, "3/4")
abjad.f(note)

# ### NOTES ###
# cannot attach to note-head
# can only tweak note-head
# can only attach leaf

print(
    Fraction(3/4) % Fraction(1, 4)
)
