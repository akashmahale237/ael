clc;
clear all;
for i=1:1:5
frequency=input('Enter Frequency of operation in MHz: ');
dist=10:10:100
f=20*log10(frequency);
freespace=32.44+f+(20*log10(dist));
disp('Free Space Propagation loss for the given distance in dB');
disp(freespace);
xlabel('Distance in Km');
ylabel('Free space Propagation Loss in dB')
title("Free Space Propagation Loss")
plot(dist,freespace);
end

