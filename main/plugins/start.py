from telethon import events, Button
from ethon.teleutils import mention
from ethon.mystarts import vc_menu

from .. import Drone, ACCESS_CHANNEL, AUTH_USERS

from main.plugins.actions import set_thumbnail, rem_thumbnail, heroku_restart
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, source_text, SUPPORT_LINK

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply('Please Join My Updates Channel to use this Bot!\n\nDue to Overload, Only Channel Subscribers can use the Bot!', 
                      buttons=[
                              [Button.url("Join Updates Channel", url="https://t.me/Comp_Logs")]
                              ])
   
@Drone.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                              [Button.inline("Info Module", data="info"),
                               Button.inline("Spam Notice", data="notice")],
                              [Button.inline("Help Module", data="help")],
                              [Button.url("Support", url=f"https://t.me/BKC00bot")]])

    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await Drone.send_message(int(ACCESS_CHANNEL), f'{tag} started the BOT')
 
@Drone.on(events.callbackquery.CallbackQuery(data="module"))
async def info(event):
    await event.edit(f'{st}',
                      buttons=[
                              [Button.inline("Info Module", data="info"),
                               Button.inline("Spam Notice", data="notice")],
                              [Button.inline("Help Module", data="help")],
                              [Button.url("Support", url=f"https://t.me/BKC00bot")]])

    
@Drone.on(events.callbackquery.CallbackQuery(data="info"))
async def info(event):
    await event.edit(f'Info Module\n\n{info_text}',
                    buttons=[[
                         Button.inline("Back", data="module")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)
    
                    
@Drone.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit('Help and Support module for me.',
                    buttons=[[
                         Button.inline("Set Thumbnail", data="sett"),
                         Button.inline("Remove Thumbnail", data='remt')],
                         [
                         Button.inline("Modules", data="plugins"),
                         Button.inline("Restsrt", data="restart")])
    
@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[Button.inline("Back", data="module")]])
                   
 #-----------------------------------------------------------------------------------------------                            
    
@Drone.on(events.callbackquery.CallbackQuery(data="sett"))
async def sett(event):    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await set_thumbnail(event, x.media)
        await xx.delete()
        
@Drone.on(events.callbackquery.CallbackQuery(data="remt"))
async def remt(event):  
    await event.delete()
    await rem_thumbnail(event)
    
@Drone.on(events.callbackquery.CallbackQuery(data="restart"))
async def res(event):
    if not f'{event.sender_id}' == f'{int(AUTH_USERS)}':
        return await event.edit("Only authorized user can restart!")
    result = await heroku_restart()
    if result is None:
        await event.edit("You have not filled `HEROKU_API` and `HEROKU_APP_NAME` vars.")
    elif result is False:
        await event.edit("An error occured!")
    elif result is True:
        await event.edit("Restarting app, wait for a minute.")
