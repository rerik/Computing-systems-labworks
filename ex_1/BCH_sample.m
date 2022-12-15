enc = comm.BCHEncoder(31,16,'x15+x11+x10+x9+x8+x7+x5+x3+x2+x+1');
fileID = fopen('bch_data.csv','w');
for i = 0:2^16-1
    data = to_bin_arr(i, 16);
    bch = enc(data);
    number = join(string(data), "");
    code = join(string(bch), "");
    fprintf(fileID, "%d;%s;%s\n", i, number, code);
end
fclose(fileID);