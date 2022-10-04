import pyperclip
import easyocr
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

x, y, w, h = cv2.selectROI(window_name, cv_img)

crop_img = cv_img[y:y+h, x:x+w]

reader = easyocr.Reader(["en", "ru"])
text = '\n'.join(reader.readtext(crop_img, detail=0, paragraph=True))

pyperclip.copy(text)

print('Text has been copied to a clipboard')
cv2.destroyAllWindows()
