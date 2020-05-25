# skyline

This is a Telegram bot that parses commands allowing the user to manipulate, store and load skylines.

## Set-up

To start using the bot, you will need to install the required Python libraries:

```bash
> pip3 install -r requirements.txt
```

You will also need a valid Telegram bot token, which has to be stored in a plain text file called `token.txt` in the same directory as the `bot.py` file.

To run the bot, simply execute:

```bash
> python3 bot.py
```

and you can start chatting!

Note: You need at least Python 3.6 because the program uses f-strings.

## Interaction

The bot understands seven commands, identified by a slash (`/`) at the start.

* `/start` initiates the conversation with the bot and greets the user.
* `/help` shows a list with all the available commands and a brief description of each one.
* `/author` shows the name and email of the author.
* `/lst` shows a list of all the valid skyline identifiers in memory, with their area and height.
* `/clean` erases all skyline identifiers in memory.
* `/save id` saves the skyline with identifier `id` to disk.
* `/load id` loads the skyline with identifier `id` from disk to memory.

The bot can also parse messages that allow the user to manipulate the skylines. These messages do not start with a slash (`/`). The following section will explain the grammar that these messages follow.

## Grammar

* The user can construct a skyline with a single building, by specifying the start x-coordinate, the height, and the end x-coordinate. An example would be `(1, 2, 3)`, where the building has height 2 and goes from the x-coordinates 1 to 3.
* The user can construct a skyline with multiple buildings by entering a list with multiple single buildings. An example would be `[(1, 2, 3), (4, 5, 6)]`.
* The user can construct a skyline with many randomly generated buildings by specifying some parameters `(n, h, w, xmin, xmax)`. An example would be `(100, 20, 4, 1, 1000)`. The meaning of the parameters is:
  * `n`: the amount of buildings
  * `h`: the maximum height of each building
  * `w`: the maximum width of each building
  * `xmin`: the minimum x-coordinate of each building
  * `xmax` the maximum x-coordinate of each building
* The union of two skylines is represented by `skyline1 + skyline2`.
* The intersection of two skylines is represented by `skyline1 * skyline2`.
* The reflection of a skyline is represented by the unary negation operator: `-skyline`.
* The right shift by `n` units of a skyline is represented by `skyline + n`.
* The left shift by `n` units of a skyline is represented by `skyline - n`.
* The replication `n` times of a skyline is represented by `skyline * n`.

Any of the previous operations can be stored into a variable with an identifier as follows: `a1 := (1, 2, 3)`. The identifiers can then be used in expressions. A valid identifier is a letter followed by zero or more digits or letters.

Note: Whitespace is always ignored in the parsing of the expressions.

## Implementation details

### Skyline representation

Skylines are represented by a series of points `(x, y)` where the skyline changes its height. Note that the last point is always of the form `(x, 0)` because the heigth from that point on is zero. This allows for easy plotting, area calculation and height calculation. The implementation of the operations is also simplified by this structure. 

The reflection operation can be achieved by simply traversing the list of points backward and setting to each point the y-coordinate of the next one, adding a zero to the end and adjusting the x-coordinates with a simple calculation.

The union and intersection of two skylines are calculated in linear time, and their implementations are simple, but prone to index errors and edge cases. 

Shifts are very easy to implement, by adding or subtracting the given offset to the x-coordinate of each point, and replications are also easy, taking into account that the zero point at the end of the original list only has to be replicated once.

The most interesting operation is the construction of a skyline given a list of buildings, randomly generated or not. It is easy to come up with an `O(n^2)` algorithm by keeping a `result` skyline and repeatedly joining it with each building. To comply with the requirements, we have to do better, and `O(n logn)` is possible, using a variant of merge sort. We start with a list of skylines which have one building each, and repeatedly divide the list into halves until the parts have one element. Then, we can just join the halves using the `O(n)` join function we previously had. By a similar argument to the one used for merge sort, this produces a tree of height `log n`, and thus the whole operation is `O(n logn)`.

### Persistent storage

Persistent storage is achieved with the `pickle` module in the Python standard library, which allows the saving and loading of arbitrary objects into binary files.

## PEP8 compliance

The code for this program has been formatted with the `black` module. The settings used were the default ones except for line length, which was set to unlimited.
