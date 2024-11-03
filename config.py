import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 29727048
API_HASH = "38d104adbd94c66a349714abd7977d80"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7605039383:AAE1mgOumbsRbJo6OYP2GUxTOCmZS68-qYs"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://ms7371091:ms7371091@cluster0.vwfw6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002467044807

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6943348077

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/+565zq0XLr2g1ZjI1"
SUPPORT_GROUP = "https://t.me/+zdzQ87N-ntxiZDNl"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQHFmUgAwzDySLMT945VnCI5m4fJ5DB2-sAkRvg29RnLJNlEdTFbIEMj-ESSCHLRhhFxdPyxrjg2InxIWALUvKm290fPmSQ9Z2T73QxgLcoa_2BQy1mgzkX5kSPNNFtg5ybRFXC5Ya07TXSGYRqlhFzPL_hzZ3WSh44RO7iM-6ZoXoO5XXQz2ngUjAl0ipt64ywZDHOUQI3kR7Frk2lAfk-KAMLJS9ggog4efXDyIRvOHe_0ImDmWWKPTE_4RQOl3736lQRzG0aiv4bIPuF3a8Vi0xeqN8oIMBFJQfzbevVvmqmgNuRyXKO1QK3aKnF_NXGtyYjupXqHKX9L0TrFIC-AW3repgAAAAGd2xVtAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"

PING_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"
STATS_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"
STREAM_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b799e84b45f58abc286c9-0ff57e5fce7d6a8dd5.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
