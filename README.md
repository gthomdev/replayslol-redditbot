# Reddit Comment Responder

Find comments that contain an op.gg link on /r/SummonerSchool, post the data to Replays.lol API (which will record a video of their last game and host it on Replays.lol)
Poll a separate API which will provide a response telling it when to post a comment (schema?)

## Basic Process

* Iterate over a number of posts in a subreddit, extract links from post bodies and validate them against a list of
target links
* What does Reddit API provide - what is the most effective way of finding these links, iterating over "New", or is there a way of detecting new posts as an event and running based on that (i.e. do we create our own schedule or run based off an event)
* How do we know which comments we are already recording a video for?
* What information do we need from the comment to have:
    a. The information required to respond to the comment
    b. The information required to hit Replays.lol API
* All one process or a separate schedule to post replies?

* Regex to detect if a comment contains an op.gg link?
* How do we make sure we don't respond to the same comment twice?

## Replays.Lol Endpoint

* Response schema

## Risks

* Repeated responses to a single post

## Hosting 

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