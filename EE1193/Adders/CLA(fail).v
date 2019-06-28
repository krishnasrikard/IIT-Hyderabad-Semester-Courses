module fa(output wire s, cout, input wire a, b, cin);
    assign s = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (cin & a);
endmodule



module CLA (output wire [3:0] psum, output wire cout, output sel, input wire [3:0] x,y);
    
    wire q1,q2,q3;
    
    wire sel;
    
    fa p_s1(psum[0],q1,x[0],y[0],1'b0);
    fa p_s2(psum[1],q2,x[1],y[1],q1);
    fa p_s3(psum[2],q3,x[2],y[2],q2);
    fa p_s4(psum[3],cout,x[3],y[3],q3);
        
    and (sel,psum[0],psum[1],psum[2],psum[3]);
    
    
    
endmodule


module halfadder (output wire [3:0] out_sum, output wire out_carry, input [3:0] in_x, input wire in_y);
	wire [3:0] a;
	assign a[0] = in_y;
	assign a[1] = 0;
	assign a[2] = 0;
	assign a[3] = 0;
	assign out_sum = in_x ^ a;
	assign out_carry = in_x & a;

endmodule


module mux (output wire o1,input wire a1,b1,sel);
	assign o1 = (~sel&a1) | (sel&b1);
endmodule
	
	
module final(output wire [3:0] z4,z3,z2,z1, output wire v4, input wire [15:0] x,y, input wire cin);
	wire sel[3:0];
	wire psum1[3:0];
	wire psum2[3:0];
	wire psum3[3:0];
	wire psum4[3:0];
	wire pcarry[3:0];
	wire v1,v2,v3;
	wire c[4:0];
	assign cin = c[0];
	assign v4 = c[4];
	
	CLA u1(psum1[3:0],pcarry[0],sel[0],x[3:0],y[3:0]);
	CLA u2(psum2[3:0],pcarry[1],sel[1],x[7:4],y[7:4]);
	CLA u3(psum3[3:0],pcarry[2],sel[2],x[11:8],y[11:8]);
	CLA u4(psum4[3:0],pcarry[3],sel[3],x[15:12],y[15:12]);
	
	mux m1(c[1],pcarry[0],c[0],sel[0]);
	mux m2(c[2],pcarry[1],c[1],sel[1]);
	mux m3(c[3],pcarry[2],c[2],sel[2]);
	mux m4(c[4],pcarry[3],c[3],sel[3]);
	
	halfadder h1(z1[3:0],v1,psum1[3:0],c[0]);
	halfadder h2(z2[3:0],v2,psum2[3:0],c[1]);
	halfadder h3(z3[3:0],v3,psum3[3:0],c[2]);
	halfadder h4(z4[3:0],v4,psum4[3:0],c[3]);
	
endmodule
