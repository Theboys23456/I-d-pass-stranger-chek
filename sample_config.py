import os

api_id = 21567814
api_hash = os.environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
bot_token = os.environ.get("7055271655:AAHbGHrfHspISSSTP0c7mCogxqufQFTFnJw")
auth_users = os.environ.get("AUTH_USERS", "6126688051")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6126688051")
owner_users = [int(num) for num in osowner_users.split(",")]
