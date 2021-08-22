# text-it-search-it
An SMS service  
[https://textitsearchit.tech/](https://textitsearchit.tech/)

Created by [Cameron Fairchild](https://github.com/camfairchild/), [Eddie Liang](https://github.com/edd1eliang/), [Bryan Lee](https://github.com/B-lee71/), [Stanley](https://github.com/stanley021/)
for [Hack the 6ix 2021](https://hackthe6ix2021.devpost.com/)

## How it Works
Text your search query to (289) 274-9428 and we will respond with a short list of results:  
  
    [0] Result 1
    [1] Result 2
    [2] Result 3
    [3] Result 4
    [4] Result 5
  
Text the number corresponding to the result you wish to learn more about and we will respond with more information.  
  
    Lorem ipsum dolor sit amet
    
### We also support other commands
Such as  
- /date <loc> - date in loc  
- /directions <locA> <locB> - directions from A to B
- /joke - a joke
- /news - lst of news frm NYT
- /time <loc> - time at loc
- /translate <txt> -> <lang>
- /weather <loc> - weather at loc

**That's it!**

 ## Technologies and Libraries
  We make use of
  - Google Cloud (GKE, Directions API, Geolocation API, Custom Search API, Translate API, Timezone API, etc.)
  - Docker
  - Flask
  - CockroachDB (postgresql-based)
  - NY Times Top Stories API
  - CloudFlare for Nameservers and Proxy
  - Domain.com for the .tech domain
  - WeatherBit Weather API
  - Twilio for SMS
  - jokeapi
  
