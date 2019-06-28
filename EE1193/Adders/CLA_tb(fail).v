module test;
 
  localparam width = 16;
  reg [width-1:0] A, B;
  reg C;
 
  initial 
	begin
		C = 1'b0;
	end

   initial 
	 begin
		{A, B} = {16'b0000000000000011, 16'b0000000000001000};
		#10;
		{A, B} = {16'b0000000000000011, 16'b0000000000000011};
		#10;
		{A, B} = {16'b0000000000000111, 16'b0000000000000001};
		#10;
		{A, B} = {16'b0000000000000101, 16'b0000000000001001};
		#10;
		{A, B} = {16'b0000000000001101, 16'b0000000000011101};
	 end
   
   
  wire [3:0] Z4, Z3, Z2, Z1;
  wire C1;
  final fa(Z4, Z3, Z2, Z1, C1, A, B, C);
  
  
  initial
    begin
        $monitor("At time %t, %b  %b %b %b %b        %b        %b  %b", $time, C1, Z4, Z3, Z2, Z1, A, B, C);
    end

	initial 
		begin
			$dumpfile("final.vcd");
			$dumpvars;
		end
endmodule

