""" @file patch.py
    @author Sean Duffie
    @brief 
"""
import datetime

# https://overwatch.blizzard.com/en-us/news/patch-notes/
# body
    # main
        # blz-section class="PatchNotesBody"
            # div class="PatchNotes-list"
                # div class="PatchNotes-body"
                # NOTE: This section contains the list of patches
                    # div class="PatchNotes-path PatchNotes-live"
                    # NOTE: This section contains the important info on each patch
                        # h3 class="PatchNotes-patchTitle"
title = "Overwatch 2 Retail Patch Notes - July 12, 2024".split(" - ")
name = title[0]
date = datetime.datetime.strptime(title[1], "%B %d, %Y")
                        # div class="PatchNotes-section PatchNotes-section-hero_update"
                            # h4 class="PatchNotes-sectionTitle"
role = "Tank"
print(name, date, role)
                                # div class="PatchNotesHeroUpdate"
                                    # div class="PatchNotesHeroUpdate-header"
                                        # h5 class="PatchNotesHeroUpdate-name"
hero = "Ramattra"
                                        # div class="PatchNotesHeroUpdate-body"
                                            # div class="PatchNotesHeroUpdate-abilitiesList"
                                                # div class="PatchNotesAbilityUpdate"
                                                    # div class="PatchNotesAbilityUpdate-name"
ability = "Nemesis Form"
                                                    # div class="PatchNotesAbilityUpdate-detailList"
                                                        # ul
                                                            # li (changes)
changes = [
    "Cooldown increased from 7 to 8 seconds.",
    "Base armor reduced from 100 to 75.",
    "Base health reduced from 275 to 250."
]
