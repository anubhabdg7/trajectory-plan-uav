function y=Integrated_Foraging_stlim_all(x,ass,Vmx,Vmn,size)
    r=ass*size;
    
    nVar=numel(x);
    
    pert=randi([0 1], 1, nVar);
    
    y=x; 
    
    y = y + (random('unif',-r,r).*pert);
    y(y>Vmx)=Vmx;
    y(y<Vmn)=Vmn;
    
end