import pyautogui
import numpy as np
import cv2

pil_img = pyautogui.screenshot()
cv_img = np.array(pil_img)
# Convert RGB to BGR
cv_img = cv_img[:, :, ::-1].copy()

window_name = "Screenshot"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow(window_name, cv_img)

cv2.waitKey()
cv2.destroyAllWindows()
