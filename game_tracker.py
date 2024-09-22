""" @file game_tracker.py
    @author Sean Duffie
    @brief Track leaderboard statistics when pressing tab

TODO: Calculate ult efficiency. How much charge would've been gained in-between reaching full charge and using ult?
TODO: Calculate damage-to-kill ratio. How much of your damage output is getting healed? (Hard to factor in assists). Compare to enemy team's health pool.
TODO: How can I calculate active combat time?
TODO: Calculate potential damage with accuracy, critical, splash, and active combat time.
TODO: Team comp analysis (Friendly and enemy)
    - counters
    - range
    - mobility

TODO: HUD Desktop App
    - Target priority
    - Tips for your hero
    - Tips against enemies
    - Map overview with health packs, objective paths, spawns, and high grounds
        - Time to walk to point from each spawn

NOTE: Eliminations / Damage dealt show how often someone you shoot dies.
    - The better this ratio is, the more effective the damage that you deal is,
      as you are actually getting elims and not feeding tanks/support
NOTE: Eliminations are given when you contribute *UNHEALED* damage to a kill
NOTE: Assists are given when you apply a buff/healing to an ally who gets a kill,
      or a debuff to an enemy who is killed.
"""
import datetime
import logging
import sys
import threading
from typing import List

import cv2

import bot
import logFormat

DEBUG = True

# Initial Logger Settings
logFormat.format_logs(logger_name="Auto")
logger = logging.getLogger("Auto")

class Row:
    def __init__(self, lst: List[str]):
        logger.warning(lst)
        self.name = lst[0]
        self.elims = lst[1]
        self.assists = lst[2]
        self.deaths = lst[3]
        self.dmg = lst[4]
        self.heals = lst[5]
        self.mit = lst[6]

    def __str__(self):
        msg = f" Player {self.name}:\n\tElims: {self.elims}\n\tAssists: {self.assists}\n\tDeaths: {self.deaths}\n\tDMG: {self.dmg}\n\tHealing: {self.heals}\n\tMit: {self.mit}"
        return msg

# function to display the coordinates of the points clicked on the image
def click_event(event, x, y, flags, params):
    """ TEMPORARY """
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

def overwatch():
    """ Monitors Stamina and chooses to sprint or walk bases on exhaustion

        FIXME: It would be cleaner to template the Hotkey interface

        Control Logic
        - Reads "current/total stamina" (ex. "87/100")
        - if current stamina is greater than 90% of total, start sprinting
        - if current stamina is less than 10% of total, stop sprinting
    """
    # Initialize the Screen Capture and the Text Reader
    top = 0.2
    left = 0.28
    width = 0.45
    height = 0.7
    bbox = {
            "top": top,
            "left": left,
            "width": width,
            "height": height
    }
    scn = bot.Screen(box=bbox)
    # scn = bot.Screen(box=bbox, path="./Example Scoreboard.png")
    rdr = bot.Reader(scn.get_image())
    htky = bot.Hotkey(toggle_key=bot.keyboard.Key.tab)
    t1 = threading.Thread(target=htky.run, args=())
    t1.start()

    while htky.alive:
        if htky.active:
            # Grab a new image from the screen and read the text
            raw_img = scn.get_image()
            now = datetime.datetime.now()

            # If in debug mode, show the image being read, and the text that came from it
            if DEBUG:
                # rdr.show_img("Preview Raw")
                logger.warning("Acquired Dimensions: %s", raw_img.shape)
                cv2.imshow("Preview Raw", raw_img)
                # cv2.waitKey(17)

                # setting mouse handler for the image
                # and calling the click_event() function
                cv2.setMouseCallback('Preview Raw', click_event)

            # TODO: Replace with actual pixel coordinates
            rows = [0, 82, 169, 254, 339, 484, 631, 717, 802, 886, 970, raw_img.shape[0]]
            cols = [36, 120, 497, 572, 645, 718, 865, 997, raw_img.shape[1]]

            for team in range(2):
                whttxt = not bool(team)
                for player in range(5):
                    lst = []
                    row = rows[5*team+player]
                    next_row = rows[5*team+player+1]
                    for col in range(len(cols)-1):
                        sub_img = raw_img[row:next_row, cols[col]:cols[col+1]]
                        # Show player icon
                        if col == 0:
                            cv2.imshow("Char", sub_img)
                            continue

                        logger.warning("Dimensions: %s | (%s:%s, %s:%s)", sub_img.shape, row, next_row, cols[col], cols[col+1])
                        rdr.update_img(sub_img)

                        try:
                            text: str = rdr.read_text(white_text=whttxt)
                            logger.info(text)
                            cv2.waitKey(0)
                        except UnboundLocalError: # Thrown when the image is blank or monocolor
                            logger.error("Failed to read Text")
                            text = ""
                        lst.append(text)

                    cur = Row(lst)
                    logger.info(cur)
                    logger.info(lst)
            htky.active = False

    t1.join()
    logger.info("End main")

if __name__ == "__main__":
    sys.exit(overwatch())
