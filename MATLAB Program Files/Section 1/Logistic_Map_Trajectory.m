%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides several time-series trajectories of the logistic map
% for six different initial conditions.  Each trajectory is attracted to
% the nontrivial fixed point.  
% (This file creates Figure 2 of Section 1.3.)
clear all, close all, clc

% Create a vector of six different initial conditions:
x0_vec = linspace(0.05,0.9,6);

% Create a string array of colors:
Color  = {'m','r','g','c','b','k'};

% Loop through the six initial conditions, plotting the trajectory for each
% iteration: 
for i = 1:length(x0_vec)
    % Parameter:
    r = 2;
    
    % Number of years:
    N = 10;
    
    % Logistic map function:
    f = @(x) r.*x.*(1-x);
    
    % Initial populations:
    x0 = x0_vec(i);
    
    % Vector initialization and tracjectory for loop:
    x = [x0 zeros(1,N-1)];
    
    for t = 1:N
        x(t+1) = r.*x(t).*(1-x(t));
    end
    
    % Plot:
    figure(1)
    plot(0:N,x,'-o','linewidth',3,'Color',Color{i})
    set(gca,'fontsize',18)
    title('Trajectories of the Logistic Map','fontsize',28,...
        'interpreter','latex')
    xlabel('$t$','fontsize',22,'interpreter','latex')
    ylabel('$x_t$','fontsize',22,'interpreter','latex')
    legend('$x_0=.05$','$x_0=.22$','$x_0=.39$','$x_0=.56$','$x_0=.73$',...
           '$x_0=.90$','interpreter','latex','fontsize',22)
    ylim([0 1])
    hold on

end

% Apply grid lines to the figure:
grid on
grid minor