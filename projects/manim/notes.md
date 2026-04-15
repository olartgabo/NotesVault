---
id: notes
aliases: []
tags: []
---

   7         self.play(Write(text))
      8         self.wait(1)
      9         self.play(FadeOut(text))
     … +56 lines (ctrl+o to expand)

● Created ~/NotesVault/projects/manim/example.py with examples.

  Basic Syntax

  from manim import *

  class MyScene(Scene):
      def construct(self):
          # Create objects
          circle = Circle(color=BLUE)

          # Animate them
          self.play(Create(circle))
          self.wait(1)

  Run it

  cd ~/NotesVault/projects/manim
  source ~/path/to/your/venv/bin/activate

  # Render one scene (low quality, fast)
  manim -pql example.py HelloWorld

  # Or in nvim: <leader>rm then type "HelloWorld"

  Common Animations
  ┌──────────────────────────┬────────────────┐
  │        Animation         │  What it does  │
  ├──────────────────────────┼────────────────┤
  │ Create(obj)              │ Draw shape     │
  ├──────────────────────────┼────────────────┤
  │ Write(text)              │ Write text     │
  ├──────────────────────────┼────────────────┤
  │ FadeIn/FadeOut           │ Fade           │
  ├──────────────────────────┼────────────────┤
  │ Transform(a, b)          │ Morph a into b │
  ├──────────────────────────┼────────────────┤
  │ obj.animate.shift(RIGHT) │ Move object    │
  ├──────────────────────────┼────────────────┤
  │ obj.animate.scale(2)     │ Scale object   │
  └──────────────────────────┴────────────────┘
  Quality Flags

  - -ql low (480p, fast)
  - -qm medium (720p)
  - -qh high (1080p)
  - -qk 4K

  The -p flag opens the video after rendering.
