from fractions import Fraction

import abjad


class HEJIVector:
    """
    HEJI vector.

    >>> from abjadext import microtones

    >>> vector = microtones.HEJIVector(syntonic_commas_down=2)
    >>> vector.syntonic_commas_down
    2

    >>> vector = microtones.HEJIVector(syntonic_commas_down=2)
    >>> vector.syntonic_commas_up
    0

    """

    def __init__(
        self,
        diatonic_accidental="natural",
        syntonic_commas_down=0,
        syntonic_commas_up=0,
        septimal_commas_down=0,
        septimal_commas_up=0,
        undecimal_quarter_tones_down=0,
        undecimal_quarter_tones_up=0,
        tridecimal_third_tones_down=0,
        tridecimal_third_tones_up=0,
        seventeen_limit_skhismas_down=0,
        seventeen_limit_skhismas_up=0,
        nineteen_limit_skhismas_down=0,
        nineteen_limit_skhismas_up=0,
        twenty_three_limit_commas_down=0,
        twenty_three_limit_commas_up=0,
    ):
        self.diatonic_accidental = diatonic_accidental
        self.syntonic_commas_down = syntonic_commas_down
        self.syntonic_commas_up = syntonic_commas_up
        self.septimal_commas_down = septimal_commas_down
        self.septimal_commas_up = septimal_commas_up
        self.undecimal_quarter_tones_down = undecimal_quarter_tones_down
        self.undecimal_quarter_tones_up = undecimal_quarter_tones_up
        self.tridecimal_third_tones_down = tridecimal_third_tones_down
        self.tridecimal_third_tones_up = tridecimal_third_tones_up
        self.seventeen_limit_skhismas_down = seventeen_limit_skhismas_down
        self.seventeen_limit_skhismas_up = seventeen_limit_skhismas_up
        self.nineteen_limit_skhismas_down = nineteen_limit_skhismas_down
        self.nineteen_limit_skhismas_up = nineteen_limit_skhismas_up
        self.twenty_three_limit_commas_down = twenty_three_limit_commas_down
        self.twenty_three_limit_commas_up = twenty_three_limit_commas_up

    def __repr__(self):
        """
        Gets interpreter representation.

        >>> microtones.HEJIVector()
        HEJIVector(
                diatonic_accidental="natural",
                syntonic_commas_down=0,
                syntonic_commas_up=0,
                septimal_commas_down=0,
                septimal_commas_up=0,
                undecimal_quarter_tones_down=0,
                undecimal_quarter_tones_up=0,
                tridecimal_third_tones_down=0,
                tridecimal_third_tones_up=0,
                seventeen_limit_skhismas_down=0,
                seventeen_limit_skhismas_up=0,
                nineteen_limit_skhismas_down=0,
                nineteen_limit_skhismas_up=0,
                twenty_three_limit_commas_down=0,
                twenty_three_limit_commas_up=0,
                )

        """

        return f"""HEJIVector(
        diatonic_accidental="{self.diatonic_accidental}",
        syntonic_commas_down={self.syntonic_commas_down},
        syntonic_commas_up={self.syntonic_commas_up},
        septimal_commas_down={self.septimal_commas_down},
        septimal_commas_up={self.septimal_commas_up},
        undecimal_quarter_tones_down={self.undecimal_quarter_tones_down},
        undecimal_quarter_tones_up={self.undecimal_quarter_tones_up},
        tridecimal_third_tones_down={self.tridecimal_third_tones_down},
        tridecimal_third_tones_up={self.tridecimal_third_tones_up},
        seventeen_limit_skhismas_down={self.seventeen_limit_skhismas_down},
        seventeen_limit_skhismas_up={self.seventeen_limit_skhismas_up},
        nineteen_limit_skhismas_down={self.nineteen_limit_skhismas_down},
        nineteen_limit_skhismas_up={self.nineteen_limit_skhismas_up},
        twenty_three_limit_commas_down={self.twenty_three_limit_commas_down},
        twenty_three_limit_commas_up={self.twenty_three_limit_commas_up},
        )"""

    def has_just_accidentals(self):
        """
        Returns boolean.

        >>> vector = microtones.HEJIVector()
        >>> vector.has_just_accidentals()
        False

        >>> vector = microtones.HEJIVector(syntonic_commas_down=1)
        >>> vector.has_just_accidentals()
        True

        """

        if self.syntonic_commas_down > 0:
            return True
        elif self.syntonic_commas_up > 0:
            return True
        elif self.septimal_commas_down > 0:
            return True
        elif self.septimal_commas_up > 0:
            return True
        elif self.undecimal_quarter_tones_down > 0:
            return True
        elif self.undecimal_quarter_tones_up > 0:
            return True
        elif self.tridecimal_third_tones_down > 0:
            return True
        elif self.tridecimal_third_tones_up > 0:
            return True
        elif self.seventeen_limit_skhismas_down > 0:
            return True
        elif self.seventeen_limit_skhismas_up > 0:
            return True
        elif self.nineteen_limit_skhismas_down > 0:
            return True
        elif self.nineteen_limit_skhismas_up > 0:
            return True
        elif self.twenty_three_limit_commas_down > 0:
            return True
        elif self.twenty_three_limit_commas_up > 0:
            return True
        else:
            return False

    def calculate_heji_accidental(self):
        r"""
        Returns markup.

        >>> vector = microtones.HEJIVector(syntonic_commas_down=1)
        >>> abjad.f(vector.calculate_heji_accidental())
        \markup {
            \concat
                {
                    \forced-natural-one-syntonic-comma-down
                }
            }

        """

        int_to_word = {"1": "one", "2": "two", "3": "three"}
        accumulated_accidentals = []
        if self.diatonic_accidental == "double sharp":
            self.diatonic_accidental = "double-sharp"
        if self.diatonic_accidental == "double flat":
            self.diatonic_accidental = "double-flat"
        if self.syntonic_commas_down == self.syntonic_commas_up:
            self.syntonic_commas_down = 0
            self.syntonic_commas_up = 0
            accumulated_accidentals.append(fr"\forced-{self.diatonic_accidental}")
        elif self.syntonic_commas_down > self.syntonic_commas_up:
            self.syntonic_commas_down = (
                self.syntonic_commas_down - self.syntonic_commas_up
            )
            self.syntonic_commas_up = 0
            accumulated_accidentals.append(
                fr"\forced-{self.diatonic_accidental}-{int_to_word[str(self.syntonic_commas_down)]}-syntonic-comma-down"
            )
        else:
            self.syntonic_commas_up = (
                self.syntonic_commas_up - self.syntonic_commas_down
            )
            self.syntonic_commas_down = 0
            accumulated_accidentals.append(
                fr"\forced-{self.diatonic_accidental}-{int_to_word[str(self.syntonic_commas_up)]}-syntonic-comma-up"
            )
        if self.septimal_commas_down == self.septimal_commas_up:
            self.septimal_commas_down = 0
            self.septimal_commas_up = 0
        elif self.septimal_commas_down > self.septimal_commas_up:
            self.septimal_commas_down = (
                self.septimal_commas_down - self.septimal_commas_up
            )
            self.septimal_commas_up = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.septimal_commas_down)]}-septimal-comma-down"
            )
        else:
            self.septimal_commas_up = (
                self.septimal_commas_up - self.septimal_commas_down
            )
            self.septimal_commas_down = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.septimal_commas_up)]}-septimal-comma-up"
            )
        if self.undecimal_quarter_tones_down == self.undecimal_quarter_tones_up:
            self.undecimal_quarter_tones_down = 0
            self.undecimal_quarter_tones_up = 0
        elif self.undecimal_quarter_tones_down > self.undecimal_quarter_tones_up:
            self.undecimal_quarter_tones_down = (
                self.undecimal_quarter_tones_down - self.undecimal_quarter_tones_up
            )
            self.undecimal_quarter_tones_up = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.undecimal_quarter_tones_down)]}-undecimal-quarter-tone-down"
            )
        else:
            self.undecimal_quarter_tones_up = (
                self.undecimal_quarter_tones_up - self.undecimal_quarter_tones_down
            )
            self.undecimal_quarter_tones_down = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.undecimal_quarter_tones_up)]}-undecimal-quarter-tone-up"
            )
        if self.tridecimal_third_tones_down == self.tridecimal_third_tones_up:
            self.tridecimal_third_tones_down = 0
            self.tridecimal_third_tones_up = 0
        elif self.tridecimal_third_tones_down > self.tridecimal_third_tones_up:
            self.tridecimal_third_tones_down = (
                self.tridecimal_third_tones_down - self.tridecimal_third_tones_up
            )
            self.tridecimal_third_tones_up = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.tridecimal_third_tones_down)]}-tridecimal-third-tone-down"
            )
        else:
            self.tridecimal_third_tones_up = (
                self.tridecimal_third_tones_up - self.tridecimal_third_tones_down
            )
            self.tridecimal_third_tones_down = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.tridecimal_third_tones_up)]}-tridecimal-third-tone-up"
            )
        if self.seventeen_limit_skhismas_down == self.seventeen_limit_skhismas_up:
            self.seventeen_limit_skhismas_down = 0
            self.seventeen_limit_skhismas_up = 0
        elif self.seventeen_limit_skhismas_down > self.seventeen_limit_skhismas_up:
            self.seventeen_limit_skhismas_down = (
                self.seventeen_limit_skhismas_down - self.seventeen_limit_skhismas_up
            )
            self.seventeen_limit_skhismas_up = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.seventeen_limit_skhismas_down)]}-seventeen-limit-skhisma-down"
            )
        else:
            self.seventeen_limit_skhismas_up = (
                self.seventeen_limit_skhismas_up - self.seventeen_limit_skhismas_down
            )
            self.seventeen_limit_skhismas_down = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.seventeen_limit_skhismas_up)]}-seventeen-limit-skhisma-up"
            )
        if self.nineteen_limit_skhismas_down == self.nineteen_limit_skhismas_up:
            self.nineteen_limit_skhismas_down = 0
            self.nineteen_limit_skhismas_up = 0
        elif self.nineteen_limit_skhismas_down > self.nineteen_limit_skhismas_up:
            self.nineteen_limit_skhismas_down = (
                self.nineteen_limit_skhismas_down - self.nineteen_limit_skhismas_up
            )
            self.nineteen_limit_skhismas_up = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.nineteen_limit_skhismas_down)]}-nineteen-limit-skhisma-down"
            )
        else:
            self.nineteen_limit_skhismas_up = (
                self.nineteen_limit_skhismas_up - self.nineteen_limit_skhismas_down
            )
            self.nineteen_limit_skhismas_down = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.nineteen_limit_skhismas_up)]}-nineteen-limit-skhisma-up"
            )
        if self.twenty_three_limit_commas_down == self.twenty_three_limit_commas_up:
            self.twenty_three_limit_commas_down = 0
            self.twenty_three_limit_commas_up = 0
        elif self.twenty_three_limit_commas_down > self.twenty_three_limit_commas_up:
            self.twenty_three_limit_commas_down = (
                self.twenty_three_limit_commas_down - self.twenty_three_limit_commas_up
            )
            self.twenty_three_limit_commas_up = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.twenty_three_limit_commas_down)]}-twenty-three-limit-comma-down"
            )
        else:
            self.twenty_three_limit_commas_up = (
                self.twenty_three_limit_commas_up - self.twenty_three_limit_commas_down
            )
            self.twenty_three_limit_commas_down = 0
            accumulated_accidentals.append(
                fr"\{int_to_word[str(self.twenty_three_limit_commas_up)]}-twenty-three-limit-comma-up"
            )
        if len(accumulated_accidentals) > 0:
            accumulated_accidentals.reverse()
            if accumulated_accidentals[-1] == r"\forced-natural":
                if self.has_just_accidentals():
                    accumulated_accidentals = [_ for _ in accumulated_accidentals[:-1]]
            literal_components = []
            for accidental_string in accumulated_accidentals:
                accidental_string = accidental_string + " "
                literal_components.append(accidental_string)
            literal = abjad.Markup(literal=True).concat(literal_components)
        else:
            literal = abjad.Markup(
                fr"  \forced-{self.diatonic_accidental}", literal=True
            )
        self.accidental_literal = literal
        return literal


class JIBundle:
    r"""
    JI bundle.

    >>> bundle = microtones.JIBundle()
    >>> bundle.pitch
    "c'"

    >>> bundle.vector
    HEJIVector(
            diatonic_accidental="natural",
            syntonic_commas_down=0,
            syntonic_commas_up=0,
            septimal_commas_down=0,
            septimal_commas_up=0,
            undecimal_quarter_tones_down=0,
            undecimal_quarter_tones_up=0,
            tridecimal_third_tones_down=0,
            tridecimal_third_tones_up=0,
            seventeen_limit_skhismas_down=0,
            seventeen_limit_skhismas_up=0,
            nineteen_limit_skhismas_down=0,
            nineteen_limit_skhismas_up=0,
            twenty_three_limit_commas_down=0,
            twenty_three_limit_commas_up=0,
            )

    """

    def __init__(self, pitch="c'", vector=HEJIVector()):
        self.pitch = pitch
        self.vector = vector

    def __repr__(self):
        """
        Gets interpreter representation.

        >>> microtones.JIBundle()
        JIBundle(
                pitch=c',
                vector=HEJIVector(
                diatonic_accidental="natural",
                syntonic_commas_down=0,
                syntonic_commas_up=0,
                septimal_commas_down=0,
                septimal_commas_up=0,
                undecimal_quarter_tones_down=0,
                undecimal_quarter_tones_up=0,
                tridecimal_third_tones_down=0,
                tridecimal_third_tones_up=0,
                seventeen_limit_skhismas_down=0,
                seventeen_limit_skhismas_up=0,
                nineteen_limit_skhismas_down=0,
                nineteen_limit_skhismas_up=0,
                twenty_three_limit_commas_down=0,
                twenty_three_limit_commas_up=0,
                ),
                )

        """

        return f"""JIBundle(
        pitch={self.pitch},
        vector={self.vector},
        )"""


def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def prime_factors(n):
    prime_factor_list = []
    while not n % 2:
        prime_factor_list.append(2)
        n //= 2
    while not n % 3:
        prime_factor_list.append(3)
        n //= 3
    i = 5
    while n != 1:
        if is_prime(i):
            while not n % i:
                prime_factor_list.append(i)
                n //= i
        i += 2
    return prime_factor_list


def ratio_to_pc(pitch, ratio):
    r"""
    Returns JI bundle.

    >>> bundle = microtones.ratio_to_pc(abjad.NamedPitch("c'"), "3/2")
    >>> bundle.pitch
    NamedPitch("g'")

    >>> bundle.vector
    HEJIVector(
            diatonic_accidental="natural",
            syntonic_commas_down=0,
            syntonic_commas_up=0,
            septimal_commas_down=0,
            septimal_commas_up=0,
            undecimal_quarter_tones_down=0,
            undecimal_quarter_tones_up=0,
            tridecimal_third_tones_down=0,
            tridecimal_third_tones_up=0,
            seventeen_limit_skhismas_down=0,
            seventeen_limit_skhismas_up=0,
            nineteen_limit_skhismas_down=0,
            nineteen_limit_skhismas_up=0,
            twenty_three_limit_commas_down=0,
            twenty_three_limit_commas_up=0,
            )

    """

    if isinstance(pitch, str):
        pitch = abjad.NamedPitch(pitch)
    elif isinstance(pitch, int):
        pitch = abjad.NumberedPitch(pitch)
    else:
        pitch = pitch
    ratio = Fraction(ratio)
    numerator_factors = prime_factors(ratio.numerator)
    denominator_factors = prime_factors(ratio.denominator)
    accidental_vector = HEJIVector(diatonic_accidental=pitch.accidental.name)
    for prime in numerator_factors:
        if prime == 2:
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
        elif prime == 3:
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P5").transpose(pitch)
        elif prime == 5:
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+M3").transpose(pitch)
            accidental_vector.syntonic_commas_down += 1
        elif prime == 7:
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+m7").transpose(pitch)
            accidental_vector.septimal_commas_down += 1
        elif prime == 11:
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P4").transpose(pitch)
            accidental_vector.undecimal_quarter_tones_up += 1
        elif prime == 13:
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+M6").transpose(pitch)
            accidental_vector.tridecimal_third_tones_down += 1
        elif prime == 17:
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+m2").transpose(pitch)
            accidental_vector.syntonic_commas_up += 1
            accidental_vector.seventeen_limit_skhismas_down += 1
        elif prime == 19:
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+m3").transpose(pitch)
            accidental_vector.nineteen_limit_skhismas_up += 1
        elif prime == 23:
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+P8").transpose(pitch)
            pitch = abjad.NamedInterval("+A4").transpose(pitch)
            accidental_vector.twenty_three_limit_commas_up += 1
        else:
            print("REDUCE RATIO")
            print("cannot calculate beyond 23-limit JI")
            assert prime < 23
    for prime in denominator_factors:
        if prime == 2:
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
        elif prime == 3:
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P5").transpose(pitch)
        elif prime == 5:
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-M3").transpose(pitch)
            accidental_vector.syntonic_commas_up += 1
        elif prime == 7:
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-m7").transpose(pitch)
            accidental_vector.septimal_commas_up += 1
        elif prime == 11:
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P4").transpose(pitch)
            accidental_vector.undecimal_quarter_tones_down += 1
        elif prime == 13:
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-M6").transpose(pitch)
            accidental_vector.tridecimal_third_tones_up += 1
        elif prime == 17:
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-m2").transpose(pitch)
            accidental_vector.syntonic_commas_down += 1
            accidental_vector.seventeen_limit_skhismas_up += 1
        elif prime == 19:
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-m3").transpose(pitch)
            accidental_vector.nineteen_limit_skhismas_down += 1
        elif prime == 23:
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-P8").transpose(pitch)
            pitch = abjad.NamedInterval("-A4").transpose(pitch)
            accidental_vector.twenty_three_limit_commas_down += 1
        else:
            print("REDUCE RATIO")
            print("cannot calculate beyond 23-limit JI")
            assert prime < 23
    accidental_vector.diatonic_accidental = pitch.accidental.name
    return JIBundle(pitch, accidental_vector)


def tune_to_ratio(note_head, ratio, add_accidental=True, tempered=False):
    r"""
    Transposes noteheads in place and tweaks accidental stencil.

    >>> note = abjad.Note()
    >>> microtones.tune_to_ratio(note.note_head, "3/1")
    >>> abjad.f(note)
    \tweak Accidental.stencil #ly:text-interface::print
    \tweak Accidental.text \markup {
        \concat {
                \forced-natural
            }
        }
    g''4

    >>> note = abjad.Note()
    >>> microtones.tune_to_ratio(note.note_head, "5/1")
    >>> abjad.f(note)
    \tweak Accidental.stencil #ly:text-interface::print
    \tweak Accidental.text \markup {
        \concat {
                \forced-natural-one-syntonic-comma-down
            }
        }
    e'''4

    >>> note = abjad.Note()
    >>> microtones.tune_to_ratio(note.note_head, "5/1", add_accidental=False)
    >>> abjad.f(note)
    e'''4

    >>> ratios = [f"{_ + 1}/1" for _ in range(11)]
    >>> notes = [abjad.Note("a,,,32") for _ in ratios]
    >>> for note, ratio in zip(notes, ratios):
    ...     microtones.tune_to_ratio(note.note_head, ratio)
    >>> staff = abjad.Staff(notes)
    >>> abjad.f(staff)
    \new Staff
    {
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \forced-natural
                }
            }
        a,,,32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \forced-natural
                }
            }
        a,,32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \forced-natural
                }
            }
        e,32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \forced-natural
                }
            }
        a,32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \forced-sharp-one-syntonic-comma-down
                }
            }
        cs32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \forced-natural
                }
            }
        e32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \one-septimal-comma-down
                }
            }
        g32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \forced-natural
                }
            }
        a32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \forced-natural
                }
            }
        b32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \forced-sharp-one-syntonic-comma-down
                }
            }
        cs'32
        \tweak Accidental.stencil #ly:text-interface::print
        \tweak Accidental.text \markup {
            \concat
                {
                    \one-undecimal-quarter-tone-up
                }
            }
        d'32
    }

    >>> note = abjad.Note("c'4")
    >>> microtones.tune_to_ratio(note.note_head, "5/1", tempered=True)
    >>> abjad.f(note)
    \tweak Accidental.stencil #ly:text-interface::print
    \tweak Accidental.text \tempered-natural
    e'''4

    >>> note = abjad.Note("cqs'4")
    >>> microtones.tune_to_ratio(note.note_head, "tempered")
    >>> abjad.f(note)
    \tweak Accidental.stencil #ly:text-interface::print
    \tweak Accidental.text \tempered-quarter-sharp
    cqs'4

    """

    if ratio == "tempered":
        tempered_accidental = note_head.written_pitch.accidental.name
        if tempered_accidental == "quarter sharp":
            tempered_accidental = "quarter-sharp"
        elif tempered_accidental == "quarter flat":
            tempered_accidental = "quarter-flat"
        elif tempered_accidental == "three-quarters sharp":
            tempered_accidental = "three-quarters-sharp"
        elif tempered_accidental == "three-quarters flat":
            tempered_accidental = "three-quarters-flat"
        elif tempered_accidental == "double sharp":
            tempered_accidental = "double-sharp"
        elif tempered_accidental == "double flat":
            tempered_accidental = "double-flat"
        abjad.tweak(
            note_head, literal=True
        ).Accidental.stencil = r"#ly:text-interface::print"
        abjad.tweak(
            note_head, literal=True
        ).Accidental.text = fr"\tempered-{tempered_accidental}"
    else:
        bundle = ratio_to_pc(note_head.written_pitch, ratio)
        note_head.written_pitch = bundle.pitch
        if add_accidental is True:
            if tempered is True:
                tempered_accidental = note_head.written_pitch.accidental.name
                if tempered_accidental == "quarter sharp":
                    tempered_accidental = "quarter-sharp"
                elif tempered_accidental == "quarter flat":
                    tempered_accidental = "quarter-flat"
                elif tempered_accidental == "three-quarters sharp":
                    tempered_accidental = "three-quarters-sharp"
                elif tempered_accidental == "three-quarters flat":
                    tempered_accidental = "three-quarters-flat"
                elif tempered_accidental == "double sharp":
                    tempered_accidental = "double-sharp"
                elif tempered_accidental == "double flat":
                    tempered_accidental = "double-flat"
                abjad.tweak(
                    note_head, literal=True
                ).Accidental.stencil = r"#ly:text-interface::print"
                abjad.tweak(
                    note_head, literal=True
                ).Accidental.text = fr"\tempered-{tempered_accidental}"
            else:
                markup = bundle.vector.calculate_heji_accidental()
                abjad.tweak(
                    note_head, literal=True
                ).Accidental.stencil = r"#ly:text-interface::print"
                alteration_literal = markup
                abjad.tweak(
                    note_head, literal=False
                ).Accidental.text = alteration_literal
