function [Cx, Cy] = circle(Xc, Yc, R)
    
    theta = 0:0.01:2*pi;
    Cx = Xc+R*cos(theta);
    Cy = Yc+R*sin(theta);

end