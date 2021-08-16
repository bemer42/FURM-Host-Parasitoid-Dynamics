%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides plots the stability region in (R,alpha) space for the
% host refuge model.
% (This file creates the left panel of Figure 7 of Section 2.3)
clear all, close all, clc

% Parameter Vectors:
N = 100;
R_vec  = linspace(1.01,5,N);
a_star = zeros(size(R_vec));

% Loop through values of R and solve for alpha*:
for i = 1:length(R_vec)
    R = R_vec(i);
    
    % Define equation to be solved:
    f = @(a) (1-a.*R).*R./(R-1).*log((1-a).*R./(1-a.*R)) - 1;
    
    % Define guess:
    a_guess = .9/R;
    
    % Solve for alpha^*
    options = optimset('MaxFunEvals',1e6,'MaxIter',1e4,'TolFun',1e-6);
    a_star(i) = fsolve(f,a_guess,options);
    
end

% Plot boundary curves:
figure(1)
plot(R_vec,1./R_vec,'k-','linewidth',3)
hold on
plot(R_vec,a_star,'k-.','linewidth',3)
set(gca,'fontsize',18)
title('Host Refuge Stability Region','fontsize',25,...
      'interpreter','latex')
xlabel('$R$ (viable eggs per adult host)','fontsize',22,'interpreter','latex')
ylabel('$\alpha$ (strength of host refuge)','fontsize',22,'interpreter','latex')
legend('$\alpha = 1/R$','$\alpha = \alpha^*$','interpreter','latex')
text(.5,.5,'Bounded Oscillations','units','normalized','fontsize',22,...
     'interpreter','latex')
text(.5,.6,'Stable Equilibrium','units','normalized','fontsize',22,...
     'interpreter','latex')
text(.5,.7,'Unbounded Solutions','units','normalized','fontsize',22,...
     'interpreter','latex')
grid on
grid minor