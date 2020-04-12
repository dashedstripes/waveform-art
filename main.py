import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from scipy.io import wavfile
from datetime import datetime

now = datetime.utcnow()

filename='moonlightsonata'

# Read the wave file to numpy array
fs, signal = wavfile.read(filename + '.wav')
channel_0 = signal[:,0]
channel_1 = signal[:,1]

# Plotting
plt.figure(figsize=(11.69, 8.27), dpi=300)
plt.axis('off')

plt.plot(channel_0, color='#5d4e2e', alpha=1, linewidth=0.05)
plt.plot(channel_1 * 0.6, color='#918267', alpha=1, linewidth=0.01)

plt.savefig('out/moonlightsonata' + str(now) + '.png', format='png', facecolor='#cdbfa4')

# plt.plot(channel_0, color='#d1ba98', alpha=1, linewidth=0.05)
# plt.plot(channel_1 * 0.6, color='#d1ba98', alpha=1, linewidth=0.01)

# plt.savefig('plot.png', format='png', facecolor='#ffffff')