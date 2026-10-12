import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_merge_sort_steps(arr):
    """
    A recursive merge sort that yields or records history states 
    of the array along with active indices for visualization.
    """
    history = []
    
    def merge_sort(a, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        yield from merge_sort(a, l, mid)
        yield from merge_sort(a, mid + 1, r)
        
        # Merge step
        left_half = a[l:mid + 1]
        right_half = a[mid + 1:r + 1]
        
        i = 0
        j = 0
        k = l
        
        while i < len(left_half) and j < len(right_half):
            history.append((list(a), k)) # Record state before placement
            if left_half[i] <= right_half[j]:
                a[k] = left_half[i]
                i += 1
            else:
                a[k] = right_half[j]
                j += 1
            history.append((list(a), k)) # Record state after placement
            k += 1
            
        while i < len(left_half):
            history.append((list(a), k))
            a[k] = left_half[i]
            i += 1
            history.append((list(a), k))
            k += 1
            
        while j < len(right_half):
            history.append((list(a), k))
            a[k] = right_half[j]
            j += 1
            history.append((list(a), k))
            k += 1

    # Run the sort to populate history
    dummy_arr = list(arr)
    # Convert generator to list consumption
    list(merge_sort(dummy_arr, 0, len(dummy_arr) - 1))
    return history

def run_visualizer():
    # Configuration
    N = 30  # Number of elements to sort
    arr = list(range(1, N + 1))
    random.shuffle(arr)
    
    # Get all animation frames
    history = generate_merge_sort_steps(arr)
    
    # Setup plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Merge Sort Animation", fontsize=14, fontweight='bold')
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    
    # Create bar containers
    bar_rects = ax.bar(range(len(arr)), arr, color="skyblue", edgecolor="black")
    
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(max(arr) * 1.1))
    
    # Text annotation for frame count
    iteration_text = ax.text(0.02, 0.92, "", transform=ax.transAxes, fontsize=12)

    def update(frame_idx):
        current_arr, active_idx = history[frame_idx]
        
        # Update bar heights and colors
        for idx, rect in enumerate(bar_rects):
            rect.set_height(current_arr[idx])
            if idx == active_idx:
                rect.set_color("crimson")  # Highlight active sorting element
            else:
                rect.set_color("skyblue")
                
        iteration_text.set_text(f"Step: {frame_idx + 1}/{len(history)}")
        return bar_rects

    # Run animation
    anim = animation.FuncAnimation(
        fig, update, frames=len(history), interval=30, repeat=False, blit=False
    )
    
    plt.show()

if __name__ == "__main__":
    run_visualizer()