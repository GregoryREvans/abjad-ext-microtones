# abjad-ext-microtones
Microtonal Abjad Extension Package <br />
![testing](https://github.com/GregoryREvans/abjad-ext-microtones/workflows/testing/badge.svg) <br />
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black) <br/>

This package currently requires installation of the `ekmelos` or `HEJI2` font into lilypond <br />

* the fonts can be found at http://www.ekmelic-music.org/en/extra/ekmelos.htm and http://www.plainsound.org/ respectively. <br />

For the display of accidentals, `\accidentalStyle dodecaphonic` must be set in the `layout` block and an `\include` for the path to `ekmelos-accidental-markups.ily` or `heji2-accidental-markups.ily` within this package must be added. <br />

Currently supports Helmholtz-Ellis Just Intonation accidentals: <br />

ekmelos <br />
![](ekmelos_overtones.png) <br />

HEJI2 <br />
![](heji2_overtones.png) <br />

Default EDO accidentals: <br />

![](edo_accidentals.png) <br />

Ekmelos EDO accidentals: <br />

![](ekmelos_edo_accidentals.png) <br />

---
Conceivably, the accidental notation is personalizable by user-defined stylesheets similar to the ones included with this package.
---
Dev branch features pitch and interval utilities.
