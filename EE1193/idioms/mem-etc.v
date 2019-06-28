module memtest;

    reg [7:0] mem[0:31];
    wire [7:0] a;
    reg [7:0] b;
    integer file, i;

    initial begin
        $readmemb ("mem.txt", mem, 5);
        for(i=20; i<100; i=i+1)
            mem[i] = 32'hdead_beef;
    end
    assign a = mem[3];

    initial begin
        b = $random;
        file = $fopen("file.txt");
        $fwrite(file, "time=%t", $time);
        $fclose(file);
    end
endmodule
