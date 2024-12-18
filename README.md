# 🚀 **InfoNexus Discord Bot**

![InfoNexus Banner](https://github.com/AnshKabra2012/InfoNexus-discord-bot/raw/main/banner.png)

**InfoNexus** is your ultimate Discord companion, packed with over **100 unique commands** that provide a wealth of information, fun facts, interactive experiences, and much more! Whether you're looking to brighten your server with jokes, dive into trivia, or fetch the latest tech news, InfoNexus has got you covered.

---

## 📜 Table of Contents

- [🌟 Features](#-features)
- [📥 Installation](#-installation)
- [🔧 Setup](#-setup)
- [💡 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [📫 Contact](#-contact)

---

## 🌟 Features

- **100+ Unique Commands:** From trivia games and jokes to fetching memes, quotes, and more.
- **Interactive Elements:** Engaging buttons for trivia and help commands.
- **User Registration:** Users must register to access full functionalities.
- **GitHub Integration:** Showcase and star the project directly from Discord.
- **Robust Error Handling:** Ensures smooth user experience.
- **Dynamic Help Menu:** Paginated embeds listing all available commands.

---

## 📥 Installation

### Prerequisites

- **Python 3.7 or higher** installed on your machine. Download it [here](https://www.python.org/downloads/).
- A **Discord account** and a **Discord server** where you have permission to add bots.
- **Git** installed (optional, but recommended). Download it [here](https://git-scm.com/downloads).

### Clone the Repository

```bash
git clone https://github.com/AnshKabra2012/InfoNexus-discord-bot.git
cd InfoNexus-discord-bot
```

### Create a Virtual Environment (Recommended)

Creating a virtual environment helps manage dependencies.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix or MacOS
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

Ensure you're in the project directory and the virtual environment is activated.

```bash
pip install -r requirements.txt
```

*If you encounter an error related to PyNaCl and don't plan to use voice features, you can safely ignore it. Otherwise, install PyNaCl:*

```bash
pip install pynacl
```

---

## 🔧 Setup

### 1. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on **"New Application"** and give your bot a name (e.g., **InfoNexus**).
3. Navigate to the **"Bot"** tab on the left sidebar.
4. Click **"Add Bot"** and confirm.
5. **Copy the Bot Token** by clicking **"Copy"** under the **"TOKEN"** section. **Keep it secure!**

### 2. Invite the Bot to Your Server

1. In the Developer Portal, go to the **"OAuth2"** tab.
2. Under **"Scopes"**, select **"bot"**.
3. Under **"Bot Permissions"**, select the necessary permissions (e.g., Send Messages, Embed Links, etc.).
4. **Copy the generated URL** and paste it into your browser.
5. Select the server you want to add the bot to and authorize.

### 3. Configure Environment Variables

1. In the project directory, create a `.env` file.

```bash
touch .env
```

2. Open the `.env` file in a text editor and add the following:

```env
BOT_TOKEN=your_discord_bot_token
TENOR_API_KEY=your_tenor_api_key
NEWS_API_KEY=your_news_api_key
OMDB_API_KEY=your_omdb_api_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
NASA_API_KEY=your_nasa_api_key
# Add other API keys as needed
```

> **Note:** Replace the placeholder values (`your_discord_bot_token`, etc.) with your actual API keys. Ensure that **`.env` is included in your `.gitignore`** to keep your credentials secure.

### 4. (Optional) Secure Your `.env` File

Add `.env` to your `.gitignore` to prevent it from being pushed to GitHub.

```gitignore
.env
```

---

## 💡 Usage

### Starting the Bot

Ensure your virtual environment is activated and run:

```bash
python bot.py
```

If everything is set up correctly, you should see logs indicating that the bot has successfully logged in:

```
INFO:discord:Logged in as InfoNexus (ID: 123456789012345678)
------
```

### Registering Yourself

Before accessing the bot's functionalities, users must register.

```plaintext
!register YourUsername
```

- **Example:**

```plaintext
!register Alex
```

### Exploring Commands

Use the `!what` command to view all available commands in a paginated format.

```plaintext
!what
```

#### Example Commands:

- **Random Fact:** `!fact`
- **Joke:** `!joke`
- **Trivia Game:** `!trivia`
- **Fetch a Meme:** `!meme`
- **GitHub User Info:** `!github <username>`
- **Translate Text:** `!translate <language_code> <text>`
- **And many more!**

### Interactive Commands

- **Trivia:** Engage in a fun trivia game with multiple-choice buttons.
- **Help:** Navigate through the help menu using "Previous" and "Next" buttons.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

### Steps to Contribute

1. **Fork the Project**

2. **Create Your Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m 'Add some feature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 📫 Contact

- **GitHub:** [AnshKabra2012](https://github.com/AnshKabra2012)
- **GitHub Repository:** [InfoNexus-discord-bot](https://github.com/AnshKabra2012/InfoNexus-discord-bot)
- **Email:** [your-email@example.com](mailto:your-email@example.com)

---

## 🌐 Connect with Me

![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) [@AnshKabra2012](https://github.com/AnshKabra2012)

---

## 🛠️ Built With

- [Discord.py](https://discordpy.readthedocs.io/en/stable/) - The Discord API wrapper for Python
- [Python](https://www.python.org/) - Programming Language
- Various Public APIs for data fetching

---

## 🖼️ Screenshots

### **1. Registration**

![Registration Command](https://github.com/AnshKabra2012/InfoNexus-discord-bot/raw/main/screenshots/register.png)

### **2. Help Menu**

![Help Command](https://github.com/AnshKabra2012/InfoNexus-discord-bot/raw/main/screenshots/help.png)

### **3. Trivia Game**

![Trivia Command](https://github.com/AnshKabra2012/InfoNexus-discord-bot/raw/main/screenshots/trivia.png)

---

## 🎉 Acknowledgments

- [Official Joke API](https://official-joke-api.appspot.com/)
- [Open Trivia DB](https://opentdb.com/)
- [Quotable API](https://github.com/lukePeavey/quotable)
- [Dog CEO API](https://dog.ceo/dog-api/)
- [The Cat API](https://thecatapi.com/)
- [Other APIs as utilized in the project]

---

✨ **Thank you for choosing InfoNexus!** ✨

Feel free to explore, have fun, and contribute to making this bot even better!

---
