function Plotting(sol,model)

    xs=model.xs;
    ys=model.ys;
    xt=model.xt;
    yt=model.yt;
    xobs=model.xobs;
    yobs=model.yobs;
    robs=model.robs;
    
    XS=sol.XS;
    YS=sol.YS;
    xx=sol.xx;
    yy=sol.yy;
    
    %importfile('Indo.png')
    %imshow(Indo)
        
    theta=linspace(0,2*pi,100);
    for k=1:numel(xobs)
        %fill(xobs(k)+robs(k)*cos(theta),yobs(k)+robs(k)*sin(theta),[0 1 0]);
        fill(xobs(k)+robs(k)*cos(theta),yobs(k)+robs(k)*sin(theta),[0 1 0],'FaceColor','b','FaceAlpha',.1,'EdgeAlpha',.1);
        hold on;
    end
    %I = imread('Indo2.png'); 
    %h = image([0,2*xlim],[-ylim,ylim],I); 
    %uistack(h,'bottom')

    
    
    plot(xx,yy,'k','LineWidth',2);
    plot(XS,YS,'ro');
    plot(xs,ys,'bs','MarkerSize',12,'MarkerFaceColor','y');
    %plot(xt,yt,'kp','MarkerSize',16,'MarkerFaceColor','g');
    plot(xt,yt,'bs','MarkerSize',12,'MarkerFaceColor','g');
    hold off;
    grid on;
    axis equal;
    
%     I = imread('Pulau_seribu.png'); 
%     h = image(xlim,ylim,I); 
%     uistack(h,'bottom')
end