classdef UAV
    
    properties
        type;                  % type of fitness function 
        xs;       
        ys;
        xt;
        yt;
        xobs;
        yobs;
        robs;
        tobs;
        n;
        xmin;
        xmax;
        ymin;
        ymax;
        definedFunctions       % functions defined in this class
    end
    
    methods
        %This function are for global minimum but in this context, it's for
        %maximum global (min(f(x)=optima(-f(x)))
        function obj = UAV(typeOfFunction,n)
            obj.definedFunctions={'T1','T2','T3'};
            obj.type=typeOfFunction;
            obj.n=n;
            switch(obj.type)
                case 'T1',
                    %n = n;
                    xs = 10;
                    ys = 10;
                    xt = 55;
                    yt= 100;
                    xobs=[45 12 32 36 55];
                    yobs=[52 40 68 26 80];
                    robs=[10 10 8 12 9];
                    tobs=[2 10 1 2 3];
                    %tobs=[0 0 0 0 0];
                    xmin=0;
                    xmax= 100;
                    ymin=0;
                    ymax= 100;
                    obj.xs = xs;
                    obj.ys = ys;
                    obj.xt = xt;
                    obj.yt= yt;
                    obj.xobs = xobs ;
                    obj.yobs = yobs ;
                    obj.robs = robs ;
                    obj.tobs = tobs ;
                    obj.xmin=xmin;
                    obj.xmax=xmax;
                    obj.ymin=ymin;
                    obj.ymax=ymax;
                case 'T2',
                    %n = n;
                    xs=11;
                    ys=11;
                    xt=75;
                    yt=75;
                    xobs=[52 32 12 36 80 63 50 30];
                    yobs=[52 40 48 26 60 56 42 70];
                    robs=[10 10 8 12 9 7 10 10];
                    tobs=[2 10 1 2 3 5 2 4];
                    xmin=0;
                    xmax= 100;
                    ymin=0;
                    ymax= 100;
                    obj.xs = xs;
                    obj.ys = ys;
                    obj.xt = xt;
                    obj.yt= yt;
                    obj.xobs = xobs ;
                    obj.yobs = yobs ;
                    obj.robs = robs ;
                    obj.tobs = tobs ;
                    obj.xmin=xmin;
                    obj.xmax=xmax;
                    obj.ymin=ymin;
                    obj.ymax=ymax;
                case 'T3',
                    %n = n;
                    xs=0;
                    ys=0;
                    xt=100;
                    yt=100;
                    xobs=[30 50 65 0 50 75 100 50];
                    yobs=[20 15 55 24 80 90 70 36];
                    robs=[10 21 10 17 12 10 20 11];
                    tobs=[5 5 5 5 5 5 5 5];
                    xmin=0;
                    xmax= 100;
                    ymin=0;
                    ymax= 100;
              otherwise,
                disp('fitness function not defined');
             end
        end
        
        
    end
end

