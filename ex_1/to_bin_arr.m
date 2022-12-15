function arr = to_bin_arr(num, len)
    binstr = dec2bin(num);
    arr = str2num(binstr(:));
    if length(arr) < len
        arr = cat(1, zeros(len - length(arr), 1), arr);
    end
end

