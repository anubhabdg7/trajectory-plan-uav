clc;
clear;
close all;
tic

%% Problem Definition
[typeOfFunction] = 'T1';
nodes=10;
Instance = UAV(typeOfFunction, nodes);  %{'Ackley_10','Griewangk_10',
% 'Griewangk_2','Rastrigin_10','Rosenbrock_10','Rosenbrock_2',
% 'Rosenbrock_4','Goldstein','Martin','Shekel_5','Easom','Schaffer_6',
% 'Schwefel_1.2','Sphere','Axis','Sum_diff_pow','Beale','Colville',
% 'Hartmann_1','Hartmann_2', 'Levy','Matyas','Perm','Zakharov',
% 'Schwefel_2.22','Schwefel_2.21', 'Quartic','Kowalik','Shekel_7',
% 'Shekel_10','Tripod','DeJong_2','Dejong_4', 'Alpine','Pathological',
% 'Masters','Step','6humpCamelBack', 'Michalewicz_5','Michalewicz_10',
% 'Branin','Weierstrass', 'Trid','Powell','MovedHyper'}

Dims = nodes;
ObjFunction = @(x) COST(x, Instance); % Objective Function
VarSize = [1 Dims]; % Decision Variables Matrix Size
xVarMin = Instance.xmin; % Decision Variables Lower Bound
xVarMax = Instance.xmax;% Decision Variables Upper Bound
yVarMin = Instance.ymin;
yVarMax = Instance.ymax;
rangex = xVarMax-xVarMin;
rangey=yVarMax-yVarMin;

%% Bees Algorithm Parameters
n = 30; m = 20; e = 5; nep = 40; nsp = 30; ngh = 0.1;

MaxEval = 1000000; accuracy = 0.001;
MaxIt = 200;

%% Initialization
Unknown_Patch.Position.x = [];
Unknown_Patch.Position.y=[];
Unknown_Patch.Cost = [];
Unknown_Patch.counter = [];
Unknown_Patch.Sol=[];
Scout = repmat(Unknown_Patch,n,1);
counter = 0;
% Generate Initial Solutions
for i = 1:n
    Scout(i).Position.x = unifrnd(xVarMin,xVarMax,VarSize);
    Scout(i).Position.y = unifrnd(yVarMin,yVarMax,VarSize);
    [Scout(i).Cost, Scout(i).Sol] = ObjFunction(Scout(i).Position);
    counter = counter+1;
    Scout(i).counter = counter;
end

%% Sites Selection 
[~, RankOrder] = sort([Scout.Cost]);
Patch = Scout(RankOrder);
BestSol.Cost = inf;

%% Bees Algorithm Local and Global Search
for it = 1:MaxIt
    if counter >= MaxEval
        break;
    end
    % Lokal Search elite
    for i = 1:e
        bestWorker.Cost = inf;
        for j = 1:nep
            Worker.Position.x = Foraging (Patch(i).Position.x,ngh,xVarMax,xVarMin);
            Worker.Position.y = Foraging (Patch(i).Position.y,ngh,yVarMax,yVarMin);
            [Worker.Cost, Worker.Sol] = ObjFunction(Worker.Position);
            counter = counter+1;
            Worker.counter = counter;
            if Worker.Cost < bestWorker.Cost
                bestWorker = Worker;
            end
        end
        if bestWorker.Cost < Patch(i).Cost
            Patch(i) = bestWorker;
        end
    end
    % Lokal Search selected non-elite
    for i = e+1:m
        bestWorker.Cost = inf;
        for j = 1:nsp
            Worker.Position.x = Foraging (Patch(i).Position.x,ngh,xVarMax,xVarMin);
            Worker.Position.y = Foraging (Patch(i).Position.y,ngh,yVarMax,yVarMin);
            [Worker.Cost, Worker.Sol] = ObjFunction(Worker.Position);
            counter = counter+1;
            Worker.counter = counter;
            if Worker.Cost < bestWorker.Cost
                bestWorker = Worker;
            end
        end
        if bestWorker.Cost < Patch(i).Cost
            Patch(i) = bestWorker;
        end
    end
    % Global Search
    for i = m+1:n
        Patch(i).Position.x = unifrnd(xVarMin,xVarMax,VarSize);
        Patch(i).Position.y = unifrnd(yVarMin,yVarMax,VarSize);
        [Patch(i).Cost, Patch(i).Sol] = ObjFunction(Patch(i).Position);
        counter = counter+1;
        Patch(i).counter = counter;
    end
    % SORTING
    [~, RankOrder] = sort([Patch.Cost]);
    Patch = Patch(RankOrder);
    % Update Best Solution Ever Found
    OptSol = Patch(1);
    if OptSol.Cost < BestSol.Cost
        BestSol = OptSol;
    end
    % taking of result
    OptCost(it) = BestSol.Cost;
    Counter(it) = counter;
    Time(it) = toc;
    % Display Iteration Information
    disp(['Iteration ' num2str(it) ': Best Cost = ' num2str(OptCost(it)) ' --> Time = ' num2str(Time(it)) ' seconds' '; Fittness Evaluations = ' num2str(Counter(it))]);
    
    figure(1);
    Plotting(OptSol.Sol,Instance);
    pause(0.01);
    %if(abs(Instance.optima-BestSol.Cost) <= accuracy) 
     %   break;
    %end
end
%% Results
figure;
semilogy(OptCost,'LineWidth',2);
xlabel('Iteration');
ylabel('Best Cost');