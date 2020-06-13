\version "2.19.84"
\language "english"
#(set-default-paper-size "letterportrait")
#(set-global-staff-size 15)
\include "ekmelos-edo-accidentals.ily"

#(define (Text_align_engraver ctx)
  (let ((scripts '())
        (note-column #f))
    (make-engraver
     (acknowledgers
      ((note-column-interface trans grob source)
       ;; cache NoteColumn in this Voice context
       (set! note-column grob))
      ((text-script-interface trans grob source)
       ;; whenever a TextScript is acknowledged,
       ;; add it to `scripts' list
       (set! scripts (cons grob scripts))))
     ((stop-translation-timestep trans)
      ;; if any TextScript grobs exist,
      ;; set NoteColumn as X-parent
      (for-each (lambda (script)
		  (set! (ly:grob-parent script X) note-column))
		scripts)
      ;; clear scripts ready for next timestep
      (set! scripts '())))))

\header {tagline = ##f}

\paper {
  system-system-spacing = #'((basic-distance . 21) (minimum-distance . 21) (padding . 6))
}

\layout {
	indent = #1
	ragged-last = ##t
    ragged-right = ##t
	\accidentalStyle "dodecaphonic"
	\override Beam.stencil = ##f
	\override Stem.stencil = ##f
	\override Staff.BarLine.stencil = ##f
	\override Flag.stencil = ##f
	\override Staff.Clef.stencil = ##f
	\override Staff.TimeSignature.stencil = ##f
	\override Staff.StaffSymbol.stencil = ##f
	\override SpacingSpanner.strict-grace-spacing = ##t
	\override SpacingSpanner.uniform-stretching = ##t
	\override SpacingSpanner.strict-note-spacing = ##t
    \override SpacingSpanner.uniform-stretching = ##t
\context {
	\Score
	proportionalNotationDuration = #(ly:make-moment 1 10)
	barNumberVisibility = ##f
}
  \context {
    \Voice
    \consists #Text_align_engraver
    \override TextScript.X-offset =
      #ly:self-alignment-interface::aligned-on-x-parent
    \override TextScript.self-alignment-X = #CENTER
  }
}


\new Score {
    <<
        \new Staff {
		\time 5/4
            \new Voice {
				\double-flat
                cff'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 1}

				\eleven-twelfths-flat
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 11 12}

				\seven-eighths-flat
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 7 8}

				\five-sixths-flat
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 6}

				\four-fifths-flat
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 4 5}
				\break

				\three-quarters-flat
                ctqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 4}

				\two-thirds-flat
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 2 3}

				\five-eighths-flat
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 8}

				\three-fifths-flat
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 5}

				\seven-twelfths-flat
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 7 12}
				\break

				\forced-flat
                cf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 2}

				\five-twelfths-flat
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 12}

				\two-fifths-flat
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 2 5}

				\three-eighths-flat
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 8}

				\one-third-flat
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 3}
				\break

				\quarter-flat
                cqf'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 4}

				\one-fifth-flat
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 5}

				\one-sixth-flat
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 6}

				\one-eighth-flat
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 8}

				\one-twelfth-flat
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 12}
				\break

				\time 1/4
				\forced-natural
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 0 1}
				\break

				\time 5/4
				\one-twelfth-sharp
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 12}

				\one-eighth-sharp
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 8}

				\one-sixth-sharp
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 6}

				\one-fifth-sharp
                c'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 5}

				\quarter-sharp
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 4}
				\break

				\one-third-sharp
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 3}

				\three-eighths-sharp
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 8}

				\two-fifths-sharp
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 2 5}

				\five-twelfths-sharp
                cqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 12}

				\forced-sharp
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 2}
				\break

				\seven-twelfths-sharp
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 7 12}

				\three-fifths-sharp
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 5}

				\five-eighths-sharp
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 8}

				\two-thirds-sharp
                cs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 2 3}
				\break

				\three-quarters-sharp
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 3 4}
				\break

				\four-fifths-sharp
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 4 5}

				\five-sixths-sharp
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 5 6}

				\seven-eighths-sharp
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 7 8}

				\eleven-twelfths-sharp
                ctqs'4
				^ \markup {\with-color #white .. \with-color #black \fraction 11 12}

				\double-sharp
                css'4
				^ \markup {\with-color #white .. \with-color #black \fraction 1 1}
            }
        }
    >>
}
