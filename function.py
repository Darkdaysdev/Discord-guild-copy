import discord
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
class Clone:
    @staticmethod
    async def rol_sil(guild_to: discord.Guild):
        for role in guild_to.roles:
            try:
                if role.name != "@everyone" and not role.managed:
                    await role.delete()
                    print(Fore.YELLOW + f"Rol silindi: {role.name}" + Style.RESET_ALL)
            except discord.Forbidden:
                print(Fore.RED + f"Rol silme yetkisi yok: {role.name}" + Style.RESET_ALL)
            except discord.HTTPException:
                print(Fore.RED + f"Rol silinemedi: {role.name}" + Style.RESET_ALL)

    @staticmethod
    async def rol_olustur(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = [role for role in guild_from.roles 
                if role.name != "@everyone" and not role.managed][::-1]
                
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print(Fore.GREEN + f"Rol oluşturuldu: {role.name}" + Style.RESET_ALL)
            except discord.Forbidden:
                print(Fore.RED + f"Rol oluşturma yetkisi yok: {role.name}" + Style.RESET_ALL)
            except discord.HTTPException:
                print(Fore.RED + f"Rol oluşturulamadı: {role.name}" + Style.RESET_ALL)

    @staticmethod
    async def kanal_sil(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print(Fore.YELLOW + f"Kanal silindi: {channel.name}" + Style.RESET_ALL)
            except discord.Forbidden:
                print(Fore.RED + f"Kanal silme yetkisi yok: {channel.name}" + Style.RESET_ALL)
            except discord.HTTPException:
                print(Fore.RED + f"Kanal silinemedi: {channel.name}" + Style.RESET_ALL)

    @staticmethod
    async def kategori_olustur(guild_to: discord.Guild, guild_from: discord.Guild):
        for channel in guild_from.categories:
            try:
                overwrites_to = {
                    discord.utils.get(guild_to.roles, name=key.name): value 
                    for key, value in channel.overwrites.items() 
                    if discord.utils.get(guild_to.roles, name=key.name) is not None
                }
                
                new_channel = await guild_to.create_category(
                    name=channel.name,
                    overwrites=overwrites_to
                )
                await new_channel.edit(position=channel.position)
                print(Fore.GREEN + f"Kategori oluşturuldu: {channel.name}" + Style.RESET_ALL)
            except discord.Forbidden:
                print(Fore.RED + f"Kategori oluşturma yetkisi yok: {channel.name}" + Style.RESET_ALL)
            except discord.HTTPException:
                print(Fore.RED + f"Kategori oluşturulamadı: {channel.name}" + Style.RESET_ALL)

    @staticmethod
    async def kanal_olustur(guild_to: discord.Guild, guild_from: discord.Guild):
  
        for channel_text in guild_from.text_channels:
            try:
                category = next(
                    (cat for cat in guild_to.categories 
                     if hasattr(channel_text, 'category') and 
                     channel_text.category and 
                     cat.name == channel_text.category.name),
                    None
                )
                
                if not hasattr(channel_text, 'category'):
                    print(Fore.YELLOW + f"{channel_text.name} kanalının kategorisi yok!" + Style.RESET_ALL)

                overwrites_to = {
                    discord.utils.get(guild_to.roles, name=key.name): value 
                    for key, value in channel_text.overwrites.items()
                    if discord.utils.get(guild_to.roles, name=key.name) is not None
                }
                
                try:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                        topic=channel_text.topic,
                        slowmode_delay=channel_text.slowmode_delay,
                        nsfw=channel_text.nsfw
                    )
                except:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position
                    )
                
                if category:
                    await new_channel.edit(category=category)
                
                print(Fore.GREEN + f"Metin kanalı oluşturuldu: {channel_text.name}" + Style.RESET_ALL)
            except discord.Forbidden:
                print(Fore.RED + f"Metin kanalı oluşturma yetkisi yok: {channel_text.name}" + Style.RESET_ALL)
            except discord.HTTPException:
                print(Fore.RED + f"Metin kanalı oluşturulamadı: {channel_text.name}" + Style.RESET_ALL)

        for channel_voice in guild_from.voice_channels:
            try:
                category = next(
                    (cat for cat in guild_to.categories 
                     if hasattr(channel_voice, 'category') and 
                     channel_voice.category and 
                     cat.name == channel_voice.category.name),
                    None
                )
                
                if not hasattr(channel_voice, 'category'):
                    print(Fore.YELLOW + f"{channel_voice.name} kanalının kategorisi yok!" + Style.RESET_ALL)

                overwrites_to = {
                    discord.utils.get(guild_to.roles, name=key.name): value 
                    for key, value in channel_voice.overwrites.items()
                    if discord.utils.get(guild_to.roles, name=key.name) is not None
                }
                
                try:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                        bitrate=channel_voice.bitrate,
                        user_limit=channel_voice.user_limit
                    )
                except:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position
                    )
                
                if category:
                    await new_channel.edit(category=category)
                
                print(Fore.GREEN + f"Ses kanalı oluşturuldu: {channel_voice.name}" + Style.RESET_ALL)
            except discord.Forbidden:
                print(Fore.RED + f"Ses kanalı oluşturma yetkisi yok: {channel_voice.name}" + Style.RESET_ALL)
            except discord.HTTPException:
                print(Fore.RED + f"Ses kanalı oluşturulamadı: {channel_voice.name}" + Style.RESET_ALL)

    @staticmethod
    async def emoji_sil(guild_to: discord.Guild):
        for emoji in guild_to.emojis:
            try:
                await emoji.delete()
                print(Fore.YELLOW + f"Emoji silindi: {emoji.name}" + Style.RESET_ALL)
            except discord.Forbidden:
                print(Fore.RED + f"Emoji silme yetkisi yok: {emoji.name}" + Style.RESET_ALL)
            except discord.HTTPException:
                print(Fore.RED + f"Emoji silinemedi: {emoji.name}" + Style.RESET_ALL)

    @staticmethod
    async def emoji_olustur(guild_to: discord.Guild, guild_from: discord.Guild):
        for emoji in guild_from.emojis:
            try:
                emoji_image = await emoji.url.read()
                await guild_to.create_custom_emoji(
                    name=emoji.name,
                    image=emoji_image
                )
                print(Fore.GREEN + f"Emoji oluşturuldu: {emoji.name}" + Style.RESET_ALL)
            except discord.Forbidden:
                print(Fore.RED + f"Emoji oluşturma yetkisi yok: {emoji.name}" + Style.RESET_ALL)
            except discord.HTTPException:
                print(Fore.RED + f"Emoji oluşturulamadı: {emoji.name}" + Style.RESET_ALL)