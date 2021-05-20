# Oxicord
An API Wrapper For Discord - Version 1.0.0

**Oxicord is an API Wrapper For [disord](https://discord.com) Using [Python](https://python.org) . This is created for developers to use and understand such commands** 
<br />

_Oxicord is an open source API Wrapper created by [Oxy](https://github.com/oxy-Op/)_



## Installation


1. ```git clone https://github.com/oxy-Op/oxicord.git```    or

1. ```pip install git+https://github.com/oxy-Op/oxicord.git```   or

1. ``` pip install oxicord``` or

1. Download [zip](https://codeload.github.com/oxy-Op/oxicord/zip/refs/heads/master)


### Requirements

1. [Python](https://python.org/downloads)
   1. [Python for Windows](https://www.python.org/downloads/windows/)
   1. [Mac Os X](https://www.python.org/downloads/mac-osx/)
   1. [Other](https://www.python.org/download/other/)

1. **Module [Requests](https://pypi.org/project/requests/)**



## Usage
###### Documentation
1. [Documentation](https://github.com/oxy-Op/oxicord/tree/master/docs)


## Example Usage

```
import oxicord
from oxicord import user

client = oxicord.Client("token")

def getMe():
    return user().getMyInfo()
getMe()
```

## Links 
* [github](https://github.com/oxy-Op/oxicord)
* [PyPi](https://example.com)
