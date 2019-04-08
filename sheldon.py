import os
import discord
import random
import weapons_list

client = discord.Client()


@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('------')


@client.event
async def on_message(message):
    # ブキリスト決定
    # if 'にゅー' in message.content:
    #     w_list = weapons_list.NEW_WEAPONS
    # elif 'べっちゅー' in message.content:
    #     w_list = weapons_list.BECCHU_WEAPONS
    # else:
    #     w_list = weapons_list.WEAPONS
    w_list = weapons_list.WEAPONS

    # コマンド別処理
    if message.content.startswith('ぶきる'):
        key = random.randint(0, len(w_list) - 1)
        m = "今回は __**%s**__ を使うでし！" % w_list[key]['name']
        await client.send_message(message.channel, m)
        await client.send_file(message.channel, w_list[key]['image'])

    elif message.content.startswith('ぶきお'):
        channel = message.author.voice_channel
        if channel is not None:
            members = channel.voice_members

            for member in members:
                key = random.randint(0, len(w_list) - 1)
                weapon = w_list[key]['name']
                m = "*%(name)s*  は __**%(weapon)s**__ を使うでし！" % {'name': member.name, 'weapon': weapon}
                await client.send_message(message.channel, m)
        else:
            m = "だれもいないでし・・・"
            await client.send_message(message.channel, m)

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
                    m_a = "*" + team + "チーム* はこのブキを使ってみるでし！" + '\n' + weapons
                else:
                    m_b = "*" + team + "チーム* はこのブキを使うでし！" + '\n' + weapons

            m = m_a + '\n\n' + m_b

        else:
            w_range = weapons_list.WEAPONS_RANGE

            for team in ['アルファ', 'ブラボー']:
                l = random.sample(w_range['long'], 1)
                m = random.sample(w_range['middle'], 1)
                s_k = random.sample(w_range['short']['kill'], 1)
                s_p = random.sample(w_range['short']['paint'], 1)

                w = [l[0], m[0], s_k[0], s_p[0]]
                random.shuffle(w)

                weapons = "　■ __**%(long)s**__ \n　■ __**%(mid)s**__ \n　■ __**%(short1)s**__ \n　■ __**%(short2)s**__" % {
                    'long': w_list[w[0]]['name'], 'mid': w_list[w[1]]['name'], 'short1': w_list[w[2]]['name'],
                    'short2': w_list[w[3]]['name']}
                if team == "アルファ":
                    m_a = "*" + team + "チーム* はこのブキを使ってみるでし！" + '\n' + weapons
                else:
                    m_b = "*" + team + "チーム* はこのブキを使うでし！" + '\n' + weapons

            m = m_a + '\n\n' + m_b

        await client.send_message(message.channel, m)

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
