function [x,y] = create_bar_data(data)
dmin = min(data);
dmax = max(data);
x = dmin:dmax;
y = zeros(size(x));

for i = 1:length(x)
    y(i) = sum(data==x(i));
end


end