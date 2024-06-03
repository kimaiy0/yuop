Telegram Link Remover Bot
This Telegram bot removes all links from text messages in a Telegram group or channel. It helps to maintain a clean and focused environment by preventing the sharing of external links.
Features

Removes links from all incoming text messages in a Telegram group or channel.
Configurable settings to allow certain users or specific groups/channels to post links.
Option to warn users about link removal.
Admin commands to manage bot settings and permissions.

Requirements

Python 3.6 or higher
Telethon library

Getting Started


Clone the repository:
bash Copy Comment Downloadgit clone https://github.com/your-username/telegram-link-remover-bot.git
cd telegram-link-remover-bot



Install the required dependencies:
bash Copy Comment Downloadpip install telethon



Create a new Telegram bot and obtain the API token. Refer to the Telegram Bot API documentation for instructions on creating a new bot.


Update the config.py file with your bot token and other desired configurations:
python Copy Comment Download# config.py
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
BOT_TOKEN = 'your_bot_token'



Run the bot:
bash Copy Comment Downloadpython bot.py



Invite the bot to your desired Telegram group or channel.


Configurations
The config.py file contains the following configurable settings:

API_ID: The API ID obtained from the Telegram API.
API_HASH: The API hash obtained from the Telegram API.
BOT_TOKEN: The token of your Telegram bot.
ALLOWED_LINKS: A list of allowed domains. Links from these domains will not be removed (e.g., ['example.com', 'telegram.org']).
WARN_ON_REMOVAL: Set to True to warn users about link removal.
ADMIN_IDS: A list of user IDs with admin access to manage bot settings and permissions.
GROUP_IDS: A list of group or channel IDs where the bot should be active.

Bot Commands
The following commands are available to the bot admins:

/start: Start the bot and display available commands.
/allowlink <domain>: Allow links from a specific domain.
/denylink <domain>: Deny links from a specific domain.
/listlinks: List all allowed domains.
/togglewarn: Toggle warning messages on link removal.
/addadmin <user_id>: Make a user an admin of the bot.
/removeadmin <user_id>: Remove admin permissions from a user.

Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push them to your branch.
Submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.