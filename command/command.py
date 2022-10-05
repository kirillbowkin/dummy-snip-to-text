import pyperclip
import pyautogui
import numpy as np
import cv2
import click

from util.util import show_timer
from . import window_name, reader


@click.command()
@click.option("--delay", "-d", default=0, help="delay in seconds")
def snip_to_text_command(delay):
    show_timer(delay)
    click.echo('starting snipping...')
    cv_img = get_screenshot()
    img_area = get_selected_area(window_name, cv_img)
    text = get_text_from_img(img_area)
    pyperclip.copy(text)
    click.echo(click.style('Text has been copied to a clipboard', fg="green"))
    cv2.destroyAllWindows()

def get_text_from_img(img_area):
    return '\n'.join(reader.readtext(img_area, detail=0, paragraph=True))

def get_screenshot():
    pil_img = pyautogui.screenshot()
    cv_img = np.array(pil_img)
    # Convert RGB to BGR
    cv_img = cv_img[:, :, ::-1].copy()
    return cv_img

def show_snipping_screen(window_name, cv_img):
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

def get_selected_area(window_name, cv_img):
    x, y, w, h = cv2.selectROI(window_name, cv_img)
    crop_img = cv_img[y:y+h, x:x+w]
    return crop_img