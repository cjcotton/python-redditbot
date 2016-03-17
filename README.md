# python-redditbot

This script is pretty straightfoward.

In the config.py you will need to be sure to supply a username/password.
In the actual lullabies.py script, you will need supply a user.
(Yes, I could have just had a user read in from the config.py. Hush!)

This script essentially reads a person's most recent comment into a text file.
It then operates as, essentially, an endless loop (since we don't have a web server)
to check if there has been any newer comment. If a user makes a new comment that
differes from what was written in the file, it will respond to that comment
with a rhyme from a lullaby (lullabies.txt). It will then update that text file
and go back into a state of waiting for it to change.
