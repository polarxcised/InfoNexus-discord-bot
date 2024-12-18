# bot.py

import os
import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import requests
import random
import asyncio
import logging
import json
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys and tokens from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
TENOR_API_KEY = os.getenv("TENOR_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NASA_API_KEY = os.getenv("NASA_API_KEY")
# Add other API keys as needed

# Validate essential API keys
required_keys = {
    "BOT_TOKEN": BOT_TOKEN,
    "TENOR_API_KEY": TENOR_API_KEY,
    "NEWS_API_KEY": NEWS_API_KEY,
    "OMDB_API_KEY": OMDB_API_KEY,
    "ALPHA_VANTAGE_API_KEY": ALPHA_VANTAGE_API_KEY,
    "NASA_API_KEY": NASA_API_KEY
}

missing_keys = [key for key, value in required_keys.items() if not value]
if missing_keys:
    missing = ", ".join(missing_keys)
    raise EnvironmentError(f"Missing required environment variables: {missing}")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')

# Define bot intents
intents = discord.Intents.default()
intents.message_content = True  # Enable access to message content

# Initialize bot
bot = commands.Bot(command_prefix="!", intents=intents, description="InfoNexus - The Ultimate Discord Bot!")

# Initialize user data storage
USER_DATA_FILE = "user_data.json"

if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump({}, f)

def load_user_data():
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)

def save_user_data(data):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Event: Bot is ready
@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user} (ID: {bot.user.id})")
    logger.info("------")
    bot.launch_time = datetime.utcnow()

# Helper Functions

def fetch_trivia_question(category=None):
    """Fetch a trivia question from Open Trivia DB."""
    base_url = "https://opentdb.com/api.php"
    params = {"amount": 1}
    if category:
        category_map = {
            "general": 9,
            "books": 10,
            "film": 11,
            "music": 12,
            "science": 17,
            "computers": 18,
            "math": 19,
            "sports": 21,
            "geography": 22,
            "history": 23,
            "politics": 24,
            "art": 25,
            "celebrities": 26,
            "animals": 27,
            "vehicles": 28,
            "comics": 29,
            "gadgets": 30,
            "anime": 31,
            "cartoon": 32
        }
        category_id = category_map.get(category.lower())
        if category_id:
            params["category"] = category_id
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["results"][0] if data["results"] else None
    return None

def fetch_random_fact():
    """Fetch a random fact from Useless Facts API."""
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    if response.status_code == 200:
        return response.json().get("text", "No fact found.")
    return "Couldn't fetch a fact right now."

def fetch_joke():
    """Fetch a random joke from Official Joke API."""
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    return "Couldn't fetch a joke right now."

def fetch_quote():
    """Fetch a random inspirational quote from Quotable API."""
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return f"\"{data['content']}\" - {data['author']}"
    return "Couldn't fetch a quote right now."

def fetch_random_dog_image():
    """Fetch a random dog image from Dog CEO API."""
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        return response.json().get("message", "")
    return ""

def fetch_random_cat_image():
    """Fetch a random cat image from TheCatAPI."""
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0].get("url", "")
    return ""

def fetch_spells():
    """Fetch spells from Harry Potter API."""
    response = requests.get("https://hp-api.onrender.com/api/spells")
    if response.status_code == 200:
        return response.json()
    return []

def fetch_random_meal():
    """Fetch a random meal from TheMealDB."""
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    if response.status_code == 200:
        data = response.json()
        if data.get("meals"):
            return data["meals"][0]
    return {}

def fetch_reddit_post(subreddit):
    """Fetch a random post from a subreddit."""
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/random.json", headers=headers)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            post = data[0]['data']['children'][0]['data']
            title = post.get("title", "No title")
            url = post.get("url", "")
            return title, url
    return None, None

def fetch_github_user(username):
    """Fetch GitHub user information."""
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        data = response.json()
        name = data.get("name", "N/A")
        bio = data.get("bio", "N/A")
        repos = data.get("public_repos", 0)
        followers = data.get("followers", 0)
        following = data.get("following", 0)
        avatar = data.get("avatar_url", "")
        return name, bio, repos, followers, following, avatar
    return None

def fetch_movie_info(title):
    """Fetch movie information from OMDB API."""
    response = requests.get(f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}")
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            title = data.get("Title", "N/A")
            year = data.get("Year", "N/A")
            genre = data.get("Genre", "N/A")
            director = data.get("Director", "N/A")
            plot = data.get("Plot", "N/A")
            poster = data.get("Poster", "")
            return title, year, genre, director, plot, poster
    return None

def fetch_alpha_vantage_stock(symbol):
    """Fetch stock price from Alpha Vantage API."""
    response = requests.get(
        f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    )
    if response.status_code == 200:
        data = response.json()
        quote = data.get("Global Quote", {})
        price = quote.get("05. price", "N/A")
        change = quote.get("09. change", "N/A")
        return price, change
    return None, None

def fetch_bitcoin_price():
    """Fetch current Bitcoin price in USD from Coindesk API."""
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
    if response.status_code == 200:
        data = response.json()
        rate = data["bpi"]["USD"]["rate"]
        return rate
    return "Couldn't fetch Bitcoin price right now."

def fetch_nasa_apod():
    """Fetch NASA Astronomy Picture of the Day."""
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}")
    if response.status_code == 200:
        data = response.json()
        title = data.get("title", "N/A")
        explanation = data.get("explanation", "N/A")
        url = data.get("url", "")
        return title, explanation, url
    return None, None, None

def fetch_tenor_gif(tag="random"):
    """Fetch a random GIF from Tenor."""
    response = requests.get(f"https://tenor.googleapis.com/v2/search?q={tag}&key={TENOR_API_KEY}&limit=1")
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            media = results[0].get("media_formats", {})
            gif = media.get("gif", {}).get("url")
            if gif:
                return gif
    return None

def fetch_trending_repositories():
    """Fetch trending repositories from GitHub Trending API."""
    # Note: GitHub doesn't provide an official trending API. Using a third-party API.
    response = requests.get("https://ghapi.huchen.dev/repositories?since=daily")
    if response.status_code == 200:
        data = response.json()
        trending_repos = [f"**{repo['name']}** by **{repo['author']}**\n[Repository]({repo['url']})" for repo in data[:5]]
        return trending_repos
    return ["Couldn't fetch trending repositories right now."]

def fetch_random_fact_about_number(number):
    """Fetch a fact about a number from Numbers API."""
    response = requests.get(f"http://numbersapi.com/{number}/trivia")
    if response.status_code == 200:
        return response.text
    return "Couldn't fetch a number fact right now."

def fetch_random_fortune():
    """Fetch a random fortune from the lucky API."""
    # As the original API may not be reliable, using a static list as a placeholder
    fortunes = [
        "You will have a great day!",
        "Success is in your future.",
        "Adventure awaits you.",
        "Embrace the challenges ahead.",
        "A pleasant surprise is waiting for you."
    ]
    return random.choice(fortunes)

def fetch_random_meme():
    """Fetch a random meme from Meme API."""
    response = requests.get("https://meme-api.herokuapp.com/gimme")
    if response.status_code == 200:
        data = response.json()
        title = data.get("title", "No title")
        url = data.get("url", "")
        return title, url
    return None, None

def fetch_dad_joke():
    """Fetch a random dad joke from icanhazdadjoke API."""
    headers = {'Accept': 'application/json'}
    response = requests.get("https://icanhazdadjoke.com/", headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("joke", "Couldn't fetch a joke right now.")
    return "Couldn't fetch a joke right now."

def fetch_random_fox_image():
    """Fetch a random fox image from randomfox.ca."""
    response = requests.get("https://randomfox.ca/floof/")
    if response.status_code == 200:
        data = response.json()
        return data.get("image", "")
    return ""

def fetch_inspirational_story():
    """Fetch an inspirational story from a public API."""
    # Placeholder: No widely available public API for inspirational stories. Using a static story.
    return "Once upon a time, in a land far, far away, there lived a brave adventurer who overcame all odds to achieve their dreams."

def fetch_horoscope(sign):
    """Fetch daily horoscope from Horoscope API."""
    response = requests.post(f"https://aztro.sameerkumar.website/?sign={sign.lower()}&day=today")
    if response.status_code == 200:
        data = response.json()
        horoscope = data.get("description", "No horoscope found.")
        return horoscope
    return "Couldn't fetch horoscope right now."

def fetch_dictionary_definition(word):
    """Fetch the definition of a word from Dictionary API."""
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()[0]
        definitions = data["meanings"][0]["definitions"][0]["definition"]
        example = data["meanings"][0]["definitions"][0].get("example", "No example provided.")
        return definitions, example
    return None, None

def fetch_random_activity():
    """Fetch a random activity suggestion from Bored API."""
    response = requests.get("https://www.boredapi.com/api/activity/")
    if response.status_code == 200:
        data = response.json()
        return data.get("activity", "Couldn't fetch an activity right now.")
    return "Couldn't fetch an activity right now."

def fetch_random_music_quote():
    """Fetch a random music-related quote from a static list."""
    music_quotes = [
        "Music is the universal language of mankind. – Henry Wadsworth Longfellow",
        "Where words fail, music speaks. – Hans Christian Andersen",
        "Without music, life would be a mistake. – Friedrich Nietzsche",
        "One good thing about music, when it hits you, you feel no pain. – Bob Marley",
        "Music expresses that which cannot be said and on which it is impossible to be silent. – Victor Hugo"
    ]
    return random.choice(music_quotes)

def fetch_random_art_quote():
    """Fetch a random art-related quote from a static list."""
    art_quotes = [
        "Every artist was first an amateur. – Ralph Waldo Emerson",
        "Art is not what you see, but what you make others see. – Edgar Degas",
        "Creativity takes courage. – Henri Matisse",
        "Art enables us to find ourselves and lose ourselves at the same time. – Thomas Merton",
        "The purpose of art is washing the dust of daily life off our souls. – Pablo Picasso"
    ]
    return random.choice(art_quotes)

def fetch_random_math_fact():
    """Fetch a random math fact from a static list."""
    math_facts = [
        "Zero is the only number that cannot be represented by Roman numerals.",
        "A triangle has three sides, a square has four.",
        "The number pi is irrational.",
        "There are infinitely many prime numbers.",
        "Euler's identity is considered the most beautiful theorem in mathematics."
    ]
    return random.choice(math_facts)

def fetch_random_geography_fact():
    """Fetch a random geography fact from a static list."""
    geography_facts = [
        "Canada has the longest coastline in the world.",
        "Russia is the largest country by area.",
        "There are seven continents on Earth.",
        "The Amazon River is the largest by discharge volume.",
        "Mount Everest is the highest mountain above sea level."
    ]
    return random.choice(geography_facts)

def fetch_random_politics_fact():
    """Fetch a random politics fact from a static list."""
    politics_facts = [
        "The United Nations has 193 member states.",
        "The first female Prime Minister was Sirimavo Bandaranaike of Sri Lanka.",
        "The term 'democracy' comes from the Greek words 'demos' and 'kratos'.",
        "There are over 200 recognized political systems globally.",
        "The longest-serving head of state was King Bhumibol Adulyadej of Thailand."
    ]
    return random.choice(politics_facts)

def fetch_random_computer_fact():
    """Fetch a random computer fact from a static list."""
    computer_facts = [
        "The first computer bug was a moth trapped in a Harvard Mark II computer.",
        "The QWERTY keyboard was designed to prevent typewriter jams.",
        "The first computer virus was created in 1983.",
        "Approximately 90% of the world's data has been created in the last two years.",
        "The term 'debugging' was popularized by Grace Hopper."
    ]
    return random.choice(computer_facts)

def fetch_random_cinema_fact():
    """Fetch a random cinema fact from a static list."""
    cinema_facts = [
        "The first feature-length film was 'The Story of the Kelly Gang' (1906).",
        "Avatar is the highest-grossing film of all time.",
        "Gone with the Wind was the first film to earn over $1 billion.",
        "The silent film era lasted from the late 1890s to the late 1920s.",
        "Pixar's 'Toy Story' was the first entirely computer-animated feature film."
    ]
    return random.choice(cinema_facts)

def fetch_random_religion_fact():
    """Fetch a random religion fact from a static list."""
    religion_facts = [
        "There are over 4,000 religions in the world.",
        "Buddhism originated in India around the 5th century BCE.",
        "Christianity is the largest religion globally.",
        "Islam was founded in the 7th century CE in Mecca.",
        "Hinduism is the oldest living religion."
    ]
    return random.choice(religion_facts)

def fetch_random_physics_fact():
    """Fetch a random physics fact from a static list."""
    physics_facts = [
        "Light can behave both as a wave and as a particle.",
        "Einstein's theory of relativity revolutionized physics.",
        "Quantum entanglement is a phenomenon where particles remain connected.",
        "The speed of light is approximately 299,792 kilometers per second.",
        "Black holes are regions in space with gravitational pulls so strong that nothing can escape."
    ]
    return random.choice(physics_facts)

def fetch_random_technology_fact():
    """Fetch a random technology fact from a static list."""
    technology_facts = [
        "The first computer was invented in the 1940s.",
        "The internet was initially developed for military use.",
        "Over 3 billion people use the internet worldwide.",
        "Artificial Intelligence is a rapidly growing field in technology.",
        "Blockchain technology underpins cryptocurrencies like Bitcoin."
    ]
    return random.choice(technology_facts)

def fetch_random_environment_fact():
    """Fetch a random environment fact from a static list."""
    environment_facts = [
        "The Amazon rainforest produces over 20% of the world's oxygen.",
        "Plastic pollution is one of the biggest threats to marine life.",
        "Renewable energy sources are crucial for combating climate change.",
        "Deforestation contributes to the loss of biodiversity.",
        "Recycling helps reduce greenhouse gas emissions."
    ]
    return random.choice(environment_facts)

def fetch_random_entertainment_fact():
    """Fetch a random entertainment fact from a static list."""
    entertainment_facts = [
        "The Grammy Awards were established in 1959.",
        "The Oscars statuette is made of gold-plated britannium.",
        "MTV was launched on August 1, 1981.",
        "The Super Bowl is one of the most-watched sporting events in the US.",
        "Broadway in New York City is known for its theater productions."
    ]
    return random.choice(entertainment_facts)

def fetch_random_fashion_fact():
    """Fetch a random fashion fact from a static list."""
    fashion_facts = [
        "The little black dress became popular thanks to Coco Chanel.",
        "Blue jeans were invented by Levi Strauss in the 1870s.",
        "The first fashion magazine was published in Germany in 1586.",
        "Heels were originally worn by men in the 10th century.",
        "Nike is one of the largest sportswear brands in the world."
    ]
    return random.choice(fashion_facts)

def fetch_random_lifestyle_fact():
    """Fetch a random lifestyle fact from a static list."""
    lifestyle_facts = [
        "Meditation can reduce stress and improve focus.",
        "A balanced diet is essential for maintaining good health.",
        "Regular exercise boosts mental and physical well-being.",
        "Adequate sleep is crucial for overall health.",
        "Hydration plays a key role in bodily functions."
    ]
    return random.choice(lifestyle_facts)

# Interactive Views

class TriviaView(View):
    def __init__(self, correct_answer, options):
        super().__init__(timeout=60)
        self.correct_answer = correct_answer
        self.options = options

        for option in options:
            button = Button(label=option, style=discord.ButtonStyle.primary)
            button.callback = self.create_callback(option)
            self.add_item(button)

    def create_callback(self, selected_option):
        async def callback(interaction: discord.Interaction):
            if selected_option == self.correct_answer:
                content = f"✅ Correct! The answer was: **{self.correct_answer}**"
            else:
                content = f"❌ Incorrect! The correct answer was: **{self.correct_answer}**"

            # Disable all buttons after answer
            for child in self.children:
                child.disabled = True

            await interaction.response.edit_message(content=content, view=self)
            self.stop()

        return callback

    async def on_timeout(self):
        # Disable all buttons on timeout
        for child in self.children:
            child.disabled = True
        if hasattr(self, 'message'):
            await self.message.edit(content="⏰ Time's up! You didn't answer in time.", view=self)

class HelpView(View):
    def __init__(self, embeds):
        super().__init__(timeout=180)
        self.embeds = embeds
        self.current = 0

        # Previous Button
        self.previous_button = Button(label="Previous", style=discord.ButtonStyle.secondary)
        self.previous_button.callback = self.previous_page
        self.add_item(self.previous_button)

        # Next Button
        self.next_button = Button(label="Next", style=discord.ButtonStyle.secondary)
        self.next_button.callback = self.next_page
        self.add_item(self.next_button)

    async def previous_page(self, interaction: discord.Interaction):
        if self.current > 0:
            self.current -= 1
            await interaction.response.edit_message(embed=self.embeds[self.current], view=self)

    async def next_page(self, interaction: discord.Interaction):
        if self.current < len(self.embeds) - 1:
            self.current += 1
            await interaction.response.edit_message(embed=self.embeds[self.current], view=self)

    async def on_timeout(self):
        # Disable buttons on timeout
        for child in self.children:
            child.disabled = True
        if hasattr(self, 'message'):
            await self.message.edit(view=self)

# Enforced Registration Decorator
def is_registered():
    async def predicate(ctx):
        user_data = load_user_data()
        return str(ctx.author.id) in user_data
    return commands.check(predicate)

# Commands

# 1. About Command
@bot.command(name="about", help="Get information about the bot. Usage: !about")
async def about(ctx):
    embed = discord.Embed(
        title="🤖 About InfoNexus",
        description="Welcome to InfoNexus! I'm your ultimate Discord companion, here to provide you with a wealth of information, fun facts, and interactive experiences.",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="⭐ Star Our Project",
        value="If you enjoy using me, please consider starring our GitHub repository!",
        inline=False
    )
    embed.add_field(
        name="💻 GitHub Repository",
        value="[InfoNexus-discord-bot](https://github.com/AnshKabra2012/InfoNexus-discord-bot)",
        inline=False
    )
    # GitHub logo URL (you can replace this with a different URL if desired)
    github_logo_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
    embed.set_footer(text="Thank you for using InfoNexus!", icon_url=github_logo_url)
    await ctx.send(embed=embed)

# 2. Register Command
@bot.command(name="register", help="Register yourself to use the bot. Usage: !register <username>")
async def register(ctx, username: str = None):
    if not username:
        await ctx.send("Please provide a username. Usage: `!register <username>`")
        return
    user_data = load_user_data()
    user_data[str(ctx.author.id)] = {
        "username": username,
        "registered_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    }
    save_user_data(user_data)
    embed = discord.Embed(
        title="✅ Registration Successful!",
        description=f"Welcome, **{username}**! You can now access all the bot's features.",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

# 3. Trivia
@bot.command(name="trivia", help="Start a trivia game. Usage: !trivia [category]")
@is_registered()
async def trivia(ctx, category: str = "general"):
    question = fetch_trivia_question(category)
    if question:
        embed = discord.Embed(
            title="Trivia Time!",
            description=question["question"],
            color=discord.Color.blue()
        )
        answers = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(answers)
        view = TriviaView(question["correct_answer"], answers)
        embed.add_field(name="Choose the correct answer:", value="Click one of the buttons below.", inline=False)
        message = await ctx.send(embed=embed, view=view)
        view.message = message  # Reference for timeout handling
    else:
        await ctx.send("Couldn't fetch a trivia question right now.")

# 4. Random Fact
@bot.command(name="fact", help="Get a random fact. Usage: !fact")
@is_registered()
async def fact(ctx):
    random_fact = fetch_random_fact()
    embed = discord.Embed(
        title="🤔 Random Fact",
        description=random_fact,
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)

# 5. Joke
@bot.command(name="joke", help="Get a random joke. Usage: !joke")
@is_registered()
async def joke(ctx):
    joke_text = fetch_joke()
    embed = discord.Embed(
        title="😂 Here's a joke for you!",
        description=joke_text,
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed)

# 6. Quote
@bot.command(name="quote", help="Get a random inspirational quote. Usage: !quote")
@is_registered()
async def quote(ctx):
    quote_text = fetch_quote()
    embed = discord.Embed(
        title="🌟 Inspirational Quote",
        description=quote_text,
        color=discord.Color.purple()
    )
    await ctx.send(embed=embed)

# 7. Dog Image
@bot.command(name="dog", help="Get a random dog image. Usage: !dog")
@is_registered()
async def dog(ctx):
    image_url = fetch_random_dog_image()
    if image_url:
        embed = discord.Embed(
            title="🐶 Here's a cute dog for you!",
            color=discord.Color.brown()
        ).set_image(url=image_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Couldn't fetch a dog image right now.")

# 8. Cat Image
@bot.command(name="cat", help="Get a random cat image. Usage: !cat")
@is_registered()
async def cat(ctx):
    image_url = fetch_random_cat_image()
    if image_url:
        embed = discord.Embed(
            title="🐱 Here's a cute cat for you!",
            color=discord.Color.dark_purple()
        ).set_image(url=image_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Couldn't fetch a cat image right now.")

# 9. Spell (Harry Potter)
@bot.command(name="spell", help="Get a random Harry Potter spell. Usage: !spell")
@is_registered()
async def spell(ctx):
    spells = fetch_spells()
    if spells:
        spell = random.choice(spells)
        embed = discord.Embed(
            title=f"🔮 {spell['name']}",
            description=spell['description'],
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Couldn't fetch a spell right now.")

# 10. Meal
@bot.command(name="meal", help="Get a random meal. Usage: !meal")
@is_registered()
async def meal(ctx):
    meal = fetch_random_meal()
    if meal:
        embed = discord.Embed(
            title=f"🍽️ {meal['strMeal']}",
            description=f"Cuisine: {meal['strArea']}\nCategory: {meal['strCategory']}\nIngredient: {meal['strIngredient1']}",
            color=discord.Color.orange()
        ).set_image(url=meal['strMealThumb'])
        await ctx.send(embed=embed)
    else:
        await ctx.send("Couldn't fetch a meal right now.")

# ... [Continue defining other commands uniquely without duplicates]

# Example of a unique command
# 11. Reddit Post
@bot.command(name="reddit", help="Get a random post from a subreddit. Usage: !reddit <subreddit>")
@is_registered()
async def reddit(ctx, subreddit: str = None):
    if not subreddit:
        await ctx.send("Please specify a subreddit. Usage: `!reddit <subreddit>`")
        return
    title, url = fetch_reddit_post(subreddit)
    if title and url:
        embed = discord.Embed(
            title=title,
            url=url,
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Couldn't fetch a Reddit post. Please check the subreddit name.")

# 12. GitHub User Info
@bot.command(name="github", help="Get GitHub user information. Usage: !github <username>")
@is_registered()
async def github(ctx, username: str = None):
    if not username:
        await ctx.send("Please specify a GitHub username. Usage: `!github <username>`")
        return
    result = fetch_github_user(username)
    if result:
        name, bio, repos, followers, following, avatar = result
        embed = discord.Embed(
            title=f"👤 GitHub User: {username}",
            description=bio,
            color=discord.Color.dark_blue()
        )
        embed.set_thumbnail(url=avatar)
        embed.add_field(name="Name", value=name, inline=True)
        embed.add_field(name="Public Repos", value=repos, inline=True)
        embed.add_field(name="Followers", value=followers, inline=True)
        embed.add_field(name="Following", value=following, inline=True)
        embed.add_field(name="Profile", value=f"[GitHub Profile](https://github.com/{username})", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Couldn't fetch GitHub user information. Please check the username.")

# ... [Continue with all other unique commands up to your desired number]

# 50. Random Technology Fact
@bot.command(name="technology_fact", help="Get a random technology fact. Usage: !technology_fact")
@is_registered()
async def technology_fact(ctx):
    fact = fetch_random_technology_fact()
    embed = discord.Embed(
        title="🖥️ Technology Fact",
        description=fact,
        color=discord.Color.teal()
    )
    await ctx.send(embed=embed)

# 63. Random Weather Fact
@bot.command(name="weather_fact", help="Get a random weather fact. Usage: !weather_fact")
@is_registered()
async def weather_fact(ctx):
    fact = fetch_random_weather_fact()
    embed = discord.Embed(
        title="🌦️ Weather Fact",
        description=fact,
        color=discord.Color.teal()
    )
    await ctx.send(embed=embed)

# 64. Random Space Fact
@bot.command(name="space_fact", help="Get a random space fact. Usage: !space_fact")
@is_registered()
async def space_fact(ctx):
    fact = fetch_random_space_fact()
    embed = discord.Embed(
        title="🚀 Space Fact",
        description=fact,
        color=discord.Color.teal()
    )
    await ctx.send(embed=embed)

# ... [Ensure all remaining commands are uniquely defined]

# 100. Random Health Tip
@bot.command(name="health_tip", help="Get a random health tip. Usage: !health_tip")
@is_registered()
async def health_tip(ctx):
    tip = fetch_random_health_tip()
    embed = discord.Embed(
        title="💊 Health Tip",
        description=tip,
        color=discord.Color.teal()
    )
    await ctx.send(embed=embed)

# Help Command

@bot.command(name="what", help="List all available commands. Usage: !what")
async def what(ctx):
    # Gather all commands with their help descriptions
    commands_list = []
    for command in bot.commands:
        if not command.hidden and command.name != "what":
            help_desc = command.help or "No description."
            commands_list.append(f"!{command.name} - {help_desc}")

    # Split commands into chunks of 10 for pagination
    per_page = 10
    chunks = [commands_list[i:i + per_page] for i in range(0, len(commands_list), per_page)]
    embeds = []
    for idx, chunk in enumerate(chunks, 1):
        embed = discord.Embed(
            title=f"📜 Available Commands (Page {idx}/{len(chunks)})",
            description="\n\n".join(chunk),
            color=discord.Color.gold()
        )
        embeds.append(embed)

    if not embeds:
        await ctx.send("No commands available.")
        return

    view = HelpView(embeds)
    message = await ctx.send(embed=embeds[0], view=view)
    view.message = message

# Error Handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❗ Missing arguments. Please check the command usage with `!what`.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("❗ Command not found. Use `!what` to see the list of available commands.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("❗ You need to register first using `!register <username>`.")
    else:
        await ctx.send("❗ An unexpected error occurred. Please try again later.")
        logger.error(f"Error: {error}")  # Log the error to console

# Run Bot
bot.run(BOT_TOKEN)
