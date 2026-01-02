%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file constructs the Jury functions as functions of R for the
% Nicholson-Bailey model and plots them versus R.  The output is a graph
% that shows how the first two Jury functions are positive and the last
% Jury function is negative.  This shows that the coexistence fixed point
% of the Nicholson-Bailey is linearly unstable. 
% (This file creates the right panel of Figure 6 in Section 2.2.)
clear all, close all, clc

% Discretizing R space: 
R = linspace(1,7,1e4);

% Jury functions:
J1 = @(R) log(R);
J2 = @(R) 2 + log(R).*(R+1)./(R-1);
J3 = @(R) 1 - log(R).*R./(R-1);

% Plot: 
figure(1)
plot(R,J1(R),'k','linewidth',5)
hold on
plot(R,J2(R),'r','linewidth',5)
plot(R,J3(R),'b','linewidth',5)
set(gca,'fontsize',18)
title('Stability Analysis of N-B Model','fontsize',25,...
      'interpreter','latex')
xlabel('$R$ (viable eggs per adult host)','fontsize',22,'interpreter',...
       'latex')
ylabel('Jury Functions','fontsize',22,'interpreter','latex')
legend('Jury 1','Jury 2','Jury 3','location','Northwest','interpreter',...
       'latex','fontsize',22)
grid on
grid minor