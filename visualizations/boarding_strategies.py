import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap

def create_boarding_strategy_visualizations():
    """
    Create visualizations for the three boarding strategies:
    1. Back-to-Front
    2. Outside-In (Window-Middle-Aisle)
    3. Hybrid Strategy
    """
    rows = list(range(28, 49))  # Rows 28 to 48
    cols = ['A', 'B', 'C', 'D', 'E', 'F']  # Columns A to F
    
    # Create visualizations for each strategy
    back_to_front_strategy()
    outside_in_strategy()
    hybrid_strategy()
    random_boarding()
    
    return "Boarding strategy visualizations created successfully."

def back_to_front_strategy():
    """
    Visualize the back-to-front boarding strategy.
    Passengers board in groups from the back to the front of the aircraft.
    """
    rows = list(range(28, 49))  # Rows 28 to 48
    cols = ['A', 'B', 'C', 'D', 'E', 'F']  # Columns A to F
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Define zones (divide into 6 groups)
    zone_size = len(rows) // 6
    zones = {}
    for i in range(6):
        if i < 5:  # First 5 groups
            start_idx = i * zone_size
            end_idx = (i + 1) * zone_size
            zone_rows = rows[start_idx:end_idx]
        else:  # Last group (may have extra rows)
            zone_rows = rows[i * zone_size:]
        
        for row in zone_rows:
            for col in cols:
                zones[(row, col)] = i
    
    # Create a colormap with 6 distinct colors
    colors = plt.cm.tab10(np.linspace(0, 1, 10))[:6]
    
    # Plot grid
    for i, row in enumerate(rows):
        for j, col in enumerate(cols):
            # Leave aisle space between C and D
            x = j + 0.5 + (0.5 if j >= 3 else 0)
            y = len(rows) - i - 0.5
            
            # Get zone number (0-5)
            zone = zones[(row, col)]
            
            # Draw seat with color based on zone
            rect = plt.Rectangle((x-0.4, y-0.4), 0.8, 0.8, fill=True, 
                                color=colors[zone], edgecolor='black', linewidth=1)
            ax.add_patch(rect)
            
            # Add seat label and boarding group number
            ax.text(x, y, f"{row}{col}", ha='center', va='center', fontsize=8)
            ax.text(x, y-0.2, f"Group {zone+1}", ha='center', va='center', fontsize=6)
    
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
    plt.title('Back-to-Front Boarding Strategy', fontsize=16, pad=20)
    
    # Add front/back indicators
    ax.text(3.25, -0.5, "BACK", ha='center', fontsize=12, fontweight='bold')
    ax.text(3.25, len(rows) + 0.5, "FRONT", ha='center', fontsize=12, fontweight='bold')
    
    # Add legend for boarding groups
    patches = []
    for i in range(6):
        patches.append(mpatches.Patch(color=colors[i], label=f'Group {i+1}'))
    
    boarding_order = mpatches.Patch(color='white', label='Boarding Order: 6→5→4→3→2→1')
    plt.legend(handles=patches + [boarding_order], loc='upper right', framealpha=0.7)
    
    # Add arrows showing boarding direction
    plt.arrow(8, len(rows)/2, 0, -2, head_width=0.3, head_length=0.3, fc='black', ec='black')
    ax.text(8.3, len(rows)/2, 'Boarding Direction', va='center')
    
    # Border around entire aircraft
    aircraft_outline = plt.Rectangle((-0.5, -0.5), 7, len(rows) + 1, fill=False, 
                                    edgecolor='gray', linewidth=2, linestyle='-')
    ax.add_patch(aircraft_outline)
    
    plt.tight_layout()
    plt.savefig('back_to_front_strategy.png', dpi=300, bbox_inches='tight')
    plt.close()

def outside_in_strategy():
    """
    Visualize the outside-in (window-middle-aisle) boarding strategy.
    Passengers board based on their seat position rather than row.
    """
    rows = list(range(28, 49))  # Rows 28 to 48
    cols = ['A', 'B', 'C', 'D', 'E', 'F']  # Columns A to F
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Define seat types
    seat_types = {
        'A': 0,  # Window
        'F': 0,  # Window
        'B': 1,  # Middle
        'E': 1,  # Middle
        'C': 2,  # Aisle
        'D': 2,  # Aisle
    }
    
    # Create a colormap with 3 distinct colors
    colors = plt.cm.Set1(np.linspace(0, 1, 3))
    
    # Plot grid
    for i, row in enumerate(rows):
        for j, col in enumerate(cols):
            # Leave aisle space between C and D
            x = j + 0.5 + (0.5 if j >= 3 else 0)
            y = len(rows) - i - 0.5
            
            # Get seat type (0=window, 1=middle, 2=aisle)
            seat_type = seat_types[col]
            
            # Draw seat with color based on seat type
            rect = plt.Rectangle((x-0.4, y-0.4), 0.8, 0.8, fill=True, 
                                color=colors[seat_type], edgecolor='black', linewidth=1)
            ax.add_patch(rect)
            
            # Add seat label and group info
            ax.text(x, y, f"{row}{col}", ha='center', va='center', fontsize=8)
            
            if seat_type == 0:
                group_text = "Group 1"
            elif seat_type == 1:
                group_text = "Group 2"
            else:
                group_text = "Group 3"
                
            ax.text(x, y-0.2, group_text, ha='center', va='center', fontsize=6)
    
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
    plt.title('Outside-In (Window-Middle-Aisle) Boarding Strategy', fontsize=16, pad=20)
    
    # Add front/back indicators
    ax.text(3.25, -0.5, "BACK", ha='center', fontsize=12, fontweight='bold')
    ax.text(3.25, len(rows) + 0.5, "FRONT", ha='center', fontsize=12, fontweight='bold')
    
    # Add legend for seat types
    window_patch = mpatches.Patch(color=colors[0], label='Group 1: Window Seats (A, F)')
    middle_patch = mpatches.Patch(color=colors[1], label='Group 2: Middle Seats (B, E)')
    aisle_patch = mpatches.Patch(color=colors[2], label='Group 3: Aisle Seats (C, D)')
    
    boarding_order = mpatches.Patch(color='white', label='Boarding Order: 1→2→3')
    plt.legend(handles=[window_patch, middle_patch, aisle_patch, boarding_order], 
              loc='upper right', framealpha=0.7)
    
    # Add arrows showing boarding direction
    plt.arrow(8, len(rows)/2, 0, -2, head_width=0.3, head_length=0.3, fc='black', ec='black')
    ax.text(8.3, len(rows)/2, 'Boarding Direction', va='center')
    
    # Border around entire aircraft
    aircraft_outline = plt.Rectangle((-0.5, -0.5), 7, len(rows) + 1, fill=False, 
                                    edgecolor='gray', linewidth=2, linestyle='-')
    ax.add_patch(aircraft_outline)
    
    plt.tight_layout()
    plt.savefig('outside_in_strategy.png', dpi=300, bbox_inches='tight')
    plt.close()

def hybrid_strategy():
    """
    Visualize the hybrid boarding strategy.
    Combines both back-to-front and outside-in approaches.
    """
    rows = list(range(28, 49))  # Rows 28 to 48
    cols = ['A', 'B', 'C', 'D', 'E', 'F']  # Columns A to F
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Define zones (divide into 3 sections: back, middle, front)
    section_size = len(rows) // 3
    sections = {}
    for i in range(3):
        if i < 2:  # First 2 sections
            start_idx = i * section_size
            end_idx = (i + 1) * section_size
            section_rows = rows[start_idx:end_idx]
        else:  # Last section (may have extra rows)
            section_rows = rows[i * section_size:]
        
        for row in section_rows:
            sections[row] = i
    
    # Define seat types
    seat_types = {
        'A': 0,  # Window
        'F': 0,  # Window
        'B': 1,  # Middle
        'E': 1,  # Middle
        'C': 2,  # Aisle
        'D': 2,  # Aisle
    }
    
    # Create a mapping for the 9 groups
    groups = {}
    group_counter = 1
    
    # Back, middle, front for window seats
    for section in [2, 1, 0]:  # Back=2, Middle=1, Front=0
        for row in rows:
            if sections[row] == section:
                for col in cols:
                    if seat_types[col] == 0:  # Window seats
                        groups[(row, col)] = group_counter
        group_counter += 1
    
    # Back, middle, front for middle seats
    for section in [2, 1, 0]:  # Back=2, Middle=1, Front=0
        for row in rows:
            if sections[row] == section:
                for col in cols:
                    if seat_types[col] == 1:  # Middle seats
                        groups[(row, col)] = group_counter
        group_counter += 1
    
    # Back, middle, front for aisle seats
    for section in [2, 1, 0]:  # Back=2, Middle=1, Front=0
        for row in rows:
            if sections[row] == section:
                for col in cols:
                    if seat_types[col] == 2:  # Aisle seats
                        groups[(row, col)] = group_counter
        group_counter += 1
    
    # Create a colormap with 9 distinct colors
    colors = plt.cm.tab10(np.linspace(0, 1, 10))[:9]
    
    # Plot grid
    for i, row in enumerate(rows):
        for j, col in enumerate(cols):
            # Leave aisle space between C and D
            x = j + 0.5 + (0.5 if j >= 3 else 0)
            y = len(rows) - i - 0.5
            
            # Get group number (1-9)
            group = groups[(row, col)]
            
            # Draw seat with color based on group
            rect = plt.Rectangle((x-0.4, y-0.4), 0.8, 0.8, fill=True, 
                                color=colors[group-1], edgecolor='black', linewidth=1)
            ax.add_patch(rect)
            
            # Add seat label and group number
            ax.text(x, y, f"{row}{col}", ha='center', va='center', fontsize=8)
            ax.text(x, y-0.2, f"Group {group}", ha='center', va='center', fontsize=6)
    
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
    plt.title('Hybrid Boarding Strategy', fontsize=16, pad=20)
    
    # Add front/back indicators
    ax.text(3.25, -0.5, "BACK", ha='center', fontsize=12, fontweight='bold')
    ax.text(3.25, len(rows) + 0.5, "FRONT", ha='center', fontsize=12, fontweight='bold')
    
    # Add legend for boarding groups
    patches = []
    group_descriptions = [
        "Back Window Seats",
        "Middle Window Seats",
        "Front Window Seats",
        "Back Middle Seats",
        "Middle Middle Seats",
        "Front Middle Seats",
        "Back Aisle Seats",
        "Middle Aisle Seats",
        "Front Aisle Seats"
    ]
    
    for i in range(9):
        patches.append(mpatches.Patch(color=colors[i], label=f'Group {i+1}: {group_descriptions[i]}'))
    
    boarding_order = mpatches.Patch(color='white', label='Boarding Order: 1→2→3→4→5→6→7→8→9')
    
    # Create a second figure for the legend due to its size
    fig_legend = plt.figure(figsize=(12, 2))
    fig_legend.legend(handles=patches + [boarding_order], loc='center', ncol=3)
    fig_legend.savefig('hybrid_strategy_legend.png', dpi=300, bbox_inches='tight')
    plt.close(fig_legend)
    
    # Add shortened legend to main plot
    short_patches = []
    for i in range(3):
        short_patches.append(mpatches.Patch(color=colors[i], label=f'Groups 1-3: Window Seats'))
    for i in range(3, 6):
        short_patches.append(mpatches.Patch(color=colors[i], label=f'Groups 4-6: Middle Seats'))
    for i in range(6, 9):
        short_patches.append(mpatches.Patch(color=colors[i], label=f'Groups 7-9: Aisle Seats'))
    
    plt.legend(handles=short_patches[:3], loc='upper right', framealpha=0.7)
    
    # Add arrows showing boarding direction
    plt.arrow(8, len(rows)/2, 0, -2, head_width=0.3, head_length=0.3, fc='black', ec='black')
    ax.text(8.3, len(rows)/2, 'Boarding Direction', va='center')
    
    # Border around entire aircraft
    aircraft_outline = plt.Rectangle((-0.5, -0.5), 7, len(rows) + 1, fill=False, 
                                    edgecolor='gray', linewidth=2, linestyle='-')
    ax.add_patch(aircraft_outline)
    
    plt.tight_layout()
    plt.savefig('hybrid_strategy.png', dpi=300, bbox_inches='tight')
    plt.close()

def random_boarding():
    """
    Visualize random boarding (baseline) for comparison.
    Passengers board in random order regardless of seat position.
    """
    rows = list(range(28, 49))  # Rows 28 to 48
    cols = ['A', 'B', 'C', 'D', 'E', 'F']  # Columns A to F
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Random assignment of boarding groups (1-5)
    np.random.seed(42)  # For reproducibility
    
    # Create a colormap with a continuous gradient
    cmap = plt.cm.viridis
    
    # Plot grid with random boarding groups
    for i, row in enumerate(rows):
        for j, col in enumerate(cols):
            # Leave aisle space between C and D
            x = j + 0.5 + (0.5 if j >= 3 else 0)
            y = len(rows) - i - 0.5
            
            # Random boarding order (normalized for color mapping)
            random_order = np.random.rand()
            
            # Draw seat with random color
            rect = plt.Rectangle((x-0.4, y-0.4), 0.8, 0.8, fill=True, 
                                color=cmap(random_order), edgecolor='black', linewidth=1)
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
    plt.title('Random Boarding (Baseline)', fontsize=16, pad=20)
    
    # Add front/back indicators
    ax.text(3.25, -0.5, "BACK", ha='center', fontsize=12, fontweight='bold')
    ax.text(3.25, len(rows) + 0.5, "FRONT", ha='center', fontsize=12, fontweight='bold')
    
    # Add a colorbar for reference
    sm = plt.cm.ScalarMappable(cmap=cmap)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', pad=0.05)
    cbar.set_label('Random Boarding Order')
    
    # Add arrows showing boarding direction
    plt.arrow(8, len(rows)/2, 0, -2, head_width=0.3, head_length=0.3, fc='black', ec='black')
    ax.text(8.3, len(rows)/2, 'Boarding Direction', va='center')
    
    # Border around entire aircraft
    aircraft_outline = plt.Rectangle((-0.5, -0.5), 7, len(rows) + 1, fill=False, 
                                    edgecolor='gray', linewidth=2, linestyle='-')
    ax.add_patch(aircraft_outline)
    
    plt.tight_layout()
    plt.savefig('random_boarding.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_boarding_strategy_visualizations()