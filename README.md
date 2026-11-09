# BlitStyledText-C
A small C script for blitting styled text.
So, I was working on a game in python for a class I was taking and was reminded how slow terminal graphics can be with python, so I went and wrote a small C script for getting fast styled text.
# Install
Download the render.c file and compile with whatever compiler you want. Nothing complex
# Use
(assuming the executable is at ./render)
 ./render width height (then for each pixel from left to right, top to bottom, provide an ANSI color code then the charactor/text)
 EX: ./render 2 2 31 A 34 B 35 C 36 D
