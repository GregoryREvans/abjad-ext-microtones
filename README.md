# abjad-ext-microtones
Microtonal Abjad Extension Package <br />
[![Build Status](https://travis-ci.com/GregoryREvans/abjad-ext-microtones.svg?branch=master)](https://travis-ci.com/GregoryREvans/abjad-ext-microtones) <br />
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black) <br/>

This package currently requires installation of the `ekmelos` or `HEJI2` font into lilypond <br />

* the fonts can be found at http://www.ekmelic-music.org/en/extra/ekmelos.htm and http://www.plainsound.org/ respectively. <br />

For the display of accidentals, `\accidentalStyle dodecaphonic` must be set in the `layout` block and an `\include` for the path to `ekmelos-accidental-markups.ily` or `heji2-accidental-markups.ily` within this package must be added. <br />

![](ekmelos_overtones.png) <br />

![](heji2_overtones.png) <br />
