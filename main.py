import pyperclip
import easyocr
import pyautogui
import numpy as np
import cv2
import click
import time

@click.command()
@click.option("--delay", "-d", default=0, help="delay in seconds")
def snip_to_text_command(delay):
    for i in range(delay,0,-1):
        print(f"sinpping will start in {i}s", end="")
        print("\r", end="")
        time.sleep(1)

    click.echo('starting snipping...')
    pil_img = pyautogui.screenshot()
    cv_img = np.array(pil_img)
    # Convert RGB to BGR
    cv_img = cv_img[:, :, ::-1].copy()

    window_name = "Screenshot"
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

    x, y, w, h = cv2.selectROI(window_name, cv_img)

    crop_img = cv_img[y:y+h, x:x+w]

    reader = easyocr.Reader(["en", "ru"])
    text = '\n'.join(reader.readtext(crop_img, detail=0, paragraph=True))

    pyperclip.copy(text)

    click.echo(click.style('Text has been copied to a clipboard', fg="green"))
    cv2.destroyAllWindows()

if __name__ == "__main__":
    snip_to_text_command()
