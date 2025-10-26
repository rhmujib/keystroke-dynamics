"""
Data Processor - Analyzes keystroke dynamics data
"""

import numpy as np
from datetime import datetime

class DataProcessor:
    def __init__(self, config):
        self.config = config
    
    def analyze(self, keystroke_data):
        """Perform statistical analysis on keystroke data"""
        if not keystroke_data:
            return {}
        
        intervals = [k['interval'] for k in keystroke_data if k['interval'] > 0]
        
        if not intervals:
            return {'error': 'No valid intervals found'}
        
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'total_keystrokes': len(keystroke_data),
            'session_duration': keystroke_data[-1]['elapsed_time'],
            
            # Interval statistics
            'avg_interval': np.mean(intervals),
            'median_interval': np.median(intervals),
            'std_interval': np.std(intervals),
            'min_interval': np.min(intervals),
            'max_interval': np.max(intervals),
            
            # Speed metrics
            'typing_speed': self.calculate_wpm(keystroke_data),
            'keystrokes_per_second': len(keystroke_data) / keystroke_data[-1]['elapsed_time'],
            
            # Pattern analysis
            'rhythm_consistency': self.calculate_consistency(intervals),
            'burst_typing_detected': self.detect_bursts(intervals),
        }
        
        return analysis
    
    def calculate_wpm(self, keystroke_data):
        """Estimate words per minute"""
        total_time_minutes = keystroke_data[-1]['elapsed_time'] / 60
        estimated_words = len(keystroke_data) / 5  # Average 5 chars per word
        return estimated_words / total_time_minutes if total_time_minutes > 0 else 0
    
    def calculate_consistency(self, intervals):
        """Calculate typing rhythm consistency (0-1, higher is more consistent)"""
        if len(intervals) < 2:
            return 0
        cv = np.std(intervals) / np.mean(intervals)  # Coefficient of variation
        return max(0, 1 - cv)
    
    def detect_bursts(self, intervals):
        """Detect if there are typing bursts (rapid sequences)"""
        if len(intervals) < 5:
            return False
        
        threshold = np.percentile(intervals, 25)  # Bottom 25%
        burst_count = sum(1 for i in intervals if i < threshold)
        return burst_count > len(intervals) * 0.3  # More than 30% are rapid