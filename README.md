# Slack-Kudos-Bot
An emoji-based reward slackbot similar to HeyTaco, but self hosted and running in AWS lambda using AWS/Chalice and backed by DynamoDB.

Side note: This is to be self-hosted and there is no support for this project. If you want to use something like this and can pay for it then please use something like https://www.heytaco.chat/

### Usage
To give kudos:

    @<person> <emoji>
    or
    <emoji> <@person>
    or
    Some <emoji> <emoji> are due to <@person> for being awesome
    
To get the leaderboard:

    @<botname> leaderboard

### Current functionality:
 - Configurable emoji token 
 - Can give multiple points at a time
 - Users cannot give themselves points
 - Users can only give a set number of points per day
 - The sender and the recipient both get notifications of the points delivery
 - Records point giving events in DynamoDB
 - Can return the sorted leaderboard
 
### Current limitations
 - Users can currently give kudos to only one user at a time
 - Cannot be deployed with cloudformation
 - No help command
 
### Setup
Note: requires python3.6

    pip install -r requirements.txt
    export BOT_TOKEN=<Bot User OAuth Access Token>
    
### To run locally
    chalice local --port=8080

### To deploy to AWS
    chalice deploy --no-autogen-policy
