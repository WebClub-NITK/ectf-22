# Time

Author: [Shashank D](https://github.com/shashank68)

Flag: `CTF{2022-03-03-22}`

## Problem Statement

Foxfire is currently chilling out in Mbabane. She did an awesome google search to find out something special. We've got hold of the search url. Now at what time did she search?

Flag format: CTF{yyyy-mm-dd-HH}

## Relevant files / links

- [Search URL](./searchurl.txt)


## Solution

Many of the google search url query parameters store various encoded timestamps that are believed to tell page load time, previous page load time etc...

Sites like [https://dfir.blog/unfurl/](https://dfir.blog/unfurl/) parse the url & decode the parameters as well. Since FoxFire was in Mbabane, convert the utc time to Africa/Mbabane timezone.

