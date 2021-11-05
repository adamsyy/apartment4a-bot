import discord
from discord.ext import commands
import notif
import os
import news
from discord.ext.commands import Bot
from discord_slash import SlashCommand
from dotenv import load_dotenv
load_dotenv()

realNews=[]
newsArray = news.news()
DISCORD_TOKEN = os.environ.get('TOKEN')
client = commands.Bot(command_prefix='?')

# help section
client.remove_command('help')
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Help", description="Here are the commands you can use", color=0x00ff00)
    em.add_field(name="?help", value="Shows this help menu", inline=False)
    em.add_field(name="?help subs", value="Shows the subject codes", inline=False)
    em.add_field(name="/news", value="Get latest news reports about KTU", inline=False)
    em.add_field(name="/q<subject_code>", value="Get question papers of specific subject eg: /qmath2", inline=False)
    em.add_field(name="/imp<subject_code>", value="Get important questions of specific subject eg: /impchem", inline=False)
    em.add_field(name="/notes<subject_code>", value="Get notes of specific subject eg: /notebec", inline=False)
    em.add_field(name="/text<subject_code>", value="Get texts of specific subject eg: /textpc", inline=False)
    em.add_field(name="/cap<subject_code>", value="Get capsules of specific subject eg: /capeg", inline=False)
    em.add_field(name="/yt<subject_code>", value="Get youtube videos of specific subject eg: /ytbee", inline=False)
    em.add_field(name="/show<subject_code>", value="Get everything on specific subject eg: /showphy", inline=False)
    await ctx.send(embed=em)
@help.command()
async def subs(ctx):
    em=discord.Embed(title="Subjects", description="Here are the subject codes you can use", color=0x00ff00)
    em.add_field(name="**Subject Codes: **", value="***maths1*** \n ***maths2***\n ***bec***\n ***bee***\n ***bme***\n***bce***\n***cp***\n***chem***\n***eg***\n***em***\n***phy***\n***life***\n***pc***\n")
    await ctx.send(embed=em)


# help section end


slash = SlashCommand(client,sync_commands=True)
@slash.slash(name="qmaths2",description="Maths 2 Question Paper")
async def qmaths2(ctx):
    await ctx.reply('https://www.notion.so/Question-papers-fe851e6798be4ad0a312bd9cd228c1ec')


@slash.slash(name="qchem",description="Chemistry Question Paper")
async def qchem(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-66615e314bae446785c1c789bba0547f")


@slash.slash(name="qbee",description="BEE Question Paper")
async def qbee(ctx):
    await ctx.reply("https://www.notion.so/Question-paper-9b1f90d3026243e283dea8098f1534ef")

@slash.slash(name="qbec",description="BEC Question Paper")
async def qbec(ctx):
    await ctx.reply("https://www.notion.so/Question-paper-9b1f90d3026243e283dea8098f1534ef")

@slash.slash(name="qbme",description="BME Question Paper")
async def qbme(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-f3b3564cb2fa4dc59504081c7f324a27")

@slash.slash(name="qbce",description="BCE Question Paper")
async def qbce(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-f3b3564cb2fa4dc59504081c7f324a27")

@slash.slash(name="qcp",description="CP Question Paper")
async def qcp(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-59813728d63a462ba6f8ae5224a1391e")

@slash.slash(name="qeg",description="EG Question Paper")
async def qeg(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-edc9f04ab0a34acd9a299e97e8110810")

@slash.slash(name="qem",description="EM Question Paper")
async def qem(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-e16af68ea0ca4cfdb3d3b73765a2cf54")
@slash.slash(name="qphy",description="Physics Question Paper")
async def qphy(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-ca7674bd4b07433f8fe0d06da43db1c0")
@slash.slash(name="qlife",description="Life SKill Question Paper")
async def qlife(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-58e9cd4b4a234201a3d7e5a2bc030d95")
@slash.slash(name="qpc",description="Maths 2 Question Paper")
async def qpc(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-d440c99661d64dbaa897196972f84590")
@slash.slash(name="qmaths1",description="Maths 1 Question Paper")
async def qmaths1(ctx):
    await ctx.reply("https://www.notion.so/Question-papers-1cddb26fbd94404ba8527c60210f613c")




@slash.slash(name="impmaths2",description="Maths 2 Important Questions")
async def impmaths2(ctx):
    await ctx.reply('https://www.notion.so/Important-Questions-f18b10449b6c44eb95b4cd8a42b5ad73')


@slash.slash(name="impchem",description="Chemistry Important Questions")
async def impchem(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-35f10aea44fb4be0b97fda75f6610d0")


@slash.slash(name="impbee",description="BEE Important Questions")
async def impbee(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-2cdfcfcc3adb43ef8c13a045a000676d")

@slash.slash(name="impbec",description="BEC Important Questions")
async def impbec(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-2cdfcfcc3adb43ef8c13a045a000676d")

@slash.slash(name="impbme",description="BME Important Questions")
async def impbme(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-9ef0acc5a83442b7ad41ecd0b3489ee2")

@slash.slash(name="impbce",description="BCE Important Questions")
async def impbce(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-9ef0acc5a83442b7ad41ecd0b3489ee2")

@slash.slash(name="impcp",description="CP Important Questions")
async def impcp(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-8abe14541bc7421eb746c0561ca50382")

@slash.slash(name="impeg",description="EG Important Questions")
async def impeg(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-f7fe41ed911043ca941cd40fbc990cff")

@slash.slash(name="impem",description="EM Important Questions")
async def impem(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-4a8d077adb214275b78cd6b46886142b")
@slash.slash(name="impphy",description="Physics Important Questions")
async def impphy(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-0ba1b68cfef2418cb361d83723b8b033")
@slash.slash(name="implife",description="Life SKill Important Questions")
async def implife(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-5b824eca3bd442478c188eb6553a253c")
@slash.slash(name="imppc",description="Maths 2 Important Questions")
async def imppc(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-348042ce384140b4b6979bea4e687c60")
@slash.slash(name="impmaths1",description="Maths 1 Important Questions")
async def impmaths1(ctx):
    await ctx.reply("https://www.notion.so/Important-Questions-0e43cfa42fcd47e2843dd9bdd344fe15")





@slash.slash(name="notesmaths2",description="Maths 2 Notes")
async def notesmaths2(ctx):
    await ctx.reply('https://www.notion.so/Notes-Text-98f64a0ec3a74d86bcb20cec29865873')


@slash.slash(name="noteschem",description="Chemistry Notes")
async def noteschem(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-47b174d79a3141069cb65bd5b8798d60")


@slash.slash(name="notesbee",description="BEE Notes")
async def notesbee(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-39ea4b5867714fbcab1bf59758849244")

@slash.slash(name="notesbec",description="BEC Notes")
async def notesbec(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-39ea4b5867714fbcab1bf59758849244")

@slash.slash(name="notesbme",description="BME Notes")
async def notesbme(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-0faa095c70154d49a758a91b0c4a2edc")

@slash.slash(name="notesbce",description="BCE Notes")
async def notesbce(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-0faa095c70154d49a758a91b0c4a2edc")

@slash.slash(name="notescp",description="CP Notes")
async def notescp(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-917d63e0cf574f05a18ab6d003f0b280")

@slash.slash(name="noteseg",description="EG Notes")
async def noteseg(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-2b0bb44379e34e16875699bc8bedbe6b")

@slash.slash(name="notesem",description="EM Notes")
async def notesem(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-e3c4a85568664cc1bf44d80ae9ad5945")
@slash.slash(name="notesphy",description="Physics Notes")
async def notesphy(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-382c2a62f02246a89d3d413679897dde")
@slash.slash(name="noteslife",description="Life SKill Notes")
async def noteslife(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-a7fceb2d86254a6582fca5da3124be6e")
@slash.slash(name="notespc",description="Maths 2 Notes")
async def notespc(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-df668242644645f6bffcd1c9cf51f453")
@slash.slash(name="notesmaths1",description="Maths 1 Notes")
async def notesmaths1(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-4c344032c66b4b9e9e3d73ee72a66239")






@slash.slash(name="textmaths2",description="Maths 2 Text")
async def textmaths2(ctx):
    await ctx.reply('https://www.notion.so/Notes-Text-98f64a0ec3a74d86bcb20cec29865873')


@slash.slash(name="textchem",description="Chemistry Text")
async def textchem(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-47b174d79a3141069cb65bd5b8798d60")


@slash.slash(name="textbee",description="BEE Text")
async def textbee(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-39ea4b5867714fbcab1bf59758849244")

@slash.slash(name="textbec",description="BEC Text")
async def textbec(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-39ea4b5867714fbcab1bf59758849244")

@slash.slash(name="textbme",description="BME Text")
async def textbme(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-0faa095c70154d49a758a91b0c4a2edc")

@slash.slash(name="textbce",description="BCE Text")
async def textbce(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-0faa095c70154d49a758a91b0c4a2edc")

@slash.slash(name="textcp",description="CP Text")
async def textcp(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-917d63e0cf574f05a18ab6d003f0b280")

@slash.slash(name="texteg",description="EG Text")
async def texteg(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-2b0bb44379e34e16875699bc8bedbe6b")

@slash.slash(name="textem",description="EM Text")
async def textem(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-e3c4a85568664cc1bf44d80ae9ad5945")
@slash.slash(name="textphy",description="Physics Text")
async def textphy(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-382c2a62f02246a89d3d413679897dde")
@slash.slash(name="textlife",description="Life SKill Text")
async def textlife(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-a7fceb2d86254a6582fca5da3124be6e")
@slash.slash(name="textpc",description="Maths 2 Text")
async def textpc(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-df668242644645f6bffcd1c9cf51f453")
@slash.slash(name="textmaths1",description="Maths 1 Text")
async def textmaths1(ctx):
    await ctx.reply("https://www.notion.so/Notes-Text-4c344032c66b4b9e9e3d73ee72a66239")






@slash.slash(name="capmaths2",description="Maths 2 Capsules")
async def capmaths2(ctx):
    await ctx.reply('https://www.notion.so/Last-minute-prep-capsule-4847bdd831c5437ebda075e9e5c25c36')


@slash.slash(name="capchem",description="Chemistry Capsules")
async def capchem(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-dbff1bb6e92a448a9b905122e0579ba6")


@slash.slash(name="capbee",description="BEE Capsules")
async def capbee(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-796af708c7564d4095ad238953546473")

@slash.slash(name="capbec",description="BEC Capsules")
async def capbec(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-796af708c7564d4095ad238953546473")

@slash.slash(name="capbme",description="BME Capsules")
async def capbme(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-136bd3cd813640fe8d4cc319c795b817")

@slash.slash(name="capbce",description="BCE Capsules")
async def capbce(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-136bd3cd813640fe8d4cc319c795b817")

@slash.slash(name="capcp",description="CP Capsules")
async def capcp(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-d9aacf3659d146d8b5d4dea2288b5394")

@slash.slash(name="capeg",description="EG Capsules")
async def capeg(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-1dcba3246cac4829ae8db5447c750463")

@slash.slash(name="capem",description="EM Capsules")
async def capem(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-fa6b7a7467a14690bcd460c9c4206886")
@slash.slash(name="capphy",description="Physics Capsules")
async def capphy(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-420e9b9cf3e348fea6a35d6536352e2d")
@slash.slash(name="caplife",description="Life SKill Capsules")
async def caplife(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-058d6e426de542e7a7316039f0f07cbe")
@slash.slash(name="cappc",description="Maths 2 Capsules")
async def cappc(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-61ff1dea99334eb7a687ecadf5e3a720")
@slash.slash(name="capmaths1",description="Maths 1 Capsules")
async def capmaths1(ctx):
    await ctx.reply("https://www.notion.so/Last-minute-prep-capsule-6e365e861fed44b2aa9a3236d3899162")








@slash.slash(name="ytmaths2",description="Maths 2 Youtube Videos")
async def ytmaths2(ctx):
    await ctx.reply('https://www.notion.so/Youtube-Channels-to-refer-dd9252b96c4e451287a2c600252fc63a')


@slash.slash(name="ytchem",description="Chemistry Youtube Videos")
async def ytchem(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-91cf2d39be9e4a4d93fb341e5f2ba5bb")


@slash.slash(name="ytbee",description="BEE Youtube Videos")
async def ytbee(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-05a444d2d89846688d9615c9d2c92c9f")

@slash.slash(name="ytbec",description="BEC Youtube Videos")
async def ytbec(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-05a444d2d89846688d9615c9d2c92c9f")

@slash.slash(name="ytbme",description="BME Youtube Videos")
async def ytbme(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-f075fb01b3be416590894abc20b6314a")

@slash.slash(name="ytbce",description="BCE Youtube Videos")
async def ytbce(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-f075fb01b3be416590894abc20b6314a")

@slash.slash(name="ytcp",description="CP Youtube Videos")
async def ytcp(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-1627e7718d514df0a9174f6af200d11d")

@slash.slash(name="yteg",description="EG Youtube Videos")
async def yteg(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-31ac4acd33794ae484ffd3cb19277e15")

@slash.slash(name="ytem",description="EM Youtube Videos")
async def ytem(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-a0e62189d1324d9abeeadfc89eb0010c")
@slash.slash(name="ytphy",description="Physics Youtube Videos")
async def ytphy(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-30c8f86862b64631a8bfc70b6faa2f48")
@slash.slash(name="ytlife",description="Life SKill Youtube Videos")
async def ytlife(ctx):
    await ctx.reply("https://www.notion.so/Life-Skills-c45a413c28014e85b8daf2a12b57305d")
@slash.slash(name="ytpc",description="Maths 2 Youtube Videos")
async def ytpc(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-17e8a8119b20472e9f92156ee76d129f")
@slash.slash(name="ytmaths1",description="Maths 1 Youtube Videos")
async def ytmaths1(ctx):
    await ctx.reply("https://www.notion.so/Youtube-Channels-to-refer-bd016c1a163c4564a01f9e09cdb56dc8")





@slash.slash(name="showmaths2",description="Maths ")
async def showmaths2(ctx):
    await ctx.reply('https://pattern-filament-145.notion.site/Maths-Sem-Two-8d524ed280304d72888cf02ce5b147ac')


@slash.slash(name="showchem",description="Chemistry ")
async def showchem(ctx):
    await ctx.reply("https://pattern-filament-145.notion.site/Engineering-Chemistry-64350211865440cbb39045aa09fa1e81")


@slash.slash(name="showbee",description="BEE ")
async def showbee(ctx):
    await ctx.reply("https://www.notion.so/Basics-of-Electrical-Electronics-a1c43bd80823432eb072e5a877fb3a5e")

@slash.slash(name="showbec",description="BEC ")
async def showbec(ctx):
    await ctx.reply("https://www.notion.so/Basics-of-Electrical-Electronics-a1c43bd80823432eb072e5a877fb3a5e")

@slash.slash(name="showbme",description="BME ")
async def showbme(ctx):
    await ctx.reply("https://www.notion.so/Basics-of-Civil-and-Mechanical-de136359168140d7989b890fdef40c65")

@slash.slash(name="showbce",description="BCE ")
async def showbce(ctx):
    await ctx.reply("https://www.notion.so/Basics-of-Civil-and-Mechanical-de136359168140d7989b890fdef40c65")

@slash.slash(name="showcp",description="CP ")
async def showcp(ctx):
    await ctx.reply("https://www.notion.so/C-Programming-103aa2ac6f6a4339915c2f57612e1200")

@slash.slash(name="showeg",description="EG ")
async def showeg(ctx):
    await ctx.reply("https://www.notion.so/Engineering-Graphics-670e52c5feb84f10aab5480b0d39cddb")

@slash.slash(name="showem",description="EM ")
async def showem(ctx):
    await ctx.reply("https://www.notion.so/Engineering-Mechanics-57859df3714345d48de7c4abf715de86")
@slash.slash(name="showphy",description="Physics ")
async def showphy(ctx):
    await ctx.reply("https://www.notion.so/Engineering-Physics-1941c174a566422789c0e644bea9bcf3")
@slash.slash(name="showlife",description="Life SKill ")
async def showslife(ctx):
    await ctx.reply("bro serious ahno?")
@slash.slash(name="showpc",description="Maths 2 ")
async def showpc(ctx):
    await ctx.reply("https://www.notion.so/Professional-Communication-f4cbc478631043f9954879f8c362f74")
@slash.slash(name="showmaths1",description="Maths 1 ")
async def showmaths1(ctx):
    await ctx.reply("https://www.notion.so/Maths-Sem-One-dc05ea826fde4833afb7ca95eac92f46")

@slash.slash(name="news",description="Show Latest News About KTU.")
async def showmaths1(ctx):
    j=0
    for i in range(len(newsArray)):

        if (newsArray[i]['heading'] not in realNews):
                j+=1
                newsVar = 'Sl.No: '+str(j)+'\n'+'Heading: '+newsArray[i]['heading']+'\n'+'Description: '+newsArray[i]['description']+'\n'+'News: '+newsArray[i]['link']+'\n'+'Date: '+ newsArray[i]['date']+'\n'
                realNews.append(newsArray[i]['heading'])
                await ctx.reply(newsVar)

print("running...")

















client.run(DISCORD_TOKEN)
# python enviornment variable
# token
 
