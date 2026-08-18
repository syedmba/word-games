from random import randint, choice

from utils.bcolors import bcolors

from global_vars import LOG_LEVEL, LOG_DIR
import logging

logger = logging.getLogger(__name__)

logging_dir = LOG_DIR + '/imposter.log'
logging.basicConfig(filename=logging_dir,
                    level=LOG_LEVEL,
                    format='[%(asctime)s][%(levelname)s][%(filename)s] %(message)s')

imposter_game_data = {
    "Mythical & Folklore": {
        "Dragon": "It is a creature often featured in ancient legends and fantasy lore.",
        "Unicorn": "It is known for a highly distinct physical feature on its head.",
        "Kraken": "It is historically considered a massive danger to travelers.",
        "Chupacabra": "It has a modern reputation for attacking and being a nuisance.",
        "Banshee": "It is strongly associated with a very specific, unsettling sound.",
        "Griffin": "It is a hybrid creature made up of two different animals.",
        "Phoenix": "It is associated with fire, cycles, and renewal.",
        "Yeti": "It is rumored to inhabit cold, isolated, high-altitude regions.",
        "Mermaid": "It is associated with the ocean and has a deceptive allure.",
        "Centaur": "It represents a blend of human intellect and animal strength."
    },
    "At the Carnival": {
        "Ferris Wheel": "It involves going in a continuous cycle or circle.",
        "Funhouse Mirrors": "It makes things look completely different than they usually do.",
        "Cotton Candy": "It is associated with a very distinct texture and usually bright colors.",
        "Bumper Cars": "It involves a lot of sudden stops and controlled chaos.",
        "Haunted House": "It is designed to elicit a strong emotional reaction from people.",
        "Corn Dog": "It requires a wooden stick to be used properly.",
        "Carousel": "It features artificial animals moving in a repetitive motion.",
        "Rollercoaster": "It is built on the principles of gravity and extreme momentum.",
        "Ring Toss": "It requires precision and often results in frustration.",
        "Tilt-a-Whirl": "It relies on centrifugal force to create an intense feeling."
    },
    "Obsolete Technology": {
        "Floppy Disk": "It was primarily used for keeping things safe for later.",
        "Typewriter": "It makes a very rhythmic, mechanical clicking sound when used.",
        "Rotary Phone": "It requires a physical spinning or turning motion to operate.",
        "Cassette Tape": "It can easily become tangled or requires winding up.",
        "Pager": "It lets you know something happened, but you can't respond to it directly.",
        "Overhead Projector": "It requires a dark room and a blank surface to be useful.",
        "VHS Player": "It requires you to physically rewind something after using it.",
        "Walkman": "It allowed people to isolate themselves while moving around.",
        "Dial-up Modem": "It is famous for making a very harsh, electronic screeching noise.",
        "CRT Monitor": "It is heavy, made of glass, and builds up static electricity."
    },
    "Deep Sea Mysteries": {
        "Anglerfish": "It uses a very specific trick to get what it wants in the dark.",
        "Giant Squid": "It is known for having many grasping appendages.",
        "Hydrothermal Vent": "It produces an extreme amount of heat in a very harsh environment.",
        "Bioluminescence": "It is a natural phenomenon that stands out beautifully in pitch black.",
        "Mariana Trench": "It is famous for being a location of extreme physical depths.",
        "Submarine": "It is built to withstand immense pressure from the outside.",
        "Jellyfish": "It has no brain but can still cause you a lot of physical pain.",
        "Shipwreck": "It is a relic of human creation reclaimed by nature.",
        "Coral Reef": "It is a colorful ecosystem built entirely by tiny living organisms.",
        "Bathysphere": "It is a heavy, sealed sphere used for extreme exploration."
    },
    "Everyday Annoyances": {
        "Traffic Jam": "It involves a lot of waiting when you'd rather be moving.",
        "Mosquito": "It is small, persistent, and leaves a lasting reminder of its presence.",
        "Stubbed Toe": "It is a sudden, sharp event usually caused by not paying attention.",
        "Spam Calls": "It constantly interrupts you, usually offering something you don't want.",
        "Wet Socks": "It creates a highly uncomfortable sensation on your extremities.",
        "Slow Wi-Fi": "It disrupts your modern routines and requires a lot of patience.",
        "Papercut": "It is a tiny injury that hurts far more than it logically should.",
        "Alarm Clock": "It is designed specifically to ruin a peaceful state.",
        "Pothole": "It is an unexpected hazard that causes a sudden jolt.",
        "Tangled Earbuds": "It is a frustrating knot that seems to form entirely on its own."
    },
    "Office Supplies": {
        "Stapler": "It uses physical force and metal to keep things organized.",
        "Paperclip": "It is a simple piece of bent wire used for temporary grouping.",
        "Sticky Note": "It is meant to be a temporary reminder that you can move around.",
        "Whiteboard": "It is a space for temporary ideas that are meant to be erased.",
        "Highlighter": "It is used to draw attention to specific, important information.",
        "Shredder": "It is designed to permanently destroy things for security.",
        "Water Cooler": "It is traditionally a central gathering place for casual conversation.",
        "Pushpin": "It requires a soft surface and physical pressure to hold things up.",
        "Binder": "It uses metal rings to permanently organize loose items.",
        "Calculator": "It is relied upon to solve complex logical problems quickly."
    },
    "Breakfast Foods": {
        "Pancakes": "It is a flat, circular food usually served in a stack.",
        "Bacon": "It is famous for its distinct, savory smell when being cooked.",
        "Cereal": "It completely changes texture if left sitting for too long.",
        "Omelette": "It is folded over and can be filled with a variety of ingredients.",
        "Waffles": "It has a distinct geometric pattern used to hold liquids.",
        "Toast": "It is a common staple made by applying dry heat to something soft.",
        "Coffee": "It is a dark liquid widely consumed for a burst of energy.",
        "Hash Browns": "It is made of shredded ingredients and fried until crispy.",
        "Oatmeal": "It is a warm, mushy bowl of grains often sweetened.",
        "Croissant": "It is highly flaky, buttery, and features a distinct curved shape."
    },
    "Extreme Sports": {
        "Skydiving": "It involves intentionally putting yourself in a falling state.",
        "Bungee Jumping": "It relies entirely on the elasticity of a single cord.",
        "Snowboarding": "It involves strapping both your feet to a single surface.",
        "Motocross": "It involves mechanical vehicles navigating dirt and mud jumps.",
        "Rock Climbing": "It requires incredible grip strength and a tolerance for heights.",
        "Surfing": "It requires balancing while riding the momentum of nature.",
        "Parkour": "It involves navigating urban environments as quickly as possible.",
        "Hang Gliding": "It uses a lightweight frame to catch thermal updrafts.",
        "Whitewater Rafting": "It involves teamwork to navigate fast, chaotic elements.",
        "Base Jumping": "It involves launching off a fixed structure rather than an aircraft."
    },
    "Musical Instruments": {
        "Piano": "It uses a complex system of internal hammers striking strings.",
        "Guitar": "It requires you to press down on metal strings with one hand.",
        "Drum Set": "It is highly physical and dictates the rhythm of the group.",
        "Violin": "It is tucked under the chin and played with a long tool.",
        "Flute": "It is held horizontally and relies entirely on breath.",
        "Trumpet": "It is made of brass and uses three distinct valves.",
        "Saxophone": "It uses a wooden reed and is highly associated with jazz.",
        "Harp": "It is quite large and requires plucking many individual strings.",
        "Accordion": "It requires you to continuously pull and push it apart.",
        "Synthesizer": "It relies entirely on electricity to create artificial sounds."
    },
    "Camping Gear": {
        "Tent": "It provides temporary, portable shelter from the elements.",
        "Sleeping Bag": "It is designed to trap body heat in a tight, confined space.",
        "Flashlight": "It provides a highly directional beam to navigate the dark.",
        "Campfire": "It is the central gathering point that provides warmth and light.",
        "Compass": "It relies on natural magnetic fields to provide direction.",
        "Swiss Army Knife": "It is famous for being incredibly versatile in a small package.",
        "Bug Spray": "It uses a distinct chemical smell to act as a deterrent.",
        "Cooler": "It is heavily insulated to maintain a specific temperature.",
        "Lantern": "It provides a wide radius of ambient light, often using fuel.",
        "Hiking Boots": "It is designed with heavy tread for ankle support and traction."
    },
    "Weather & Nature": {
        "Tornado": "It is a highly destructive, spinning funnel of wind.",
        "Hurricane": "It is a massive storm system that forms over the ocean.",
        "Blizzard": "It causes extremely low visibility and dangerous temperatures.",
        "Thunderstorm": "It features sudden, loud noises and flashes of light.",
        "Fog": "It obscures vision and creates a highly eerie atmosphere.",
        "Hail": "It consists of solid objects unexpectedly falling from above.",
        "Rainbow": "It is a brief visual phenomenon caused by light and water.",
        "Drought": "It is characterized by a severe and prolonged lack of moisture.",
        "Heatwave": "It creates an oppressive atmosphere that exhausts people quickly.",
        "Tsunami": "It is a massive force displaced by an underwater disturbance."
    },
    "Clothing & Accessories": {
        "Socks": "It is a layer of fabric meant to prevent friction and absorb sweat.",
        "Jacket": "It has an opening down the front and provides exterior insulation.",
        "Hat": "It is worn primarily to shield the top of you from the elements.",
        "Scarf": "It is a long piece of fabric wrapped to protect a specific area.",
        "Gloves": "It has individual compartments to maintain dexterity in the cold.",
        "Jeans": "It is a highly durable fabric traditionally associated with labor.",
        "Sneakers": "It features a rubber sole designed for quiet, athletic movement.",
        "Tie": "It serves no practical purpose other than formal aesthetics.",
        "Belt": "It uses tension to hold other items securely in place.",
        "Sunglasses": "It alters your vision to protect against intense brightness."
    },
    "Space & Astronomy": {
        "Black Hole": "It exerts a force so strong that nothing can escape it.",
        "Asteroid": "It is a large piece of rocky debris drifting aimlessly.",
        "Moon": "It heavily influences the natural tides of our planet.",
        "Sun": "It is a massive sphere of plasma that sustains our solar system.",
        "Spaceship": "It is a highly engineered vessel built to survive a vacuum.",
        "Astronaut": "It requires intense physical training to survive zero gravity.",
        "Telescope": "It uses specialized lenses to make the distant seem close.",
        "Galaxy": "It is a massive collection of billions of star systems.",
        "Comet": "It leaves a highly visible trail of gas and dust behind it.",
        "Satellite": "It is an artificial object placed into a continuous orbit."
    },
    "Tools & Hardware": {
        "Hammer": "It is used to apply blunt force to drive things in or pull things out.",
        "Screwdriver": "It relies on torque and a specific shaped head to work.",
        "Wrench": "It uses leverage to grip and turn difficult hardware.",
        "Pliers": "It pinches tightly to hold or bend stubborn materials.",
        "Drill": "It uses rapid rotational motion to create holes or drive hardware.",
        "Tape Measure": "It is flexible, retractable, and essential for precision.",
        "Saw": "It uses a jagged edge and back-and-forth motion to cut.",
        "Level": "It relies on a tiny bubble in liquid to ensure perfect alignment.",
        "Sandpaper": "It uses friction to gradually smooth down rough surfaces.",
        "Nail": "It is driven by force to securely fasten two things together."
    },
    "Board Games & Toys": {
        "Dice": "It is used to introduce an element of pure random chance.",
        "Playing Cards": "It is a standard deck used for hundreds of different games.",
        "Puzzle": "It requires patience to assemble a fragmented image.",
        "Lego": "It is an interlocking system used for structural creativity.",
        "Yo-Yo": "It relies on string tension and momentum to perform tricks.",
        "Action Figure": "It features articulating joints for posable play.",
        "Chess": "It is a highly strategic game with uniquely moving pieces.",
        "Monopoly": "It is famous for causing arguments over imaginary wealth.",
        "Rubik's Cube": "It is a three-dimensional mechanical puzzle involving colors.",
        "Kite": "It requires wind and tension to be operated properly."
    }
}

class ImposterGameInstance:
    def __init__(self, numPlayers: int = 1, numImposters: int = 1, hintOn: bool = False, showCategory = False):
        self.numPlayers = numPlayers
        self.playerNames = [f"Player {i+1}" for i in range(self.numPlayers)]
        self.numImposters = numImposters
        self.hintOn = hintOn
        self.showCategory = showCategory
        self.categories = [category for category in imposter_game_data]

    def _init_players(self):
        for i in range(self.numPlayers):
            self.playerNames[i] = self._get_player_name(i+1)

    def _get_player_name(self, player_id):
        name = input(f"[Player {player_id}] Enter Name: ")
        if name == "":
            return f"Player {player_id}"
        return name

    def _pick_word(self):
        i = randint()

    def _select_category(self):
        print(f"Input the number of the category you want to play.")
        for i in range(len(self.categories)):
            print(f"{i+1}: {self.categories[i]}")

        print(f"{len(self.categories) + 1}: Random")

        user_selection = input(f"Enter your choice: ")
        if not user_selection.isnumeric():
            print(f"Invalid input! Proceeding with random category...")
            user_selection = "Random"
        else:
            idx = int(user_selection) - 1

            if idx >= 0 and idx < len(self.categories):
                user_selection = self.categories[idx]
            else:
                print(f"Invalid input! Proceeding with random category...")
                user_selection = "Random"


        return user_selection
        
    def begin(self):
        self._init_players()
        category = self._select_category()

        if category == "Random":
            category = self.categories[randint(0, len(self.categories) - 1)]

        print("\n" * 100)

        while True:
            dict_to_list = list(imposter_game_data[category])
            word = choice(dict_to_list)

            imposter_id = randint(0, self.numPlayers - 1)

            logger.warning(f"<---------- Imposter ---------->")
            logger.info(f"The category is {category}.")
            logger.info(f"The word is {word}.")
            logger.info(f"The imposter was {self.playerNames[imposter_id]}.\n")

            for player_id in range(self.numPlayers):
                input(f"{self.playerNames[player_id]}. Press ENTER to view.")

                if self.showCategory:
                    print(f"Game Category: {category}")

                if player_id == imposter_id:
                    if self.hintOn:
                        print(f"You are the impostor. Hint: [{imposter_game_data[category][word]}] Good luck !")
                    else:
                        print(f"You are the impostor. Good luck !")
                else:
                    print(f"Your word is {word}. Good luck !")

                input(f"Press ENTER when done.")
                print("\n" * 100)

            print(f"The game has begun.")
            print(f"{self.playerNames[randint(0, self.numPlayers - 1)]} starts the round.")

            input(f"Press ENTER to reveal game results:")

            print(f"<-------------- {self.playerNames[imposter_id]} was the Imposter -------------->")

            game_continue_choice = input(f"Press ENTER to continue playing. Type 0 and ENTER to quit playing: ")
            while not (game_continue_choice == "" or game_continue_choice == "0"):
                game_continue_choice = input(f"Press ENTER to continue playing. Type 0 and ENTER to quit playing: ")

            if game_continue_choice == "0":
                break

            reselect_category = input("Press ENTER to continue with the same category choice. Type 1 and ENTER to change category: ")
            while not (reselect_category == "" or reselect_category == "1"):
                reselect_category = input("Press ENTER to continue with the same category choice. Type 1 and ENTER to change category: ")

            if reselect_category == "1":
                category = self._select_category()
                
                if category == "Random":
                    category = self.categories[randint(0, len(self.categories) - 1)]
            


# TODO add arg parsing and input validation
NUM_PLAYERS = 2
NUM_IMPOSTERS = 1
SHOW_CATEGORY = False
HINT_ENABLED = True
game = ImposterGameInstance(numPlayers=NUM_PLAYERS, numImposters=NUM_IMPOSTERS, hintOn=True, showCategory=SHOW_CATEGORY)
game.begin()
