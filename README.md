# Reddit Comment Responder

This is a simple application that identifies comments on Reddit that match a given pattern and (in future) will respond
to them.

It is designed to be run on a server, and can be configured to target any subreddit. It is written in Python 3, and uses
the [PRAW](https://praw.readthedocs.io/en/latest/) library.

## Installation

1. Clone the repository
2. Install the requirements with `pip install -r requirements.txt`
3. Create a Reddit account for the bot
4. Configure the .env file based on the .env.example file
5. Run the bot file with `python bot.py`

![Tests](https://github.com/gthomdev/replayslol-redditbot/actions/workflows/tests.yml/badge.svg)

## Basic Workflow

1. The bot will check the subreddit for new comments periodically
2. If the comment matches the pattern, it will record the comment ID and the user who made the comment
3. If the comment does not match the pattern, it will do nothing
4. The bot will then sleep for a given amount of time (default 10 seconds)
5. The bot will then repeat the process

## Replays.Lol Endpoint

* to be added

## Risks

| Risks                                                    | Mitigation                                                       |
|----------------------------------------------------------|------------------------------------------------------------------|
| The bot could be banned from the subreddit               | The bot will only respond to comments that match a given pattern |
| The bot could respond to the same comment multiple times | Handled by the ReplaysLolAPI                                     |
| The bot could respond to a comment that is not a replay  | Handled by pattern matching/ReplaysLolAPI                        |
| Storage of credentials                                   | Handled by .env file, not stored in plain text                   |
| The bot could be used to spam the subreddit              | The bot will only respond to comments that match a given pattern |
| The bot could be used to spam the replays.lol API        | The bot will only respond to comments that match a given pattern |
| The bot could respond to users who do not want it to     | Implement blacklist?                                             |

## Hosting

Supports hosting on Windows and Ubuntu.

## Example links

### u.gg

``` html
https://u.gg/lol/profile/euw1/:Name/overview
```

### blitz.gg

``` html
https://blitz.gg/lol/profile/euw1/:Name
```

### op.gg

``` html
https://na.op.gg/summoners/na/:Name
```

### Future Work

* Add support for other patterns
* Add support for other responses
* Add support for mobalytics.gg, earlyGame, and other sites