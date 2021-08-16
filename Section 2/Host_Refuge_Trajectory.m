%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides a trajectory of the host refuge model with two
% different values of alpha: alpha = .2 and alpha = .4.  The figure shows a
% comparison of the trajectories with a weak and strong refuge,
% respectively.
% (This file creates the right panel of Figure 7 of Section 2.3)
clear all, close all, clc

% Parameter Variation:
alpha_vec = [.2 .4];

% Create two trajectories using a for loop:
for i = 1:length(alpha_vec)
    
    % Parameters:
    alpha = alpha_vec(i);
    c = .1;
    k = 1;
    R = 2;
    
    % Number of years:
    N = 50;
    
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
        H(t+1) = alpha*R*H(t) + (1-alpha)*R*H(t)*f(P(t));
        P(t+1) = k*(1-alpha)*R*H(t)*(1-f(P(t)));
    end
    
    % Plot:
    figure(1)
    subplot(2,1,i)
    plot(0:N,H,'r-o','linewidth',3)
    hold on
    plot(0:N,P,'b-o','linewidth',3)
    set(gca,'fontsize',18)
    if i == 1
        title('Host Refuge Trajectories','fontsize',25,...
            'interpreter','latex')
        ylim([0 75])
    end
    xlabel('$t$ (years)','fontsize',22,'interpreter','latex')
    ylabel('$H_t$, $P_t$','fontsize',22,'interpreter','latex')
    legend('Hosts','Parasitoids','location','Northeast')
    if i == 1
        text(.01,.9,['Weak Refuge - Limit Cycle ($\alpha = $'...
             num2str(alpha) ')'],'fontsize',22,'interpreter','latex',...
             'units','normalized')
    end
    if i == 2
        text(.2,.1,['Strong Refuge - Stable ($\alpha = $'...
            num2str(alpha) ')'],'fontsize',22,'interpreter','latex',...
            'units','normalized')
    end
    grid on
    grid minor
    
end