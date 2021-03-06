N = 16;                  //Chip rate = As 2^4
t = 0:3*N-1;
wt = 0:0.01:1;

//bt = [-1*ones(1,N) 1*ones(1,N) -1*ones(1,N)];    //Data signal
bt = [zeros(1,N) ones(1,N) zeros(1,N)];
bt_polar = [-1*ones(1,N) ones(1,N) -1*ones(1,N)];

ct =       [0, 0 ,1,1,1,0 ,1, 0, 0,1,1,1, 0, 0,1,1, 0, 0,1, 0,1,1, 0, 0,0, 0 ,1,1,1,0 ,1, 0, 0,1,1,1, 0, 0,1,1, 0, 0,1, 0,1,1, 0, 0];     //Spreading code
ct_polar = [-1,-1,1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,1,1,-1,-1,0, 0 ,1,1,1,0 ,1, 0, 0,1,1,1, 0, 0,1,1, 0, 0,1, 0,1,1, 0, 0];     //Spreading code in polar form

//mt = bt.*ct_polar;                      //Product of chips and data bits
mt = bitxor(bt, ct);

for i = 1:length(mt)
    if mt(i) == 0 then
        mt(i) = -1;
    end
end
Carrier = 2 * cos(2*wt*2*%pi);          //Carrier Signal
st = [];
for i = 1:length(mt)
    st = [st mt(i)*Carrier];            
end

figure
subplot(3,1,1)
a=gca();
a.x_location ="origin";
a.y_location ="origin";
a.data_bounds = [0,-2;20,2];
plot2d2(t,bt_polar ,5)
xlabel('t')
title('Data b(t)')

subplot(3,1,2)
a =gca();
a.x_location ="origin";
a.y_location ="origin";
a.data_bounds = [0,-2;20,2];
plot2d2(t,ct_polar ,5)
xlabel('t')
title('Spreading code c(t)')
subplot(3,1,3)

a =gca();
a.x_location ="origin";
a.y_location ="origin";
a.data_bounds = [0,-2;20,2];
plot2d2(t,mt ,5)
xlabel('t')
title('Product Signal m(t)')

figure
subplot(3,1,1)
a =gca();
a.x_location ="origin";
a.y_location ="origin";
a.data_bounds = [0,-2;20,2];
plot2d2(t,mt ,5)
xlabel('t')
title('Product Signal m(t)')

subplot(3,1,2)
a =gca();
a.x_location ="origin";
a.y_location ="origin";
a.data_bounds = [0,-2;20,2];
plot(Carrier)
xlabel('t')
title('Carrier Signal')

subplot(3,1,3)
a =gca();
a.x_location ="origin";
a.y_location ="origin";
a.data_bounds = [0,-2;20,2];
plot(st)
xlabel('t')
title('Final carrier signal s(t)')
