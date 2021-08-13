import discord
import pytz
import datetime
import os

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
                            value="```7.62x25mm Tokarev, 9x18mm Makarov, 9x19mm Parabellum, 9x21mm Gyurza, .45 ACP```",
                            inline=False)
        ammo_list.add_field(name="PDW탄", value="```4.6x30mm HK, 5.7x28mm FN```", inline=False)
        ammo_list.add_field(name="소총탄",
                            value="```5.45x39mm, 5.56x45mm NATO, .300 Blackout, 7.62x39mm, 7.62x51mm NATO, 7.62x54mmR, .338 Lapua Magnum, 9x39mm, .366 TKM, 12.7x55mm STs-130, 12.7x108mm```",
                            inline=False)
        ammo_list.add_field(name="산탄", value="```12x70mm, 20x70mm, 23x75mm```", inline=False)
        ammo_list.add_field(name="유탄", value="```30x29mm, 40x46 mm```", inline=False)

        await ctx.send(embed=ammo_list)

    else:
        if args == "5.56":
            ammo_5_56_45mm = discord.Embed(colour=gold)
            ammo_5_56_45mm.set_author(name="5.56x45mm NATO"
                                      ,
                                      icon_url='https://images-ext-1.discordapp.net/external/_K_Dcb42dq0n6fRZ6YCA8A4ZxCZRnxii4mYfycBV55c/%3Fversion%3Dbf32b6e1010535acf27240bf56221c43/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/c/ce/5.56x45_NATO.gif')
            ammo_5_56_45mm.add_field(name="최고성능", value="M995, M855A1", inline=False)
            ammo_5_56_45mm.add_field(name="가성비", value="M855, M856A1", inline=False)
            ammo_5_56_45mm.add_field(name="4~6클래스 방어구에 효과적", value="M995, M855A1", inline=False)
            ammo_5_56_45mm.add_field(name="3~4클래스 이하 방어구에 효과적", value="M855, 55 FMJ", inline=False)
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
        else:
            if args == ".366":
                ammo_366 = discord.Embed(colour=gold)
                ammo_366.set_author(name=".366 TKM"
                                    ,
                                    icon_url='https://images-ext-2.discordapp.net/external/uFxThmSv77znUrWFKG6a0MdGXISx5ASNPt-DoeN7kxo/%3Fversion%3Dc9b1e8b857006ac86baf9a190175447c/https/gamepedia.cursecdn.com/escapefromtarkov_gamepedia/3/39/.366_TKM.gif')
                ammo_366.add_field(name='최고성능', value='AP', inline=False)
                ammo_366.add_field(name='우호도 1 이상 상인에게서 구매 가능', value='FMJ', inline=False)
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
            else:
                if args == ".45":
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
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=red)
        embed.add_field(name='<:error:875606527740870717>에러! 필요한 값이 없음', value="필요한 인자가 없습니다!")  # 이거 좀 수정해주셈
        embed.set_footer(text='Stella Bot#9903',
                         icon_url="https://cdn.discordapp.com/avatars/806729801086926869/6d3c0df30e9a81cddf3622e630978b0c.png")
        await ctx.send(embed=embed)

    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(colour=red)
        embed.add_field(name='<:error:875606527740870717>에러! 잘못된 값', value="인자의 값이 잘못되었습니다!")
        embed.set_footer(text='Stella Bot#9903',
                         icon_url="https://cdn.discordapp.com/avatars/806729801086926869/6d3c0df30e9a81cddf3622e630978b0c.png")
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(colour=red)
        embed.add_field(name='<:error:875606527740870717>존재하지 않는 명령어!', value="존재하지 않는 명령어입니다!")
        embed.set_footer(text='Stella Bot#9903',
                         icon_url="https://cdn.discordapp.com/avatars/806729801086926869/6d3c0df30e9a81cddf3622e630978b0c.png")
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(colour=red)
        a = error.retry_after
        after = round(a, 2)
        await ctx.send(f"<a:load:853480729945309204>**쿨다운 가동!** : `{after}초 남음`")

    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(colour=red)
        embed.add_field(name='<:error:875606527740870717>권한 부족!', value="이 명령어를 실행하기에는 권한이 부족합니다!")
        embed.set_footer(text='Stella Bot#9903',
                         icon_url="https://cdn.discordapp.com/avatars/806729801086926869/6d3c0df30e9a81cddf3622e630978b0c.png")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(colour=red)
        embed.add_field(name='<:error:875606527740870717>알 수 없는 에러!',
                        value=f"명령어 오류 발생! 개발자한테 DM ```{str(error)}```")
        embed.set_footer(text='Stella Bot#9903',
                         icon_url="https://cdn.discordapp.com/avatars/806729801086926869/6d3c0df30e9a81cddf3622e630978b0c.png")
        await ctx.send(embed=embed)


acces_token = os.environ["BOT_TOKEN"]
bot.run(acces_token)
