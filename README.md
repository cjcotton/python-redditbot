# python-redditbot

This script is pretty straightfoward.

You will need to add the proper data to the creds.py or this wont work.

You will have to supply an account to login with, and the user you are wanting to
comment against.

This script essentially reads a person's most recent comment into a text file.
It then operates as, essentially, an endless loop (since we don't have a web server)
to check if there has been any newer comment. If a user makes a new comment that
differes from what was written in the file, it will respond to that comment
with a rhyme from a lullaby (lullabies.txt). It will then update that text file
and go back into a state of waiting for it to change.
