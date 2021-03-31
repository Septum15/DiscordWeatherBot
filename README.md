# DiscordWeatherBot

Ez a discord bot egy egyszerű időjárás lekérdező bot.

A felhasználó megtudhatja a keresett város hőmérsékletét, érzékelt hőmérsékletét, légnyomását, páratartalmát, láthatóságot illetve a szélsebességet.

Használathoz szükség van a [discord.py](https://pypi.org/project/discord.py/) library-re.

## setup
A program melletti keys.txt fájlban tároljuk a két API kulcsokat.

Az első sorban a Discord botunk tokenjé-t tároljuk, amit [itt](https://discord.com/developers/) lehet létrehozni.

A második sorban pedig az [openweathermap](https://home.openweathermap.org/api_keys) API kulcsnak kell lennie, ami regisztráció után érhető el.

## Használat
Miután beállítottuk  és elkezdtük futtatni a botunkat már lehet használni discordon.

A bot a `!weather <városnév>` parancsra hallgat. 

Fontos odafigyelni arra, hogy mivel a bot URL-ben kérdezi le a városokat, ezért ékezet nélkül adjuk meg a városok nevét.
