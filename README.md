# The Eye

## Assumptions
* I assume that there would be a database and saving to the database would be done in the process.
* More validation wold be done. I set up the structre of the validation. 
We could do some more direct validation by naming the validation methods validate_<category>_<name> or something like that.
We could also just leave it like it is if there aren't many categoy/name combos. 
* I assumed that incoming events happen very fast, but requests for events (i.e. GETs) don't happen very ofter.  
If that assumption is wrong then the we would need either change the queue so that requests preempt writes or have the data returned to the user differently. 

## Todo:
* Add database
* Logging - ran out of time to setup logging
* Testing - really needed

## Discussions
I would have gone further, but I had already put 4 hours into this and It seemed like this was a good representitive of my style.

I didn't really like that I added the queue and worker in the same file that the other methods are in.  The reason I left it is because it is easy to move later and I just couldn't think of a good name for the file.

## Conclusion
Although this was fun to write, there is way more to do to make this system complete.