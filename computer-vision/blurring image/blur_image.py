import cv2
import numpy as np

def glow(img):
#    img = img.copy()
    blurred = cv2.GaussianBlur(img, (0, 0), sigmaX=3)
    return np.clip(blurred + img * .5, 0, 1)
"""
def glow(self, img, tint, radius, tolerance, saturation, brightness):
        Defaults:
        radius = 0
        tolerance = 0
        tint = [1, 1, 1]
        saturation = 1
        brightness = 1
        average = 0

    r, g, b, *a = cv2.split(img)
    avg = (r + g + b) * .33333
    div = 1 / max(1 - tolerance, .001)
    mult = div
    r = np.clip(((r - avg) * saturation + avg - tolerance) * mult, 0, 1) * brightness * tint[0]
    g = np.clip(((g - avg) * saturation + avg - tolerance) * mult, 0, 1) * brightness * tint[1]
    b = np.clip(((b - avg) * saturation + avg - tolerance) * mult, 0, 1) * brightness * tint[2]
    output = cv2.merge(((r, g, b, a.astype(r.dtype)) if a else (r, g, b)))
    if radius:
        output = cv2.GaussianBlur(output[:, :, :3], (0, 0), 5)
    return np.clip(output * .5 + img * .5, 0, 1)
"""

img = glow('unknown.png')
cv2.imshow('img',img)
cv2.waitKey(0)

# Q: But what does this mean  :  output[:, :, :3]
# A: every channel in output, up to channel 3, which is the alpha

