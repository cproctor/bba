Title: Interface design
Index: 6.2

Design and implement a user experience for the game "Treasure" or for your final project. For the purposes of this assignment, 
the nature of the application is not important. Rather, your focus will be on designing user interfaces and 
user experiences for learning. You will discuss these ideas in depth in class in upcoming weeks; taking a stab at it first
on your own will prepare you to engage more deeply with the theory later.

- **Programming**: Writing a working piece of code. The technical quality or impressiveness is not important--choose the right level of challenge for yourself.
- **Designing experiences**: Going from theory to implementation
- **Connecting the interface to the code**: The interface might be physical buttons, an on-screen display, or some other surface where the user and the program meet.

# Option 1: Treasure

Working alone or in a group of 2, create an interface to the game "Treasure." In this game, you and an opponent are competing for thirteen treasures, with point values ranging 1 to 13. 
Each round, a random treasure is displayed and then you and the opponent each choose a card from your hand, showing them at the same time. Whoever plays the higher card wins the treasure. 
(However, a 1 beats a 13.) Whoever has the most treasure points at the end wins. 

Chris has built a treasure server at [http://treasure.chrisproctor.net](http://treasure.chrisproctor.net), which you can play by typing in URLs in your browser. Play with it so you understand
how it works:

- Create a new user by going to [treasure.chrisproctor.net/players/new/USERNAME](http://treasure.chrisproctor.net/players/new/USERNAME), replacing `USERNAME` with the username you want. You will get a 
  secret `pid`. Don't lose this!
- Now you can see your profile at [http://treasure.chrisproctor.net/players/PID](http://treasure.chrisproctor.net/players/PID), again replacing `PID` with your PID.
- Now create a new game with `/players/PID/games/new`. You'll be redirected to `/players/PID/games/GID` (where `GID` is the ID of the new game). You don't want to wait around for another player to join,
  so set this game to autoplay by navigating to `/players/PID/games/GID/autoplay`. 
- Now you can play your next card with `/players/PID/games/GID/play/CARD`, where CARD is a number between 1 and 13. You'll see that the bot player automatically played as well.
- Later, you can join a game against another live player with `/players/PID/games/join`, join a specific game with `/players/PID/games/GID/join`, or resume a game you're already playing with `/players/PID/games/resume`.

You can play a whole game, just by typing URLs. You could create two different users and play against each other if you like, each in a separate tab. This works, but it's not a nice interface or a particularly 
nice experience. Your job is to build a better interface. 

### Designing the interface

First, think about what kind of experience you want your user to have. For example, 

- Who is your target user? What do you expect will be the context of use?
- Do you want to encourage the user to think about game strategy? Will this function as some kind of microworld? 
- Do you want to encourage social play? Do you want to encourage competition?
- What kinds of emotions do you want the user to have?
- What tasks will the user need to perform? (These are sometimes described using [user stories](https://en.wikipedia.org/wiki/User_story).) 
- What representations and interactions will you supply to help the user accomplish these tasks?
- How would you decide your interface was successful?

Develop and iterate some ideas for the user interface. You will need to articulate a rationale for your choices connected to learning.

### Implementing the interface
You may use any technology you want, but code is provided for Python, Scratch, and Processing. 

- If you want to use Scratch there is a Scratch3 extension coming... (Chris needs to update the old Scratch 2 extension).
- If you want to use Processing, there is a client API coming as well.
- If you want to use Python, there is a [client API](https://github.com/cproctor/treasure/blob/master/treasure/api.py) and [demo command-line program](https://github.com/cproctor/treasure/blob/master/treasure/client.py) in the [Treasure repo](https://github.com/cproctor/treasure). If Python/Git/django/APIs/aahhh!!!! feels unfamiliar, but it's a learning opportunity you want to pursue, Chris will be happy to provide extensive support. Update: here's a [simpler example](https://github.com/cproctor/treasure/blob/master/treasure/client_autoplay.py) that uses autoplay. And here's an [example of an interface that inherits from the autoplay example](https://github.com/cproctor/treasure/blob/master/treasure/example_client.py), just as yours might. 

### Deliverables

- Your interface, in some playable format.
- Your code. 
- A brief writeup explaining your design choices in terms of learning. Explain how you want your user to think or interact with your interface, and connect this to specific design choices in the interface. Aim for ~300 words. Possible formats:
    - Annotated screenshots, wireframes, or sketches (See Teacher Portal or Student Journalism in [Interface design case studies]({filename}/curriculum/interface.md))
    - A list of user stories with interface features supporting them (See Interactive Storytelling in [Interface design case studies]({filename}/curriculum/interface.md))
    - Several paragraphs summarizing your design process, explaining what you were trying to achieve and options you considered for achieving it. 
