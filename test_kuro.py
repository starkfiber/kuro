import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import cv2
import numpy as np
import kuro

class RegressionTests(unittest.TestCase):
    def setUp(self):
        self.image = np.arange(6*10*3, dtype=np.uint8).reshape(6,10,3)
    def test_fill_preserves_non_square_dimensions(self):
        self.assertEqual(kuro.fill(self.image,6,10).shape,(6,10,3))
    def test_shift_preserves_non_square_dimensions(self):
        with patch('kuro.random.uniform',return_value=0.4):
            self.assertEqual(kuro.horizontal_shift(self.image,0.4).shape,self.image.shape)
            self.assertEqual(kuro.vertical_shift(self.image,0.4).shape,self.image.shape)
    def test_zoom_zero_sample_does_not_create_empty_crop(self):
        with patch('kuro.random.uniform',return_value=0):
            self.assertEqual(kuro.zoom(self.image,0).shape,self.image.shape)
    def test_channel_shift_clips_instead_of_wrapping(self):
        pixels=np.array([[[0,250,255]]],dtype=np.uint8)
        with patch('kuro.random.uniform',return_value=20):
            np.testing.assert_array_equal(kuro.channel_shift(pixels,20),[[[20,255,255]]])
        with patch('kuro.random.uniform',return_value=-20):
            np.testing.assert_array_equal(kuro.channel_shift(pixels,20),[[[0,230,235]]])
    def test_cli_writes_flipped_image_without_display(self):
        with tempfile.TemporaryDirectory() as tmp:
            src=Path(tmp)/'in.png'; dst=Path(tmp)/'out.png'
            cv2.imwrite(str(src),self.image)
            subprocess.run([sys.executable,str(Path(__file__).with_name('main.py')),str(src),'--output',str(dst)],check=True)
            np.testing.assert_array_equal(cv2.imread(str(dst)),self.image[:,::-1])
    def test_cli_rejects_missing_input(self):
        r=subprocess.run([sys.executable,str(Path(__file__).with_name('main.py')),'/nonexistent/sfe-test.png'],capture_output=True,text=True)
        self.assertEqual(r.returncode,2)
        self.assertIn('Could not read image',r.stderr)

if __name__=='__main__': unittest.main()
