"""
Notification Handler - Sends summaries to Telegram/Discord
"""

import requests
import json

class NotificationHandler:
    def __init__(self, config):
        self.config = config
    
    def send_summary(self, analysis):
        """Send analysis summary to configured platforms"""
        message = self.format_message(analysis)
        
        if self.config['notifications']['telegram']['bot_token']:
            self.send_telegram(message)
        
        if self.config['notifications']['discord']['webhook_url']:
            self.send_discord(message)
    
    def format_message(self, analysis):
        """Format analysis into a readable message"""
        return f"""
🔔 Keystroke Dynamics Report

📊 Total Keystrokes: {analysis['total_keystrokes']}
⚡ Typing Speed: {analysis['typing_speed']:.1f} WPM
⏱️ Avg Interval: {analysis['avg_interval']:.3f}s
🎯 Consistency: {analysis['rhythm_consistency']*100:.1f}%
⏳ Session Duration: {analysis['session_duration']:.1f}s
        """
    
    def send_telegram(self, message):
        """Send message to Telegram"""
        try:
            url = f"https://api.telegram.org/bot{self.config['notifications']['telegram']['bot_token']}/sendMessage"
            data = {
                'chat_id': self.config['notifications']['telegram']['chat_id'],
                'text': message,
                'parse_mode': 'HTML'
            }
            response = requests.post(url, data=data, timeout=10)
            if response.status_code == 200:
                print("✅ Telegram notification sent")
            else:
                print(f"⚠️  Telegram error: {response.status_code}")
        except Exception as e:
            print(f"❌ Telegram failed: {str(e)}")
    
    def send_discord(self, message):
        """Send message to Discord"""
        try:
            url = self.config['notifications']['discord']['webhook_url']
            data = {'content': message}
            response = requests.post(url, json=data, timeout=10)
            if response.status_code == 204:
                print("✅ Discord notification sent")
            else:
                print(f"⚠️  Discord error: {response.status_code}")
        except Exception as e:
            print(f"❌ Discord failed: {str(e)}")