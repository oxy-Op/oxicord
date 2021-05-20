# Documentation

1. [Getting Started](https://github.com/oxy-Op/oxicord/tree/master/docs#getting-started)
    1. [Using oxicord to make selfbots](https://github.com/oxy-Op/oxicord/tree/master/docs#creating-first-selfbot)

1. [Usage](#Usage)

1. [Audit Logs](https://github.com/oxy-Op/oxicord/blob/master/docs/audit.md)
1. [Guild](https://github.com/oxy-Op/oxicord/blob/master/docs/guild.md)
1. [Channel](https://github.com/oxy-Op/oxicord/blob/master/docs/channel.md)
1. [Emoji](https://github.com/oxy-Op/oxicord/blob/master/docs/emoji.md)
1. [Invite](https://github.com/oxy-Op/oxicord/blob/master/docs/invite.md)
3. [Webhook](https://github.com/oxy-Op/oxicord/blob/master/docs/webhook.md)
4. [Template](https://github.com/oxy-Op/oxicord/blob/master/docs/template.md)
5. [User](https://github.com/oxy-Op/oxicord/blob/master/docs/user.md)




# Getting started

* Import Oxicord After [Installing](https://github.com/oxy-Op/oxicord#installation) <br />
**Example**
```
import oxicord
```

* Import all classes <br />
**Example**
```
import oxicord
from oxicord import auditlog
from oxicord import invite
from oxicord import emoji
from oxicord import guild
from oxicord import channel
from oxicord import user
from oxicord import template
from oxicord import webhook


# or do in single line

```
# Creating selfbot

```
import oxicord

bot = oxicord.Client("token")

```
> NOTE : Please Enter a valid user token <br/> <br / >
> Congo! You created your selfbot


# Usage

* **Example Join guild by invite**
 ```
 import oxicord
from oxicord import guild


client = oxicord.Client("token")

def joinserver():
    return guild().join("xnUQqtUE")
joinserver()
```
