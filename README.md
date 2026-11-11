# Kuro

Small OpenCV image-augmentation experiments, maintained by [Stark Fiber Enterprise](https://starkfiber.my).

## Try the image demo

Use a Python virtual environment with NumPy and OpenCV installed. For a headless environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install numpy opencv-python-headless
python main.py path/to/image.png --output flipped.png
python -m unittest discover -p 'test_*.py' -v
```

The command reads your image, flips it horizontally and saves a new image. It reports unreadable input instead of opening a blank window. To use `--show`, install the GUI-enabled `opencv-python` package instead of the headless package; do not install both in the same environment.

## Included operations

Horizontal/vertical flips, shifts, resizing, zoom, rotation, colour adjustment and sharpening are in [kuro.py](kuro.py). Dataset splitting separately requires `split-folders`; it is imported only when that operation is used.

The regression suite covers non-square image dimensions, zero-sized zoom samples, channel clipping and the command-line image workflow. The maintenance check used Python 3.9, NumPy 2.0.2 and OpenCV 5.0.0 on macOS. This is not a trained cat/dog classifier, a model release or a cross-platform packaged application.

## Next steps

Add labelled dataset provenance, deterministic augmentation seeds and measured model evaluation before introducing classification claims. Keep training images and model weights out of commits unless their redistribution rights are known.

See [LICENSE](LICENSE). Original attribution in the source is preserved.
