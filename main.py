"""Flip an image horizontally and save the result."""
import argparse
from pathlib import Path
import cv2
import kuro


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Path to an input image")
    parser.add_argument("--output", type=Path, default=Path("flipped.png"))
    parser.add_argument("--show", action="store_true", help="Open preview windows (requires GUI OpenCV)")
    args = parser.parse_args()
    image = cv2.imread(str(args.image))
    if image is None:
        parser.error(f"Could not read image: {args.image}")
    result = kuro.horizontal_flip(image)
    if not cv2.imwrite(str(args.output), result):
        parser.error(f"Could not write image: {args.output}")
    if args.show:
        try:
            cv2.imshow("result", result)
            cv2.imshow("original", image)
            cv2.waitKey(0)
        finally:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
