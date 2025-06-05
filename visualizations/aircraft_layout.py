import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

def create_aircraft_seating_chart():
    """
    Create a visual representation of the Boeing 737-800 seating layout
    with rows 28-48 and columns A-F.
    """
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Set up grid parameters
    rows = list(range(28, 49))  # Rows 28 to 48
    cols = ['A', 'B', 'C', 'D', 'E', 'F']  # Columns A to F
    
    # Create grid
    grid = np.zeros((len(rows), len(cols)))
    
    # Plot grid
    for i, row in enumerate(rows):
        for j, col in enumerate(cols):
            # Leave aisle space between C and D
            x = j + 0.5 + (0.5 if j >= 3 else 0)
            y = len(rows) - i - 0.5
            
            # Draw seat
            rect = plt.Rectangle((x-0.4, y-0.4), 0.8, 0.8, fill=True, 
                                color='lightblue', edgecolor='black', linewidth=1)
            ax.add_patch(rect)
            
            # Add seat label
            ax.text(x, y, f"{row}{col}", ha='center', va='center', fontsize=8)
    
    # Draw aisle
    aisle_x = 3.25
    aisle_height = len(rows) + 1
    plt.plot([aisle_x, aisle_x], [0, aisle_height], 'k--', alpha=0.5)
    
    # Set axis limits and labels
    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-0.5, len(rows) + 0.5)
    
    # Hide regular axes
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Add column labels at top
    for j, col in enumerate(cols):
        x = j + 0.5 + (0.5 if j >= 3 else 0)
        ax.text(x, len(rows) + 0.2, col, ha='center', va='center', fontweight='bold')
    
    # Add row labels on left side
    for i, row in enumerate(rows):
        y = len(rows) - i - 0.5
        ax.text(-0.2, y, str(row), ha='right', va='center', fontweight='bold')
    
    # Set title
    plt.title('Boeing 737-800 Seating Chart (Rows 28-48)', fontsize=16, pad=20)
    
    # Add front/back indicators
    ax.text(3.25, -0.5, "BACK", ha='center', fontsize=12, fontweight='bold')
    ax.text(3.25, len(rows) + 0.5, "FRONT", ha='center', fontsize=12, fontweight='bold')
    
    # Add legend for seat positions
    window_patch = mpatches.Patch(color='lightblue', label='Seat')
    plt.legend(handles=[window_patch], loc='upper right', framealpha=0.7)
    
    # Add arrows showing directions
    plt.arrow(8, len(rows)/2, 0, -2, head_width=0.3, head_length=0.3, fc='black', ec='black')
    ax.text(8.3, len(rows)/2, 'Boarding Direction', va='center')
    
    # Border around entire aircraft
    aircraft_outline = plt.Rectangle((-0.5, -0.5), 7, len(rows) + 1, fill=False, 
                                    edgecolor='gray', linewidth=2, linestyle='-')
    ax.add_patch(aircraft_outline)
    
    plt.tight_layout()
    plt.savefig('aircraft_layout.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return "Aircraft seating chart created successfully."

if __name__ == "__main__":
    create_aircraft_seating_chart()