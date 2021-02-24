"""DA.GD helpers in @UniBorg
Available Commands:
.isup URL
.dns google.com
.url <long url>
.unshort <short url>"""
import requests

from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("dns (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await tr(event, "DNS records of {} are \n{}".format(input_str, response_api))
    else:
        await tr(event, "i can't seem to find {} on the internet".format(input_str))


@friday.on(friday_on_cmd("url (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await tr(event, "Generated {} for {}.".format(response_api, input_str))
    else:
        await tr(event, "something is wrong. please try again later.")


@friday.on(friday_on_cmd("unshort (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await tr(event, 
            "Input URL: {}\nReDirected URL: {}".format(input_str, r.headers["Location"])
        )
    else:
        await tr(event, 
            "Input URL {} returned status_code {}".format(input_str, r.status_code)
        )
