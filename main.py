import discord
import pytz
import datetime
import os
import requests

from discord import colour as c
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents = discord.Intents.all()

dt_mtn = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul'))

bot = commands.Bot(command_prefix='!', intents=intents)

# ---------- 색상표 시작 ----------
color_default = 0
teal = c.Colour.teal()
dark_teal = c.Colour.dark_teal()
green = c.Colour.green()
dark_green = c.Colour.dark_green()
blue = c.Colour.blue()
dark_blue = c.Colour.dark_blue()
purple = c.Colour.purple()
dark_purple = c.Colour.dark_purple()
magenta = c.Colour.magenta()
dark_magenta = c.Colour.dark_magenta()
gold = c.Colour.gold()
dark_gold = c.Colour.dark_gold()
orange = c.Colour.orange()
dark_orange = c.Colour.dark_orange()
red = c.Colour.red()
dark_red = c.Colour.dark_red()
lighter_grey = c.Colour.lighter_grey()
dark_grey = c.Colour.dark_grey()
light_grey = c.Colour.light_grey()
darker_grey = c.Colour.darker_grey()
blurple = c.Colour.blurple()
greyple = c.Colour.greyple()


# ---------- 색상표 끝 ----------

@bot.event
async def on_ready():
    print(bot.user)
    print("봇 로그인 됨")
    print(dt_mtn.strftime('%Y/%m/%d'))
    await bot.change_presence(status=discord.Status.online)
    await bot.change_presence(activity=discord.Game(name="Escape from Tarkov"))

    presence_alarm = bot.get_channel(861136275130023976)

    dt_year = (dt_mtn.strftime('%Y'))
    dt_month = (dt_mtn.strftime('%m'))
    dt_day = (dt_mtn.strftime('%d'))
    dt_time = (dt_mtn.strftime('%X'))

    online = discord.Embed(colour=green, title="**Reserver Online!**")
    online.add_field(name='현재 핑', value=f'{round(bot.latency * 1000)}ms')
    online.add_field(name='켜진 시간', value=f'{dt_year}/{dt_month}/{dt_day} {dt_time}')

    await presence_alarm.send(embed=online)


@bot.command(aliases=["ping"])
async def 핑(ctx):
    ping = discord.Embed(colour=blue)
    ping.add_field(name=':green_circle: Reserver 핑', value=f'**Ping : {round(bot.latency * 1000)}ms**', inline=True)
    ping.set_footer(text='Reserver [Tarkov]#8584',
                    icon_url="https://cdn.discordapp.com/attachments/804503457536409620/874812953029926932/img_1.png")
    await ctx.send(embed=ping)


@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(colour=purple, title='📃 Reserver 명령어 리스트')
    embed.add_field(name='🗺 **맵 정보**', value='`!맵 [맵 이름]`')
    embed.add_field(name='🏹 **탄약 정보**', value='`!탄약 [구경]`')
    embed.add_field(name='💡 **봇 상태**', value='`!핑`')
    embed.set_footer(text='개발 : DO_S#0313')
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/804503457536409620/874812953029926932/img_1.png")
    await ctx.send(embed=embed)


@bot.command()
async def 탄약(ctx, *, args):
    if args == "목록":
        ammo_list = discord.Embed(colour=gold, title="📦 탄약 목록")
        ammo_list.add_field(name="권총 탄약",
                            value="```7.62x25mm, 9x18mm, 9x19mm, 9x21mm, .45 ACP```",
                            inline=False)
        ammo_list.add_field(name="PDW탄", value="```4.6x30mm, 5.7x28mm```", inline=False)
        ammo_list.add_field(name="소총탄",
                            value="```5.45x39mm, 5.56x45mm, .300, 7.62x39mm, 7.62x51mm, 7.62x54mmR, .338, 9x39mm, .366, 12.7x55mm, 12.7x108mm```",
                            inline=False)
        ammo_list.add_field(name="산탄", value="```12x70mm, 20x70mm, 23x75mm```", inline=False)
        ammo_list.add_field(name="유탄", value="```30x29mm, 40x46 mm```", inline=False)

        await ctx.send(embed=ammo_list)

    else:
        if args == "5.56x45mm" or args == "5.56x45" or args == "5.56":
            ammo_5_56_45mm = discord.Embed(colour=gold)
            ammo_5_56_45mm.set_author(name="5.56x45mm NATO"
                                      ,
                                      icon_url='https://images-ext-1.discordapp.net/external/_K_Dcb42dq0n6fRZ6YCA8A4ZxCZRnxii4mYfycBV55c/%3Fversion%3Dbf32b6e1010535acf27240bf56221c43/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/c/ce/5.56x45_NATO.gif')
            ammo_5_56_45mm.add_field(name="최고성능", value="M995, M855A1", inline=False)
            ammo_5_56_45mm.add_field(name="가성비", value="M855, M856A1", inline=False)
            ammo_5_56_45mm.add_field(name="4~6 클래스 방어구에 효과적", value="M995, M855A1", inline=False)
            ammo_5_56_45mm.add_field(name="3~4 클래스 이하 방어구에 효과적", value="M855, 55 FMJ", inline=False)
            ammo_5_56_45mm.add_field(name="상세 종류", value="""```
5.56x45 mm 55 FMJ
5.56x45 mm 55 HP
5.56x45 mm M855
5.56x45 mm M855A1
5.56x45 mm M856
5.56x45 mm M856A1
5.56x45 mm M995
5.56x45 mm Mk 255 Mod 0
5.56x45 mm Warmage```""", inline=True)
            ammo_5_56_45mm.add_field(name="사용 무기", value="""```
Assault rifles:
    ADAR 2-15
    AK-101
    AK-102
    DT MDR 5.56x45
    HK 416A5
    M4A1
    TX-15 DML```""", inline=True)

            await ctx.send(embed=ammo_5_56_45mm)

        elif args == ".366":
            ammo_366 = discord.Embed(colour=gold)
            ammo_366.set_author(name=".366 TKM"
                                ,
                                icon_url='https://images-ext-2.discordapp.net/external/uFxThmSv77znUrWFKG6a0MdGXISx5ASNPt-DoeN7kxo/%3Fversion%3Dc9b1e8b857006ac86baf9a190175447c/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/3/39/.366_TKM.gif')
            ammo_366.add_field(name='최고성능', value='AP', inline=False)
            ammo_366.add_field(name='우호도 레벨 1 이상 상인에게서 구매 가능', value='FMJ', inline=False)
            ammo_366.add_field(name='1 클래스 이하의 방어구에 매우 효과적', value='Geksa', inline=False)
            ammo_366.add_field(name='2~3 클래스 이하의 방어구에 매우 효과적', value='FMJ, EKO', inline=False)
            ammo_366.add_field(name='5 클래스 이하의 방어구에 매우 효과적', value='AP', inline=False)
            ammo_366.add_field(name='상세종류', value="""```
.366 AP
.366 TKM EKO
.366 TKM FMJ
.366 TKM Geksa```""", inline=True)
            ammo_366.add_field(name='사용 무기', value="""```
Assault rifles:
Vepr AKM/VPO-209

Sniper rifles:
VPO-215```""")

            await ctx.send(embed=ammo_366)

        elif args == ".45":
            ammo_45 = discord.Embed(colour=gold)
            ammo_45.set_author(name=".45 ACP"
                               ,
                               icon_url='https://images-ext-2.discordapp.net/external/eVvZwCusDYEC37KJFra5GBgurPnkfsaDsapgbf4N-Po/%3Fversion%3D63967d4d1c016e2c20e24fded8e7e850/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/1/12/.45_Icon.gif')
            ammo_45.add_field(name="최고성능", value="RIP, ACP FMJ", inline=False)
            ammo_45.add_field(name="방어구를 입지 않은 적에게 효과적", value="RIP", inline=False)
            ammo_45.add_field(name="1~2 클래스 방어구에 효과적", value="ACP FMJ", inline=False)
            ammo_45.add_field(name="상세 종류", value="""```
.45 ACP FMJ
.45 RIP```""", inline=True)
            ammo_45.add_field(name="사용 무기", value="""```
Pistol:
M1911A1```""", inline=True)
            await ctx.send(embed=ammo_45)

        elif args == "12.7x55mm" or args == "12.7x55":
            ammo_12_7_55mm = discord.Embed(colour=gold)
            ammo_12_7_55mm.set_author(name="12.7x55mm Sts-130"
                                 ,
                                 icon_url='https://images-ext-2.discordapp.net/external/poXpvnavXvbroL4221Hx_PSrYAYMl94lr_5D5_9Te9I/%3Fversion%3Df0106cb488cf6b6bf7277d09925150c0/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/7/78/12.7x55.gif')
            ammo_12_7_55mm.add_field(name="최고성능", value="PS12B", inline=False)
            ammo_12_7_55mm.add_field(name="1 클래스 이하의 방어구에 매우 효과적", value="PS12A", inline=False)
            ammo_12_7_55mm.add_field(name="3 클래스 이하의 방어구에 매우 효과적", value="PS12", inline=False)
            ammo_12_7_55mm.add_field(name="5 클래스 이하의 방어구에 매우 효과적", value="PS12B", inline=False)
            ammo_12_7_55mm.add_field(name="상세종류", value="""```
12.7x55mm PS12
12.7x55mm PS12A
12.7x55mm PS12B```""", inline=True)
            ammo_12_7_55mm.add_field(name="사용 무기", value="""```
Assault rifles:
    Ash-12```""", inline=True)

            await ctx.send(embed=ammo_12_7_55mm)

        elif args == "12.7x108mm" or args == "12.7x108":
            ammo_12_7_108mm = discord.Embed(colour=gold)
            ammo_12_7_108mm.set_author(name="12.7x108mm"
                                      ,
                                      icon_url='https://images-ext-2.discordapp.net/external/poXpvnavXvbroL4221Hx_PSrYAYMl94lr_5D5_9Te9I/%3Fversion%3Df0106cb488cf6b6bf7277d09925150c0/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/7/78/12.7x55.gif')
            ammo_12_7_108mm.add_field(name="6 클래스 방어구 관통, 매우 효과적", value="B-32, BZT-44M", inline=False)
            ammo_12_7_108mm.add_field(name="상세종류", value="""```
12.7x108mm B-32
12.7x108mm BZT-44M```""", inline=True)
            ammo_12_7_108mm.add_field(name="사용 무기", value="""```
HMGs:
    NSV "Utes"```""", inline=True)

            await ctx.send(embed=ammo_12_7_108mm)

        elif args == "12.7":
            ammo_12_7_55mm = discord.Embed(colour=gold)
            ammo_12_7_55mm.set_author(name="12.7x55mm Sts-130"
                                      ,
                                      icon_url='https://images-ext-2.discordapp.net/external/poXpvnavXvbroL4221Hx_PSrYAYMl94lr_5D5_9Te9I/%3Fversion%3Df0106cb488cf6b6bf7277d09925150c0/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/7/78/12.7x55.gif')
            ammo_12_7_55mm.add_field(name="최고성능", value="PS12B", inline=False)
            ammo_12_7_55mm.add_field(name="1 클래스 이하의 방어구에 매우 효과적", value="PS12A", inline=False)
            ammo_12_7_55mm.add_field(name="3 클래스 이하의 방어구에 매우 효과적", value="PS12", inline=False)
            ammo_12_7_55mm.add_field(name="5 클래스 이하의 방어구에 매우 효과적", value="PS12B", inline=False)
            ammo_12_7_55mm.add_field(name="상세종류", value="""```
12.7x55mm PS12
12.7x55mm PS12A
12.7x55mm PS12B```""", inline=True)
            ammo_12_7_55mm.add_field(name="사용 무기", value="""```
Assault rifles:
    Ash-12```""", inline=True)

            ammo_12_7_108mm = discord.Embed(colour=gold)
            ammo_12_7_108mm.set_author(name="12.7x108mm"
                                       ,
                                       icon_url='https://images-ext-2.discordapp.net/external/poXpvnavXvbroL4221Hx_PSrYAYMl94lr_5D5_9Te9I/%3Fversion%3Df0106cb488cf6b6bf7277d09925150c0/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/7/78/12.7x55.gif')
            ammo_12_7_108mm.add_field(name="6 클래스 방어구 관통, 매우 효과적", value="B-32, BZT-44M", inline=False)
            ammo_12_7_108mm.add_field(name="상세종류", value="""```
12.7x108mm B-32
12.7x108mm BZT-44M```""", inline=True)
            ammo_12_7_108mm.add_field(name="사용 무기", value="""```
HMGs:
    NSV "Utes"```""", inline=True)

            await ctx.send(embed=ammo_12_7_108mm)

            await ctx.send(embed=ammo_12_7_55mm)

        elif args == "12x70mm" or args == "12x70" or args == "12ga":
            ammo_12_70mm = discord.Embed(colour=gold)
            ammo_12_70mm.set_author(name="12x70mm"
                                    ,
                                    icon_url='https://images-ext-1.discordapp.net/external/l5gDMOHPsWo83QNAuyiNUYN1AKFreqR-rJ3j6hY4t4A/%3Fversion%3D41ffae1304dd29cf788f6469a849bc33/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/9/92/12x70.gif')
            ammo_12_70mm.add_field(name="우호도 레벨 1 상인에게서 구매 가능", value="""5.25mm Buckshot, 7mm Buckshot, Led slug, "Poleva-3" Slug""", inline=False)
            ammo_12_70mm.add_field(name="모든 방어구 클래스에 약간 효과적", value="""5.25mm Buckshot, 8.5 mm "Magnum" Buckshot, 6.5 mm "Express" Buckshot, 7mm Buckshot""", inline=False)
            ammo_12_70mm.add_field(name="방어구를 입지 않은 적에게 매우 효과적", value="""RIP, HP Slug "SuperFormance" """, inline=False)
            ammo_12_70mm.add_field(name="1 클래스 이하의 방어구에 효과적", value="""Grizzly 40 Slug, HP Slug Copper Sabot Premier, Led slug""", inline=False)
            ammo_12_70mm.add_field(name="1~2 클래스 이하의 방어구에 효과적", value=""""Poleva-3" Slug, Dual Sabot Slug, FTX Custom LIte Slug, "Poleva-6u" Slug""", inline=False)
            ammo_12_70mm.add_field(name="3~6 클래스 방어구에 효과적", value="Flechette", inline=False)
            ammo_12_70mm.add_field(name="3~4 클래스 이하의 방어구에 효과적", value="""shell with .50 BMG bullet, AP-20 Slug""", inline=False)
            ammo_12_70mm.add_field(name="상세 종류", value="""```
12/70 5.25mm Buckshot
12x70 6.5 mm "Express" Buckshot
12x70 7mm Buckshot
12/70 8.5 mm "Magnum" Buckshot
12/70 AP-20 Slug
12/70 Dual Sabot Slug
12/70 Flechette
12/70 FTX Custom LIte Slug
12/70 Grizzly 40 Slug
12/70 HP Slug Copper Sabot Premier
12/70 HP Slug "SuperFormance"
12x70 Led slug
12/70 "Poleva-3" Slug
12/70 "Poleva-6u" Slug
12x70 RIP
12x70 shell with .50 BMG bullet```""")
            ammo_12_70mm.add_field(name="사용 무기", value="""```
Shotguns:
    590A1
    M870
    MP-133
    MP-153
    Saiga-12```""")
            await ctx.send(embed=ammo_12_70mm)

        elif args == "20x70mm" or args == "20x70" or args == "20ga":
            ammo_20_70mm = discord.Embed(colour=gold)
            ammo_20_70mm.set_author(name="20x70mm"
                                    ,
                                    icon_url='https://images-ext-1.discordapp.net/external/pHC5gleSVGgzmmoeNkxGnrZf-5_l_QQaTBrsO_q4OkA/%3Fversion%3Dd18fedabeec0b5d9a1282686a1e399df/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/6/63/20-70.gif')
            ammo_20_70mm.add_field(name="모든 방어구 클래스에 약간 효과적", value="5.6mm Buckshot, 6.2mm Buckshot, 7.5mm Buckshot, 7.3mm Buckshot", inline=False)
            ammo_20_70mm.add_field(name="방어구를 입지 않은 적에게 매우 효과적", value="Devastator Slug", inline=False)
            ammo_20_70mm.add_field(name="1 클래스 이하의 방어구에 매우 효과적", value="""Slug "Poleva-3" """, inline=False)
            ammo_20_70mm.add_field(name="1~2 클래스 이하의 방어구에 매우 효과적", value="Star Slug, Slug Poleva-6u", inline=False)
            ammo_20_70mm.add_field(name="상세 종류", value="""```
20/70 5.6mm Buckshot
20/70 6.2mm Buckshot
20/70 7.3mm Buckshot
20x70 7.5mm Buckshot
20/70 Devastator Slug
20/70 Slug "Poleva-3"
20/70 Slug Poleva-6u
20/70 Star Slug```""", inline=True)
            ammo_20_70mm.add_field(name="사용 무기", value="""```
Shotguns:
    TOZ-106```""")

            await ctx.send(embed=ammo_20_70mm)

        elif args == "4.6x30mm" or args == "4.6x30" or args == "4.6":
            ammo_4_6_30mm = discord.Embed(colour=gold)
            ammo_4_6_30mm.set_author(name="4.6x30mm HK"
                                     ,
                                     icon_url='https://images-ext-2.discordapp.net/external/ivuFTCkuiwFhcD382JniFg1hYG5JEbLzskBV3Wjs6Tk/%3Fversion%3Dcedf8d2b62f583c0bc9622c05044f2ad/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/0/05/4.6x30.gif')
            ammo_4_6_30mm.add_field(name="최고 성능", value="AP SX, FMJ SX", inline=False)
            ammo_4_6_30mm.add_field(name="방어구를 입지 않은 적에게 효과적", value="Action SX", inline=False)
            ammo_4_6_30mm.add_field(name="5-6 클래스 방어구에 효과적", value="AP SX", inline=False)
            ammo_4_6_30mm.add_field(name="상세 종류", value="""```
4.6x30mm Action SX
4.6x30mm AP SX
4.6x30mm FMJ SX
4.6x30mm Subsonic SX```""", inline=True)
            ammo_4_6_30mm.add_field(name="사용 무기", value="""```
SMGs:
    MP7A1
    MP7A2```""", inline=True)

            await ctx.send(embed=ammo_4_6_30mm)

        elif args == "5.45x39mm" or args == "5.45x39" or args == "5.45":
            ammo_5_45_39mm = discord.Embed(colour=gold)
            ammo_5_45_39mm.set_author(name='5.45x39mm'
                                      ,
                                      icon_url='https://images-ext-1.discordapp.net/external/seyt563VfxPAQ4VpmQf7ZZeS_MA3XhjMY2bJXFAtKZA/%3Fversion%3D085f3db32282652bede65cbc1c594edc/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/3/34/5.45x39.gif')
            ammo_5_45_39mm.add_field(name="최고 성능", value="7N39, BS", inline=False)
            ammo_5_45_39mm.add_field(name="가성비", value="BT", inline=False)
            ammo_5_45_39mm.add_field(name="5-6 클래스 방어구에 효과적", value="7N39, BS", inline=False)
            ammo_5_45_39mm.add_field(name="4 클래스 이하의 방어구에 효과적", value="BT", inline=False)
            ammo_5_45_39mm.add_field(name="우호도 레벨 1 상인에게서 구매 가능", value="BT, BP, PS, FMJ, T, PRS", inline=False)
            ammo_5_45_39mm.add_field(name="상세 종류", value="""```
5.45x39 mm 7N39 "Igolnik"
5.45x39 mm BP
5.45x39 mm BS
5.45x39 mm BT
5.45x39 mm FMJ
5.45x39 mm HP
5.45x39 mm PP
5.45x39 mm PRS
5.45x39 mm PS
5.45x39 mm SP
5.45x39 mm T
5.45x39 mm US```""", inline=True)
            ammo_5_45_39mm.add_field(name="사용 무기", value="""```
Assault rifles:
    AK-105
    AK-74
    AK-74M
    AK-74N
    AKS-74
    AKS-74N
    AKS-74U
    AKS-74UB
    AKS-74UN```""", inline=True)

            await ctx.send(embed=ammo_5_45_39mm)

        elif args == "5.7x28mm" or args == "5.7x28" or args == "5.7":
            ammo_5_7_28mm = discord.Embed(colour=gold)
            ammo_5_7_28mm.set_author(name="5.7x28mm FN"
                                     ,
                                     icon_url='https://images-ext-2.discordapp.net/external/YB1FVk73crSmYllbAq9mLsdvJjNCYKAVoxTd8c4qfW8/%3Fversion%3Db091b9e424fb51a4518088d3f4169f09/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/9/97/5.7x28.gif')
            ammo_5_7_28mm.add_field(name="최고 성능", value="SS190, SB193", inline=False)
            ammo_5_7_28mm.add_field(name="방어구를 입지 않은 적에게 효과적", value="R37.F", inline=False)
            ammo_5_7_28mm.add_field(name="3~4 클래스 방어구에 효과적", value="SS190, SB193", inline=False)
            ammo_5_7_28mm.add_field(name="상세 종류", value="""```
5.7x28 mm L191
5.7x28 mm R37.F
5.7x28 mm R37.X
5.7x28 mm SB193
5.7x28 mm SS190
5.7x28 mm SS197SR
5.7x28 mm SS198LF```""", inline=True)
            ammo_5_7_28mm.add_field(name="사용 무기" , value="""```
Pistols:
    FN 5-7

SMGs:
    P90```""", inline=True)

            await ctx.send(embed=ammo_5_7_28mm)

        elif args == "7.62x25mm" or args == "7.62x25":
            ammo_7_62_25mm = discord.Embed(colour=gold)
            ammo_7_62_25mm.set_author(name="7.62x25mm Tokarev"
                                      ,
                                      icon_url='https://images-ext-2.discordapp.net/external/gkJeiqhRjMhg_Jz33Rsk9CkuU_nSzE4yZFhq37mja_g/%3Fversion%3D4949252643f6a38658e6bc8308e8930c/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/f/ff/TT_7.62x25.gif')
            ammo_7_62_25mm.add_field(name="최고성능", value="Pst gzh, LRNPC", inline=False)
            ammo_7_62_25mm.add_field(name="가성비", value="Pst gzh, LRNPC", inline=False)
            ammo_7_62_25mm.add_field(name="우호도 레벨 1 상인에게서 구매 가능", value="AKBS, FMJ43, LRN", inline=False)
            ammo_7_62_25mm.add_field(name="방어구를 입지 않은 적에게 효과적", value="LRNPC", inline=False)
            ammo_7_62_25mm.add_field(name="1~3 클래스 방어구에 효과적", value="Pst gzh", inline=False)
            ammo_7_62_25mm.add_field(name="상세 종류", value="""```
7.62x25mm TT AKBS
7.62x25mm TT FMJ43
7.62x25mm TT LRN
7.62x25mm TT LRNPC
7.62x25mm TT P gl
7.62x25mm TT Pst gzh
7.62x25mm TT PT gzh```""", inline=True)
            ammo_7_62_25mm.add_field(name="사용 무기", value="""```
Pistols:
    TT pistol
    TT pistol (gold)

SMGs:
    PPSH-41```""", inline=True)

            await ctx.send(embed=ammo_7_62_25mm)

        elif args == "7.62x39mm" or args == "7.62x39":
            ammo_7_62_39mm = discord.Embed(colour=gold)
            ammo_7_62_39mm.set_author(name="7.62x39mm"
                                      ,
                                      icon_url='https://images-ext-2.discordapp.net/external/XqtzEILLOWRw-3JCWI1tkxjzVOnt-GpRJ6Jxlkjh2bg/%3Fversion%3D1be7daae85ee44fd47169c0be1896a59/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/9/9f/7.62x39.gif')
            ammo_7_62_39mm.add_field(name="최고 성능", value="BP", inline=False)
            ammo_7_62_39mm.add_field(name="가성비", value="PS", inline=False)
            ammo_7_62_39mm.add_field(name="4~5 클래스 방어구에 효과적", value="BP", inline=False)
            ammo_7_62_39mm.add_field(name="3~4 클래스 이하의 방어구에 효과적", value="PS", inline=False)
            ammo_7_62_39mm.add_field(name="상세 종류", value="""```
7.62x39 mm BP
7.62x39 mm HP
7.62x39 mm PS
7.62x39 mm T45M
7.62x39 mm US```""", inline=True)
            ammo_7_62_39mm.add_field(name="사용 무기", value="""```
Assault carbines:
    OP-SKS
    SKS

Assault rifles:
    AK-103
    AK-104
    AKM
    AKMN
    AKMS
    AKMSN
    Vepr KM/VPO-136```""", inline=True)

            await ctx.send(embed=ammo_7_62_39mm)

        elif args == "7.62x51mm" or args == "7.62x51":
            ammo_7_62_51mm = discord.Embed(colour=gold)
            ammo_7_62_51mm.set_author(name="7.62x51mm NATO"
                                      ,
                                      icon_url='https://images-ext-1.discordapp.net/external/RAt3SD7oIflrL9gQ6h0eCvpkPOPpRHTDEL70FMXSpjM/%3Fversion%3D7412bd55a2ee6eff524c35b81387cea5/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/1/1f/7.62x51_NATO.gif')
            ammo_7_62_51mm.add_field(name="최고 성능", value="M61, M62, M993", inline=False)
            ammo_7_62_51mm.add_field(name="가성비", value="M80", inline=False)
            ammo_7_62_51mm.add_field(name="우호도 레벨 1 상인에게서 구매 가능", value="TPZ SP", inline=False)
            ammo_7_62_51mm.add_field(name="방어구를 입지 않은 적에게 매우 효과적", value="Ultra Nosler", inline=False)
            ammo_7_62_51mm.add_field(name="4~5 클래스 이하의 방어구에 효과적", value="M80, TPZ SP", inline=False)
            ammo_7_62_51mm.add_field(name="5~6 클래스 방어구에 효과적", value="M61, M62", inline=False)
            ammo_7_62_51mm.add_field(name="6 클래스 방어구 완전 관통", value="M61, M993", inline=False)
            ammo_7_62_51mm.add_field(name="상세 종류", value="""```
7.62x51 mm BPZ FMJ
7.62x51 mm M61
7.62x51 mm M62
7.62x51 mm M80
7.62x51 mm M993
7.62x51 mm TPZ SP
7.62x51 mm Ultra Nosler```""", inline=True)
            ammo_7_62_51mm.add_field(name="사용 무기", value="""```
Assault carbines:
    Vepr Hunter/VPO-101

Assault rifles:
    SA-58
    DT MDR .308

DMRs:
    M1A
    RSASS
    SR-25

Sniper rifles:
    DVL-10
    M700
    T-5000```""", inline=True)

            await ctx.send(embed=ammo_7_62_51mm)

        elif args == "7.62x54mmR" or args == "7.62x54R" or args == "7.62x54":
            ammo_7_62_54mm = discord.Embed(colour=gold)
            ammo_7_62_54mm.set_author(name="7.62x54mmR"
                                      ,
                                      icon_url='https://images-ext-1.discordapp.net/external/QTomJi-VZpc32_hnVgtSactcKunPxQpsngYYV65gHcw/%3Fversion%3D54cf97e9a230c556df82fd0201cbabcb/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/5/59/7.62x54R.gif')
            ammo_7_62_54mm.add_field(name="최고 성능", value="7N37, SNB, 7N1", inline=False)
            ammo_7_62_54mm.add_field(name="가성비", value="LPS Gzh", inline=False)
            ammo_7_62_54mm.add_field(name="우호도 레벨 1 상인에게서 구매 가능", value="LPS Gzh", inline=False)
            ammo_7_62_54mm.add_field(name="6 클래스에까지 효과 있음, 가장 데미지 높음", value="7N1", inline=False)
            ammo_7_62_54mm.add_field(name="6 클래스 방어구 완전 관통", value="7N37, SNB, 7BT1", inline=False)
            ammo_7_62_54mm.add_field(name="상세 종류", value="""```
7.62x54R 7BT1
7.62x54R 7N1 Sniper cartridge
7.62x54R 7N37
7.62x54R LPS Gzh
7.62x54R SNB
7.62x54R T-46M```""", inline=True)
            ammo_7_62_54mm.add_field(name="사용 무기", value="""```
DMRs:
    SVDS

Sniper rifles:
    Mosin
    Mosin Inf.
    SV-98```""", inline=True)

            await ctx.send(embed=ammo_7_62_54mm)

        elif args == "7.62":
            ammo_7_62_25mm = discord.Embed(colour=gold)
            ammo_7_62_25mm.set_author(name="7.62x25mm Tokarev"
                                      ,
                                      icon_url='https://images-ext-2.discordapp.net/external/gkJeiqhRjMhg_Jz33Rsk9CkuU_nSzE4yZFhq37mja_g/%3Fversion%3D4949252643f6a38658e6bc8308e8930c/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/f/ff/TT_7.62x25.gif')
            ammo_7_62_25mm.add_field(name="최고성능", value="Pst gzh, LRNPC", inline=False)
            ammo_7_62_25mm.add_field(name="가성비", value="Pst gzh, LRNPC", inline=False)
            ammo_7_62_25mm.add_field(name="우호도 레벨 1 상인에게서 구매 가능", value="AKBS, FMJ43, LRN", inline=False)
            ammo_7_62_25mm.add_field(name="방어구를 입지 않은 적에게 효과적", value="LRNPC", inline=False)
            ammo_7_62_25mm.add_field(name="1~3 클래스 방어구에 효과적", value="Pst gzh", inline=False)
            ammo_7_62_25mm.add_field(name="상세 종류", value="""```
7.62x25mm TT AKBS
7.62x25mm TT FMJ43
7.62x25mm TT LRN
7.62x25mm TT LRNPC
7.62x25mm TT P gl
7.62x25mm TT Pst gzh
7.62x25mm TT PT gzh```""", inline=True)
            ammo_7_62_25mm.add_field(name="사용 무기", value="""```
Pistols:
    TT pistol
    TT pistol (gold)

SMGs:
    PPSH-41```""", inline=True)

            ammo_7_62_39mm = discord.Embed(colour=gold)
            ammo_7_62_39mm.set_author(name="7.62x39mm"
                                      ,
                                      icon_url='https://images-ext-2.discordapp.net/external/XqtzEILLOWRw-3JCWI1tkxjzVOnt-GpRJ6Jxlkjh2bg/%3Fversion%3D1be7daae85ee44fd47169c0be1896a59/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/9/9f/7.62x39.gif')
            ammo_7_62_39mm.add_field(name="최고 성능", value="BP", inline=False)
            ammo_7_62_39mm.add_field(name="가성비", value="PS", inline=False)
            ammo_7_62_39mm.add_field(name="4~5 클래스 방어구에 효과적", value="BP", inline=False)
            ammo_7_62_39mm.add_field(name="3~4 클래스 이하의 방어구에 효과적", value="PS", inline=False)
            ammo_7_62_39mm.add_field(name="상세 종류", value="""```
7.62x39 mm BP
7.62x39 mm HP
7.62x39 mm PS
7.62x39 mm T45M
7.62x39 mm US```""", inline=True)
            ammo_7_62_39mm.add_field(name="사용 무기", value="""```
Assault carbines:
    OP-SKS
    SKS

Assault rifles:
    AK-103
    AK-104
    AKM
    AKMN
    AKMS
    AKMSN
    Vepr KM/VPO-136```""", inline=True)

            ammo_7_62_51mm = discord.Embed(colour=gold)
            ammo_7_62_51mm.set_author(name="7.62x51mm NATO"
                                      ,
                                      icon_url='https://images-ext-1.discordapp.net/external/RAt3SD7oIflrL9gQ6h0eCvpkPOPpRHTDEL70FMXSpjM/%3Fversion%3D7412bd55a2ee6eff524c35b81387cea5/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/1/1f/7.62x51_NATO.gif')
            ammo_7_62_51mm.add_field(name="최고 성능", value="M61, M62, M993", inline=False)
            ammo_7_62_51mm.add_field(name="가성비", value="M80", inline=False)
            ammo_7_62_51mm.add_field(name="우호도 레벨 1 상인에게서 구매 가능", value="TPZ SP", inline=False)
            ammo_7_62_51mm.add_field(name="방어구를 입지 않은 적에게 매우 효과적", value="Ultra Nosler", inline=False)
            ammo_7_62_51mm.add_field(name="4~5 클래스 이하의 방어구에 효과적", value="M80, TPZ SP", inline=False)
            ammo_7_62_51mm.add_field(name="5~6 클래스 방어구에 효과적", value="M61, M62", inline=False)
            ammo_7_62_51mm.add_field(name="6 클래스 방어구 완전 관통", value="M61, M993", inline=False)
            ammo_7_62_51mm.add_field(name="상세 종류", value="""```
7.62x51 mm BPZ FMJ
7.62x51 mm M61
7.62x51 mm M62
7.62x51 mm M80
7.62x51 mm M993
7.62x51 mm TPZ SP
7.62x51 mm Ultra Nosler```""", inline=True)
            ammo_7_62_51mm.add_field(name="사용 무기", value="""```
Assault carbines:
    Vepr Hunter/VPO-101

Assault rifles:
    SA-58
    DT MDR .308

DMRs:
    M1A
    RSASS
    SR-25

Sniper rifles:
    DVL-10
    M700
    T-5000```""", inline=True)

            ammo_7_62_54mm = discord.Embed(colour=gold)
            ammo_7_62_54mm.set_author(name="7.62x54mmR"
                                      ,
                                      icon_url='https://images-ext-1.discordapp.net/external/QTomJi-VZpc32_hnVgtSactcKunPxQpsngYYV65gHcw/%3Fversion%3D54cf97e9a230c556df82fd0201cbabcb/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/5/59/7.62x54R.gif')
            ammo_7_62_54mm.add_field(name="최고 성능", value="7N37, SNB, 7N1", inline=False)
            ammo_7_62_54mm.add_field(name="가성비", value="LPS Gzh", inline=False)
            ammo_7_62_54mm.add_field(name="우호도 레벨 1 상인에게서 구매 가능", value="LPS Gzh", inline=False)
            ammo_7_62_54mm.add_field(name="6 클래스에까지 효과 있음, 가장 데미지 높음", value="7N1", inline=False)
            ammo_7_62_54mm.add_field(name="6 클래스 방어구 완전 관통", value="7N37, SNB, 7BT1", inline=False)
            ammo_7_62_54mm.add_field(name="상세 종류", value="""```
7.62x54R 7BT1
7.62x54R 7N1 Sniper cartridge
7.62x54R 7N37
7.62x54R LPS Gzh
7.62x54R SNB
7.62x54R T-46M```""", inline=True)
            ammo_7_62_54mm.add_field(name="사용 무기", value="""```
DMRs:
    SVDS

Sniper rifles:
    Mosin
    Mosin Inf.
    SV-98```""", inline=True)

            await ctx.send(embed=ammo_7_62_25mm)
            await ctx.send(embed=ammo_7_62_39mm)
            await ctx.send(embed=ammo_7_62_51mm)
            await ctx.send(embed=ammo_7_62_54mm)

        elif args == "9x18mm" or args == "9x18":
            ammo_9_18mm = discord.Embed(colour=gold)
            ammo_9_18mm.set_author(name="9x18mm Makarov"
                                   ,
                                   icon_url="https://images-ext-2.discordapp.net/external/EGJOPgryIk3LcWB9JHAkKEFbCVEjMVATnRiUt3KRzPg/%3Fversion%3D99ed656ae09b19dd9783ea85e5645566/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/c/c2/9x18_PM.gif")
            ammo_9_18mm.add_field(name="최고 성능", value="PMM, PBM, SP8 gzh", inline=False)
            ammo_9_18mm.add_field(name="가성비", value="Pst gzh", inline=False)
            ammo_9_18mm.add_field(name="방어구를 입지 않은 적에게 효과적", value="SP7, SP8", inline=False)
            ammo_9_18mm.add_field(name="1 클래스 방어구에 효과적", value="Pst gzh", inline=False)
            ammo_9_18mm.add_field(name="상세 종류", value="""```
9x18 mm PM 9 BZT gzh
9x18 mm PM 9 P gzh
9x18 mm PM PBM
9x18 mm PM PMM
9x18 mm PM PPe gzh
9x18 mm PM PPT gzh
9x18 mm PM PRS gs
9x18 mm PM PS gs PPO
9x18 mm PM PSO gzh
9x18 mm PM Pst gzh
9x18 mm PM PSV
9x18 PM mm RG028 gzh
9x18 mm PM SP7 gzh
9x18 mm PM SP8 gzh```""", inline=True)
            ammo_9_18mm.add_field(name="사용 무기", value="""```
Pistols:
    APB
    PB pistol
    PM (t) pistol
    PM pistol

SMGs:
    PP-9 "Klin"
    PP-91 "Kedr"
    pp-91-01 "Kedr-B"```""", inline=True)

            await ctx.send(embed=ammo_9_18mm)

        elif args == "9x19mm" or args == "9x19":
            ammo_9_19mm = discord.Embed(colour=gold)
            ammo_9_19mm.set_author(name="9x19mm Parabellum"
                                   ,
                                   icon_url='https://images-ext-2.discordapp.net/external/litvvTzPGp_oyHBMDoaZWPoOCit-5PlnCN8p9nOg-Ws/%3Fversion%3D1937b477b094f3c53ff668cc813d1a63/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/d/db/9x19_para.gif')
            ammo_9_19mm.add_field(name="최고 성능", value="7N31, AP 6.3, Luger CCI, RIP, QuakeMaker", inline=False)
            ammo_9_19mm.add_field(name="가성비", value="Pst gzh", inline=False)
            ammo_9_19mm.add_field(name="우호도 레벨 1 상인에게서 구매 가능", value="PSO gzh, Pst gzh", inline=False)
            ammo_9_19mm.add_field(name="방어구를 입지 않은 적에게 매우 효과적", value="RIP", inline=False)
            ammo_9_19mm.add_field(name="1 클래스 이하의 방어구에 매우 효과적", value="QuakeMaker", inline=False)
            ammo_9_19mm.add_field(name="1~2 클래스 방어구에 효과적", value="Luger CCI, Pst gzh", inline=False)
            ammo_9_19mm.add_field(name="2~3 클래스 방어구에 효과적", value="AP 6.3", inline=False)
            ammo_9_19mm.add_field(name="4 클래스 방어구에까지 효과 있음", value="7N31", inline=False)
            ammo_9_19mm.add_field(name="상세 종류", value="""```
9x19 mm 7N31
9x19 mm AP 6.3
9x19 mm Green Tracer
9x19 mm Luger CCI
9x19 mm PSO gzh
9x19 mm Pst gzh
9x19 mm QuakeMaker
9x19 mm RIP```""", inline=True)
            ammo_9_19mm.add_field(name="사용 무기", value="""```
Pistols:
    GLOCK17
    GLOCK18C
    M9A3
    MP-443 "Grach"
    P226R

SMGs:
    MP5
    MP5K-N
    MPX
    PP-19-01 Vityaz-SN
    Saiga-9
    MP9
    MP9-N```""", inline=True)
            await ctx.send(embed=ammo_9_19mm)

        elif args == "9x21mm" or args == "9x21":
            ammo_9_21mm = discord.Embed(colour=gold)
            ammo_9_21mm.set_author(name="9x21mm Gyurza"
                                   ,
                                   icon_url='https://images-ext-1.discordapp.net/external/jGPMFRvzGZ8355kXvGmuEHabKud-Ho0mL92X-VZMxXA/%3Fversion%3De98e984060a4661f83efd39ec603425e/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/5/53/9x21_gyurza.gif')
            ammo_9_21mm.add_field(name="최고 성능", value="SP13", inline=False)
            ammo_9_21mm.add_field(name="가성비", value="SP11", inline=False)
            ammo_9_21mm.add_field(name="방어구를 입지 않은 적에게 효과적", value="SP12", inline=False)
            ammo_9_21mm.add_field(name="2~4 클래스 방어구에 효과적", value="SP13, SP10", inline=False)
            ammo_9_21mm.add_field(name="상세 종류", value="""```
9x21 mm SP10
9x21 mm SP11
9x21 mm SP12
9x21 mm SP13```""", inline=True)
            ammo_9_21mm.add_field(name="사용 무기", value="""```
Pistols:
    SR-1MP Gyurza```""", inline=True)

            await ctx.send(embed=ammo_9_21mm)

        elif args == "9x39mm" or args == "9x39":
            ammo_9_39mm = discord.Embed(colour=gold)
            ammo_9_39mm.set_author(name=""
                                   ,
                                   icon_url='https://images-ext-1.discordapp.net/external/feaZCL4bQKZ4Fdyo3vimFuUplB4gYQJKdwZ32GAdxlk/%3Fversion%3D75c3300cd1dcff5977fd9a4f4903f7ff/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/2/29/9x39.gif')
            ammo_9_39mm.add_field(name="최고 성능", value="7N12 BP, 7N9 SPP, SP-6", inline=False)
            ammo_9_39mm.add_field(name="가성비", value="SP-5, SP-6", inline=False)
            ammo_9_39mm.add_field(name="4~6 클래스 방어구에 매우 효과적", value="7N12 BP", inline=False)
            ammo_9_39mm.add_field(name="6 클래스 방어구까지 효과적, 5 클래스 이하의 방어구에 매우 효과적", value="7N9 SPP, SP-6", inline=False)
            ammo_9_39mm.add_field(name="상세 종류", value="""```
9x39 mm 7N9 SPP
9x39 mm 7N12 BP
9x39 mm SP-5
9x39 mm SP-6```""", inline=True)
            ammo_9_39mm.add_field(name="사용 무기", value="""```
Assault carbines:
    AS VAL

DMRs:
    VSS Vintorez```""", inline=True)

            await ctx.send(embed=ammo_9_39mm)

        else:
            ammo_list = discord.Embed(colour=gold, title="📦 탄약 목록")
            ammo_list.add_field(name="권총 탄약",
                                value="```7.62x25mm, 9x18mm, 9x19mm, 9x21mm, .45 ACP```",
                                inline=False)
            ammo_list.add_field(name="PDW탄", value="```4.6x30mm, 5.7x28mm```", inline=False)
            ammo_list.add_field(name="소총탄",
                                value="```5.45x39mm, 5.56x45mm, .300, 7.62x39mm, 7.62x51mm, 7.62x54mmR, .338, 9x39mm, .366, 12.7x55mm, 12.7x108mm```",
                                inline=False)
            ammo_list.add_field(name="산탄", value="```12x70mm, 20x70mm, 23x75mm```", inline=False)
            ammo_list.add_field(name="유탄", value="```30x29mm, 40x46 mm```", inline=False)

            await ctx.send('❌ **존재 하지 않는 탄약 이름입니다!** (아래의 탄약 목록을 확인해주세요)')
            await ctx.send(embed=ammo_list)


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def 맵(ctx, *, args):
    if args == "목록":
        map_list = discord.Embed(colour=blue, title='🗺 **맵 목록**')
        map_list.add_field(name='공장(Factory)', value='```보스 : Tagilla(타길라) 18%```')
        map_list.add_field(name='세관(Customs)', value='```보스 : Reshala(르샬라) 35%```')
        map_list.add_field(name='삼림(Woods)', value='```보스 : Shturman(슈트르만) 41%```')
        map_list.add_field(name='해안선(Shoreline)', value='```보스 : Sanitar(세니타) 35%```')
        map_list.add_field(name='나들목(Interchange)', value='```보스 : Killa(킬라) 38%```')
        map_list.add_field(name='연구소(The lab)', value='```보스 : X```')
        map_list.add_field(name='리저브(Reserve)', value='```보스 : Glukhar(글루하) 41%```')
        await ctx.send(embed=map_list)

    else:
        if args == "공장" or args == "팩토리" or args == "Factory":
            factory = discord.Embed(colour=blue, title='공장(Factory)')
            factory.set_image(
                url='https://cdn.discordapp.com/attachments/804503457536409620/874820779542454312/EFT_-_v0.12.8.png')

            await ctx.send(embed=factory)

        elif args == "세관" or args == "커스텀" or args == "Customs":
            customs = discord.Embed(colour=blue, title='세관(Customs)')
            customs.set_image(
                url='https://cdn.discordapp.com/attachments/804503457536409620/874820772953194546/EFT_-_v0.12.8.png')

            await ctx.send(embed=customs)

        elif args == "삼림" or args == "우드" or args == "Woods":
            woods = discord.Embed(colour=blue, title='삼림(Woods)')
            woods.set_image(
                url='https://cdn.discordapp.com/attachments/804503457536409620/874992648467922964/c2e80271cb3a2e14.png')

            await ctx.send(embed=woods)

        elif args == "해안선" or args == "쇼어라인" or args == "Shoreline":
            shoreline = discord.Embed(colour=blue, title='해안선(Shoreline)')
            shoreline.set_image(
                url='https://cdn.discordapp.com/attachments/804503457536409620/874820769182523412/EFT_-_v0.12.8.png')

            await ctx.send(embed=shoreline)

        elif args == "나들목" or args == "인터체인지" or args == "Interchange":
            interchange = discord.Embed(colour=blue,
                                        title='나들목(Interchange)')
            interchange.set_image(
                url='https://cdn.discordapp.com/attachments/804503457536409620/874820773645287424/1606983666.png')

            await ctx.send(embed=interchange)

        elif args == "연구소" or args == "랩" or args == "The Lab":
            thelab_1 = discord.Embed(colour=blue,
                                     title='연구소(The Lab) 상층')
            thelab_1.set_image(
                url='https://cdn.discordapp.com/attachments/804503457536409620/874820762282909736/EFT_-_1_v0.12.8.png')

            thelab_2 = discord.Embed(colour=blue,
                                     title='연구소(The Lab) 하층')
            thelab_2.set_image(
                url='https://cdn.discordapp.com/attachments/804503457536409620/874820780783972413/EFT_-_2_v0.12.8.png')

            await ctx.send(embed=thelab_1)
            await ctx.send(embed=thelab_2)

        elif args == "리저브" or args == "보급고" or args == "Reserve":
            reserve = discord.Embed(colour=blue,
                                    title='리저브(Reserve)')
            reserve.set_image(
                url='https://cdn.discordapp.com/attachments/804503457536409620/874820775197163520/1606983675.png')

            await ctx.send(embed=reserve)

        else:
            map_list = discord.Embed(
                colour=blue,
                title='🗺 **맵 목록**')
            map_list.add_field(
                name='공장(Factory)',
                value='```보스 : Tagilla(타길라) 18%```')
            map_list.add_field(
                name='세관(Customs)',
                value='```보스 : Reshala(르샬라) 35%```')
            map_list.add_field(
                name='삼림(Woods)',
                value='```보스 : Shturman(슈트르만) 41%```')
            map_list.add_field(
                name='해안선(Shoreline)',
                value='```보스 : Sanitar(세니타) 35%```')
            map_list.add_field(
                name='나들목(Interchange)',
                value='```보스 : Killa(킬라) 38%```')
            map_list.add_field(
                name='연구소(The lab)',
                value='```보스 : X```')
            map_list.add_field(
                name='리저브(Reserve)',
                value='```보스 : Glukhar(글루하) 41%```')
            await ctx.send(
                '❌ **존재 하지 않는 맵 이름입니다!** (아래의 맵 목록을 확인해주세요)')
            await ctx.send(
                embed=map_list)

@bot.event
async def on_command_error(ctx, error):  # 예외 처리 싫으시면 pass 치시던가요
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(colour=red)
        a = error.retry_after
        after = round(a, 2)
        await ctx.send(f"<a:load:853480729945309204>**쿨다운 가동!** : `{after}초 남음`")

    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(colour=red)
        embed.add_field(name='<:error:875606527740870717>권한 부족!', value="이 명령어를 실행하기에는 권한이 부족합니다!")
        await ctx.send(embed=embed)


acces_token = os.environ["BOT_TOKEN"]
bot.run(acces_token)
