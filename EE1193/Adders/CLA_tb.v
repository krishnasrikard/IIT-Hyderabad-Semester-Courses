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
		{A, B} = {16'b0000000100000011, 16'b0000000100000011};
		#10;
		{A, B} = {16'b0000011000000111, 16'b0000110000000001};
		#10;
		{A, B} = {16'b0001010000000101, 16'b0001100000001001};
		#10;
		{A, B} = {16'b0001000000001101, 16'b0011100000011101};
	 end
   
   
  wire [15:0] Z;
  wire C1;
  final fa(Z, C1, A, B, C);
  
  
  initial
    begin
        $monitor("At time %t, %b	%b 		%b		%b  %b", $time, C1, Z, A, B, C);
    end

	initial 
		begin
			$dumpfile("CLA.vcd");
			$dumpvars;
		end
endmodule

