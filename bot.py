import discord
import notif

class MyClient(discord.Client):


    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {403490445298237461})')
        print('------')
    

    async def on_message(self, message):
        
        if message.author.id == self.user.id:
            return

        if message.content.startswith('?help'):
            await message.reply('A quick guide to use the Apartment 4A bot🚀 \nUse the command  ?𝐬𝐮𝐛𝐣𝐞𝐜𝐭𝐧𝐚𝐦𝐞 or  ?𝐬𝐮𝐛𝐣𝐞𝐜𝐭𝐧𝐚𝐦𝐞.𝗮𝗰𝘁𝗶𝗼𝗻 to get the respective resource links \n𝗘𝘅𝗮𝗺𝗽𝗹𝗲\n?chem\n?chem.qp\n?chem.imp\n?chem.note\n?chem.capsule\n?chem.yt\n\n𝗟𝗶𝘀𝘁 𝗼𝗳 𝘀𝘂𝗯𝗷𝗲𝗰𝘁 𝗰𝗼𝗱𝗲𝘀\n1.chem 2.maths\n3.bee 4.bec\n5.bme 6.bce\n7.cp 8.eg\n9.em 10.phy\n11.lifeskill 12.pc\n13.Latest KTU notifications ', mention_author=True)
           
        


        elif message.content.startswith('?math2.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-fe851e6798be4ad0a312bd9cd228c1ec', mention_author=True)
        elif message.content.startswith('?chem.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-66615e314bae446785c1c789bba0547f', mention_author=True)
        elif message.content.startswith('?bee.qp'):
            await message.channel.send('https://www.notion.so/Question-paper-9b1f90d3026243e283dea8098f1534ef', mention_author=True)
        elif message.content.startswith('?bec.qp'):
            await message.channel.send('https://www.notion.so/Question-paper-9b1f90d3026243e283dea8098f1534ef', mention_author=True)
        elif message.content.startswith('?bme.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-f3b3564cb2fa4dc59504081c7f324a27', mention_author=True)
        elif message.content.startswith('?bce.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-f3b3564cb2fa4dc59504081c7f324a27', mention_author=True)
        elif message.content.startswith('?cp.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-59813728d63a462ba6f8ae5224a1391e', mention_author=True)    
        elif message.content.startswith('?eg.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-edc9f04ab0a34acd9a299e97e8110810', mention_author=True)
        elif message.content.startswith('?em.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-e16af68ea0ca4cfdb3d3b73765a2cf54', mention_author=True)
        elif message.content.startswith('?phy.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-ca7674bd4b07433f8fe0d06da43db1c0', mention_author=True)
        elif message.content.startswith('?lifeskill.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-58e9cd4b4a234201a3d7e5a2bc030d95', mention_author=True)
        elif message.content.startswith('?pc.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-d440c99661d64dbaa897196972f84590', mention_author=True)
        elif message.content.startswith('?math1.qp'):
            await message.channel.send('https://www.notion.so/Question-papers-1cddb26fbd94404ba8527c60210f613c', mention_author=True)  
        
        

        elif message.content.startswith('?math2.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-f18b10449b6c44eb95b4cd8a42b5ad73', mention_author=True)
        elif message.content.startswith('?chem.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-35f10aea44fb4be0b97fda75f6610d06', mention_author=True)
        elif message.content.startswith('?bee.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-2cdfcfcc3adb43ef8c13a045a000676d', mention_author=True)
        elif message.content.startswith('?bec.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-2cdfcfcc3adb43ef8c13a045a000676d', mention_author=True)
        elif message.content.startswith('?bme.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-9ef0acc5a83442b7ad41ecd0b3489ee2', mention_author=True)
        elif message.content.startswith('?bce.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-9ef0acc5a83442b7ad41ecd0b3489ee2', mention_author=True)
        elif message.content.startswith('?cp.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-8abe14541bc7421eb746c0561ca50382', mention_author=True)    
        elif message.content.startswith('?eg.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-f7fe41ed911043ca941cd40fbc990cff', mention_author=True)
        elif message.content.startswith('?em.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-4a8d077adb214275b78cd6b46886142b', mention_author=True)
        elif message.content.startswith('?phy.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-0ba1b68cfef2418cb361d83723b8b033', mention_author=True)
        elif message.content.startswith('?lifeskill.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-5b824eca3bd442478c188eb6553a253c', mention_author=True)
        elif message.content.startswith('?pc.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-348042ce384140b4b6979bea4e687c60', mention_author=True)
        elif message.content.startswith('?math1.imp'):
            await message.channel.send('https://www.notion.so/Important-Questions-0e43cfa42fcd47e2843dd9bdd344fe15', mention_author=True) 



        elif message.content.startswith('?math2.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-98f64a0ec3a74d86bcb20cec29865873', mention_author=True)
        elif message.content.startswith('?chem.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-47b174d79a3141069cb65bd5b8798d60', mention_author=True)
        elif message.content.startswith('?bee.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-39ea4b5867714fbcab1bf59758849244', mention_author=True)
        elif message.content.startswith('?bec.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-39ea4b5867714fbcab1bf59758849244', mention_author=True)
        elif message.content.startswith('?bme.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-0faa095c70154d49a758a91b0c4a2edc', mention_author=True)
        elif message.content.startswith('?bce.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-0faa095c70154d49a758a91b0c4a2edc', mention_author=True)
        elif message.content.startswith('?cp.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-917d63e0cf574f05a18ab6d003f0b280', mention_author=True)    
        elif message.content.startswith('?eg.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-2b0bb44379e34e16875699bc8bedbe6b', mention_author=True)
        elif message.content.startswith('?em.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-e3c4a85568664cc1bf44d80ae9ad5945', mention_author=True)
        elif message.content.startswith('?phy.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-382c2a62f02246a89d3d413679897dde', mention_author=True)
        elif message.content.startswith('?lifeskill.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-a7fceb2d86254a6582fca5da3124be6e', mention_author=True)
        elif message.content.startswith('?pc.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-df668242644645f6bffcd1c9cf51f453', mention_author=True)
        elif message.content.startswith('?math1.note'):
            await message.channel.send('https://www.notion.so/Notes-Text-4c344032c66b4b9e9e3d73ee72a66239', mention_author=True)    

        elif message.content.startswith('?math2.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-98f64a0ec3a74d86bcb20cec29865873', mention_author=True)
        elif message.content.startswith('?chem.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-47b174d79a3141069cb65bd5b8798d60', mention_author=True)
        elif message.content.startswith('?bee.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-39ea4b5867714fbcab1bf59758849244', mention_author=True)
        elif message.content.startswith('?bec.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-39ea4b5867714fbcab1bf59758849244', mention_author=True)
        elif message.content.startswith('?bme.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-0faa095c70154d49a758a91b0c4a2edc', mention_author=True)
        elif message.content.startswith('?bce.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-0faa095c70154d49a758a91b0c4a2edc', mention_author=True)
        elif message.content.startswith('?cp.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-917d63e0cf574f05a18ab6d003f0b280', mention_author=True)    
        elif message.content.startswith('?eg.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-2b0bb44379e34e16875699bc8bedbe6b', mention_author=True)
        elif message.content.startswith('?em.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-e3c4a85568664cc1bf44d80ae9ad5945', mention_author=True)
        elif message.content.startswith('?phy.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-382c2a62f02246a89d3d413679897dde', mention_author=True)
        elif message.content.startswith('?lifeskill.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-a7fceb2d86254a6582fca5da3124be6e', mention_author=True)
        elif message.content.startswith('?pc.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-df668242644645f6bffcd1c9cf51f453', mention_author=True)
        elif message.content.startswith('?math1.text'):
            await message.channel.send('https://www.notion.so/Notes-Text-4c344032c66b4b9e9e3d73ee72a66239', mention_author=True)

        elif message.content.startswith('?math2.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-4847bdd831c5437ebda075e9e5c25c36', mention_author=True)
        elif message.content.startswith('?chem.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-dbff1bb6e92a448a9b905122e0579ba6', mention_author=True)
        elif message.content.startswith('?bee.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-796af708c7564d4095ad238953546473', mention_author=True)
        elif message.content.startswith('?bec.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-796af708c7564d4095ad238953546473', mention_author=True)
        elif message.content.startswith('?bme.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-136bd3cd813640fe8d4cc319c795b817', mention_author=True)
        elif message.content.startswith('?bce.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-136bd3cd813640fe8d4cc319c795b817', mention_author=True)
        elif message.content.startswith('?cp.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-d9aacf3659d146d8b5d4dea2288b5394', mention_author=True)    
        elif message.content.startswith('?eg.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-1dcba3246cac4829ae8db5447c750463', mention_author=True)
        elif message.content.startswith('?em.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-fa6b7a7467a14690bcd460c9c4206886', mention_author=True)
        elif message.content.startswith('?phy.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-420e9b9cf3e348fea6a35d6536352e2d', mention_author=True)
        elif message.content.startswith('?lifeskill'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-058d6e426de542e7a7316039f0f07cbe', mention_author=True)
        elif message.content.startswith('?pc.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-61ff1dea99334eb7a687ecadf5e3a720', mention_author=True)
        elif message.content.startswith('?math1.capsule'):
            await message.channel.send('https://www.notion.so/Last-minute-prep-capsule-6e365e861fed44b2aa9a3236d3899162', mention_author=True)   
  

        elif message.content.startswith('?math2.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-dd9252b96c4e451287a2c600252fc63a', mention_author=True)
        elif message.content.startswith('?chem.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-91cf2d39be9e4a4d93fb341e5f2ba5bb', mention_author=True)
        elif message.content.startswith('?bee.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-05a444d2d89846688d9615c9d2c92c9f', mention_author=True)
        elif message.content.startswith('?bec.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-05a444d2d89846688d9615c9d2c92c9f', mention_author=True)
        elif message.content.startswith('?bme.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-f075fb01b3be416590894abc20b6314a', mention_author=True)
        elif message.content.startswith('?bce.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-f075fb01b3be416590894abc20b6314a', mention_author=True)
        elif message.content.startswith('?cp.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-1627e7718d514df0a9174f6af200d11d', mention_author=True)    
        elif message.content.startswith('?eg.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-31ac4acd33794ae484ffd3cb19277e15', mention_author=True)
        elif message.content.startswith('?em.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-a0e62189d1324d9abeeadfc89eb0010c', mention_author=True)
        elif message.content.startswith('?phy.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-30c8f86862b64631a8bfc70b6faa2f48', mention_author=True)
        elif message.content.startswith('?lifeskill'):
            await message.channel.send('https://www.notion.so/Life-Skills-c45a413c28014e85b8daf2a12b57305d', mention_author=True)
        elif message.content.startswith('?pc.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-17e8a8119b20472e9f92156ee76d129f', mention_author=True)
        elif message.content.startswith('?math1.yt'):
            await message.channel.send('https://www.notion.so/Youtube-Channels-to-refer-bd016c1a163c4564a01f9e09cdb56dc8', mention_author=True)  

        elif message.content.startswith('?math'):
            await message.channel.send('https://pattern-filament-145.notion.site/Maths-Sem-Two-8d524ed280304d72888cf02ce5b147ac', mention_author=True)
        elif message.content.startswith('?math2'):
            await message.channel.send('https://pattern-filament-145.notion.site/Maths-Sem-Two-8d524ed280304d72888cf02ce5b147ac', mention_author=True)
        elif message.content.startswith('?chem'):
            await message.channel.send('https://pattern-filament-145.notion.site/Engineering-Chemistry-64350211865440cbb39045aa09fa1e81', mention_author=True)
        elif message.content.startswith('?bee'):
            await message.channel.send('https://www.notion.so/Basics-of-Electrical-Electronics-a1c43bd80823432eb072e5a877fb3a5e', mention_author=True)
        elif message.content.startswith('?bec'):
            await message.channel.send('https://www.notion.so/Basics-of-Electrical-Electronics-a1c43bd80823432eb072e5a877fb3a5e', mention_author=True)
        elif message.content.startswith('?bme'):
            await message.channel.send('https://www.notion.so/Basics-of-Civil-and-Mechanical-de136359168140d7989b890fdef40c65', mention_author=True)
        elif message.content.startswith('?bce'):
            await message.channel.send('https://www.notion.so/Basics-of-Civil-and-Mechanical-de136359168140d7989b890fdef40c65', mention_author=True)
        elif message.content.startswith('?cp'):
            await message.channel.send('https://www.notion.so/C-Programming-103aa2ac6f6a4339915c2f57612e1200', mention_author=True)    
        elif message.content.startswith('?eg'):
            await message.channel.send('https://www.notion.so/Engineering-Graphics-670e52c5feb84f10aab5480b0d39cddb', mention_author=True)
        elif message.content.startswith('?em'):
            await message.channel.send('https://www.notion.so/Engineering-Mechanics-57859df3714345d48de7c4abf715de86', mention_author=True)
        elif message.content.startswith('?phy'):
            await message.channel.send('https://www.notion.so/Engineering-Physics-1941c174a566422789c0e644bea9bcf3', mention_author=True)
        elif message.content.startswith('?lifeskill.yt'):
            await message.channel.send('bro serious ahno?', mention_author=True)
        elif message.content.startswith('?pc'):
            await message.channel.send('https://www.notion.so/Professional-Communication-f4cbc478631043f9954879f8c362f74f', mention_author=True)
        elif message.content.startswith('?1math'):
            await message.channel.send('https://www.notion.so/Maths-Sem-One-dc05ea826fde4833afb7ca95eac92f46', mention_author=True)
        elif message.content.startswith('?'):
            await message.channel.send('did not get you.. maybe try ?help', mention_author=True)
        elif message.content.startwith('?notif'):
            await message.channel.send(notif.notifications(),mention_author=True)     



        #else:
            #await message.channel.send('didnt get you boi', mention_author=False)
client = MyClient() 
client.run('OTA1MTUzMDgyODI3MTA0MzI2.YYF7fw.Z1HzJBTlQmzATmo1eyahbLw-R7A')
