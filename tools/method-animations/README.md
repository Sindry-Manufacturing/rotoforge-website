# Method animations

Generates the looping GIF schematics shown on the Process animations page
(`source/process-animations.md`) and linked from `source/a-list-of-methods.md`.
Every method is a short Python class that draws one frame as a function of time,
on a shared canvas (head-fixed side view, workpiece moving right, warm colours =
heat, dots = material flow). Change a scene, re-run, copy the GIF over.

Requirements: Python 3, Pillow, ffmpeg on the PATH (used for the GIF palette).

```sh
cd tools/method-animations
python3 build.py sheet sheet.png 1.3        # one frame of every scene, for a quick look
python3 build.py frame afrb 2.0 afrb.png    # one frame of one scene at t = 2.0 s
python3 build.py gifs                        # all GIFs -> out/
python3 build.py gifs afrb cold-spray        # just these
cp out/*.gif ../../source/img/methods/
```

Conventions (see `engine.py`): 640 x 360 px, 15 fps, 6 s seamless loop, rendered
at 2x and downsampled. Anything periodic must complete a whole number of cycles
in 6 s or the loop will jump. Slugs and the scene list live in `build.py`.
