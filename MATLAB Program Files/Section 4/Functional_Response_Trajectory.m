%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides a trajectory of the functional response model with 
% m = 1.  In this case, the model is neutrally stable and the trajectory is
% an example of a limit cycle. 
% (This file creates Figure 11 of Section 4.1.2)
clear all, close all, clc

% Parameters: 
c = .1;
k = 1;
R = 2;
T = 1;

% Number of years: 
N = 50; 

% Escape response:
f = @(H,P) 1./(1+c*R*H*P*T);

% Initial populations:
H0 = 5;
P0 = 8;

% Vector initialization: 
H = [H0 zeros(1,N-1)];
P = [P0 zeros(1,N-1)];

% Function iteration to create the trajectory:
for t = 1:N
    H(t+1) = R*H(t)*f(H(t),P(t));
    P(t+1) = k*R*H(t)*(1-f(H(t),P(t)));
end

% Plot: 
figure(1)
sgtitle('Trajectory of Functional Response Model','fontsize',28,...
        'interpreter','latex')
subplot(1,2,1)
plot(0:N,H,'r-o','linewidth',3)
hold on
plot(0:N,P,'b-o','linewidth',3)
set(gca,'fontsize',18)
title('Time Series Plot','fontsize',25,...
      'interpreter','latex')
xlabel('$t$ (years)','fontsize',22,'interpreter','latex')
ylabel('$H_t$, $P_t$','fontsize',22,'interpreter','latex')
legend('Hosts','Parasitoids','location','Northwest',...
       'interpreter','latex','fontsize',22)
grid on
grid minor

% Phase plane plot: 
figure(1)
subplot(1,2,2)
plot(H,P,'k-o','linewidth',3)
hold on
plot(H0,P0,'go','linewidth',5)
set(gca,'fontsize',18)
title('Phase Plane Plot','fontsize',25,...
      'interpreter','latex')
xlabel('$H_t$','fontsize',22,'interpreter','latex')
ylabel('$P_t$','fontsize',22,'interpreter','latex')
legend('$(H_t,P_t)$','$(H_0,H_0)$','location','Northeast',...
       'interpreter','latex','fontsize',22)
grid on
grid minor