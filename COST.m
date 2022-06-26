function [z,sol] = COST(sol1,model)
    %beta=100;
    x=sol1.x;
    y=sol1.y;
    
    xs=model.xs;
    ys=model.ys;
    xt=model.xt;
    yt=model.yt;
    tobs=model.tobs;
    xobs=model.xobs;
    yobs=model.yobs;
    robs=model.robs;
    lambda=0.5;
    
    
    XS=[xs x xt];
    YS=[ys y yt];

    k=numel(XS);
    TS=linspace(0,1,k);
    
    tt=linspace(0,1,102);
    xx=spline(TS,XS,tt);
    yy=spline(TS,YS,tt);
    %tt1=linspace(0,1,5);
    %xx1=spline(TS,XS,tt1);
    %yy1=spline(TS,YS,tt1);

    xx1=[xs,xx(17),xx(34),xx(51),xx(68),xx(85),xt];
    yy1=[ys,yy(17),yy(34),yy(51),yy(68),yy(85),yt];
    dx=diff(xx);
    dy=diff(yy);
    dx1=diff(xx(1:17));
    dx2=diff(xx(17:34));
    dx3=diff(xx(34:51));
    dx4=diff(xx(51:68));
    dx5=diff(xx(68:85));
    dx6=diff(xx(85:102));

    dy1=diff(yy(1:17));
    dy2=diff(yy(17:34));
    dy3=diff(yy(34:51));
    dy4=diff(yy(51:68));
    dy5=diff(yy(68:85));
    dy6=diff(yy(85:102));
    
    L=sum(sqrt(dx.^2+dy.^2));
    l1=sum(sqrt(dx1.^2+dy1.^2));
    l2=sum(sqrt(dx2.^2+dy2.^2));
    l3=sum(sqrt(dx3.^2+dy3.^2));
    l4=sum(sqrt(dx4.^2+dy4.^2));
    l5=sum(sqrt(dx5.^2+dy5.^2));
    l6=sum(sqrt(dx6.^2+dy6.^2));
    length=[l1,l2,l3,l4,l5,l6];
    nobs = numel(xobs); 
    Violation = 0;
    cost=(1-lambda)*L;
    
    for j=2:7

        newx=linspace(xx1(j-1),xx1(j),7);
        newy=linspace(yy1(j-1),yy1(j),7);
        sum1=0;
        flag=0;


        

        for k=1:nobs
            
            d1=(((newx(2)-xobs(k)).^2+(newy(2)-yobs(k)).^2)^2);
            d2=(((newx(3)-xobs(k)).^2+(newy(3)-yobs(k)).^2)^2);
            d3=(((newx(4)-xobs(k)).^2+(newy(4)-yobs(k)).^2)^2);
            d4=(((newx(5)-xobs(k)).^2+(newy(5)-yobs(k)).^2)^2);
            d5=(((newx(6)-xobs(k)).^2+(newy(6)-yobs(k)).^2)^2);
            temp=((1/d1)+(1/d2)+(1/d3)+(1/d4)+(1/d5))*tobs(k);
            sum1=sum1+temp;
            if d1<robs(k)^4
                flag=flag+1;
            end
            if d2<robs(k)^4
                flag=flag+1;
            end
            if d3<robs(k)^4
                flag=flag+1;
            end
            if d4<robs(k)^4
                flag=flag+1;
            end
            if d5<robs(k)^4
                flag=flag+1;
            end


            %v=max(1-d/robs(k),0);
            %Violation=Violation+mean(v);
        end

        if flag>0

            cost=cost+(lambda)*(length(j-1).^2)*(sum1/5.00);
        end

    end
    
    sol.TS=TS;
    sol.XS=XS;
    sol.YS=YS;
    sol.tt=tt;
    sol.xx=xx;
    sol.yy=yy;
    sol.dx=dx;
    sol.dy=dy;
    sol.L=L;
    sol.Violation=0;
    sol.IsFeasible=(Violation==0);
    
    %z=sol.L*(1+beta*sol.Violation);
    z=cost;
    
end