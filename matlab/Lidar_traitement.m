close all;
clear variables;
clc;

%% Variables globales

sigma = 0.01; % Largeur d'une ligne
d = 0.01;      % Rayon max dans lequel se trouvent 2 points d'une même ligne
n = 10;       % Nbs de points minimum dans une ligne
gamma = 0.4; % Difference accepté pour regrouper 2 lignes

%% Récupération des données

%Ouvre le fichier texte
[fid, message]=fopen("RPLIDAR.txt","r");
%enlève les 3 premieres lignes du fichier
for i=1:3
    fgetl(fid);
end

[A,count]=fscanf(fid,'%g%g%g',[3 inf]); %sépare les données en 3 colonnes
A(3,:)=[];%supprime la ligne qualité

%% Changement de bases

X=A(2,:).*cos(A(1,:).*(pi/180))./1000;
Y=A(2,:).*sin(A(1,:).*(pi/180))./1000;

points = [X;Y];

%% Traçage de lignes
k = 1;
lines = [];
coeffsDir = [];

while(k<length(X)-1) 
   flag = true;
   line = [];
   
   while(flag && k<length(X)-1)
       
       [Cx, Cy] = circle(X(k), Y(k), d);
      % plot(Cy, Cx); hold on;
       
       if((X(k+1) - X(k))^2 + (Y(k+1) - Y(k))^2 < d^2)
           line = cat(1, line, [X(k+1), Y(k+1)]);
           
       else
           flag = false;
       end
       
       k = k + 1;
       
   end
   
   if(isempty(line) == false)
       m = (line(end, 2) - line(1, 2))/(line(end, 1) - line(1, 1)); % Coeff directeur de la ligne en cours
       coeffsDir = cat(1, coeffsDir, m);                            % Ajout du coeff dans la matrice lines
       
       lines = cat(1, lines, [line(1,:); line(end,:)]); % Ajout des coors des 2 point de la ligne dans la matrice lines
  
       
       
   end
end

% for i = 2:2:length(lines)
%     for j = 2:2:length(lines)
%        if(i ~= j && abs(coeffsDir(i/2) - coeffsDir(j/2)) < gamma ...
%                && abs(lines(i, 1) - lines(j, 1)) < gamma && abs(lines(i, 2) - lines(j, 2)) < gamma)
%            lines(i,:) = []; 
%            lines(i+1,:) = [];
% 
%        else
%        end
%     end
%    
% end

%% Affichage
for i = 0:length(lines)/2 - 1
    plot(lines(1+2*i:2*(i+1),1), lines(1+2*i:2*(i+1), 2)); hold on;
   
end

status=fclose(fid); %ferme fichier