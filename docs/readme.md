# Documentation

1. Getting Started
    1. Using oxicord to make selfbots

1. [Usage](#Usage)

1. [Audit Logs](https://github.com/oxy-Op/oxicord/blob/master/docs/audit.md)
1. [Guild](https://github.com/oxy-Op/oxicord/blob/master/docs/guild.md)
1. [Channel](https://github.com/oxy-Op/oxicord/blob/master/docs/channel.md)
1. [Emoji](https://github.com/oxy-Op/oxicord/blob/master/docs/emoji.md)
1. [Webhook](https://github.com/oxy-Op/oxicord/blob/master/docs/webhook.md)
1. [Template](https://github.com/oxy-Op/oxicord/blob/master/docs/template.md)
1. [User](https://github.com/oxy-Op/oxicord/blob/master/docs/user.md)




# Getting started

1. Import Oxicord After [Installing](https://github.com/oxy-Op/oxicord#installation)
**Example**
```
import oxicord
```

1. Import all classes
**Example**
```
import oxicord
from oxicord import auditlog
from oxicord import guild
from oxicord import channel
from oxicord import user
from oxicord import template
from oxicord import webhook

# or do in single line
```


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
