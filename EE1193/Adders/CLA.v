module fa(output wire s, cout, input wire a, b, cin);
    assign s = a ^ b ^ cin;
    assign cout = (a & b) | (b & cin) | (cin & a);
endmodule


module halfadder (output wire sum, output wire carry, input wire x, input wire y);
	assign sum = x ^ y;
	assign carry = x & y;
endmodule


module mux (output wire o,input wire a,b,sel);
	assign o = (~sel&a) | (sel&b);
endmodule
	
	
module final(output wire [15:0] z, output wire cout, input wire [15:0] x,y, input wire cin);
	wire sel[3:0];
	wire psum[15:0];
	wire pcarry[3:0];
	wire v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12;
	wire c[4:0];
	assign cout = c[4];
	
	fa p1_s1(psum[0],q1,x[0],y[0],1'b0);
    fa p1_s2(psum[1],q2,x[1],y[1],q1);
    fa p1_s3(psum[2],q3,x[2],y[2],q2);
    fa p1_s4(psum[3],pcarry[0],x[3],y[3],q3);
    
    fa p2_s1(psum[4],q4,x[4],y[4],1'b0);
    fa p2_s2(psum[5],q5,x[5],y[5],q4);
    fa p2_s3(psum[6],q6,x[6],y[6],q5);
    fa p2_s4(psum[7],pcarry[1],x[7],y[7],q6);
    
    fa p3_s1(psum[8],q7,x[8],y[8],1'b0);
    fa p3_s2(psum[9],q8,x[9],y[9],q7);
    fa p3_s3(psum[10],q9,x[10],y[10],q8);
    fa p3_s4(psum[11],pcarry[2],x[11],y[11],q9);
    
    fa p4_s1(psum[12],q10,x[12],y[12],1'b0);
    fa p4_s2(psum[13],q11,x[13],y[13],q10);
    fa p4_s3(psum[14],q12,x[14],y[14],q11);
    fa p4_s4(psum[15],pcarry[3],x[15],y[15],q12);
    
    and (sel[0],psum[0],psum[1],psum[2],psum[3]);
    and (sel[1],psum[4],psum[5],psum[6],psum[7]);
    and (sel[2],psum[11],psum[10],psum[9],psum[8]);
    and (sel[3],psum[12],psum[13],psum[14],psum[15]);
    
    
    mux m1(c[1],pcarry[0],c[0],sel[0]);
	mux m2(c[2],pcarry[1],c[1],sel[1]);
	mux m3(c[3],pcarry[2],c[2],sel[2]);
	mux m4(c[4],pcarry[3],c[3],sel[3]);
	
	halfadder h1(z[0],v1,psum[0],cin);
	halfadder h2(z[1],v2,psum[1],v1);
	halfadder h3(z[2],v3,psum[2],v2);
	halfadder h4(z[3],v4,psum[3],v3);
	
	halfadder h5(z[4],v5,psum[4],c[1]);
	halfadder h6(z[5],v6,psum[5],v5);
	halfadder h7(z[6],v7,psum[6],v6);
	halfadder h8(z[7],v8,psum[7],v7);
	
	halfadder h9(z[8],v9,psum[8],c[2]);
	halfadder h10(z[9],v10,psum[9],v9);
	halfadder h11(z[10],v11,psum[10],v10);
	halfadder h12(z[11],v12,psum[11],v11);
	
	halfadder h13(z[12],v13,psum[12],c[3]);
	halfadder h14(z[13],v14,psum[13],v13);
	halfadder h15(z[14],v15,psum[14],v14);
	halfadder h16(z[15],c[4],psum[15],v15);
		
endmodule
