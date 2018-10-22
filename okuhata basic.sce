clc;
clear all
d1=input("Enter Distance: ")
if d1>10 then:
	hre=input('Enter the receiver antenna height 3m < hre< 10m : ');    	 
	for i=1:1:5
    	frequency=input('Enter Frequency of operation in MHz: ');
    	dist=10:1:100
    	f=20*log10(frequency);
    	Lo=(32.45+ 20*log10(dist)+20*log10(f)-((1.1* log10(f) -0.7) * hre -(1.56* log10 (f) -0.8)));
    	disp('Okumura propagation  for the given distance in dB');
    	disp(Lo);
    	xlabel('Distance in Km');
    	ylabel('Loss in dB')
    	title('Okumura Model')
    	plot(dist,Lo);
	end
else
	ht=input('Enter height of antenna: ');
	for i=1:1:5
    	frequency=input('Enter Frequency of operation in MHz: ');
    	d=10:1:100
    	f=20*log10(frequency);
    	hata=69.55 + (26.16*log(f))-(13.28*log(ht)) + (44.9 - 6.55*log(ht))*log(d)
    	xlabel('Distance in Km');
    	ylabel('Loss in dB')
    	title('Hata Model')
    	plot(d,hata);
	end
end
