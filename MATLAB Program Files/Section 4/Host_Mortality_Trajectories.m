%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides a trajectory of the host mortality semi-discrete model
% for several values of the lumped parameter z. 
% (This file creates the right panel of Figure 12 of Section 4.2)
clear all, close all, clc

% Parameter Vector: 
z_vec = [.8 .5 .23];

% Create three trajectories using a for loop:
for i = 1:3
    
    % Parameters:
    c = .1;
    z = z_vec(i);
    k = 1;
    R = 2;
    T = 1;
    
    cd = z*c*k;
    
    % Number of years:
    N = 50;
    
    % Escape responses:
    f = @(H,P) exp(-c*P*T)./(1+cd*R*H*(-exp(-c*P*T)+1)/c/P);
    g = @(H,P) P./z.*log(1+cd*R*H*(1-exp(-c*P*T))/c/P);
    
    % Initial populations:
    H0 = 5;
    P0 = 8;
    
    % Vector initialization and tracjectory for loop:
    H = [H0 zeros(1,N-1)];
    P = [P0 zeros(1,N-1)];
       
    % Function iteration to create the trajectory:
    for t = 1:N
        H(t+1) = R*H(t)*f(H(t),P(t));
        P(t+1) = g(H(t),P(t));        
    end
    
    % Plot:
    figure(1)
    subplot(3,1,i)
    plot(0:N,H,'r-o','linewidth',3)
    hold on
    plot(0:N,P,'b-o','linewidth',3)
    set(gca,'fontsize',15)
    if i ==1
        title('Trajectories of Host Mortality Model','fontsize',25,...
            'interpreter','latex')
    end
    xlabel('$t$ (years)','fontsize',22,'interpreter','latex')
    ylabel('$H_t$, $P_t$','fontsize',22,'interpreter','latex')
    legend('Hosts','Parasitoids','location','Northwest','fontsize',22,...
           'interpreter','latex')
    grid on
    grid minor
    hold on
    
end