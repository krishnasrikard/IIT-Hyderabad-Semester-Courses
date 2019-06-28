module test;
  localparam width1 = 4;
  localparam width2 = 3;
  reg [3:0] x,u;
  reg [2:0] y,v;
  wire [6:0] s;
  wire cout;
  reg clk,reset;

	initial begin 
        v = 3'b010; 
        u = 4'b0110;
        clk = 0;
        reset = 0;
    end
 
    
    initial begin
        $dumpfile("nXm_multiplier.vcd");
        $dumpvars;
    end
  
  nXm_multiplier nm (s,x,u,y,v,clk,reset);

	initial begin
		x = 4'b1100;y = 3'b110;
		#10;
		x = 4'b1000;y = 3'b110;
		#10;
		x = 4'b1011;y = 3'b101;
		#10;
		x = 4'b1001;y = 3'b111;
		$finish;
    end

	initial begin
        $monitor("At time %t,  %d	%d  %d  %d %d", $time,s,x,y,u,v);
	end
	
endmodule


