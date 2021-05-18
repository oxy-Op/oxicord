"""
The MIT License (MIT)
Copyright (c) 2021 -  Oxy 

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

# -*- coding: utf-8 -*-

import time
import requests as rs 


url = "https://discord.com/api/v6/"

class Client():
	def __init__(self,token):
		self.token = token
		global headers
		headers = {
			'authorization':token,
			'content-type':'application/json'
			}
class guild():
	def join(self,invite:str):
		self.invite = invite
		res = rs.post(url + f"invites/{invite}",headers=headers)
		data = res.json()
		if res.status_code == 200:
			try:
				print(f"""
					Joined Guild : {data['guild']['name']} \nInvited By : {data['inviter']['username']}#{data['inviter']['discriminator']} \n Invite Code : {data['code']}
				""")
			except KeyError:
				print(f"""
					Joined Guild : {data['guild']['name']} \n
				""")

		else:
			print(data)
	
	def leave(self,guildid):
		self.guildid = guildid
		r = rs.delete(url + f"users/@me/guilds/{guildid}",headers=headers)
		data = r.json()
		print(data)

	def createGuild(self,name):
		self.name = name
		json = {
			"name":name
		}
		r = rs.post(url + "guilds",headers=headers,json=json)
		print(r.json())

	def getGuildInfo(self,guildid):
		self.guildid = guildid
		r = rs.get(url + f"guilds/{guildid}?with_counts=true",headers=headers)
		data = r.json()
		try:

			print(f""" Guild Information : \n Name : {data['name']} \n ID : {data['id']} \n Icon : {data["icon"]} \n Description : {data["description"]}   \n  
Splash : {data["splash"]} \nFeatures : {data['features']} \n Banner : {data['banner']} \n Owner ID : {data['owner_id']} \n Application ID : {data['application_id']} \n Region : {data['region']} \n Afk channel ID :  {data['afk_channel_id']} \n Afk Timeout : {data['afk_timeout']} \n System Channrl ID : {data[ "system_channel_id"]} \n 
Widget Enabled :  {data["widget_enabled"]} \n Widget Channel ID : {data["widget_channel_id"]} \n Verifiction Level : {data[ "verification_level"]} \nMessage Level : {data["default_message_notifications"]} \n MFA level : {data["mfa_level"]}
\n Explicit Content Filter : {data["explicit_content_filter"]} \n Vanity URL : {data["vanity_url_code"]} \n Boost Level :  {data["premium_tier"]} \n Boosters : {data["premium_subscription_count"]} \n System Channel Flags :  {data["system_channel_flags"]} \n Locale :  {data["preferred_locale"]} \n Rules channel id : {data["rules_channel_id"]} \n """)  
        
		except KeyError:
			print("KeyError")

	def editGuild(self,guildid,name):
		self.guildid = guildid
		self.name = name
		json = {
			"name":name
		}
		r = rs.patch(url + f"guilds/{guildid}",headers=headers,json=json)
		print(r.json())

	def deleteGuild(self,guildid):
		self.guildid = guildid
		r = rs.delete(url + f"guilds/{guildid}",headers=headers)
		print(r.json())

	def getGuildChannels(self,guildid):
		self.guildid = guildid
		r = rs.get(url + f"guilds/{guildid}/channels",headers=headers)
		data = r.json()
		try:
			for data in data:
				print(f"""Name : {data['name']} \n ID : {data['id']} \n Type : {data['type']} \n Topic : {data['topic']} NSFW : {data['nsfw']}""")
		except KeyError:
			print("KeyError")

	def getGuildMember(self,userid,guildid):
		self.guildid = guildid
		self.userid = userid
		r = rs.get(url + f"guilds/{guildid}/members/{userid}",headers=headers)
		print(r.json())
	
	def createGuildChannel(self,guildid,name,topic):
		self.guildid = guildid
		self.name = name
		self.topic = topic
		json = {
			'name':str(name),
			'topic':str(topic)
		}
		r = rs.post(url + f"guilds/{guildid}/channels",headers=headers,json=json)
		print(r.json())

	def changeMyNick(self,guildid,nick):
		self.guildid = guildid
		self.nick = nick
		json = {
			'nick':str(nick)
		}
		r = rs.patch(url + f'guilds/{guildid}/members/@me/nick',headers=headers,json=json)
		print(r.json())

	def addRoleToMember(self,guildid,userid,roleid):
		self.guildid = guildid
		self.userid= userid
		self.roleid = roleid
		r = rs.put(url + f"guilds/{guildid}/members/{userid}/roles/{roleid}",headers=headers)
		print(r.json())
	
	def removeMemberRole(self,guildid,userid,roleid):
		self.guildid = guildid
		self.userid= userid
		self.roleid = roleid
		r = rs.delete(url + f"guilds/{guildid}/members/{userid}/roles/{roleid}",headers=headers)
		print(r.json())

	def kickMember(self,guildid,userid):
		self.guildid = guildid
		self.userid= userid
		r = rs.delete(url + f"guilds/{guild.id}/members/{userid}",headers=headers)
		print(r.json())

	def getGuildBans(self,guildid):
		self.guildid = guildid
		try:
			r = rs.get(url + f"guilds/{guildid}/bans",headers=headers)
			data = r.json()
			for data in data:
				time.sleep(1)
				print(
					f'''Name : {data['user']['username']}#{data['user']['disriminator']} \n ID : {data['user']['id']} \n Reason : {data['reason']} '''
				)
		except KeyError:
			print("KeyError")

	def getGuildRoles(self,guildid):
		self.guilidid = guildid
		r = rs.get(url + f"guilds/{guildid}",headers=headers)
		data = r.json()
		for role in data['roles']:
			print(f"Role : \n Name : {role['name']} \n ID : {role['id']} \n Color : {role['color']} \n Mentionable : {role['mentionable']} \n Display Role : {role['hoist']} \n Position : {role['postion']} ")
		else:
			return

	def getGuildEmojis(self,guildid):
		self.guildid = guildid
		r = rs.get(url + f"guilds/{guildid}",headers=headers)
		data = r.json()
		for emojis in data['emojis']:
			print(
				f'''Emoji : \n Name : {emojis['name']} \n ID : {emojis['id']} \n Animated : {emojis['animated']} \n Available : {emojis['available']} '''
			)
		else:
			return
	
	def getUserBanInfo(self,guildid,userid):
		self.guildid = guildid
		self.userid = userid
		r = rs.get(url + f"guilds/{guildid}/bans/{userid}",headers=headers)
		data = r.json()
		try:
			print(
				f'''Name : {data['user']['username']}#{data['user']['disriminator']} \n ID : {data['user']['id']} \n Reason : {data['reason']} '''
			)
		except KeyError:
			print("KeyError")

	def banMember(self,guildid,userid,reason):
		self.guildid = guildid
		self.userid = userid
		self.reason = reason
		reason = {
			'reason': str(reason)
		}
		r = rs.put(url + f"guilds/{guildid}/bans/{userid}",headers=headers,json=reason)
		print(r.json())
		
	def removeBan(self,guildid,userid):
		self.guildid = guildid
		self.userid = userid
		r =  rs.delete(url + f"guilds/{guildid}/bans/{userid}",headers=headers)
		print(r.json())
	
	def createGuildRole(self,guildid,name,hoist:bool,mentionable:bool,color:int=0):
		"""NOTE :  PERMISSIONS IS NOT SUPPORTED BECAUSE THEY ARE BITWISE VALUES AND CANNOT BE USED BY NORMAL PEOPLES"""
		self.guildid = guildid
		self.name = name 
		self.color = color
		self.hoist = hoist
		self.mentionable = mentionable
		param = {
			'name':str(name),
			'color': color,
			'hoist': hoist,
			'mentionable':mentionable
		}
		r = rs.post(url + f"guilds/{guildid}/roles",headers=headers,json=param)
		print(r.json())

	def editGuildRole(self,guildid,roleid,name,hoist:bool,mentionable:bool,color:int=0):
		"""NOTE :  PERMISSIONS IS NOT SUPPORTED BECAUSE THEY ARE BITWISE VALUES AND CANNOT BE USED BY NORMAL PEOPLES"""
		self.guildid = guildid
		self.roleid = roleid
		self.name = name 
		self.color = color
		self.hoist = hoist
		self.mentionable = mentionable
		json = {
			'name':str(name),
			'color': color,
			'hoist': hoist,
			'mentionable':mentionable
		}
		r = rs.patch(url + f"guilds/{guildid}/roles/{roleid}",headers=headers,json=json)
		print(r.json())

	def deleteGuildRole(self,guildid,roleid):
		self.guildid = guildid
		self.roleid = roleid
		r = rs.delete(url + f"guilds/{guildid}/roles/{roleid}",headers=headers)
		print(r.json())
	
	def getPruneCount(self,guildid):
		self.guilidid = guildid
		r = rs.get(url + f"guilds/{guildid}/prune",headers=headers)
		print(r.json())

	def pruneMembers(self,guildid,reason,days:int):
		self.guildid = guildid
		self.days = days
		self.reason = reason
		json = {
			'days':days,
			'reason':reason
		}
		r = rs.post(url + f"guilds/{guildid}/prune",headers=headers,json=json)
		print(r.json())
	
	def getGuildInvites(self,guildid):
		self.guildid = guildid
		r = rs.get(url + f"guilds/{guildid}/invites",headers=headers)
		data = r.json()
		try:
			for data in data:
				print(
				f''' Guild Information : \n Name : {data['guild']['name']} \n ID : {data['guild']['id']} \n Description : {data['guild']['description']} \n Banner : {data['guild']['banner']} \n Icon : {data['guild']['icon']} \n Verification Level : {data['guild']['verification_level']} \n Vanity : {data['guild']['vanity_url_code']} \n  '''
				)
				time.sleep(1)
				print(f"""Invite Information: \n Invite code: {data['code']} \n Uses : {data['uses']} \n Max Age : {data['max_age']} \n Max uses : {data['max_uses']} \n Temporary : {data['temporary']} \n Created : {data['created_at']} \n   """)
				time.sleep(1)
				print(f"""
				Inviter Info : \n \n Name : {data['inviter']['username']} \n {data['inviter']['id']} \n Tag : {data['inviter']['discriminator']} \n Avatar : {data['inviter']['avatar']} \n \n Channel : \n Name :  {data['channel']['name']} \n ID : {data['channel']['id']} \n 
				""")
		except KeyError:
			return

	def getGuildIntegrations(self,guildid):
		self.guildid = guildid
		r = rs.get(url + f"guilds/{guildid}/integrations",headers=headers)
		data = r.json()
		for data in data:
			print(f'''
				Integration Info : \n Name : {data['name']} \n ID : {data['id']} \n Type : {data['type']} \n Enbaled : {data['enabled']} \n 
			''')
	
	def getGuildIntegrationsRaw(self,guildid):
		self.guildid = guildid
		r = rs.get(url + f"guilds/{guildid}/integrations",headers=headers)
		data = r.json()
		print(data)

	def deleteIntegrations(self,guildid,integrationid):
		self.guildid = guildid
		self.integrationid = integrationid
		r = rs.delete(url + f"guilds/{guildid}/integrations/{integrationid}",headers=headers)
		print(r.json())

	def getWidgetSetting(self,guildid):
		self.guildid = guildid
		r = rs.get(url + f"guilds/{guildid}/widget",headers=headers)
		print(r.json())

	def editWidgetSetting(self,guildid,enable:bool,channelid):
		self.guildid = guildid
		self.enable = enable
		self.channelid = channelid
		json = {
			"enabled": enable,
			"channel_id":str(channelid)
}
		r = rs.patch(url + f"guilds/{guildid}/widget",headers=headers,json=json)
		print(r.json())

	def getWidget(self,guildid):
		self.guildid= guildid
		r = rs.get(url + f"guilds/{guildid}/widget.json",headers=headers)
		print(r.json())

	



class channel():
	
	
	 #CHANNEL OBJECT
	
	def getChannel(self,channel_id):
		self.channel_id = channel_id
		r = rs.get(url + f"channels/{channel_id}",headers=headers)
		data = r.json()
		print(r.json())

	def editChannel(self,channelid,name,topic):
		self.channelid = channelid
		self.name = name
		self.topic = topic
		params = {
			'name':str(name),
			'topic':str(topic)
		}
		try:
			r = rs.patch(url + f"channels/{channelid}",headers=headers,json=params)
			print(r.json())
		except KeyError:
			print("KeyError")

	def getChannelMessages(self,channelid,limit:int=50):
		self.channelid = channelid
		self.limit = limit
		try:
			r = rs.get(url + f"channels/{channelid}/messages?limit={limit}",headers=headers)
			print(r.json())
		except KeyError:
			print("KeyError")

	def getSpecificMessages(self,channelid,messageid):
		self.channelid = channelid
		self.messageid = messageid
		try:
			r = rs.get(url + f"channels/{channelid}/messages/{messageid}",headers=headers)
			print(r.json())
		except KeyError:
			print("KeyError")
	
	def react(self,channelid,messageid,emojiname,emojiid):
		self.channelid = channelid
		self.messageid = messageid
		self.emojiname = emojiname
		self.emojiid = emojiid
		try:
			r = rs.put(url + f"channels/{channelid}/messages/{messageid}/reactions/{emojiname}:{emojiid}/@me",headers=headers)
			print(r.json())
		except KeyError:
			print('KeyError')

	def unreact(self,channelid,messageid,emojiname,emojiid):
		self.channelid = channelid
		self.messageid = messageid
		self.emojiname = emojiname
		self.emojiid = emojiid
		r = rs.delete(url + f"channels/{channelid}/messages/{messageid}/reactions/{emojiname}:{emojiid}/@me",headers=headers)
		print(r.json())
	
	def deleteUserReaction(self,channelid,messageid,emojiname,emojiid,userid):
		self.channelid = channelid
		self.messageid = messageid
		self.emojiname = emojiname
		self.emojiid = emojiid
		self.userid = userid
		r = rs.delete(url + f"channels/{channelid}/messages/{messageid}/reactions/{emojiname}:{emojiid}/{userid}",headers=headers)
		print(r.json())
	
	def deleteReactionForEmoji(self,channelid,messageid,emojiname,emojiid):
		self.channelid = channelid
		self.messageid = messageid
		self.emojiname = emojiname
		self.emojiid = emojiid
		r = rs.delete(url + f"channels/{channelid}/messages/{messageid}/reactions/{emojiname}:{emojiid}",headers=headers)
		print(r.json())
	
	def deleteAllReaction(self,channelid,messageid):
		self.channelid = channelid
		self.messageid = messageid
		r = rs.delete(url + f"channels/{channelid}/messages/{messageid}/reactions",headers=headers)
		print(r.json())

	def deleteMessage(self,channelid,messageid):
		self.channelid = channelid
		self.messageid = messageid
		r = rs.delete(url + f"channels/{channelid}/messages/{messageid}",headers=headers)
		print(r.json())

	def getChannelInvites(self,channelid):
		self.channelid = channelid
		r = rs.get(url + f"channels/{channelid}/invites",headers=headers)
		print(r.json())

	def createChannelInvite(self,channelid:str):
		self.channelid = channelid
		json = {
			'max_age':0
		}
		r = rs.post(url + f"channels/{channelid}/invites",headers=headers,json=json)
		print("\n \n RAW DATA \n \n \n" , r.json())
		print(f"INVITE CODE of {r.json()['guild']['name']} : " ,r.json()['code'])

class emoji():
	def getAllEmoji(self,guildid):
		self.guildid = guildid
		try:
			r = rs.get(url + f"guilds/{guildid}/emojis",headers=headers)
			key = r.json()
			for data in key:
				print(f''' \nEmoji Name : {data['name']} \nID: {data['id']} \n Animated : {data['animated']} \n Available : {data['available']} \n User Added : \n Name :  {data['user']['username']} \n ID : {data['user']['id']}  \n Tag : {data['user']['discriminator']} ''')
		except KeyError:
			print("KeyError")
		
		
	def getEmoji(self,guildid,emojiid):
		self.guildid = guildid
		self.emojiid = emojiid
		try:
			r = rs.get(url + f"guilds/{guildid}/emojis/{emojiid}",headers=headers)
			data = r.json()
			print(f''' \nEmoji Name : {data['name']} \nID: {data['id']} \n Animated : {data['animated']} \n Available : {data['available']} \n User Added : \n Name :  {data['user']['username']} \n ID : {data['user']['id']}  \n Tag : {data['user']['discriminator']} ''')
		except KeyError:
			print("KeyError")

	def editEmoji(self,guildid,emojiid,name):
		self.guildid = guildid
		self.emojiid = emojiid
		self.name = name
		try:
			json = {
				'name':name
			}
			r = rs.patch(url + f"guilds/{guildid}/emojis/{emojiid}",headers=headers,json=json)
			print(r.json())
		except KeyError:
			print('KeyError')

	def deleteEmoji(self,guildid,emojiid):
		self.guildid = guildid
		self.emojiid = emojiid
		r = rs.delete(url + f"guilds/{guildid}/emojis/{emojiid}",headers=headers)
		print(r.json())
	
class invite():
	def getInfoInvite(self,invitecode):
		self.invitecode = invitecode
		r = rs.get(url + f"invites/{invitecode}",headers=headers)
		print(r.json())
	
	def deleteInvite(self,invitecode):
		self.invitecode = invitecode
		r = rs.delete(url + f"invites/{invitecode}",headers=headers)
		print(r.json())

class auditlog():
	def auditlogs(self,guildid,limit:int,actiontype:None):
		self.guildid = guildid
		self.limit = limit
		self.actiontype = actiontype
		if not limit and actiontype:
			r = rs.get(url + f"guilds/{guildid}/audit-logs",headers=headers)
			print(r.json())
		elif actiontype == None:
			r = rs.get(url + f"guilds/{guildid}/audit-logs?limit=" + str(limit),headers=headers)
			print(r.json())
		elif actiontype != None:
			r = rs.get(url + f"guilds/{guildid}/audit-logs?ation_type=" + str(actiontype),headers=headers)
			print(r.json())

	def userAuditLogs(self,guildid,userid):
		self.guildid = guildid
		self.userid = userid
		if not userid == None:
			r = rs.get(url + f"guilds/{guildid}/audit-logs?limit=100?user_id" + str(userid),headers=headers)
			print(r.json())
		else:
			print("Please put user id")
		
class template():
	def getInfoTemplate(self,templatecode:str):
		self.templatecode = templatecode
		r = rs.get(url + f"guilds/templates/{templatecode}",headers=headers)
		print(r.json())
	
	def createTemplateGuild(self,templatecode):
		self.templatecode = templatecode
		r = rs.post(url + f"guilds/templates/{templatecode}",headers=headers)
		print(r.json())
	
	def getGuildTemplate(self,guildid):
		self.guildid = guildid
		r = rs.get(url + f"guilds/{guildid}/templates",headers=headers)
		print(r.json())

	def createGuildTemplate(self,guildid,name,description):
		self.name = name
		self.description = description
		self.guildid = guildid 
		json = {
			'name':str(name),
			'desccrption': str(description)
		}
		r = rs.post(url + f"guilds/{guildid}/templates",headers=headers,json=json)
		print(r.json())

	def syncTemplate(self,guildid,templatecode):
		self.guildid = guildid
		self.templatecode = templatecode
		r = rs.put(url + f"guilds/{guildid}/templates/{templatecode}",headers=headers)
		print(r.json())
	
	def modifyTemplate(self,guildid,templatecode,name,description):
		self.guildid = guildid
		self.name = name
		self.description = description
		self.templatecode = templatecode
		json = {
			'name': str(name),
			'description':str(description)
		}
		r = rs.patch(url + f"guilds/{guildid}/templates/{templatecode}",headers=headers,json=json)
		print(r.json())

	def deleteTemplate(self,guildid,templatecode):
		self.guildid = guildid
		self.templatecode = templatecode
		r = rs.delete(url + f"guilds/{guildid}/templates/{templatecode}",headers=headers)
		print(r.json())

class webhook():
	def createWebhook(self,channelid,name):
		self.channelid = channelid
		self.name = name
		json = {
			'name':str(name)
		}
		r = rs.post(url + f"channels/{channelid}/webhooks",headers=headers,json=json)
		print(r.json())
	

	def getChannelWebhooks(self,channelid):
		self.channelid = channelid
		r = rs.get(url + f"channels/{channelid}/webhooks",headers=headers)
		print(r.json())
	
	def getGuildWebhooks(self,guildid):
		self.guildid = guildid
		r = rs.get(url + f"guilds/{guildid}/webhooks",headers=headers)
		print(r.json())

	def getWebhook(self,webhookid):
		self.wehookid = webhookid
		r = rs.get(url + f"webhooks/{webhookid}",headers=headers)
		print(r.json())

	def getWebhookFromToken(self,webhookid,webhooktoken):
		self.webhookid = webhookid
		self.webhooktoken = webhooktoken
		r = rs.get(url + f"webhooks/{webhookid}/{webhooktoken}",headers=headers)
		print(r.json())

	def editWebhook(self,webhookid,name,channelid):
		self.webhookid = webhookid
		self.name = name
		self.channelid = channelid
		json = {
			'name':str(name),
			'channel_id':(channelid)
		}
		r = rs.patch(url + f"webhooks/{webhookid}",headers=headers,json=json)
		print(r.json())

	def deleteWebhook(self,webhookid):
		self.webhook = webhookid
		r = rs.delete(url + f"webhooks/{webhookid}",headers=headers)
		print(r.json())

	def exeuteWebhook(self,webhookid,webhooktoken,text):
		self.webhookid = webhookid
		self.webhooktoken = webhooktoken
		self.text = text
		json = {
			'content': str(text)
		}
		r = rs.post(url + f"webhooks/{webhookid}/{webhooktoken}",headers=headers,json=json)
		print(r.json())

	def deleteWebhookMessage(self,webhookid,webhooktoken,messageid):
		self.messageid = messageid
		self.webhookid = webhookid
		self.webhooktoken = webhooktoken
		r = rs.delete(url + f"webhooks/{webhookid}/{webhooktoken}/messages/{messageid}",headers=headers)
		print(r.json())
		
class user():

	def getMyInfo(self):
		r = rs.get(url + "users/@me",headers=headers)
		print(r.json())
	
	def getUser(self,userid):
		self.userid = userid
		r = rs.get(url + f"users/{userid}",headers=headers)
		print(r.json())
	
	def editUsername(self,name):
		self.name = name
		json = {
			'name':str(name)
		}
		r = rs.patch(url + 'users/@me',headers=headers,json=json)
		print(r.json())
	
	def editAvatar(self,avatar):
		self.avatar = avatar
		json = {
			'avatar':avatar
		}
		r = rs.patch(url + 'users/@me',headers=headers,json=json)
		print(r.json())

	def createDM(self,recipientid):
		self.recipientid = recipientid
		json = {
			'recipient_id':recipientid
		}
		r = rs.post(url + f"users/@me/channels",headers=headers,json=json)
		print(r.json())

	def getConnections(self):
		r = rs.get(url + "users/@me/connections",headers=headers)
		print(r.json())


