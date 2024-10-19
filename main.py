import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from simulation import Simulation
from grid import Grid

s = Simulation(
    grid_x=Grid(128, -4),
    grid_p=Grid(128, -4),
    grid_t=Grid(1024, -4),
)
s.t.shift_up()
s.simulate()

# Animation
fig, ax = plt.subplots()
line, = ax.plot(s.x.space, np.abs(s.wf_t[0])**2)
ax.set_xlabel("Position")
ax.set_ylabel("Probability Density")
ax.set_title("Wavepacket Probability Density")

def animate(i):
    line.set_ydata(np.abs(s.wf_t[i])**2)  # Update the data
    return line,

ani = FuncAnimation(fig, animate, frames=len(s.wf_t), interval=50, blit=True)
# plt.show()
# ani.save("wavepacket_animation.gif", writer="pillow", fps=20)  # Save as GIF
ani.save("wavepacket_animation.mp4", writer="ffmpeg", fps=20)  # Save as MP4