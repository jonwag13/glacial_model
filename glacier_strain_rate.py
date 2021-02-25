#Strain rate calculations
import numpy as np

A_star = 3.5e-25
Q_c = 85000
R = 8.314
delta_z = 50
h = 2800
z = np.arange(0,h,delta_z)
rho = vDensity
g = 9.8
T = vTemp + 273.15
theta = 0.2
n = 3

#1
P = rho * g * z
# 2
T_star = 263 + 7e-8 * P
# 3
T_h = T + 7e-8 * P
# 4
A = A_star * exp(-Q_c / R * (1 / T_h - 1 / T_star));
A = A

# 5
tao_xz = rho * g * z * sind(theta)

# 6
E_xz = A * tao_xz ** (n / 60 * 60 * 24 * 365)

# 7
dudz = 2 * E_xz

# 8
u_z = np.zeros(size(z))

'''

for t = 1:length(z)

if t == 1
    u_z(1) = dudz(t). * delta_z;
else
    u_z(t) = u_z(t - 1) + dudz(t). * delta_z;
'''

'''
% % Figures

% Make
control
lines
bold

% stress
plot(tao_xz, z, 'LineWidth', 2, 'Color', 'k')
set(gca, 'Ydir', 'reverse')
xlabel('tao_{xz}', 'FontWeight', 'bold')
ylabel('depth (m)', 'FontWeight', 'bold')

% strain
rate
figure
plot(E_xz, z, 'LineWidth', 2, 'Color', 'k')
set(gca, 'Ydir', 'reverse')
xlabel('Strain Rate', 'FontWeight', 'bold')
ylabel('depth (m)', 'FontWeight', 'bold')

% velocity
figure
plot(dudz, z, 'LineWidth', 2, 'Color', 'k')
set(gca, 'Ydir', 'reverse')
xlabel('Velocity (m a^{-1}', 'FontWeight', 'bold')
ylabel('depth (m)', 'FontWeight', 'bold')
'''
