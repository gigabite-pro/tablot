<h1 align="center">Tablot</h1>

<p align="center">
  <a href="https://discord.gg/YRvmXT">
    <img src="https://badgen.net/badge/discord/join%20chat/7289DA?icon=discord" alt="Discord Server" />
  </a>
</p>

Whenever someone sends a public google sheets link in the server, Tablot takes the google sheet data and displays it in the form of a table.

We currently use <a href='https://pypi.org/project/terminaltables/'>terminaltables</a> to generate the table.

We are working on this just for the sake of getting familiarized with <a href='https://discordpy.readthedocs.io/en/latest/'>discord.py</a>

### why tablot?
"It's like one of those small things that makes your life 1% easier <3" ~ clash

### requirements
requires python
requires python-dotenv 
requires terminaltables

"hi rachit, pls create `requirements.txt` file"
"ok"

### commands

#### about
command: `$about`
action: bot introduces itself

#### ping
command: `$ping`
action: pings bot, returns bot latency in `ms`

#### stats
command: `$stats`
action: shows bot statistics and technical data

### building from source
Install everything written in "requirements" with pip install.
(or wait for rachit to create `requirements.txt`)

`cd` to `tablot` directory.

Create `.env` file and fill it with token

`BOT_TOKEN=<your token>`