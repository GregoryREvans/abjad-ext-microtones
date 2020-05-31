from fractions import Fraction

import abjad


class HEJIVector:
    r"""
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
        return "HEJIVector()"

    def __str__(self):
        return f"{self.diatonic_accidental} + {self.calculate_heji_accidental()}"

    def has_just_accidentals(self):
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
            literal_string_start = [
                r"\once \override Voice.Accidental.stencil =",
                r"       #ly:text-interface::print",
                r"       \once \override Voice.Accidental.text =",
                r"           \markup {",
                r"               \concat {",
            ]
            literal_string_stop = ["               }", "           }"]
            literal_components = []
            for literal_string in literal_string_start:
                literal_components.append(literal_string)
            for accidental_string in accumulated_accidentals:
                accidental_string = "                   " + accidental_string
                literal_components.append(accidental_string)
            for literal_string in literal_string_stop:
                literal_components.append(literal_string)
            literal = abjad.LilyPondLiteral(literal_components, format_slot="before")
        else:
            literal = abjad.LilyPondLiteral(
                fr"\forced-{self.diatonic_accidental}", format_slot="before"
            )
        self.accidental_literal = literal
        return literal


class JIBundle:
    def __init__(self, pitch="c'", vector=HEJIVector()):
        self.pitch = pitch
        self.vector = vector

    def __repr__(self):
        return "JIBundle()"

    def __str__(self):
        return f"{self.pitch} + {self.vector.calculate_heji_accidental()}"


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
    return JIBundle(pitch, accidental_vector.calculate_heji_accidental())


def tune_to_ratio(note, ratio):
    r"""
    >>> import abjad
    >>> from abjadext import microtones
    >>> note = abjad.Note()
    >>> microtones.tune_to_ratio(note, "3/1")
    >>> abjad.f(note)
    \once \override Voice.Accidental.stencil =
           #ly:text-interface::print
           \once \override Voice.Accidental.text =
               \markup {
                   \concat {
                       \forced-natural
                   }
               }
    g''4

    >>> microtones.tune_to_ratio(note, "3/2")
    >>> abjad.f(note)
    \once \override Voice.Accidental.stencil =
           #ly:text-interface::print
           \once \override Voice.Accidental.text =
               \markup {
                   \concat {
                       \forced-natural
                   }
               }
    \once \override Voice.Accidental.stencil =
           #ly:text-interface::print
           \once \override Voice.Accidental.text =
               \markup {
                   \concat {
                       \forced-natural
                   }
               }
    d'''4

    """
    selection = abjad.select(note).leaves()
    for note in selection:
        if abjad.inspect(note).annotation("ratio added") is not None:
            ratio = Fraction(abjad.inspect(note).annotation("ratio added")) * Fraction(
                ratio
            )
            note.written_pitch = abjad.inspect(note).annotation("fundamental")
        abjad.annotate(note, "fundamental", f"{note.written_pitch}")
        abjad.annotate(note, "ratio added", f"{ratio}")
        bundle = ratio_to_pc(note.written_pitch, ratio)
        note.written_pitch = bundle.pitch
    alteration_literal = bundle.vector
    abjad.attach(alteration_literal, selection[0])

### LILY STUFF ###
# ITERATE NOTEHEADS AND USE TWEAKS
# \version "2.19.84"  % necessary for upgrading to future LilyPond versions.
# \language "english"
#
# \layout{\accidentalStyle "dodecaphonic"}
#
# \new Score {
# 	\new Staff{
# 		<
# 			\tweak Accidental.stencil #ly:text-interface::print
# 			\tweak Accidental.text \markup{\musicglyph #"accidentals.natural"}
# 			cs'
# 			\tweak Accidental.stencil #ly:text-interface::print
# 			\tweak Accidental.text \markup{\musicglyph #"accidentals.natural"}
# 			fs'
# 			\tweak Accidental.stencil #ly:text-interface::print
# 			\tweak Accidental.text \markup{\musicglyph #"accidentals.sharp"}
# 			g'
# 		>1
# 	}
# }
