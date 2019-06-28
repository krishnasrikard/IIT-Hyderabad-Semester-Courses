module xin (output wire [7:0] storage, input wire [7:0] s,input wire clk);
integer k;
integer v;
integer t;

always @(posedge clk)
	begin
		 k=1;
		 v=7;
		 t=0;
	end

assign storage[7:0]=k;
endmodule
