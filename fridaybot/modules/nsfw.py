#    Copyright (C) Midhun KM 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os

import requests
from telethon.tl.types import MessageMediaPhoto

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd, sudo_cmd, admin_cmd
from uniborg.util import friday_on_cmd



@friday.on(friday_on_cmd(pattern=r"oldnsfw"))
@friday.on(sudo_cmd(pattern=r"oldnsfw", allow_sudo=True))
async def nsfw(event):
    if event.fwd_from:
        return
    url = "https://nsfw-categorize.it/api/upload"
    await tr(event, "`Processing..`")
    sed = await event.get_reply_message()
    photo = None
    sedpath = "./fridaydevs/"
    if sed and sed.media:
        if isinstance(sed.media, MessageMediaPhoto):
            photo = await borg.download_media(sed.media, sedpath)
        elif "image" in sed.media.document.mime_type.split("/"):
            photo = await borg.download_media(sed.media, sedpath)
        else:
            await tr(event, "Reply To Image")
            return
    if photo:
        files = {"image": (f"{photo}", open(f"{photo}", "rb"))}
        r = requests.post(url, files=files).json()
        if r["status"] == "OK":
            await tr(event, 
                "This image is classified as " + str(r["data"]["classification"])
            )
        if os.path.exists(photo):
            os.remove(photo)
        else:
            await tr(event, "Response UnsucessFull. Try Again.")
            if os.path.exists(photo):
                os.remove(photo)



CMD_HELP.update(
    {
        "nsfw": "**NSFW**\
\n\n**Syntax : **`.oldnsfw <reply to image>`\
\n**Usage :** Checks if the replyed image is nsfw or not.\
\n\n**Syntax : **`.phs <query>`\
\n**Usage :** Searches PornHub Website With Given Query."
    }
)
