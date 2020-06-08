\version "2.19.84"
\language "english"


%%% one eighth tone up %%%
one-eighth-sharp-markup = \markup {
    \musicglyph #"accidentals.natural"
    \postscript #"gsave
        0.17 setlinewidth
        -1.2 1.25 moveto
        -1.2 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.5 1.4 moveto
        -1.2 2.18 lineto
        -0.9 1.4 lineto
        stroke grestore"
}

%%% three eighth tones up %%%
three-eighths-sharp-markup = \markup {
    \musicglyph #"accidentals.sharp.slashslash.stem"
    \postscript #"gsave
        0.17 setlinewidth
        -0.95 1.25 moveto
        -0.95 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.25 1.4 moveto
        -0.95 2.18 lineto
        -0.65 1.4 lineto
        stroke grestore"
}

%%% five eighth tones up %%%
five-eighths-sharp-markup = \markup {
    \musicglyph #"accidentals.sharp"
    \postscript #"gsave
        0.17 setlinewidth
        -0.91 1.25 moveto
        -0.91 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.21 1.4 moveto
        -0.91 2.18 lineto
        -0.61 1.4 lineto
        stroke grestore"
}

%%% seven eighth tones up %%%
seven-eighths-sharp-markup = \markup {
    \musicglyph #"accidentals.sharp.slashslash.stemstemstem"
    \postscript #"gsave
        0.17 setlinewidth
        -0.95 1.25 moveto
        -0.95 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.25 1.4 moveto
        -0.95 2.18 lineto
        -0.65 1.4 lineto
        stroke grestore"
}

%%% one eighth tone down %%%
one-eighth-flat-markup = \markup {
    \musicglyph #"accidentals.natural"
    \postscript #"gsave
        0.15 setlinewidth
        -0.67 -1.35 moveto
        -0.67 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -0.97 -1.4 moveto
        -0.67 -2.18 lineto
        -0.37 -1.4 lineto
        stroke grestore"
}

%%% three eighth tones down %%%
three-eighths-flat-markup = \markup {
    \musicglyph #"accidentals.mirroredflat"
    \postscript #"gsave
        0.15 setlinewidth
        -0.73 -0.25 moveto
        -0.73 -1.4 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.03 -0.7 moveto
        -0.73 -1.48 lineto
        -0.43 -0.7 lineto
        stroke grestore"
}

%%% five eighth tones down %%%
five-eighths-flat-markup = \markup {
    \musicglyph #"accidentals.flat"
    \postscript #"gsave
        0.15 setlinewidth
        -1.38 -0.25 moveto
        -1.38 -1.4 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.68 -0.7 moveto
        -1.38 -1.48 lineto
        -1.08 -0.7 lineto
        stroke grestore"
}

%%% seven eighth tones down %%%
seven-eighths-flat-markup = \markup {
    \musicglyph #"accidentals.mirroredflat.flat"
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -0.25 moveto
        -1.40 -1.4 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -0.7 moveto
        -1.40 -1.48 lineto
        -1.10 -0.7 lineto
        stroke grestore"
}

%%% one third up %%%
one-third-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 1 3
    \postscript #"gsave
        0.17 setlinewidth
        -0.95 1.25 moveto
        -0.95 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.25 1.4 moveto
        -0.95 2.18 lineto
        -0.65 1.4 lineto
        stroke grestore"
}

%%% two thirds up %%%
two-thirds-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 2 3
    \postscript #"gsave
        0.17 setlinewidth
        -0.95 1.25 moveto
        -0.95 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.25 1.4 moveto
        -0.95 2.18 lineto
        -0.65 1.4 lineto
        stroke grestore"
}

%%% one third down %%%
one-third-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 1 3
    \postscript #"gsave
        0.15 setlinewidth
        -1 -1.35 moveto
        -1 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.30 -1.4 moveto
        -1 -2.18 lineto
        -0.7 -1.4 lineto
        stroke grestore"
}

%%% two thirds down %%%
two-thirds-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 2 3
    \postscript #"gsave
        0.15 setlinewidth
        -1 -1.35 moveto
        -1 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.30 -1.4 moveto
        -1 -2.18 lineto
        -0.7 -1.4 lineto
        stroke grestore"
}

%%% one sixth up %%%
one-sixth-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 1 6
    \postscript #"gsave
        0.17 setlinewidth
        -0.95 1.25 moveto
        -0.95 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.25 1.4 moveto
        -0.95 2.18 lineto
        -0.65 1.4 lineto
        stroke grestore"
}

%%% five sixths up %%%
five-sixths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 5 6
    \postscript #"gsave
        0.17 setlinewidth
        -0.95 1.25 moveto
        -0.95 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.25 1.4 moveto
        -0.95 2.18 lineto
        -0.65 1.4 lineto
        stroke grestore"
}

%%% one sixth down %%%
one-sixth-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 1 6
    \postscript #"gsave
        0.15 setlinewidth
        -1 -1.35 moveto
        -1 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.30 -1.4 moveto
        -1 -2.18 lineto
        -0.7 -1.4 lineto
        stroke grestore"
}

%%% five sixths down %%%
five-sixths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 5 6
    \postscript #"gsave
        0.15 setlinewidth
        -1 -1.35 moveto
        -1 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.30 -1.4 moveto
        -1 -2.18 lineto
        -0.7 -1.4 lineto
        stroke grestore"
}

%%% one twelfth up %%%
one-twelfth-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 1 12
    \postscript #"gsave
        0.17 setlinewidth
        -1.35 1.25 moveto
        -1.35 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.65 1.4 moveto
        -1.35 2.18 lineto
        -1.05 1.4 lineto
        stroke grestore"
}

%%% five twelfths up %%%
five-twelfths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 5 12
    \postscript #"gsave
        0.17 setlinewidth
        -1.35 1.25 moveto
        -1.35 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.65 1.4 moveto
        -1.35 2.18 lineto
        -1.05 1.4 lineto
        stroke grestore"
}

%%% seven twelfths up %%%
seven-twelfths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 7 12
    \postscript #"gsave
        0.17 setlinewidth
        -1.35 1.25 moveto
        -1.35 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.65 1.4 moveto
        -1.35 2.18 lineto
        -1.05 1.4 lineto
        stroke grestore"
}

%%% eleven twelfths up %%%
eleven-twelfths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 11 12
    \postscript #"gsave
        0.17 setlinewidth
        -1.35 1.25 moveto
        -1.35 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.65 1.4 moveto
        -1.35 2.18 lineto
        -1.05 1.4 lineto
        stroke grestore"
}

%%% one twelfth down %%%
one-twelfth-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 1 12
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -1.35 moveto
        -1.40 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -1.4 moveto
        -1.40 -2.18 lineto
        -1.10 -1.4 lineto
        stroke grestore"
}

%%% five twelfths down %%%
five-twelfths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 5 12
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -1.35 moveto
        -1.40 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -1.4 moveto
        -1.40 -2.18 lineto
        -1.10 -1.4 lineto
        stroke grestore"
}

%%% seven twelfths down %%%
seven-twelfths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 7 12
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -1.35 moveto
        -1.40 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -1.4 moveto
        -1.40 -2.18 lineto
        -1.10 -1.4 lineto
        stroke grestore"
}

%%% eleven twelfths down %%%
eleven-twelfths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 11 12
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -1.35 moveto
        -1.40 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -1.4 moveto
        -1.40 -2.18 lineto
        -1.10 -1.4 lineto
        stroke grestore"
}

%%% one fifth up %%%
one-fifth-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 1 5
    \postscript #"gsave
        0.17 setlinewidth
        -1.35 1.25 moveto
        -1.35 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.65 1.4 moveto
        -1.35 2.18 lineto
        -1.05 1.4 lineto
        stroke grestore"
}

%%% two fifths up %%%
two-fifths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 2 5
    \postscript #"gsave
        0.17 setlinewidth
        -1.35 1.25 moveto
        -1.35 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.65 1.4 moveto
        -1.35 2.18 lineto
        -1.05 1.4 lineto
        stroke grestore"
}

%%% three fifths up %%%
three-fifths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 3 5
    \postscript #"gsave
        0.17 setlinewidth
        -1.35 1.25 moveto
        -1.35 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.65 1.4 moveto
        -1.35 2.18 lineto
        -1.05 1.4 lineto
        stroke grestore"
}

%%% four fifths up %%%
four-fifths-sharp-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 4 5
    \postscript #"gsave
        0.17 setlinewidth
        -1.35 1.25 moveto
        -1.35 2 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.65 1.4 moveto
        -1.35 2.18 lineto
        -1.05 1.4 lineto
        stroke grestore"
}

%%% one fifth down %%%
one-fifth-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 1 5
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -1.35 moveto
        -1.40 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -1.4 moveto
        -1.40 -2.18 lineto
        -1.10 -1.4 lineto
        stroke grestore"
}

%%% two fifths down %%%
two-fifths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 2 5
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -1.35 moveto
        -1.40 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -1.4 moveto
        -1.40 -2.18 lineto
        -1.10 -1.4 lineto
        stroke grestore"
}

%%% three fifths down %%%
three-fifths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 3 5
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -1.35 moveto
        -1.40 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -1.4 moveto
        -1.40 -2.18 lineto
        -1.10 -1.4 lineto
        stroke grestore"
}

%%% four fifths down %%%
four-fifths-flat-markup = \markup {
    \fontsize #-4
    \translate #'(0 . -0.5)
    \fraction 3 5
    \postscript #"gsave
        0.15 setlinewidth
        -1.40 -1.35 moveto
        -1.40 -2.1 lineto
        stroke grestore
        gsave
        0.1 setlinewidth
        -1.70 -1.4 moveto
        -1.40 -2.18 lineto
        -1.10 -1.4 lineto
        stroke grestore"
}
