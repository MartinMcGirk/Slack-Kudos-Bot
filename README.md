# Slack-Kudos-Bot
An emoji-based reward slackbot similar to HeyTaco, but self hosted and running in AWS lambda using AWS/Chalice.

Side note: This is to be self-hosted and there is no support for this project. If you want to use something like this and can pay for it then please use something like https://www.heytaco.chat/

### Usage
To give kudos:

    @<person> <emoji>
    
To get leaderboard:

    @<botname> leaderboard

### Current functionality:
 - Configurable emoji token 
 - Can give multiple points at a time
 - Users cannot give themselves points
 - Tallies user scores in memory
 - Can dump the leaderboard out as json
 
### Current limitations
 - Does not yet connect to database
 - Does not yet limit the number of points a person can give per day
 - Leaderboard does not return nicely, or for that matter sorted according to points
 - It will not yet handle the case where someone tries to give points but does not start off their message with the @username
 
### Setup
Note: requires python3.6

    pip install -r requirements.txt
    export BOT_TOKEN=<Bot User OAuth Access Token>
    
### To run locally
    chalice local --port=8080

### To deploy to AWS
    chalice deploy
