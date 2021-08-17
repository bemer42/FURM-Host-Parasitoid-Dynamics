%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file solves the egg maturation delay ODE system given by Equations
% 91 and 92 of the text, with constant rates of parasitism and delay.
% (This file can essentially be used to solve Exercise 21.)
close all, clear all, clc

% Time Discretization:
T   = 1;
tau = linspace(0,T,1e3);

% Parameters:
beta = .5;
c    = .1;
cr   = 1e1;
R    = 2;
H    = 5;
P    = 8;

% Define the initial conditions for the ODEs and place them in a global
% vector:
L_0 = R*H;
I_0 = 0;
P0_0 = beta*P;
P1_0 = (1-beta)*P;

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
[tau,Y] = ode45(dYdtau,tau,Y_0);

L  = Y(:,1);
I  = Y(:,2);
P0 = Y(:,3);
P1 = Y(:,4);

% Plot:
figure(1)
plot(tau,L,'k','linewidth',5)
hold on
plot(tau,I,'r','linewidth',5)
plot(tau,P0,'b:','linewidth',5)
plot(tau,P1,'b','linewidth',5)
set(gca,'fontsize',18)
title('Constant Attack with Host Mortality','fontsize',28,...
    'interpreter','latex')
xlabel('$\tau$ (time in vulnerable period)','fontsize',22,'interpreter','latex')
ylabel('$L(\tau,t)$ and $I(\tau, t)$','fontsize',22,'interpreter','latex')
legend('$L(\tau,t)$','$I(\tau,t)$','$P_0(\tau,t)$','$P_1(\tau,t)$',...
    'interpreter','latex','location','Northeast','fontsize',22)
grid on
grid minor

