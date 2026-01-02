%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file shows the solutions to the ODE system using constant parasitism
% coupled with a density dependent host mortality.  Although the solutions
% to the ODE can be found explicitly, we demonstrate how to solve the
% system numericall using MATLAB's built-in ODE solver.  The solution is 
% shown with respect to the vulnerable period time variable tau. 
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

    % Define the initial conditions for the ODEs and place them in a global
    % vector: 
    L_0 = R*H;
    I_0 = 0;
    P_0 = P;
    
    Y_0 = [L_0; I_0; P_0];
    
    % Define the right-hand side of the ODEs as function handles and define
    % a global vector function: 
    dLdtau = @(tau,L,I,P) -c*L*P - cd*L.^2;
    dIdtau = @(tau,L,I,P) c*L*P;
    dPdtau = @(tau,L,I,P) 0;
    
    dYdtau = @(tau,Y) [dLdtau(tau,Y(1),Y(2),Y(3));
                       dIdtau(tau,Y(1),Y(2),Y(3));
                       dPdtau(tau,Y(1),Y(2),Y(3))];
                   
    % Call the built-in ODE solver ode45 to solve the sytem: 
    [tau,Y] = ode45(dYdtau,tau,Y_0);
    
    L = Y(:,1);
    I = Y(:,2);
    P = Y(:,3);
    
    % Plot String:
    L_string = {'k','k:'};
    I_string = {'r','r:'};
    
    % Plot:
    figure(1)
    plot(tau,L,L_string{i},'linewidth',5-i)
    hold on
    plot(tau,I,I_string{i},'linewidth',5-i)
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