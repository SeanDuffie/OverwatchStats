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
    top = 0.2
    left = 0.28
    width = 0.4
    height = 0.7
    bbox = {
            "top": top,
            "left": left,
            "width": width,
            "height": height
    }
    # scn = bot.Screen(box=bbox)
    scn = bot.Screen(box=bbox, path="./Scoreboard.webp")
    rdr = bot.Reader(scn.get_image())
    plyr = bot.Player()
    htky = bot.Hotkey(toggle_key=bot.keyboard.Key.tab)
    t1 = threading.Thread(target=htky.run, args=())
    t1.start()

    while htky.alive:
        if htky.active:
            # Grab a new image from the screen and read the text
            raw_img = scn.get_image()

            # If in debug mode, show the image being read, and the text that came from it
            if DEBUG:
                # rdr.show_img("Preview Raw")
                cv2.imshow("Preview Raw", raw_img)
                cv2.waitKey(17)

            rows = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, raw_img.shape[2]]
            cols = [ 0, 1, 2, 3, 4, 5, 6, raw_img.shape[1] ]

            for team in range(2):
                whttxt = not bool(team)
                for player in range(5):
                    row = rows[5*team+player]
                    next_row = rows[5*team+player+1]
                    for col in range(len(cols)-1):
                        if col == 0:
                            continue
                        logger.warning("Cropping dimensions: [%d:%d, %d:%d]", cols[col], cols[col+1], rows[row], rows[next_row])
                        rdr.update_img(raw_img[cols[col]:cols[col+1], rows[row]:rows[next_row]])

                        try:
                            text: str = rdr.read_text(white_text=whttxt)
                            logger.info("Team %d | Player %d | %s", team, player, text)
                        except UnboundLocalError: # Thrown when the image is blank or monocolor
                            logger.error("Failed to read Text")
                            text = ""
            htky.active = False

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
