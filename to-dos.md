---
layout: post
title: To-dos
description: Things I want to do with my website.
---
> **NOTE:** <br>
> This page is my personal test of transparently showing my running list of things I need to fix or want to try to do with my website as a means to encourage a fluid process and accomplishment. 
>
> I was inspired by Michael Nielsen's post [_"Using a personal website to enhance your ability to think and create."_](https://mnielsen.github.io/wn/website_enhance.html#fnref4)

<br>
**Next**

- [ ] **improve task list style**<br>
This one is turning out to be tough! I'm trying to make it so I can use markdown for these tasks, but it appears CSS doesn't do anything for these kinds of "dead" checkboxes. My attempts either don't do anything, or create usable web checkboxes. I don't want to style them so that they are usable; rather, I want to be able to "check" them in markdown and simply display its status on the site. Part of the issue is likely that I am styling them with ```list-style-type: none``` because markdown task list is showing bullets alongside the checkboxes, instead of turning the list into a checkbox list. I took to [stackoverflow](https://stackoverflow.com/questions/70546139/how-do-i-style-markdown-checklists-with-css-in-jekyll) to try to find a solution...
- [ ] improve footer style on mobile viewport
- [ ] improve style of external link posts
- [ ] **improve workflow for posts that are links to external sites**<br>
I was able to automate post cards that are external links. It was a simple mistake in the yaml front-matter. Now, I want to figure out a way to quickly share a website I am looking at into my list of posts. It will be complicated.  The steps I see are: 1. grab the link of the website, 2. create markdown file with today's date and title, 3. input correct front-matter, 4. include link in the correct line, 5. saving the file, 6. pushing to git. I might be missing some crucial steps but that's the high-level flow as I understand it. 

**Complete**

- [x] ~~create post card for external links~~
- [x] ~~Add and style next/previous post at the bottom of posts~~
- [x] ~~Add public to-dos list of things I'd like to do for my website~~
- [x] ~~Fix bullets showing on task list~~
- [x] ~~```justify-content: space-between``` for footer links~~ 
- [x] ~~make image width to match post header card width~~ 
- [x] ~~improve block quote style~~ 