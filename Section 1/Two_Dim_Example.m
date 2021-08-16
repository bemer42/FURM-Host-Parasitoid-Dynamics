%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides a trajectory of the 2-D Example in Section 1.3. 
% The output of this program is Figure 2 in the text, which shows a
% trajectory of the dynamical system.  Two figures are created: 
%   - The first figure shows a time-series representation of the trajectory 
%     that clearly demonstrates the stability of the fixed point 
%     (x1*, y1*) = (3,11).  
%   - The second figure shows the phase plane representation of the
%     trajectory which also demonstrates the stability of the fixed point.
% (This file creates Figure 2 of Section 1.3.)
% This file also outputs the maximum eigenvalue for the Jacobian matrix
% evalated at each fixed point.
clear all, close all, clc

% Number of years: 
N = 150; 

% Define the 2-D system functions:
f = @(x,y) 5 + 1/4*(x-y);
g = @(x,y) 2 + 1/4*x*(1+y);

% Initial populations:
x0 = 5;
y0 = 1;

% Vector initialization: 
x = [x0 zeros(1,N-1)];
y = [y0 zeros(1,N-1)];

% Function iteration to create the trajectory:
for t = 1:N
    x(t+1) = f(x(t),y(t));
    y(t+1) = g(x(t),y(t));
end

% Time series plot: 
figure(1)
sgtitle('Trajectory of 2D Example','fontsize',28,'interpreter','latex') 
subplot(1,2,1)
plot(0:N,x,'r-o','linewidth',3)
hold on
plot(0:N,y,'b-o','linewidth',3)
set(gca,'fontsize',18)
title('Time Series Plot','fontsize',25,...
      'interpreter','latex')
xlabel('$t$','fontsize',22,'interpreter','latex')
ylabel('$x_t$, $y_t$','fontsize',22,'interpreter','latex')
legend('$x_t$','$y_t$','location','Northeast','interpreter','latex',...
       'fontsize',22)
grid on
grid minor

% Phase plane plot: 
figure(1)
subplot(1,2,2)
plot(x,y,'k-o','linewidth',3)
hold on
plot(x0,y0,'go','linewidth',5)
set(gca,'fontsize',18)
title('Phase Plane Plot','fontsize',25,...
      'interpreter','latex')
xlabel('$x_t$','fontsize',22,'interpreter','latex')
ylabel('$y_t$','fontsize',22,'interpreter','latex')
legend('$(x_t,y_t)$','$(x_0,y_0)$','location','Northeast',...
       'interpreter','latex','fontsize',22)
grid on
grid minor

% Output the maximum eigenvalue of the Jacobian matrix evaluated at each 
% fixed point: 
J_1 = [1/4 -1/4; 3 3/4];
Evals_1 = eigs(J_1);
rho_1   = max(abs(Evals_1))

J_2 = [1/4 -1/4; -3/4 2];
Evals_2 = eigs(J_2);
rho_2   = max(abs(Evals_2))