%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file shows the solutions to the ODE system using constant parasitism
% coupled with a density dependent host mortality.  We plot the explicit
% solution found in the text.  The solution is shown with respect to the 
% vulnerable period time variable tau. 
% (This file creates Figure 10 of Section 3.2)
close all, clear all, clc

% Time Discretization:
T   = 1;
tau = linspace(0,T,1e3);

% Parameter c Variation:
cd_vec = logspace(-1,0,2);

% Create two trajectories using a for loop:
for i = 1:length(cd_vec)
    
    % Parameters:
    cd = cd_vec(i);
    c = .1;
    R = 2;
    H = 5;
    P = 8;
    
    % Solutions to basic parasitism with constant rate and host mortality:
    L = @(tau) R*H./(exp(c*P*tau)+cd*R*H*(exp(c*P*tau)-1)/c/P);
    I = @(tau) c*P/cd*log(1+cd*R*H*(1-exp(-c*P*tau))/c/P);
    P = @(tau) P*ones(size(tau));
    
    % Plot String:
    L_string = {'k','k:'};
    I_string = {'r','r:'};
    
    % Plot:
    figure(1)
    plot(tau,L(tau),L_string{i},'linewidth',5-i)
    hold on
    plot(tau,I(tau),I_string{i},'linewidth',5-i)
    set(gca,'fontsize',18)
    title('Constant Attack with Host Mortality','fontsize',28,...
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