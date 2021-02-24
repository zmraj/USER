import asyncio

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("gangasta ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await tr(event, "EVERyBOdy")
        await asyncio.sleep(0.3)
        await tr(event, "iZ")
        await asyncio.sleep(0.2)
        await tr(event, "GangSTur")
        await asyncio.sleep(0.5)
        await tr(event, "UNtIL ")
        await asyncio.sleep(0.2)
        await tr(event, "I")
        await asyncio.sleep(0.3)
        await tr(event, "ArRivE")
        await asyncio.sleep(0.3)
        await tr(event, "🔥🔥🔥")
        await asyncio.sleep(0.3)
        await tr(event, "EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥🔥🔥")


CMD_HELP.update(
    {
        "gangasta": "**Gangasta**\
\n\n**Syntax : **`.gangasta`\
\n**Usage :** shows your gangster skills."
    }
)
