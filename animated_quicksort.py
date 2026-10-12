import random
import matplotlib.pyplot as plt

# Configuration
ARRAY_SIZE = 25
original_arr = [random.randint(10, 100) for _ in range(ARRAY_SIZE)]


def get_quick_sort_states(arr):
  """Pre-computes all states of the array during the Quick Sort process

  to enable interactive stepping.
  """
  states = []
  a = list(arr)

  def partition(low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
      # Record state during comparison
      states.append((list(a), j, high, 'comparing'))
      if a[j] < pivot:
        i += 1
        a[i], a[j] = a[j], a[i]
        # Record state after swap
        states.append((list(a), i, high, 'swapping'))

    a[i + 1], a[high] = a[high], a[i + 1]
    # Record state after placing pivot in final sorted position
    states.append((list(a), i + 1, high, 'pivot placed'))
    return i + 1

  def sort(low, high):
    if low < high:
      pi = partition(low, high)
      sort(low, pi - 1)
      sort(pi + 1, high)

  sort(0, len(a) - 1)
  # Final sorted state
  states.append((list(a), -1, -1, 'sorted'))
  return states


# Generate states
states = get_quick_sort_states(original_arr)

# Setup Matplotlib Interactive Figure
fig, ax = plt.subplots(figsize=(10, 6))
fig.canvas.manager.set_window_title('Interactive Quick Sort Visualizer')

bars = ax.bar(
    range(ARRAY_SIZE), states[0][0], color='skyblue', edgecolor='black'
)
ax.set_ylim(0, 115)
ax.set_ylabel('Value')
ax.set_xlabel('Index')

current_step = [0]


def update_plot(step_idx):
  arr, active_idx, pivot_idx, mode = states[step_idx]

  for idx, bar in enumerate(bars):
    bar.set_height(arr[idx])
    # Color-coding logic for visualization clarity
    if idx == pivot_idx:
      bar.set_color('#e74c3c')  # Crimson Red for Pivot
    elif idx == active_idx:
      bar.set_color('#f39c12')  # Orange for Active Comparison/Swap
    else:
      bar.set_color('#3498db')  # Blue for Unsorted/Normal

  ax.set_title(
      f'Quick Sort Visualizer\nStep: {step_idx + 1} / {len(states)} | Status:'
      f' {mode.upper()}\n[Controls: Press Space / Right Arrow to Advance, Left'
      ' Arrow to Reverse]',
      fontsize=12,
      fontweight='bold',
  )
  fig.canvas.draw_idle()


def on_key(event):
  """Keyboard event listener for interactive navigation"""
  if event.key in [' ', 'right', 'enter']:
    if current_step[0] < len(states) - 1:
      current_step[0] += 1
      update_plot(current_step[0])
  elif event.key == 'left':
    if current_step[0] > 0:
      current_step[0] -= 1
      update_plot(current_step[0])


# Connect the key press event handler
fig.canvas.mpl_connect('key_press_event', on_key)

# Initialize display
update_plot(0)
plt.show()