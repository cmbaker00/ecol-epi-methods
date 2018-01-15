function convert_csv()
files = dir;
fnames = {files.name};
for i = 1:length(fnames)
    cname = fnames{i};
    if length(cname) > 3 && strcmp(cname(end-2:end),'xls')
        single_file(cname)
    end
end

end

function single_file(fname)
[~,~,r] = xlsread(fname);

xlswrite([fname(1:end-3),'csv'],r)


end