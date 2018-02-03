# Slack-Kudos-Bot
An emoji-based reward slackbot similar to HeyTaco, but self hosted and running in AWS lambda using AWS/Chalice and backed by DynamoDB.

Side note: This is to be self-hosted and there is no support for this project. If you want to use something like this and can pay for it then please use something like https://www.heytaco.chat/

### Usage
To give kudos:

    @<person> <emoji>
    or
    <emoji> @<person>
    or
    Some <emoji> <emoji> are due to @<person> for being awesome
    
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
 
### Setup
First, create the "emoji_log" DynamoDB table in AWS using Cloudformation 

    aws cloudformation create-stack --stack-name emoji-log \ 
    --template-body file://cloudformation.yaml


Then build the package with dependencies. __Note: requires python3.6__

    pip install -r requirements.txt

### To deploy to AWS
First fill in the BOT_TOKEN environment variable in `.chalice/config.json`, then

    chalice deploy --no-autogen-policy

### To run locally
Requires DynamoDB installed locally

    export BOT_TOKEN=<Bot User OAuth Access Token>
    chalice local --port=8080