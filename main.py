"""
Keystroke Dynamics Analyzer - Main Entry Point
"""

import json
import os
import sys
from datetime import datetime
from keystroke_logger import KeystrokeLogger
from data_processor import DataProcessor
from report_generator import ReportGenerator
from notification_handler import NotificationHandler
from utils import ensure_directory, load_config, print_banner

def main():
    """Main execution flow"""
    print_banner()
    
    # Load configuration
    config = load_config('config.json')
    
    # Ethical consent check
    print("\n" + "="*60)
    print("ETHICAL USE AGREEMENT")
    print("="*60)
    print("\nThis tool collects keystroke timing data for analysis.")
    
    if config['privacy']['log_actual_keys']:
        print("\n⚠️  WARNING: You have enabled actual key logging!")
        print("   The tool will record WHAT you type, not just timing.")
        print("   This data will be saved in the reports.\n")
    
    print("By continuing, you confirm that:")
    print("  1. You are analyzing your OWN typing behavior")
    print("  2. You have consent if analyzing others")
    print("  3. You will use this tool ethically and legally")
    print("\nPress ENTER to continue or CTRL+C to exit...")
    print("="*60 + "\n")
    
    try:
        input()
    except KeyboardInterrupt:
        print("\nExiting. Thank you for using responsibly.")
        sys.exit(0)
    
    # Ensure output directories exist
    ensure_directory('reports')
    
    # Initialize components
    logger = KeystrokeLogger(config)
    processor = DataProcessor(config)
    report_gen = ReportGenerator(config)
    notifier = NotificationHandler(config)
    
    # Start logging session
    print(f"\n🎯 Starting {config['session']['duration_minutes']}-minute session...")
    print("📊 Collecting keystroke dynamics data...")
    if config['privacy']['log_actual_keys']:
        print("🔍 Logging actual keys pressed...")
    print("⏹️  Press ESC to stop early\n")
    
    keystroke_data = logger.start_session()
    
    if not keystroke_data or len(keystroke_data) < config['session']['min_keystrokes']:
        print(f"\n⚠️  Insufficient data collected (minimum {config['session']['min_keystrokes']} keystrokes required)")
        sys.exit(1)
    
    print(f"\n✅ Session complete! Collected {len(keystroke_data)} keystrokes")
    
    # Get typed text if enabled
    typed_text = ""
    if config['privacy']['save_typed_text']:
        typed_text = logger.get_typed_text()
        print(f"📝 Captured {len(typed_text)} characters of text")
    
    # Process data
    print("🔬 Analyzing keystroke patterns...")
    analysis = processor.analyze(keystroke_data)
    
    # Generate reports
    print("📄 Generating reports...")
    json_path = report_gen.generate_json(keystroke_data, analysis, typed_text)
    html_path = report_gen.generate_html(keystroke_data, analysis, typed_text)
    
    print(f"\n✨ Reports generated successfully!")
    print(f"   📊 JSON: {json_path}")
    print(f"   🌐 HTML: {html_path}")
    
    if config['privacy']['log_actual_keys']:
        print("\n⚠️  Remember: Your reports contain actual keystroke data!")
        print("   Keep them secure and delete when no longer needed.")
    
    # Send notifications if enabled
    if config['notifications']['enabled']:
        print("\n📤 Sending notifications...")
        notifier.send_summary(analysis)
    
    print("\n" + "="*60)
    print("Session Summary:")
    print("="*60)
    print(f"Total Keystrokes: {analysis['total_keystrokes']}")
    print(f"Average Speed: {analysis['avg_interval']:.3f}s between keys")
    print(f"Typing Speed: {analysis['typing_speed']:.1f} WPM (estimated)")
    if typed_text:
        print(f"Text Length: {len(typed_text)} characters")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()