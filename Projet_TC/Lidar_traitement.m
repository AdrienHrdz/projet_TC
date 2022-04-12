close all;
clear variables;
clc;

%% Variables globales

sigma = 0.05; % Largeur d'une ligne
d = 0.01;      % Rayon max dans lequel se trouvent 2 points d'une même ligne
n = 10;       % Nbs de points minimum dans une ligne
gamma = 0.04; % Difference accepté pour regrouper 2 lignes

%% Récupération des données

%Ouvre le fichier texte
[fid, message]=fopen("RPLIDAR.txt","r");
%enlève les 3 premieres lignes du fichier
for i=1:3
    fgetl(fid);
end

[A,count]=fscanf(fid,'%g%g%g',[3 inf]); %sépare les données en 3 colonnes
A(3,:)=[];%supprime la ligne qualité
disp(A);%affichage matrice angle-distance

%% Changement de bases

X=A(2,:).*cos(A(1,:).*(pi/180))./1000;
Y=A(2,:).*sin(A(1,:).*(pi/180))./1000;

points = [X;Y];

%% Traçage de lignes
k = 1;
lines = [];

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
        lines = cat(1, lines, [line(1,:); line(end,:)]);
   end
end

%% Affichage
scatter(X, Y); hold on;
uhuh = size(lines);

for i = 0:length(lines)/2 - 1
    plot(lines(1+2*i:2*(i+1),1), lines(1+2*i:2*(i+1), 2));

end

status=fclose(fid); %ferme fichier