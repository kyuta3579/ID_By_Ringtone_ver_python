#!/usr/local/bin/pyenv/versions/3.6.5/bin/python
import os
import sys
import discord
from time import sleep

TOKEN = "NTE5ODM2MTQzNTEyOTc3NDM5.DulIIA.-gwDVbkz1UIsRK6NwmW_i2rMS4o"
NOSTALGIA_TEXT_CHANNEL = "293293134560100353"
NOSTALGIA_VOICE_CHANNEL = "280222178929278976"
TNS_VOICE_CHANNEL = "579685636647157760"

client = discord.Client()
connect_flag = True

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	global voice
	if message.author.bot:
		return
	if message.content == "&join":
		if client.user != message.author:
			if client.voice_client_in(message.server) is not None:
				voice = await client.join_voice_channel(client.get_channel(VOICE_CHANNEL))
			else:
				await client.send_message(message.channel, "already connected.")
			if voice.is_connected():
				await client.send_message(message.channel, "success!")

	if message.content == "&exit":
		if client.user != message.author:
			if voice.is_connected():
				await voice.disconnect()
			else:
				m = "Not connected!!"
				await client.send_message(message.channel, m)

@client.event
async def on_voice_state_update(before,after):
	global connect_flag
	global vc
	if before.bot:
		return
	if before.server.id == "280222178497003521":
		VOICE_CHANNEL = NOSTALGIA_VOICE_CHANNEL
	else:
		VOICE_CHANNEL = TNS_VOICE_CHANNEL

	if ((before.voice.self_mute is not after.voice.self_mute) or (before.voice.self_deaf is not after.voice.self_deaf)):
		print("exist changing mute setting")
		return
	if (before.voice_channel is not after.voice_channel) and (after.voice_channel is client.get_channel(VOICE_CHANNEL)):
		if connect_flag:
			await client.join_voice_channel(client.get_channel(VOICE_CHANNEL))
			connect_flag = False
#		m = before.name + "が" + after.voice_channel.name + "へ入室しました。"
#		await client.send_message(client.get_channel(TEXT_CHANNEL), m)
		file_name = before.name + ".mp3"
		path = "/home/sshuser/discord_bot/ID_By_Ringtone/" + file_name
		vc = client.voice_client_in(before.server)
		player = vc.create_ffmpeg_player(path)
		player.volume = 0.2
		sleep(1)
		player.start()
	if (before.voice_channel is not after.voice_channel) and (after.voice_channel is None):
		mem = client.get_channel(VOICE_CHANNEL).voice_members
		len_mem = len(mem)
		if (len_mem == 1) and (mem.pop().bot):
			await vc.disconnect()
			connect_flag = True

client.run(TOKEN)