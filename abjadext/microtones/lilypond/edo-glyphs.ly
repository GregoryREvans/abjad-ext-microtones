\version "2.19.84"
\language "english"
#(set-default-paper-size "letterportrait")
#(set-global-staff-size 15)
\include "default-edo-accidental-markups.ily"
\include "all-edo-markups-example.ily"


\layout {\accidentalStyle "dodecaphonic"}


\new Score {
    <<
        \new Staff {
		\time 5/4
            \new Voice {
                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \double-flat-markup
                cff'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 1}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \eleven-twelfths-flat-markup
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 11 12}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \seven-eighths-flat-markup
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 7 8}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \five-sixths-flat-markup
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 6}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \four-fifths-flat-markup
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 4 5}
				\break

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \three-quarters-flat-markup
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 4}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \two-thirds-flat-markup
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 2 3}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \five-eighths-flat-markup
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 8}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \three-fifths-flat-markup
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 5}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \seven-twelfths-flat-markup
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 7 12}
				\break

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \flat-markup
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 2}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \five-twelfths-flat-markup
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 12}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \two-fifths-flat-markup
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 2 5}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \three-eighths-flat-markup
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 8}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-third-flat-markup
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 3}
				\break

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-quarter-flat-markup
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 4}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-fifth-flat-markup
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 5}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-sixth-flat-markup
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 6}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-eighth-flat-markup
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 8}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-twelfth-flat-markup
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 12}
				\break

                \tweak Accidental.stencil #ly:text-interface::print
				\time 1/4
				\tweak Accidental.text \natural-markup
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 0 1}
				\break

				\time 5/4
                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-twelfth-sharp-markup
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 12}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-eighth-sharp-markup
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 8}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-sixth-sharp-markup
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 6}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-fifth-sharp-markup
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 5}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-quarter-sharp-markup
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 4}
				\break

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \one-third-sharp-markup
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 3}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \three-eighths-sharp-markup
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 8}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \two-fifths-sharp-markup
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 2 5}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \five-twelfths-sharp-markup
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 12}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \sharp-markup
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 2}
				\break

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \seven-twelfths-sharp-markup
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 7 12}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \three-fifths-sharp-markup
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 5}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \five-eighths-sharp-markup
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 8}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \two-thirds-sharp-markup
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 2 3}
				\break

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \three-quarters-sharp-markup
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 4}
				\break

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \four-fifths-sharp-markup
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 4 5}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \five-sixths-sharp-markup
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 6}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \seven-eighths-sharp-markup
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 7 8}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \eleven-twelfths-sharp-markup
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 11 12}

                \tweak Accidental.stencil #ly:text-interface::print
				\tweak Accidental.text \double-sharp-markup
                css'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 1}
            }
        }
    >>
}
