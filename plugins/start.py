# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

 
@app.on_message(filters.command("start")) 
async def start_command(client: Client, message: Message): 
    user = message.from_user 
 
    # Check if the user has a profile photo using get_chat_photos 
    chat_photos = await client.get_chat_photos(user.id, limit=1) 
     
    if chat_photos.total_count > 0: 
        # If the user has a profile photo, send it with the welcome message 
        profile_photo = chat_photos.photos[0][0].file_id 
        await message.reply_photo(profile_photo, caption=f"Welcome, {user.first_name}!") 
    else: 
        # If the user doesn't have a profile photo, send only the welcome message 
        await message.reply_text(f"Welcome, {user.first_name}!")
