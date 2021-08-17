%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file solves the egg maturation delay ODE system given by Equations
% 91 and 92 of the text, with constant rates of parasitism and delay.
% (This file can essentially be used to solve Exercise 21.)
close all, clear all, clc

% Vulnerable Period Time Discretization:
T   = 1;
tau = linspace(0,T,1e3);

% Number of years:
N = 50;

% Parameters:
beta = .5;
c    = .1;
cr   = 1e0;
R    = 2;
k    = 1;

% Initial populations:
H_0 = 5;
P_0 = 8;

% Vector initialization:
H = [H_0 zeros(1,N-1)];
P = [P_0 zeros(1,N-1)];

% Function iteration to create the trajectory:
for t = 1:N
    
    % Define the initial conditions for the ODEs and place them in a global
    % vector:
    L_0 = R*H(t);
    I_0 = 0;
    P0_0 = beta*P(t);
    P1_0 = (1-beta)*P(t);
    
    Y_0 = [L_0; I_0; P0_0; P1_0];
    
    % Define the right-hand side of the ODEs as function handles and define
    % a global vector function:
    dLdtau  = @(tau,L,I,P0,P1) -c*L*P1;
    dIdtau  = @(tau,L,I,P0,P1) c*L*P1;
    dP0dtau = @(tau,L,I,P0,P1) c*L*P1 - cr*P0;
    dP1dtau = @(tau,L,I,P0,P1) -c*L*P1 + cr*P0;
    
    dYdtau = @(tau,Y) [dLdtau(tau,Y(1),Y(2),Y(3),Y(4));
        dIdtau(tau,Y(1),Y(2),Y(3),Y(4));
        dP0dtau(tau,Y(1),Y(2),Y(3),Y(4));
        dP1dtau(tau,Y(1),Y(2),Y(3),Y(4))];
    
    % Call the built-in ODE solver ode45 to solve the sytem:
    [tau,Y] = ode15s(dYdtau,tau,Y_0);
    
    L  = Y(:,1);
    I  = Y(:,2);
    P0 = Y(:,3);
    P1 = Y(:,4);
    
    % Define the next year update values for H_t and P_t:
    H(t+1) = L(end);
    P(t+1) = k*I(end);
    
end

% Plot: 
figure(1)
sgtitle('Trajectory of Egg Maturation Delay Model','fontsize',28,...
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
plot(H_0,P_0,'go','linewidth',5)
set(gca,'fontsize',18)
title('Phase Plane Plot','fontsize',25,...
      'interpreter','latex')
xlabel('$H_t$','fontsize',22,'interpreter','latex')
ylabel('$P_t$','fontsize',22,'interpreter','latex')
legend('$(H_t,P_t)$','$(H_0,H_0)$','location','Northeast',...
       'interpreter','latex','fontsize',22)
grid on
grid minor

