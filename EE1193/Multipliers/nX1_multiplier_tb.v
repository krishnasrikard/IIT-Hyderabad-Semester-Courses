module test;
  localparam width = 4;
  wire [width:0] s;
  reg [width-1:0] x,u;
  wire cout;
  reg b,d;
  reg clk,reset;

	initial begin 
        d = 1; 
        clk = 0;
        u = 4'b0110;
    end
    
    always #10 clk = ~clk;
    
    initial begin
        $dumpfile("nX1_multiplier.vcd");
        $dumpvars;
    end
  
  nX1_multiplier wa (s,x,u,d,b);

	initial begin // stimulus
		x = 4'b1100;b = 1;
		@(posedge clk)
		x = 4'b1000;b = 0;
		@(posedge clk)
		x = 4'b1011;b = 0;
		@(posedge clk)
		x = 4'b1001;b = 1;
		$finish;
    end

	initial begin
        $monitor("At time %t,  %b	%b  %b  %b %b", $time,s,x,b,u,d);
	end
	
endmodule // test


