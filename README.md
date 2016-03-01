# md5Comparator
Throwaway scrpt written to settle an imgur argument and learn the argparse module in python.

# Original Thread

http://imgur.com/gallery/rUv6q/comment/595908078

In this thread, someone claims to have produced some gifs from a video and another user says that it must have, in fact, been a repost of a similar post. The first poster then proceeds to get a deluge of downvotes (score of -122 at time of writing). Someone else mentions that the claim has no proof, and I wish I had a tool to check the validity of this sort of claim, as it appears often.

So, with time to kill and score to settle, I set out to build such a tool.

# Objectives
 * Be able to compare hashes of web resources
 * Practice Python scripting
 * Practice project documentation
 * Investigate file structures
 * Investigate command line argument parsing in python

# Conclusion
As [posted to imgur](http://imgur.com/gallery/rUv6q/comment/596599167):
 > Okay, so I developed a python script to fetch the links, compute the hashes and compare. They all came back distinct. Trouble is my control group (1 I reposted) ALSO came back distinct, so maybe there's a timestamp or filename in the webm that's updated by imgur on upload. I'll have to investigate the webm standard and find how to distinguish the payload from the headers. I might have to decompress them, too. In other words this is beginning to be more trouble than it's worth. Here's a repo with what I've written and a log of what was run: https://github.com/crow1170/md5Comparator
 
 As stated above, the initial procedure was inconclusive. I need to get a better understanding of the webm payload to determine how, or even if, distinguishing between post and repost is possible.
