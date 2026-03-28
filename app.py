#Muhammad Bilal - 2023395 - CE308 Assignment 1
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Insert your Ticketmaster API key below
    api_key = "	ksfCEC423msYKAVTVFSSsh4eT73EOYgN"
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&size=5"
    
    response = requests.get(url)
    events_data = response.json()
    
    # Process the structured JSON data
    events = []
    if '_embedded' in events_data:
        for event in events_data['_embedded']['events']:
            events.append({
                'title': event.get('name'),
                'date': event['dates']['start'].get('localDate'),
                'image': event['images'][0]['url'] if 'images' in event else ''
            })
            
    return render_template('index.html', events=events)

if __name__ == '__main__':
    # Runs on port 80 so the Load Balancer can connect
    app.run(host='0.0.0.0', port=80)