cwnorm;
deleteall;

buffer_array = linspace(0,1.0E-06,101);

um = 1E-06;

offset = 0.1 * um;
res = 4;

metaheight = 	0.15 * um;
metacenter = 	0;
period = 		0.368 * um;
ylength = 		1 * um;
fillfactor =	0.86;
charge_T = 		0;
wg_T = 		0.1 * um;
AlOx_T = 		0.05 * um;
optbuffer_T = 	0.24 * um;
Au_T = 		0.075 * um;
Bottom_T = 		0.02 * um;
Top_T = 		0.005 * um;
sub_T = 		3 * um;
ncover = 		1.00 ;
ngrating = 		2.0 ;
nalox = 		1.6 ;
nsub = 		1.45;

wavelength_center = 635E-09;
wavelength_span = 40E-09;

height = metaheight + Au_T + optbuffer_T + sub_T;
monitorZ = 0.7E-06 - metaheight;
sourceZ = 0.5E-06 - metaheight;

GMRM_build_script;
save('testing22');
run;
        
Ez = getdata('R','Ez');
f = getdata('R','f');
Ez = pinch(Ez(1,1,1,:));

monitorZ = 0.7E-06 - metaheight;
sourceZ = 0.5E-06 - metaheight;

k0 = 2*pi*f/c;
#Ez1 = Ez*(-1i*k0*(monitorZ+sourceZ));
Ez1=Ez*exp(-1i*k0*(monitorZ+sourceZ));
Ez_field = Ez*(-1i*k0*(monitorZ+sourceZ));

phase = unwrap(angle(Ez));
phase2 = unwrap(angle(Ez_field));
R = abs(Ez1)^2;
wav = c/f * 1E9;

plot(wav,phase,'Wavelength (nm)', 'Phase (rad)');
#holdon;
#plot(wav,phase2, 'Wavelength (nm)', 'Phase (rad)');
#holdoff;
plot(wav,R,'Wavelength (nm)', 'Refl');
#str = num2str(wav)+", "+num2str(phase);
    
#write("data\refl\reflection"+num2str(label)+".txt","Refl");
#write("data\refl\reflection"+num2str(label)+".txt",num2str(R));
    
#write("data\wav\wavelength.txt","Wav");
#write("data\wav\wavelength.txt",num2str(wav));     
    
#write("data\phase\phase"+num2str(label)+".txt","Phase");
#write("data\phase\phase"+num2str(label)+".txt",num2str(phase));
    
    switchtolayout;
    newproject;