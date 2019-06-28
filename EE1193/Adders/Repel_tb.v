module test;
 
  localparam width = 8;
  reg [width-1:0] A, B;
  reg C;
 
  initial 
	begin
		C = 1'b0;
	end

   initial 
	 begin
		{A, B} = {8'b00000110, 8'b10000000};
		#10;
		{A, B} = {8'b00111111, 8'b00100001};
		#10;
		{A, B} = {8'b01000011, 8'b11110001};
		#10;
		{A, B} = {8'b00000101, 8'b10011111};
		#10;
		{A, B} = {8'b11000001, 8'b11000001};
	 end
   
   
  wire [7:0] S;
  wire C1;
  Repel rl(C1, S, A, B, C);
  
  
  initial
    begin
        $monitor("At time %t, %b    %b      %b  %b  %b", $time, C1, S, A, B, C);
    end

	initial 
		begin
			$dumpfile("Repel.vcd");
			$dumpvars;
		end
endmodule

