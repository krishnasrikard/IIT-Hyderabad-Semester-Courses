module tb_division;
    parameter WIDTH = 8;
    // Inputs
    reg [WIDTH-1:0] A;
    reg [WIDTH-1:0] B;
    // Outputs
    wire [WIDTH-1:0] Res;
	wire [WIDTH-1:0] rem;
    // Instantiate the division module (UUT)
    division #(WIDTH) uut (
        .A(A), 
        .B(B), 
        .Res(Res),
        .rem(rem)
    );

    initial begin
        // Initialize Inputs and wait for 100 ns
        A = 0;  B = 0;  #100;  //Undefined inputs
        //Apply each set of inputs and wait for 100 ns.
        A = 100;    B = 10; #100;
        A = 200;    B = 40; #100;
        A = 90; B = 9;  #100;
        A = 70; B = 10; #100;
        A = 16; B = 3;  #100;
        A = 255;    B = 5;  #100;
    end
    initial
    begin
        $monitor("At time %t, %0d %0d %0d %0d", $time, A, B, Res,rem);
    end
      
endmodule
