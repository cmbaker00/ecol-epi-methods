method_vec = {'adaptive','adaptive_control','costben','ensemble','ethics','ibm','optim','sdm','SDP','voi'};
method_vec = {'ethics','optim','costben','voi','adaptive','ibm','adaptive_control','ensemble','sdm','SDP'};

method_vec = {'ethics','optim','costben','voi','adaptive','ibm','sdm','ensemble'};

% method = 'ethics';
method = method_vec{4}
ff = [method,'_fisheries.xls'];
[fnum,fstr,fraw] = xlsread(ff);
fc = [method,'_cons.xls'];
[cnum,cstr,craw] = xlsread(fc);
fe = [method,'_epi.xls'];
[enum,estr,eraw] = xlsread(fe);

cons_total = 44703;
fisheries_total = 119246;
epi_total = 517428;

%%
threshold = 10;
close all
figure(1)

eyears = enum(7:end,7);
fyears = fnum(7:end,7);
cyears = cnum(7:end,7);

ecites = enum(7:end,21:end);
cite_yr = enum(6,21:end);

[eyr,ebdata] = create_bar_data(eyears);
% ebdata = ebdata/epi_total;
cum_ebdata = cumsum(ebdata);
e_start = eyr(find(cum_ebdata >= threshold,1));
% ebdata = log10(ebdata);
[fyr,fbdata] = create_bar_data(fyears);
% fbdata = fbdata/fisheries_total;
cum_fbdata = cumsum(fbdata);
f_start = fyr(find(cum_fbdata >= threshold,1));
% fbdata = log10(fbdata);
[cyr,cbdata] = create_bar_data(cyears);
% cbdata = cbdata/cons_total;
cum_cbdata = cumsum(cbdata);
c_start = cyr(find(cum_cbdata >= threshold,1));
% cbdata = log10(cbdata);

if length(eyr) > length(fyr) && length(eyr) > length(cyr)
    fyr = eyr;
    cyr = eyr;
    
    fbdata = [zeros(1,length(fyr)-length(fbdata)),fbdata];
    cbdata = [zeros(1,length(cyr)-length(cbdata)),cbdata];
else
    if length(fyr) > length(eyr) && length(fyr) > length(cyr)
        eyr = fyr;
        cyr = fyr;
        
        ebdata = [zeros(1,length(eyr)-length(ebdata)),ebdata];
        cbdata = [zeros(1,length(cyr)-length(cbdata)),cbdata];
    else
        eyr = cyr;
        fyr = cyr;
        
        fbdata = [zeros(1,length(fyr)-length(fbdata)),fbdata];
        ebdata = [zeros(1,length(eyr)-length(ebdata)),ebdata];
    end
end


xmin = min([eyr,fyr,cyr])-.5;
xmax = max([eyr,fyr,cyr])+.5;
% ymax = max([ebdata,fbdata,cbdata]);
subplot(3,1,1)
bar(eyr,ebdata)
hold on
try
plot([e_start,e_start],ylim,'r','linewidth',2)
end
ylabel('Epi')
title(method)
xlim([xmin,xmax])
% ylim([0,ymax])
subplot(3,1,2)
bar(fyr,fbdata)
hold on
try
plot([f_start,f_start],ylim,'r','linewidth',2)
end
ylabel('Fisheries')
xlim([xmin,xmax])
% ylim([0,ymax])
subplot(3,1,3)
bar(cyr,cbdata)
hold on
try
plot([c_start,c_start],ylim,'r','linewidth',2)
end
ylabel('Conservation')
xlim([xmin,xmax])
% ylim([0,ymax])


%% 
intro_data = zeros(length(method_vec),3);
for i = 1:length(method_vec)

method = method_vec{i}
ff = [method,'_fisheries.xls'];
[fnum,fstr,fraw] = xlsread(ff);
fc = [method,'_cons.xls'];
[cnum,cstr,craw] = xlsread(fc);
fe = [method,'_epi.xls'];
[enum,estr,eraw] = xlsread(fe);

cons_total = 44703;
fisheries_total = 119246;
epi_total = 517428;


eyears = enum(7:end,7);
fyears = fnum(7:end,7);
cyears = cnum(7:end,7);

ecites = enum(7:end,21:end);
cite_yr = enum(6,21:end);

[eyr,ebdata] = create_bar_data(eyears);
% ebdata = ebdata/epi_total;
cum_ebdata = cumsum(ebdata);
e_start = eyr(find(cum_ebdata >= threshold,1));
if isempty(e_start)
    e_start = nan;
end
% ebdata = log10(ebdata);
[fyr,fbdata] = create_bar_data(fyears);
% fbdata = fbdata/fisheries_total;
cum_fbdata = cumsum(fbdata);
f_start = fyr(find(cum_fbdata >= threshold,1));
if isempty(f_start)
    f_start = nan;
end
% fbdata = log10(fbdata);
[cyr,cbdata] = create_bar_data(cyears);
% cbdata = cbdata/cons_total;
cum_cbdata = cumsum(cbdata);
c_start = cyr(find(cum_cbdata >= threshold,1));
if isempty(f_start)
    f_start = nan;
end
% cbdata = log10(cbdata);

try
intro_data(i,:) = [e_start,f_start,c_start];
catch
    intro_data(i,:) = nan;
end
end
%%
figure(2)
plot(intro_data,'.','MarkerSize',40)
set(gca,'XTickLabel',method_vec)
rotateXLabels(gca,-15)
legend('Epidemiology','Fisheries','Conservation','Location','NorthWest')