function [ angka ] = D_Tri_real(k,t,b)
%disp(t);
m=randi([1 10]);
    a=(t-k)/10;
    b=(b-t)/10;
    switch m
        case 1
            angka=lapis1(t,a,b);
        case 2
            angka=lapis2(t,a,b);
        case 3
            angka=lapis3(t,a,b);
        case 4
            angka=lapis4(t,a,b);
        case 5
            angka=lapis5(t,a,b);
        case 6
            angka=lapis6(t,a,b);
        case 7
            angka=lapis7(t,a,b);
        case 8
            angka=lapis8(t,a,b);
        case 9
            angka=lapis9(t,a,b);
        case 10
            angka=lapis10(t,a,b);
    end
end

function angka=lapis1(t,a,b)
    angka=unifrnd((t-a),(t+b),1);
end

function angka=lapis2(t,a,b)
    angka=unifrnd((t-2*a),(t+2*b),1);
end

function angka=lapis3(t,a,b)
    angka=unifrnd((t-3*a),(t+3*b),1);
end

function angka=lapis4(t,a,b)
    angka=unifrnd((t-4*a),(t+4*b),1);
end

function angka=lapis5(t,a,b)
    angka=unifrnd((t-5*a),(t+5*b),1);
end

function angka=lapis6(t,a,b)
    angka=unifrnd((t-6*a),(t+6*b),1);
end

function angka=lapis7(t,a,b)
    angka=unifrnd((t-7*a),(t+7*b),1);
end

function angka=lapis8(t,a,b)
    angka=unifrnd((t-8*a),(t+8*b),1);
end

function angka=lapis9(t,a,b)
    angka=unifrnd((t-9*a),(t+9*b),1);
end

function angka=lapis10(t,a,b)
    angka=unifrnd((t-10*a),(t+10*b),1);
end