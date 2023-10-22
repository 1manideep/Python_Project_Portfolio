# chart.py

import matplotlib.pyplot as plt
import numpy as np

def generate_radar_chart(scores):
    topics = list(scores.keys())
    num_topics = len(topics)
    
    # Calculate the average score for each topic
    average_scores = [np.mean(scores[topic]) for topic in topics]
    
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(6, 9), subplot_kw=dict(polar=True))
    
    # Set the number of angles and the angle values
    angles = np.linspace(0, 2 * np.pi, num_topics, endpoint=False).tolist()
    angles += angles[:1]
    
    # Also add the first score to the end of the average_scores list
    average_scores += average_scores[:1]
    
    # Plot the radar chart
    ax.plot(angles, average_scores, linewidth=2, linestyle='solid', color='darkred')
    ax.fill(angles, average_scores, alpha=0.25, color='green')
    
    # Set the labels for each angle
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(topics, color='darkblue')
    
    # Set the y-axis limit
    ax.set_ylim(0, max(average_scores) + 10)
    
    # Add a title
    ax.set_title("Your python profile", size=20, color='darkblue', weight='bold', y=1.05)
    
    # Change the background color
    fig.patch.set_facecolor('#E6E6FA')  # Dark Purple
    ax.set_facecolor('lightgray')
    

    # Add a grid
    ax.grid(True, color='white')
    
    # Show the radar chart
    plt.show()