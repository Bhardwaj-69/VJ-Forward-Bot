import os
from config import Config

class  Script(object):
  START_TXT = """<b><blockquote>🧤Ahhoyy! Pirate {}🧤
  
🧤Pirate Forword Bot here</blockquote></b>
**<b><i>🧤i can forward Old Msg from one Channel to Other Channel**

🧤i have UserBot option mean
If you are not Admin and your Bot not Admin But you are Just Member of the Channel
still you can forward Using UserBot Option🧤</i></b>"""
  HELP_TXT = """<b><u>🧤hyy Help Here🧤</b></u>

<u>**💢CMD's:**</u>
<b>🧪 __/start - Slap me.__ 
🧪 __/forward - Start Forward__
🧪 __/settings - Manage your Needs__
🧪 __ /unequify - Delete duplicate media messages in chats__
🧪 __ /stop - Stop Running Task__
🧪 __ /reset - to Reset Settings__</b>

<b><u>💢 Features:</b></u>
<b>⚗ __Forward message from public channel to your channel without admin permission. if the channel is private need admin permission, if you can't give admin permission then use userbot, but in userbot there is a chance to get your account ban so use fake account__
⚗ __custom caption__
⚗ __custom button__
⚗ __skip duplicate messages__
⚗ __filter type of messages__</b>
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
<b>🧬 __add a bot or userbot__
🧬 __add atleast one to channel__ `(your bot/userbot must be admin in there)`
🧬 __You can add chats or bots by using /settings__
🧬 __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there also__
🧬 __Then use /forward to forward messages__

👻 How to USe. [Tutorial](https://t.me/LarvaLinks)</b>"""
  
  ABOUT_TXT = """<b>
       🧤Forward Bot🧤
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
    🧤   Bot   : [💀Click kar ke dekh🗿](https://t.me/PiratesHunts_Bot)
    🧤Redirect : [💀Click kar ke dekh🗿](https://t.me/LarvaLinks)
    🧤Redirect : [💀Click kar ke dekh🗿](https://t.me/+Y_QdbkhM2OFmNmZl)
    🧤Redirect : [💀Click kar ke dekh🗿](https://t.me/+rB85LI4q54I2NDRl)
    🧤Redirect : [💀Click kar ke dekh🗿](https://t.me/+1s4iBWhHUyczM2M9)
    🧤Redirect : [💀Click kar ke dekh🗿](https://t.me/DM_HUB_69) 
    🧤Redirect : [💀Click kar ke dekh🗿](https://t.me/+L0Mj3fc1ETs3YWY9)
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
</b>"""
  STATUS_TXT = """
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
🧪
💢Bot Uptime:**`{}`
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
⚗Total Users:** `{}`
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
⚜Total Bot:** `{}`
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
🧬Forwarding:** `{}`
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
"""
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>❪ SET MESSAGE SKIPING NUMBER ❫</b>\n\n<b>Skip the message as much as you enter the number and the rest of the message will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skiped\n You enter 5 = 5 message skiped</code>\n/cancel <b>- cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
🧤<b>Feched Msg :</b> <code>{}</code>

🧤<b>SuccesFully Fwd :</b> <code>{}</code>

🧤<b>Duplicate Msg :</b> <code>{}</code>

🧤<b>Deleted Msg :</b> <code>{}</code>

🧤<b>Skipped Msg :</b> <code>{}</code>

🧤<b>Filtered Msg :</b> <code>{}</code>

🧤<b>Current Status:</b> <code>{}</code>

🧤<b>PercenTage</b> <code>{}</code> %
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
"""
  DUPLICATE_TEXT = """
       UniQuiFy Status
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
<b>Fetched Files:</b> <code>{}</code>
<b>Duplicate Deleted:</b> <code>{}</code> 
━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━⬍━
"""
  DOUBLE_CHECK = """<b><u>DOUBLE CHECKING ⚠️</b></u>
<code>Before forwarding the messages Click the Yes button only after checking the following</code>

<b>🧤 YOUR BOT:</b> [{botname}](t.me/{botuname})
<b>🧤 FROM CHANNEL:</b> `{from_chat}`
<b>🧤 TO CHANNEL:</b> `{to_chat}`
<b>🧤 SKIP MESSAGES:</b> `{skip}`

<i>° [{botname}](t.me/{botuname}) must be admin in **TARGET CHAT**</i> (`{to_chat}`)
<i>° If the **SOURCE CHAT** is private your userbot must be member or your bot must be admin in there also</b></i>

<b>If the above is checked then the yes button can be clicked</b>"""
  
SETTINGS_TXT = """<b>change your settings as your wish</b>"""
