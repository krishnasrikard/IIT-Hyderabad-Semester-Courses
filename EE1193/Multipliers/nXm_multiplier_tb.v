module test;
  localparam width1 = 4;
  localparam width2 = 3;
  reg [width1-1:0] x,u;
  reg [width2-1:0] y,v;
  wire [width1 + width2 - 1:0] s;
  wire cout;
  reg clk,reset;

	initial begin 
        v = 3'b100; 
        u = 4'b0110;
        clk = 0;
    end
        
    always #10 clk = ~clk;
    
    initial begin
        $dumpfile("nXm_multiplier.vcd");
        $dumpvars;
    end
  
  nXm_multipler #(.width1(width1), .width2(width2)) nm (s,x,u,y,v);

	initial begin
		x = 4'b1100;y = 3'b100;
		@(posedge clk)
		x = 4'b1000;y = 3'b110;
		@(posedge clk)
		x = 4'b1011;y = 3'b101;
		@(posedge clk)
		x = 4'b1001;y = 3'b111;
		$finish;
    end

	initial begin
        $monitor("At time %t,  %b %b	%b  %b  %b %b", $time,cout,s,x,y,u,v);
	end
	
endmodule


