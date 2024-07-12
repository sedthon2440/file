import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

super_sudoers = [7291869416]

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 9671629))
API_HASH = getenv("API_HASH", "be5c84e9dc1ca0e2b53d54b71e575124")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7390916656:AAHOpQV8TsCRuS2cwubLbsdyyrJf9wpgsb4")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://proceed58:proceed58@cluster0.p5s9ym5.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002059513294))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7291869416))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sedthon2440/file-sudo-left",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/veevvw")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



CHANNEL_NAME = getenv("CHANNEL_NAME", "سِۅٛࢪسِ مِاެتَࢪكَسِ")
CHANNEL_LINK = getenv("CHANNEL_LINK", "vvizinn")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/veevvw")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BACHw4IAWc8Cc9FBXg3Y9_L6oyx7p5DHrLtpj7A0SXJrUb3EyMVcAFLF_Ci04i5LT9R7C-SnD3VThQra6-JYVXF14bOvUSnoV8-oYmIBBtJgP0zLqYBIVkU9UkHMVOESi5PF4fzYaKOaehKUcqAzdqRVUum95DHcygHw177uKRcn0Ds3O5oOK5IsuRO0EOgWYKzvS3U35SAKFmJHNKTnCYwdu1wC-LFY59icP8bN5SKFBo0ruSvhfKryLTMgb_-VW1LgP1KNwvFwGNBdDM-8PzubhAHCAiWJppOAUVij8_Dcui26j7vBwerD95l7V-3FfXgfOCFP9zIYcPUcJp3K8viiiKAdhQAAAAEvAALVAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# API keys
TENOR_API_KEY = "2MAL8NKBOO01"

# Bot version, do not touch this
with open("version.txt") as f:
    version = f.read().strip()


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
disabled_plugins = []
get_bot_information = []
sudoers = []
backup_file = []
developer = []
command = ["/"]


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
STATS_IMG_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6be44cf94eb02b3b48275.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
