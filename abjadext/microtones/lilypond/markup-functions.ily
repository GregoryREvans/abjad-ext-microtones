#(define-markup-command
    (heji-accidental-markup layout props point-code)
    (number?)
    (interpret-markup layout props
    #{
    \markup
    \fontsize #5
    \override #(cons 'font-name font-name)
    \char #point-code
    #}))

#(define-markup-command
    (heji-double-accidental-markup layout props point-code1 point-code2 kern)
    (number? number? number?)
    (interpret-markup layout props
    #{
    \markup
    \fontsize #5
    \override #(cons 'font-name font-name)
    \concat {
    \char #point-code1
    \hspace #kern
    \char #point-code2
    }
    #}))

#(define-markup-command
    (heji-triple-accidental-markup layout props point-code kern)
    (number? number?)
    (interpret-markup layout props
    #{
    \markup
    \fontsize #5
    \override #(cons 'font-name font-name)
    \concat {
    \char #point-code
    \hspace #kern
    \char #point-code
    \hspace #kern
    \char #point-code
    }
    #}))

#(define-markup-command
    (letter-heji-accidental-markup layout props letter)
    (string?)
    (interpret-markup layout props
    #{
    \markup
    \fontsize #5
    \override #(cons 'font-name font-name)
    #letter
    #}))


% diatonic accidentals %
forced-natural = \markup \heji-accidental-markup ##x266e
forced-sharp = \markup \heji-accidental-markup ##xe262
forced-flat = \markup \heji-accidental-markup##xe260
forced-double-sharp = \markup \heji-accidental-markup ##xe263
forced-double-flat = \markup \heji-accidental-markup ##xe264


% natural syntonic commas %
forced-natural-one-syntonic-comma-down = \markup \heji-accidental-markup ##xe2c2
forced-natural-two-syntonic-comma-down = \markup \heji-accidental-markup ##xe2cc
forced-natural-three-syntonic-comma-down = \markup \heji-accidental-markup ##xe2d6
forced-natural-one-syntonic-comma-up = \markup \heji-accidental-markup ##xe2c7
forced-natural-two-syntonic-comma-up = \markup \heji-accidental-markup ##xe2d1
forced-natural-three-syntonic-comma-up = \markup \heji-accidental-markup ##xe2db
% sharp syntonic commas %
forced-sharp-one-syntonic-comma-down = \markup \heji-accidental-markup ##xe2c3
forced-sharp-two-syntonic-comma-down = \markup \heji-accidental-markup ##xe2cd
forced-sharp-three-syntonic-comma-down = \markup \heji-accidental-markup ##xe2d7
forced-sharp-one-syntonic-comma-up = \markup \heji-accidental-markup ##xe2c8
forced-sharp-two-syntonic-comma-up = \markup \heji-accidental-markup ##xe2d2
forced-sharp-three-syntonic-comma-up = \markup \heji-accidental-markup ##xe2dc
% flat syntonic commas %
forced-flat-one-syntonic-comma-down = \markup \heji-accidental-markup ##xe2c1
forced-flat-two-syntonic-comma-down = \markup \heji-accidental-markup ##xe2cb
forced-flat-three-syntonic-comma-down = \markup \heji-accidental-markup ##xe2d5
forced-flat-one-syntonic-comma-up = \markup \heji-accidental-markup ##xe2c6
forced-flat-two-syntonic-comma-up = \markup \heji-accidental-markup ##xe2d0
forced-flat-three-syntonic-comma-up = \markup \heji-accidental-markup ##xe2da
% double sharp syntonic commas %
forced-double-sharp-one-syntonic-comma-down = \markup \heji-accidental-markup ##xe2c4
forced-double-sharp-two-syntonic-comma-down = \markup \heji-accidental-markup ##xe2ce
forced-double-sharp-three-syntonic-comma-down = \markup \heji-accidental-markup ##xe2d8
forced-double-sharp-one-syntonic-comma-up = \markup \heji-accidental-markup ##xe2c9
forced-double-sharp-two-syntonic-comma-up = \markup \heji-accidental-markup ##xe2d3
forced-double-sharp-three-syntonic-comma-up = \markup \heji-accidental-markup ##xe2dd
% double flat syntonic commas %
forced-double-flat-one-syntonic-comma-down = \markup \heji-accidental-markup ##xe2c0
forced-double-flat-two-syntonic-comma-down = \markup \heji-accidental-markup ##xe2ca
forced-double-flat-three-syntonic-comma-down = \markup \heji-accidental-markup ##xe2d4
forced-double-flat-one-syntonic-comma-up = \markup \heji-accidental-markup ##xe2c5
forced-double-flat-two-syntonic-comma-up = \markup \heji-accidental-markup ##xe2cf
forced-double-flat-three-syntonic-comma-up = \markup \heji-accidental-markup ##xe2d9


% septimal commas %
one-septimal-comma-down = \markup \heji-accidental-markup ##xe2de
two-septimal-comma-down = \markup \heji-accidental-markup ##xe2e0
three-septimal-comma-down = \markup \heji-double-accidental-markup ##xe2de ##xe2e0 #0.125
one-septimal-comma-up = \markup \heji-accidental-markup ##xe2df
two-septimal-comma-up = \markup \heji-accidental-markup ##xe2e1
three-septimal-comma-up = \markup \heji-double-accidental-markup ##xe2df ##xe2e1 #0.125


% undecimal quarter tones %
one-undecimal-quarter-tone-down = \markup \heji-accidental-markup ##xe2e2
two-undecimal-quarter-tone-down = \markup \heji-double-accidental-markup ##xe2e2 ##xe2e2 #0.035
three-undecimal-quarter-tone-down = \markup \heji-triple-accidental-markup ##xe2e2 #0.035

one-undecimal-quarter-tone-up = \markup \heji-accidental-markup ##xe2e3
two-undecimal-quarter-tone-up = \markup \heji-double-accidental-markup ##xe2e3 ##xe2e3 #0.125
three-undecimal-quarter-tone-up = \markup \heji-triple-accidental-markup ##xe2e3 #0.125


% tridecimal third tones %
one-tridecimal-third-tone-down = \markup \heji-accidental-markup ##xe2e4
two-tridecimal-third-tone-down = \markup \heji-double-accidental-markup ##xe2e4 ##xe2e4 #0.035
three-tridecimal-third-tone-down = \markup \heji-triple-accidental-markup ##xe2e4 #0.035
one-tridecimal-third-tone-up = \markup \heji-accidental-markup ##xe2e5
two-tridecimal-third-tone-up = \markup \heji-double-accidental-markup ##xe2e5 ##xe2e5 #0.125
three-tridecimal-third-tone-up = \markup \heji-triple-accidental-markup ##xe2e5 #0.125


% seventeen-limit skhismas %
one-seventeen-limit-skhisma-down = \markup \heji-accidental-markup ##xe2e6
two-seventeen-limit-skhisma-down = \markup \heji-double-accidental-markup ##xe2e6 ##xe2e6 #0.125
three-seventeen-limit-skhisma-down = \markup \heji-triple-accidental-markup ##xe2e6 #0.125
one-seventeen-limit-skhisma-up = \markup \heji-accidental-markup ##xe2e7
two-seventeen-limit-skhisma-up = \markup \heji-double-accidental-markup ##xe2e7 ##xe2e7 #0.125
three-seventeen-limit-skhisma-up = \markup \heji-triple-accidental-markup ##xe2e7 #0.125


% nineteen-limit skhismas %
one-nineteen-limit-skhisma-down = \markup \heji-accidental-markup ##xe2e8
two-nineteen-limit-skhisma-down = \markup \heji-double-accidental-markup ##xe2e8 ##xe2e8 #0.125
three-nineteen-limit-skhisma-down = \markup \heji-triple-accidental-markup ##xe2e8 #0.125
one-nineteen-limit-skhisma-up = \markup \heji-accidental-markup ##xe2e9
two-nineteen-limit-skhisma-up = \markup \heji-double-accidental-markup ##xe2e9 ##xe2e9 #0.125
three-nineteen-limit-skhisma-up = \markup \heji-triple-accidental-markup ##xe2e9 #0.125


% twenty-three-limit commas %
one-twenty-three-limit-comma-down = \markup \heji-accidental-markup ##xe2eb
two-twenty-three-limit-comma-down = \markup \heji-double-accidental-markup ##xe2eb ##xe2eb #0.125
three-twenty-three-limit-comma-down = \markup \heji-triple-accidental-markup ##xe2eb #0.125
one-twenty-three-limit-comma-up = \markup \heji-accidental-markup ##xe2ea
two-twenty-three-limit-comma-up = \markup \heji-double-accidental-markup ##xe2ea ##xe2ea #0.125
three-twenty-three-limit-comma-up = \markup \heji-triple-accidental-markup ##xe2ea #0.125
