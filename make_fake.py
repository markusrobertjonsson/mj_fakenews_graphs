import matplotlib.pyplot as plt
import numpy as np

##################### Figure 19.1
plt.figure(1)

# Number of interactions (x-values)
x_values = np.arange(0, 51, 1)

# Blue line (10% Fake News)
y_blue = [0.5, 0.39, 0.42, 0.5, 0.6, 0.71, 0.81, 0.9, 0.95, 0.98] + [1.0] * 41

# Orange line (30% Fake News)
y_orange = [0.5, 0.35, 0.35, 0.38, 0.37, 0.35, 0.34, 0.365, 0.39, 0.38,
            0.385, 0.39, 0.38, 0.42, 0.39, 0.405, 0.38, 0.4, 0.42, 0.45,
            0.52, 0.51, 0.54, 0.56, 0.57, 0.55, 0.6, 0.61, 0.625, 0.64,
            0.65, 0.63, 0.7, 0.68, 0.675, 0.78, 0.81, 0.805, 0.82, 0.83,
            0.85, 0.86, 0.87, 0.86, 0.86, 0.85, 0.87, 0.88, 0.89, 0.9, 0.92]

# Green line (70% Fake News)
y_green = [0.5, 0.2, 0.15, 0.13, 0.10, 0.08, 0.06, 0.05, 0.04, 0.03,
           0.01, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0] + [0] * 31

# Purple line (90% Fake News)
y_purple = [0.5, 0.1, 0.012, 0.005] + [0] * 47

# Red line (50% Fake News)
y_red = [0.5, 0.15, 0.04, 0.015, 0.010, 0.005] + [0] * 45

# Plotting
plt.plot(x_values, y_blue, label='10% Fake News')
plt.plot(x_values, y_orange, label='30% Fake News')
plt.plot(x_values, y_green, label='70% Fake News')
plt.plot(x_values, y_red, label='50% Fake News')
plt.plot(x_values, y_purple, label='90% Fake News')

# Annotate the curves with text
fs = 10
plt.text(18, 0.95, 'Proportion fake news: 10%', fontsize=fs)
plt.text(32, 0.61, '30%', fontsize=fs)
plt.text(8, 0.05, '50%', fontsize=fs)
plt.text(2.5, 0.03, '70%', fontsize=fs)
plt.text(-2, 0.02, '90%', fontsize=fs)

plt.xlabel('Number of interactions')
plt.ylabel('Fraction of sharers in population')
plt.ylim([0, 1.05])

plt.grid(True)
# plt.legend()

###################### Figure 19.3
plt.figure(2, figsize=(18, 8))

plt.subplot(131)
plt.plot(x_values, y_blue, label='10% Fake News')
plt.plot(x_values, y_orange, label='30% Fake News')
plt.plot(x_values, y_green, label='70% Fake News')
plt.plot(x_values, y_red, label='50% Fake News')
plt.plot(x_values, y_purple, label='90% Fake News')
plt.grid(True)
plt.xlabel('Number of rounds')
plt.ylabel('Fraction of sharers in population')
fs = 8
plt.text(18, 0.97, 'Proportion fake news: 10%', fontsize=fs)
plt.text(32, 0.61, '30%', fontsize=fs)
plt.text(8, 0.05, '50%', fontsize=fs)
plt.text(2.5, 0.03, '70%', fontsize=fs)
plt.text(-2, 0.02, '90%', fontsize=fs)
plt.xlim([-3, 55])
plt.ylim([0, 1.05])
plt.title("Proportion of trolls: 0%")

plt.subplot(132)
y10 = [0.5, 0.4, 0.45, 0.6, 0.85, 0.97] + [1] *45
plt.plot(x_values, y10)
y30 = [0.5, 0.35, 0.31, 0.37, 0.45, 0.6, 0.8, 0.9, 0.95, 0.97, 0.99] + [1] * 40
plt.plot(x_values, y30)
y50 = [0.5, 0.25, 0.2, 0.21, 0.22, 0.4, 0.5, 0.6, 0.8, 0.9, 0.95, 0.97, 0.99] + [1] * 38
plt.plot(x_values, y50)
y70 = [0.5, 0.15, 0.12, 0.1, 0.097, 0.099, 0.15, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95, 0.98, 0.99] + [1] * 36
plt.plot(x_values, y70)
y90 = [0.5, 0.10, 0.05, 0.051, 0.053, 0.056, 0.07, 0.085, 0.1, 0.12, 0.15, 0.175, 0.19, 0.22, 0.33, 0.4, 0.6, 0.8, 0.9, 0.95, 0.97, 0.98, 0.995] + [1] * 28
plt.plot(x_values, y90)
plt.xlim([-3, 55])
plt.ylim([0, 1.05])
plt.title("Proportion of trolls: 1%")
plt.xlabel('Number of rounds')

plt.text(1, 0.95, '10%', fontsize=fs)
plt.text(5, 0.9, '30%', fontsize=fs)
plt.text(7, 0.85, '50%', fontsize=fs)
plt.text(10, 0.8, '70%', fontsize=fs)
plt.text(17, 0.8, '90%', fontsize=fs)

# plt.ylabel('Fraction of sharers in population')
plt.grid(True)

plt.subplot(133)
y10 = [0.5, 0.48, 0.6, 0.7, 0.8, 0.95, 1] + [1] * 44
plt.plot(x_values, y10, label='10%')
y30 = [0.5, 0.42, 0.5, 0.6, 0.7, 0.8, 0.95, 0.97, 1] + [1] * 42
plt.plot(x_values, y30, label='30%')
y50 = [0.5, 0.3, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.95, 0.98, 1] + [1] * 40
plt.plot(x_values, y50, label='50%')
y70 = [0.5, 0.24, 0.27, 0.3, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.95, 0.98, 0.99, 1] + [1] * 37
plt.plot(x_values, y70, label='70%')
x90 = np.arange(0, 51, 2)
y90 = [0.5, 0.18, 0.1, 0.12, 0.14, 0.16, 0.2, 0.3, 0.4, 0.45, 0.8, 0.95, 0.98, 0.99, 1] + [1] * 11
plt.plot(x90, y90, label='90%')
plt.xlim([-3, 55])
plt.ylim([0, 1.05])
plt.title("Proportion of trolls: 5%")
plt.xlabel('Number of rounds')

plt.text(1, 0.95, '10%', fontsize=fs)
plt.text(5, 0.9, '30%', fontsize=fs)
plt.text(6, 0.85, '50%', fontsize=fs)
plt.text(9, 0.8, '70%', fontsize=fs)
plt.text(20, 0.8, '90%', fontsize=fs)

# plt.ylabel('Fraction of sharers in population')
plt.grid(True)
# plt.legend(title='Proportion fake news')


plt.show()

