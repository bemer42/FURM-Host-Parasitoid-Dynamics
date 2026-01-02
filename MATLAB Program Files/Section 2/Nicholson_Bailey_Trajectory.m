%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file graphs a time series trajectory of the Nicholson-Bailey Model.
% (This file creates the left panel of Figure 6 in Section 2.2.)
clear all, close all, clc

% Model Parameters: 
c = .1;
R = 2;
k = 1;

% Number of years: 
N = 20; 

% Escape response:
f = @(P) exp(-c*P);

% Initial populations:
H0 = 5;
P0 = 8;

% Vector initialization: 
H = [H0 zeros(1,N-1)];
P = [P0 zeros(1,N-1)];

% Function iteration to create the trajectory:
for t = 1:N
    H(t+1) = R*H(t)*f(P(t));
    P(t+1) = k*R*H(t)*(1-f(P(t)));
end

% Time Series Plot: 
figure(1)
plot(0:N,H,'r-o','linewidth',3)
hold on
plot(0:N,P,'b-o','linewidth',3)
set(gca,'fontsize',18)
title('Trajectory of Nicholson-Bailey Model','fontsize',25,...
      'interpreter','latex')
xlabel('$t$ (years)','fontsize',22,'interpreter','latex')
ylabel('$H_t$, $P_t$','fontsize',22,'interpreter','latex')
legend('Hosts','Parasitoids','interpreter','latex','location','Northwest')
grid on
grid minor

% Phase Plane Plot:
figure(2)
plot(H,P,'k-o','linewidth',3)
hold on
plot(H0,P0,'go','linewidth',5)
set(gca,'fontsize',18)
title('Trajectory of Nicholson-Bailey Model','fontsize',25,...
      'interpreter','latex')
xlabel('$H_t$ (hosts)','fontsize',22,'interpreter','latex')
ylabel('$P_t$ (parsitoids)','fontsize',22,'interpreter','latex')
legend('$(H_t,P_t)$','$(H_0,P_0)$','interpreter','latex','location','Northwest')
grid on
grid minor
