#(set-default-paper-size "letterportrait")
#(set-global-staff-size 15)

\header {tagline = ##f}

\paper {
  system-system-spacing = #'((basic-distance . 23) (minimum-distance . 23) (padding . 6))
}

\layout {
	indent = #1
	ragged-last = ##t
    ragged-right = ##t
	\override Beam.stencil = ##f
	\override Stem.stencil = ##f
	\override Staff.BarLine.stencil = ##f
	\override Flag.stencil = ##f
	\override Staff.TimeSignature.stencil = ##f
	\override SpacingSpanner.strict-grace-spacing = ##t
	\override SpacingSpanner.uniform-stretching = ##t
	\override SpacingSpanner.strict-note-spacing = ##t
    \override SpacingSpanner.uniform-stretching = ##t
\context {
	\Score
	proportionalNotationDuration = #(ly:make-moment 1 25)
	barNumberVisibility = ##f
}
}
