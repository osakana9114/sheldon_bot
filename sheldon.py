import os
import discord
import random
import weapons_list

client = discord.Client()


@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + str(client.user.id))
    print('------')


@client.event
async def on_message(message):
    w_list = weapons_list.WEAPONS

    # コマンド別処理
    if message.content.startswith('ぶきる'):
        key = random.randint(0, len(w_list) - 1)

        embed = discord.Embed(title=w_list[key]['name'], description="を使うでし！", color=0xfec87d)
        embed.set_thumbnail(url=os.environ['S3_BUCKET_URL'] + w_list[key]['image'])
        embed.add_field(name="sub", value="`%(sub)s`" % {'sub': w_list[key]['sub']}, inline=True)
        embed.add_field(name="special", value="`%(special)s`" % {'special': w_list[key]['special']}, inline=True)

        await message.channel.send(embed=embed)

    elif message.content.startswith('ぶきお'):
        author_voice = message.author.voice

        if author_voice is not None:
            members = author_voice.channel.members

            embed = discord.Embed(title="みんなのブキを選んだでし！", color=0xf02c7d)
            for member in members:
                key = random.randint(0, len(w_list) - 1)
                embed.add_field(name=member.name, value="　👉 **%(weapon)s**" % {'weapon': w_list[key]['name']})

            await message.channel.send(embed=embed)
        else:
            await message.channel.send("だれもいないでし・・・")

    elif message.content.startswith('ぶきち'):
        if 'kp' in message.content:
            kill_paint = weapons_list.WEAPONS_KILL_PAINT
            for team in ['α', 'β']:
                kill = random.sample(kill_paint['kill'], 2)
                paint = random.sample(kill_paint['paint'], 2)

                w = [kill[0], kill[1], paint[0], paint[1]]
                random.shuffle(w)

                weapons = "　■ __**%(1)s**__ \n　■ __**%(2)s**__ \n　■ __**%(3)s**__ \n　■ __**%(4)s**__" % {
                    '1': w_list[w[0]]['name'], '2': w_list[w[1]]['name'], '3': w_list[w[2]]['name'],
                    '4': w_list[w[3]]['name']}
                if team == "α":
                    m_a = "***" + team + "チーム***" + '\n' + weapons
                else:
                    m_b = "***" + team + "チーム***" + '\n' + weapons

            m = m_a + '\n\n' + m_b

        else:
            w_range = weapons_list.WEAPONS_RANGE

            for team in ['アルファ', 'ブラボー']:
                long = random.sample(w_range['long'], 1)
                middle = random.sample(w_range['middle'], 1)
                short_k = random.sample(w_range['short']['kill'], 1)
                short_p = random.sample(w_range['short']['paint'], 1)

                w = [long[0], middle[0], short_k[0], short_p[0]]
                random.shuffle(w)

                weapons = "　■ __**%(long)s**__ \n　■ __**%(mid)s**__ \n　■ __**%(short1)s**__ \n　■ __**%(short2)s**__" % {
                    'long': w_list[w[0]]['name'], 'mid': w_list[w[1]]['name'], 'short1': w_list[w[2]]['name'],
                    'short2': w_list[w[3]]['name']}
                if team == "アルファ":
                    m_a = "***" + team + "チーム***" + '\n' + weapons
                else:
                    m_b = "***" + team + "チーム***" + '\n' + weapons

            m = m_a + '\n\n' + m_b

        embed = discord.Embed(title="このブキでバトルするでし！", description=m, color=0x1cd718)

        await message.channel.send(embed=embed)

    # elif message.content.startswith('list'):
    #     ary = "";
    #     for key, weapon in enumerate(list):
    #         ary += str(key) + '：' + weapon['name'] + '\n'
    #
    #     await client.send_message(message.channel, ary)

    # elif message.content.startswith('range'):
    #     range = weapons_list.WEAPONS_RANGE
    #     long_list = "**長射程**\n"
    #     for number in range['long']:
    #         long_list += list[number]['name'] + "\n"
    #
    #     middle_list = "\n**中射程**\n"
    #     for number in range['middle']:
    #         middle_list += list[number]['name'] + "\n"
    #
    #     short_list = "\n**短射程**\n"
    #     for number in range['short']:
    #         short_list += list[number]['name'] + "\n"
    #
    #     await client.send_message(message.channel, long_list)
    #     await client.send_message(message.channel, middle_list)
    #     await client.send_message(message.channel, short_list)

client.run(os.environ['DISCORD_ACCESS_TOKEN'])
