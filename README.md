# 🚀 **InfoNexus Discord Bot**

**InfoNexus** is your ultimate Discord companion, packed with over **100 API-based commands** that deliver information, fun, and interactive experiences! From trivia games to memes, GitHub integrations, and real-time data from public APIs, InfoNexus makes your Discord server more exciting than ever.

**Contact AnshKabra2012 on Discord to test the bot live!**

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

- **100+ API-Powered Commands:** Seamlessly integrated with APIs like NASA, OMDB, Tenor, and more.
- **Interactive Trivia Games:** Test your knowledge with trivia questions and engage with multiple-choice buttons.
- **User Registration:** Access commands only after registering for a more personalized experience.
- **Dynamic Help Menu:** Discover all commands with paginated embeds for easier navigation.
- **GitHub Integration:** Showcases your GitHub profile and encourages users to star your project directly from Discord.
- **Robust Error Handling:** Keeps everything running smoothly, even in unexpected scenarios.

**Contact AnshKabra2012 on Discord to test it now!**

---

## 📥 Installation

### Prerequisites

- **Python 3.7 or higher** installed on your machine. Download it [here](https://www.python.org/downloads/).
- A **Discord account** and a **Discord server** where you have permission to add bots.
- **Git** installed (optional but recommended). Download it [here](https://git-scm.com/downloads).

### Clone the Repository

```bash
git clone https://github.com/AnshKabra2012/InfoNexus-discord-bot.git
cd InfoNexus-discord-bot
```

### Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Unix or MacOS
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

Ensure your virtual environment is activated and run:

```bash
pip install -r requirements.txt
```

---

## 🔧 Setup

### 1. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **"New Application"** and give your bot a name (e.g., **InfoNexus**).
3. Navigate to the **"Bot"** tab and click **"Add Bot"**.
4. **Copy the Bot Token** and store it securely.

### 2. Invite the Bot to Your Server

1. Under **"OAuth2" > "Scopes"**, select **"bot"**.
2. Choose permissions like **Send Messages**, **Embed Links**, etc.
3. Copy the URL and paste it in your browser.
4. Select the server and click **"Authorize"**.

### 3. Configure Environment Variables

Create a `.env` file in the project directory and add your API keys:

```env
BOT_TOKEN=your_discord_bot_token
TENOR_API_KEY=your_tenor_api_key
NEWS_API_KEY=your_news_api_key
OMDB_API_KEY=your_omdb_api_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
NASA_API_KEY=your_nasa_api_key
```

---

## 💡 Usage

### Starting the Bot

```bash
python bot.py
```

You'll see a message in the console confirming the bot is online:

```
INFO:discord:Logged in as InfoNexus (ID: 123456789012345678)
------
```

### Registering Yourself

Before accessing commands, register with:

```plaintext
!register YourUsername
```

### Exploring Commands

View all commands using `!what`, which lists 100+ commands across multiple categories.

#### Popular Commands

- **Trivia Game:** `!trivia`
- **Random Joke:** `!joke`
- **Movie Info:** `!movie <movie name>`
- **Daily Horoscope:** `!horoscope <zodiac sign>`
- **NASA Astronomy Picture:** `!nasa_apod`
- **Random GIF:** `!gif <tag>`

### Interactive Features

- **Trivia:** Use multiple-choice buttons to answer trivia questions.
- **Help Menu:** Browse commands page by page with interactive buttons.

---

## 🤝 Contributing

Contributions are welcome to enhance InfoNexus! Here's how:

1. Fork the repository.
2. Create a branch: `git checkout -b feature/AmazingFeature`.
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`.
4. Push to the branch: `git push origin feature/AmazingFeature`.
5. Open a Pull Request.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 📫 Contact

- **GitHub:** [AnshKabra2012](https://github.com/AnshKabra2012)
- **GitHub Repository:** [InfoNexus-discord-bot](https://github.com/AnshKabra2012/InfoNexus-discord-bot)
- **Email:** [anshkabra.india@gmail.com](mailto:anshkabra.india@gmail.com)

---

✨ **Thank you for choosing InfoNexus!** 🎉
