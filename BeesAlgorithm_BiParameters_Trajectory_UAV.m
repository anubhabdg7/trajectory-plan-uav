clc;
clear;
close all;
tic
%% Problem Definition
nodes= 10;

[typeOfFunction] = 'T1';
Instance=UAV(typeOfFunction, nodes);
ObjFunction=@(x) COST (x,Instance);    % Cost Function
VarMin.x=Instance.xmin;           % Lower Bound of Variables
VarMax.x=Instance.xmax;           % Upper Bound of Variables
VarMin.y=Instance.ymin;           % Lower Bound of Variables
VarMax.y=Instance.ymax;           % Upper Bound of Variables
rangex=(VarMax.x-VarMin.x)/4;
rangey=(VarMax.y-VarMin.y)/4;
%% Bees Algorithm Parameters
MaxEval = 500000;
n=7;                                
nep=10;                             
Shrink =0.8;
stlim=5;
accuracy=0.001;
recruitment = round(linspace(nep,1,n));
assigntment = linspace(0,1,n);
ColonySize = sum(recruitment);        
MaxIt=50; 
%% Initialization
Empty_patch.Position=[];
Empty_patch.Cost=[];
Empty_patch.Sol=[];
Empty_patch.Size=[];
Empty_patch.Stagnated =[];
Empty_patch.counter=[];
Patch=repmat(Empty_patch,n,1);
counter=0;
% Generate Initial Solutions
for i=1:n
    if i > 1
        Patch(i).Position.x=unifrnd(VarMin.x,VarMax.x,1,nodes);
    	Patch(i).Position.y=unifrnd(VarMin.y,VarMax.y,1,nodes);
    else
        xx = linspace(Instance.xs, Instance.xt, Instance.n+2);
        yy = linspace(Instance.ys, Instance.yt, Instance.n+2);
        Patch(i).Position.x = xx(2:end-1);
        Patch(i).Position.y = yy(2:end-1);
    end
    [Patch(i).Cost,Patch(i).Sol] = ObjFunction(Patch(i).Position);
    Patch(i).Size = [rangex rangey];
    Patch(i).Stagnated = 0;
    counter=counter+1;
    Patch(i).counter= counter;
end

size = linspace(0,1,n);

%% Sites Selection 
[~, RankOrder]=sort([Patch.Cost]);
Patch=Patch(RankOrder);

P=1;
%% Bees Algorithm Local and Global Search
for it=1:MaxIt
    if counter >= MaxEval
        break;
    end

    % All Sites (Exploitation and Exploration)
    for i=1:n

        bestnewbee.Cost=inf;

        assigntment=D_Tri_real_array(0,size(i),1,1,recruitment(i));
        %disp([size(i)]);
        

        for j=1:recruitment(i)
            
            if P==1
                ForagerBees.Position.x= Integrated_Foraging_stlim_all(Patch(i).Position.x,assigntment(j),VarMax.x,VarMin.x,Patch(i).Size(1));
                ForagerBees.Position.y= Integrated_Foraging_stlim_all(Patch(i).Position.y,assigntment(j),VarMax.y,VarMin.y,Patch(i).Size(2));
            else
                ForagerBees.Position.x= Integrated_Foraging_stlim(Patch(i).Position.x,assigntment(j),VarMax.x,VarMin.x,Patch(i).Size(1));
                ForagerBees.Position.y= Integrated_Foraging_stlim(Patch(i).Position.y,assigntment(j),VarMax.y,VarMin.y,Patch(i).Size(2));
            end
            [ForagerBees.Cost,ForagerBees.Sol] = ObjFunction(ForagerBees.Position);
            ForagerBees.Size= Patch(i).Size;
            ForagerBees.Stagnated = Patch(i).Stagnated;
            counter=counter+1;
            ForagerBees.counter= counter;
            if ForagerBees.Cost<bestnewbee.Cost
                bestnewbee=ForagerBees;
            end
        end

        if bestnewbee.Cost<Patch(i).Cost
            Patch(i)=bestnewbee;
            Patch(i).Stagnated=0;
        else
            Patch(i).Stagnated=Patch(i).Stagnated+1;
            Patch(i).Size=Patch(i).Size*Shrink;
        end
        

        %site abandonment procedure
        if(Patch(i).Stagnated>stlim)
            Patch(i)=Patch(end);
            Patch(i).Size=[rangex rangey];
            Patch(i).Stagnated=0;
            P=P*-1;
        end
        

    end

    % SORTING
    [~, RankOrder]=sort([Patch.Cost]);
    Patch=Patch(RankOrder);

    % Update Best Solution Ever Found
    OptSol=Patch(1);
    
    % taking of result
    OptCost(it)=OptSol.Cost;
    optCost = zeros(MaxIt+1,1);
    optCost(1)=inf;
    optCost(it+1)=OptCost(it); %buat check dibuat it+1
    Counter(it)=counter;
    Time(it)=toc;
    
    if OptSol.Sol.IsFeasible
        Flag=' *';
    else
        Flag=[', Violation = ' num2str(OptSol.Sol.Violation)];
    end
    disp(['Iteration ' num2str(it) ': Best Cost = ' num2str(OptCost(it)) Flag ' --> Time = ' num2str(Time(it))]);
    
    % Plot Solution
    figure(1);
    Plotting(OptSol.Sol,Instance);
    pause(0.01);

end

%% Results
figure;
plot(OptCost,'LineWidth',2);
xlabel('Iteration');
ylabel('Best Cost');
grid on;
