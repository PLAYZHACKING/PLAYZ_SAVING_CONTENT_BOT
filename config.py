# Copyrighted by PLAY-Z 90 (2025)
# Please do not modify any file if you don't know what you're doing.
# --------------------------------------Credits---------------------------------#
# PLAY-Z 90 -> Modified & Optimized Version
# Original by Sentric Nova & Aresona
# Support channel --> t.me/PLAYZ_HACKING
# Support Group --> t.me/PLAY_Z_HACKING_DISCUSSION
# Please give credits if you fork or modify this bot.

# Configuration variables
CONFIG_VARS = {
    "API_ID": 22161204,  # API ID
    "API_HASH": "fdffc74281153b3338e4474f5640095e",  # API Hash
    "BOT_TOKEN": "7624968723:AAG7pNc3o4KMW4emb6xXVnj-GymqvdgKK3Y",  # Bot Token
    "LOGGER_GROUP": -1002466528202,  # Updated Logger Group Chat ID
    "PHONE_NUMBER": "",  # (Agar zaroori ho toh dal sakte ho)
    "OWNER_ID": [7107162691]  # Owner Telegram ID
}

# OWNER ko hi SUDO bana diya
SUDO_USERS = CONFIG_VARS["OWNER_ID"][:]  

# Check for missing configuration variables
missing_vars = [var for var, value in CONFIG_VARS.items() if not value]

if missing_vars:
    print("The following variables are missing:")
    for var in missing_vars:
        print(f"  - {var}")
    print("Please fill in the above variables for the userbot to work properly.")
    import sys
    sys.exit("User bot exited due to missing configuration variables.")
else:
    print("✅ All configuration variables are set! Bot is now running...")

# Accessing variables
API_ID = CONFIG_VARS["API_ID"]
API_HASH = CONFIG_VARS["API_HASH"]
BOT_TOKEN = CONFIG_VARS["BOT_TOKEN"]
LOGGER_GROUP = CONFIG_VARS["LOGGER_GROUP"]
PHONE_NUMBER = CONFIG_VARS["PHONE_NUMBER"]
OWNER_ID = CONFIG_VARS["OWNER_ID"]