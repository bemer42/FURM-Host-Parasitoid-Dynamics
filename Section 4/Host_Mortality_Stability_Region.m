%% The Mathematics of Host-Parsitoid Population Dynamics:
% This file provides the stability region in (R,z) space for the host
% mortality semi-discrete model. 
% (This file creates the left panel of Figure 12 of Section 4.2)
clear all, close all, clc

% Parameter Vectors: 
N = 100;
R_vec  = linspace(1.01,5,N);

% Loop through values of R and solve for z*:
for i = 1:length(R_vec)
    R = R_vec(i);   

    % Define equation to be solved: 
    f = @(z) R.*(log(R)-z)./(R-exp(z))-z-1;

    % Define guess: 
    z_guess = .5*log(R);
    
    % Solve for alpha^*
    options = optimset('MaxFunEvals',1e6,'MaxIter',1e4,'TolFun',1e-6);
    z_star(i) = fsolve(f,z_guess,options);

end

% Plot boundary curves:
figure(1)
plot(R_vec,log(R_vec),'k-','linewidth',3)
hold on
plot(R_vec,z_star,'k-.','linewidth',3)
set(gca,'fontsize',18)
title('Host Mortality Stability Region','fontsize',25,...
      'interpreter','latex')
xlabel('$R$ (viable eggs per adult host)','fontsize',22,...
       'interpreter','latex')
ylabel('$z = c_d/kc$ (relative strength of host mortality to parasitism)',...
       'fontsize',22,'interpreter','latex')
legend('$z = \ln(R)$','$z = z^*$','fontsize',22,'interpreter','latex')  
text(.5,.5,'No-Parasitoid Equilibrium','units','normalized','fontsize',22,...
     'interpreter','latex')
text(.5,.6,'Stable Coexistence','units','normalized','fontsize',22,...
     'interpreter','latex')
text(.5,.7,'Bounded Oscillations','units','normalized','fontsize',22,...
     'interpreter','latex')
grid on 
grid minor