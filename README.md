# irccloud_profanity 

Download your IRCCloud channel log and put it in this script. This script will naively parses the logs and output a list of nicks together with a count of profane words. This uses a library called  
[better_profanity](https://github.com/snguyenthanh/better_profanity). 

The library supports [modified spellings](https://en.wikipedia.org/wiki/Leet) (such as `p0rn`, `h4NDjob`, `handj0b` and `b*tCh`).

## Requirements

This works with `Python 3.5+` and `PyPy3`

## Usage 

```sh
./parse.py example.txt
```

## Notes 

This might have false positives as someone might use a profane word, movie quote or something else that was not meant explicitly. To have more accurate results, one might to involve better methods in the field of Sentiment Analysis. This script was only meant as a quick test. 

## To-do

- [ ] Fairer statistics depending on how much the person talks in the channel
- [ ] Output graphs with time periods and the persons cursing volume
- [ ] Prettify output in terminal

