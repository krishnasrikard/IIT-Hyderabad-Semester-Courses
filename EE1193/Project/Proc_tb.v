module test;
 
  localparam width = 32;
  wire [7:0] y;
  reg [width-1:0] x;
   initial 
		begin
			x = 152654;
			#10;
			x = 83164;
			#10;
			x = 974949;
			#10;
			x = 316161;
		end
 

	Project r1(y,x);
  
  
  initial
    begin
        $monitor("At time %t, %b  %b", $time, y, x);
    end

	initial 
		begin
			$dumpfile("Project.vcd");
			$dumpvars;
		end
endmodule


