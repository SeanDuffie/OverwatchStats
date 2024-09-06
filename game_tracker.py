""" @file game_tracker.py
    @author Sean Duffie
    @brief Track leaderboard statistics when pressing tab

NOTE: Eliminations / Damage dealt show how often someone you shoot dies.
    - The better this ratio is, the more effective the damage that you deal is,
      as you are actually getting elims and not feeding tanks/support
NOTE: Eliminations are given when you contribute *UNHEALED* damage to a kill
NOTE: Assists are given when you apply a buff/healing to an ally who gets a kill,
      or a debuff to an enemy who is killed.
"""
import logging
import sys
import threading

import cv2

import bot
import logFormat

DEBUG = True

# Initial Logger Settings
logFormat.format_logs(logger_name="Auto")
logger = logging.getLogger("Auto")


def overwatch():
    """ Monitors Stamina and chooses to sprint or walk bases on exhaustion

        FIXME: It would be cleaner to template the Hotkey interface

        Control Logic
        - Reads "current/total stamina" (ex. "87/100")
        - if current stamina is greater than 90% of total, start sprinting
        - if current stamina is less than 10% of total, stop sprinting
    """
    # Initialize the Screen Capture and the Text Reader
    top = 7 / 52
    left = 12 / 72
    width = 31 / 72
    height = 27 / 52
    bbox = {
            "top": top,
            "left": left,
            "width": width,
            "height": height
    }
    scn = bot.Screen(box=bbox, path="./Scoreboard.webp")
    rdr = bot.Reader(scn.get_image())
    plyr = bot.Player()
    htky = bot.Hotkey()
    t1 = threading.Thread(target=htky.run, args=())
    t1.start()

    while htky.alive:
        if htky.active:
            # Grab a new image from the screen and read the text
            rdr.update_img(scn.get_image())

            # If in debug mode, show the image being read, and the text that came from it
            if DEBUG:
                rdr.show_img("Preview Raw")

            try:
                text: str = rdr.read_text()
            except UnboundLocalError: # Thrown when the image is blank or monocolor
                logger.error("Failed to read Text")
                text = ""

            # If in debug mode, show the image being read, and the text that came from it
            if DEBUG:
                rdr.show_img()

            # # Split values and remove incorrect numbers
            # try:
            #     if text != "":
            #         logger.debug(text)
            #         current, total = text.split("/", 1)
            #         current = int("".join(c for c in current if c.isdigit()))
            #         total = int("".join(c for c in total if c.isdigit()))
            #         ratio = current/total
            #         logger.info("Ratio = %.2f", ratio)

            #         # if current is greater than 90% total, start sprinting
            #         if ratio > .9:
            #             plyr.key_down("shiftleft")
            #         # if current is less than 10% total, stop sprinting
            #         elif ratio < .1:
            #             plyr.key_up("shiftleft")
            #     else:
            #         logger.warning("No text detected")
            #         # pass
            # except ValueError:
            #     logger.error("Failed to split text")
            #     # pass
        else:
            logger.info("Inactive")
            plyr.key_up("w")
            plyr.key_up("shiftleft")
            while not htky.active:
                if htky.alive:
                    cv2.waitKey(17)
                else:
                    break
            logger.info("Active")

    t1.join()
    logger.info("End main")

if __name__ == "__main__":
    sys.exit(overwatch())
