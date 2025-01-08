import os
import json
import urllib.request
import boto3

from datetime import datetime, timedelta, timezone

# Function to format the game data based on its status
def format_game_data(game):
    # Extract relevant game information (status, teams, scores, etc.)
    status = game.get("Status", "Unknown")
    away_team = game.get("AwayTeam", "Unknown")
    home_team = game.get("HomeTeam", "Unknown")
    final_score = f"{game.get('AwayTeamScore', 'N/A')}-{game.get('HomeTeamScore', 'N/A')}"
    start_time = game.get("DateTime", "Unknown")
    channel = game.get("Channel", "Unknown")

    # Format quarter scores if they exist
    quarters = ', '.join([f"Q{q['Number']}: {q.get('AwayScore', 'N/A')}-{q.get('HomeScore', 'N/A')}" for q in game.get("Quarters", [])])

    # Return a formatted string based on the status of the game
    if status == "Final":
        # For games that are finished, include the final score and quarter scores
        return f"Game Status: {status}\n{away_team} vs {home_team}\nFinal Score: {final_score}\nStart Time: {start_time}\nChannel: {channel}\nQuarter Scores: {quarters}\n"
    elif status == "InProgress":
        # For games that are still ongoing, include the last play made
        last_play = game.get("LastPlay", "N/A")
        return f"Game Status: {status}\n{away_team} vs {home_team}\nCurrent Score: {final_score}\nLast Play: {last_play}\nChannel: {channel}\n"
    elif status == "Scheduled":
        # For scheduled games, include the start time
        return f"Game Status: {status}\n{away_team} vs {home_team}\nStart Time: {start_time}\nChannel: {channel}\n"
    return f"Game Status: {status}\n{away_team} vs {home_team}\nDetails are unavailable at the moment.\n"

# Lambda function handler that is triggered when the Lambda function is invoked
def lambda_handler(event, context):
    # Retrieve environment variables for API key and SNS topic ARN
    api_key = os.getenv("NBA_API_KEY")  # NBA API key for accessing game data
    sns_topic_arn = os.getenv("SNS_TOPIC_ARN")  # SNS topic ARN for publishing messages
    sns_client = boto3.client("sns")  # Create an SNS client to interact with AWS SNS

    # Get the current date in UTC and adjust to Central Time (UTC-6)
    central_time = datetime.now(timezone.utc) - timedelta(hours=6)  # Central Time is UTC-6
    today_date = central_time.strftime("%Y-%m-%d")  # Format the date as YYYY-MM-DD for API request

    # Construct the API URL to fetch NBA game data for the specified date
    api_url = f"https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{today_date}?key={api_key}"
    try:
        # Send the API request and retrieve the response
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode())  # Parse the JSON response
    except Exception as e:
        # If there is an error in fetching data from the API, log the error and return a failure status
        print(f"Error fetching data: {e}")
        return {"statusCode": 500, "body": "Error fetching data"}

    # Format the fetched game data into readable strings
    final_message = "\n---\n".join([format_game_data(game) for game in data]) if data else "No games available for today."

    # Publish the formatted message to an SNS topic
    try:
        sns_client.publish(TopicArn=sns_topic_arn, Message=final_message, Subject="NBA Game Updates")
        print("Message published to SNS successfully.")
    except Exception as e:
        # If there is an error in publishing to SNS, log the error and return a failure status
        print(f"Error publishing to SNS: {e}")
        return {"statusCode": 500, "body": "Error publishing to SNS"}

    # Return a success response when data is processed and sent to SNS
    return {"statusCode": 200, "body": "Data processed and sent to SNS"}
