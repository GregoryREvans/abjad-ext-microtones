#(set-default-paper-size "letterportrait")
#(set-global-staff-size 15)

\header {tagline = ##f}

\paper {
  system-system-spacing = #'((basic-distance . 21) (minimum-distance . 21) (padding . 6))
}

\layout {
	indent = #1
	ragged-last = ##t
    ragged-right = ##t
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
}
