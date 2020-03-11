# Dev Ops
## Overview
This doc overviews how dev ops will be handled for this app.

## Deploy
Deploys will be done with Heroku probably. Digital Ocean seems really nice, but they don't do add-ons. This means that to use DO, we need to either run the database ourselves within a droplet, or provision an external database and connect it to our app.
- The first one doesn't seem very advisable for scaling as we're taking on the maintenance costs of having our out database
- The second one isn't as bad for growing new skills, but also means messing with external vendors

If we do go with Digital Ocean, then we'll probably go for AWS for the database for convenience and cost. I'm not expecting 100% uptime so AWS makes sense.

The big downsize for Heroku is that the dyno sleeps after inactivity for the free tier. The upside is that Heroku actually has a add-on ecosystem which makes a lot of different things easier. Upgrading from the free tier to hobby tier is an option though and would mean having to pay $7 a month, but that's not too bad.

## Database
I'll be using Redis for the database/ caching as we'll be doing some data-processing and we want to minimize the number of requests we make to the external API.