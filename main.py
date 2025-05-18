
import os
import asyncio
import discord
import platform
import colorama
from function import Clone
from colorama import Fore, Style

colorama.init(autoreset=True)

def display_banner():
    banner = """
    ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  █████╗ ██╗   ██╗███████╗
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
    ██║  ██║███████║██████╔╝█████╔╝ ██║  ██║███████║ ╚████╔╝ ███████╗
    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║  ██║██╔══██║  ╚██╔╝  ╚════██║
    ██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝██║  ██║   ██║   ███████║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
    """
    print(Fore.RED + banner)
    print(Fore.YELLOW + "\n\t\tSunucu Kopyalayıcı - DarkdaysDev Tarafından Yapılmıştır\n" + Style.RESET_ALL)

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")
    display_banner()

class CloneClient(discord.Client):
    async def on_ready(self):
        clear_screen()
        print(Fore.GREEN + f"\n{self.user} olarak giriş yapıldı." + Style.RESET_ALL)
        print(Fore.BLUE + "Sunucu kopyalama işlemi başlatılıyor...\n" + Style.RESET_ALL)
        
        guild_from = self.get_guild(int(FROM_GUILD))
        guild_to = self.get_guild(int(TO_GUILD))
        
        try:
            await Clone.rol_sil(guild_to)
            await Clone.kanal_sil(guild_to)
            await Clone.rol_olustur(guild_to, guild_from)
            await Clone.kategori_olustur(guild_to, guild_from)
            await Clone.kanal_olustur(guild_to, guild_from)
            
            print(Fore.GREEN + "\nSunucu başarıyla kopyalandı!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"\nHata oluştu: {e}" + Style.RESET_ALL)
        
        await asyncio.sleep(5)
        await self.close()

if __name__ == "__main__":
    clear_screen()
    TO_GUILD = input(Fore.BLUE + "Aktarılacak sunucu ID (Aktarılacak sunucu):\n> " + Style.RESET_ALL)
    FROM_GUILD = input(Fore.BLUE + "Hedef sunucu ID (kopyalanacak sunucu):\n> " + Style.RESET_ALL)
    TOKEN = input(Fore.BLUE + "\nDiscord tokeniniz:\n> " + Style.RESET_ALL)
    
    client = CloneClient()
    client.run(TOKEN, bot=False)