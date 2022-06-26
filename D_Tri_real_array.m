function [ M ] = D_Tri_real_array(k,t,b,baris,kolom)
    M=zeros(baris,kolom);
    for i=1:baris
        for j=1:kolom
            M(i,j)=D_Tri_real(k,t,b);
        end
    end
     
end
