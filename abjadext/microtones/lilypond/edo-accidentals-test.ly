\version "2.19.84"
\language "english"
#(set-default-paper-size "letterlandscape")
#(set-global-staff-size 15)
\include "ekmelos-edo-accidentals.ily"

\layout {
	indent = #1
	ragged-last = ##t
    ragged-right = ##t
	\accidentalStyle "dodecaphonic"
	\override Beam.transparent = ##t
	\override Stem.transparent = ##t
	\override Staff.BarLine.stencil = ##f
	\override Flag.transparent = ##t
	\override Staff.Clef.stencil = ##f
	\override Staff.TimeSignature.stencil = ##f
	\override Staff.StaffSymbol.transparent = ##t
	\override SpacingSpanner.strict-grace-spacing = ##t
	\override SpacingSpanner.uniform-stretching = ##t
	\override SpacingSpanner.strict-note-spacing = ##t
    \override SpacingSpanner.uniform-stretching = ##t
\context {
	\Score
	proportionalNotationDuration = #(ly:make-moment 1 8)
}
}


\new Score {
    <<
        \new Staff {
		\time 3/4
            \new Voice {
                cff'4
				^ \markup {\halign #0 - \fraction 1 1}

				\eleven-twelfths-flat
                ctqf'4
				^ \markup {\halign #0 - \fraction 11 12}

				\seven-eighths-flat
                ctqf'4
				^ \markup {\halign #0 - \fraction 7 8}

				\five-sixths-flat
                ctqf'4
				^ \markup {\halign #0 - \fraction 5 6}

				\three-quarters-flat
                ctqf'4
				^ \markup {\halign #0 - \fraction 3 4}

				\two-thirds-flat
                cf'4
				^ \markup {\halign #0 - \fraction 2 3}

				\five-eighths-flat
                cf'4
				^ \markup {\halign #0 - \fraction 5 8}

				\seven-twelfths-flat
                cf'4
				^ \markup {\halign #0 - \fraction 7 12}

                cf'4
				^ \markup {\halign #0 - \fraction 1 2}

				\five-twelfths-flat
                cqf'4
				^ \markup {\halign #0 - \fraction 5 12}

				\three-eighths-flat
                cqf'4
				^ \markup {\halign #0 - \fraction 3 8}

				\one-third-flat
                cqf'4
				^ \markup {\halign #0 - \fraction 1 3}

				\one-quarter-flat
                cqf'4
				^ \markup {\halign #0 - \fraction 1 4}

				\one-sixth-flat
                c'4
				^ \markup {\halign #0 - \fraction 1 6}

				\one-eighth-flat
                c'4
				^ \markup {\halign #0 - \fraction 1 8}

				\one-twelfth-flat
                c'4
				^ \markup {\halign #0 - \fraction 1 12}

                c'4

				\one-twelfth-sharp
                c'4
				^ \markup {\halign #0 + \fraction 1 12}

				\one-eighth-sharp
                c'4
				^ \markup {\halign #0 + \fraction 1 8}

				\one-sixth-sharp
                c'4
				^ \markup {\halign #0 + \fraction 1 6}

                cqs'4
				^ \markup {\halign #0 + \fraction 1 4}

				\one-third-sharp
                cqs'4
				^ \markup {\halign #0 + \fraction 1 3}

				\three-eighths-sharp
                cqs'4
				^ \markup {\halign #0 + \fraction 3 8}

				\five-twelfths-sharp
                cqs'4
				^ \markup {\halign #0 + \fraction 5 12}

                cs'4
				^ \markup {\halign #0 + \fraction 1 2}

				\seven-twelfths-sharp
                cs'4
				^ \markup {\halign #0 + \fraction 7 12}

				\five-eighths-sharp
                cs'4
				^ \markup {\halign #0 + \fraction 5 8}

				\two-thirds-sharp
                cs'4
				^ \markup {\halign #0 + \fraction 2 3}

                ctqs'4
				^ \markup {\halign #0 + \fraction 3 4}

				\five-sixths-sharp
                ctqs'4
				^ \markup {\halign #0 + \fraction 5 6}

				\seven-eighths-sharp
                ctqs'4
				^ \markup {\halign #0 + \fraction 7 8}

				\eleven-twelfths-sharp
                ctqs'4
				^ \markup {\halign #0 + \fraction 11 12}

                css'4
				^ \markup {\halign #0 + \fraction 1 1}
            }
        }
    >>
}
