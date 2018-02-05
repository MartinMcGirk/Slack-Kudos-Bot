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
 - Can give multiple users a point at once
 - Users cannot give themselves points
 - Users can only give a set number of points per day
 - The sender and the recipient both get notifications of the points delivery
 - Records point giving events in DynamoDB
 - Can return the sorted leaderboard
 
### Installation
First, create the "emoji_log" DynamoDB table in AWS using Cloudformation 

    aws cloudformation create-stack --stack-name emoji-log \ 
    --template-body file://cloudformation.yaml


Then install the project dependencies. __Note: requires python3.6__

    pip install -r requirements.txt
    
Then create a Slack application at https://api.slack.com/. You'll need to do the following for your slack app:

- Add a bot user to your application
- Take note of the Verification Token given to your app, which can be found on the "Basic Information" tab. This will be used later for setting the `VERIFICATION_TOKEN` in config
- Take note of the Bot User OAuth Access Token which can be found on the "OAuth & Permissions" tab. This will be used later for setting the `BOT_TOKEN` in config
- Then configure and deploy the code as outlined below
- Then go to the "Event Subscriptions" tab and subscribe to the `message.channels` event, with the POST url for your APP.


### To deploy to AWS
First fill in the `BOT_TOKEN` and `VERIFICATION_TOKEN` environment variables in `.chalice/config.json`, then in the same file configure the bot to your preference. You can choose:

- `EMOJI`: The emoji or string that users can use to gift points to each other
- `EMOJI_PLURAL`: The word that represents several `EMOJI`. So if you are gifting taco emojis then this should be `"tacos"`. Used for writing messsages like "You have been given 4 tacos"
- The number of points per user per day that someone is allowed to give out.
- `BOT_NAME`: This should equal the bot user name for your slack app

```
chalice deploy --no-autogen-policy
```

### To run locally
Requires DynamoDB installed locally

    export BOT_TOKEN=<Bot User OAuth Access Token>
    chalice local --port=8080
