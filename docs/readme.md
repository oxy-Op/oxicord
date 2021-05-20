# Documentation

1. Getting Started
    1. Using oxicord to make selfbots

1. Usage 

1. [Audit Logs](https://github.com/oxy-Op/oxicord/blob/master/docs/audit.md)
1. [Guild](https://github.com/oxy-Op/oxicord/blob/master/docs/guild.md)
1. [Channel](https://github.com/oxy-Op/oxicord/blob/master/docs/channel.md)
1. [Emoji](https://github.com/oxy-Op/oxicord/blob/master/docs/emoji.md)
1. [Webhook](https://github.com/oxy-Op/oxicord/blob/master/docs/webhook.md)
1. [Template](https://github.com/oxy-Op/oxicord/blob/master/docs/template.md)
1. [User](https://github.com/oxy-Op/oxicord/blob/master/docs/user.md)


# Start

* **Example Join guild by invite **
 ```
 import oxicord
from oxicord import guild


client = oxicord.Client("token")

def joinserver():
    return guild().join("xnUQqtUE")
joinserver()
```
