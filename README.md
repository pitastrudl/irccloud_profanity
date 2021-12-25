# irccloud_profanity 

Download your IRCCloud channel log and put it in this script. This script will naively parse the logs and output a list of nicks together with a count of profane words. This uses a library called  
[better_profanity](https://github.com/snguyenthanh/better_profanity). 



It supports [modified spellings](https://en.wikipedia.org/wiki/Leet) (such as `p0rn`, `h4NDjob`, `handj0b` and `b*tCh`).

## Requirements

This works with `Python 3.5+` and `PyPy3`

## Usage 

```sh
./parse.py example.txt
```

## Notes

1. It outputs everything in a some

2. Any word in [wordlist](https://github.com/snguyenthanh/better_profanity/blob/master/better_profanity/profanity_wordlist.txt) that have non-space separators cannot be recognised, such as `s & m`, and therefore, it won't be filtered out. This problem was raised in [#5](https://github.com/snguyenthanh/better_profanity/issues/5).

