# main.py

import score
import chart

def main():
    # Load student scores from data.json
    scores = score.load_scores("data.json")
    
    # Generate radar chart
    chart.generate_radar_chart(scores)

if __name__ == "__main__":
    main()
