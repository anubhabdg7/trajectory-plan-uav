function y = Foraging (patchPosition, ngh, upper, lower)
 
    nVar = numel (patchPosition);
    
    k = randi ([1 nVar]);
       
    y = patchPosition;

    y(k) = y(k) + ngh * ((-1)^randi(2)) * (upper-lower);

    y(y>upper) = upper;
    y(y<lower) = lower;
    
end
