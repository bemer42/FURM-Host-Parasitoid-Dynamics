%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file shows the solutions to the ODE systems using constant and
% functional response parsitism for different values of the attack
% parameter c.  The output is two figures of both models that shows the
% solution during the vulnerable period. 
% (This file creates Figure 9 of Section 3.1.1)
close all, clear all, clc

% Time Discretization:
T   = 1;
tau = linspace(0,T,1e3);

% Parameter c variation:
c_vec = logspace(-1,0,2);

% Create two trajectories using a for loop:
for i = 1:length(c_vec)
    
    % Parameters:
    c = c_vec(i);
    R = 2;
    H = 5;
    P = 8;
    
    % Solutions to Basic Parasitism with Constant Rate:
    L1 = @(tau) R*H*exp(-c*P*tau);
    I1 = @(tau) R*H*(1-exp(-c*P*tau));
    P1 = @(tau) P*ones(size(tau));
    
    % Solutions to Basic Parasitism with Functional Rate:
    L2 = @(tau) R*H./(1+c*R*H*P*tau);
    I2 = @(tau) R*H.*(1-1./(1+c*R*H*P*tau));
    P2 = @(tau) P*ones(size(tau));
    
    % Plot String:
    L_string = {'k','k:'};
    I_string = {'r','r:'};
    
    % Plot:
    figure(1)
    subplot(1,2,1)
    plot(tau,L1(tau),L_string{i},'linewidth',5-i)
    hold on
    plot(tau,I1(tau),I_string{i},'linewidth',5-i)
    set(gca,'fontsize',8)
    title('Constant Attack','fontsize',28,...
        'interpreter','latex')
    xlabel('$\tau$ (time in vulnerable period)','fontsize',22,...
        'interpreter','latex')
    ylabel('$L(\tau,t)$ and $I(\tau, t)$','fontsize',22,'interpreter','latex')
    legend('$L(\tau,t)$','$I(\tau,t)$','interpreter','latex',...
        'location','Northeast','fontsize',22)
    hold on
    if i ==1
        grid on
        grid minor
    end
    
    subplot(1,2,2)
    plot(tau,L2(tau),L_string{i},'linewidth',5-i)
    hold on
    plot(tau,I2(tau),I_string{i},'linewidth',5-i)
    set(gca,'fontsize',18)
    title('Functional Response Attack','fontsize',28,...
          'interpreter','latex')
    xlabel('$\tau$ (time in vulnerable period)','fontsize',22,'interpreter','latex')
    ylabel('$L(\tau,t)$ and $I(\tau, t)$','fontsize',22,'interpreter','latex')
    legend('$L(\tau,t)$','$I(\tau,t)$','interpreter','latex',...
           'location','Northeast','fontsize',22)   
    if i ==1
        grid on
        grid minor
    end
    
end