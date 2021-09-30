//Turns LED on and off
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>

int main (void) {
	
	/* 
	- Arduino boards have a LED at PB5
	- Set PB5, pin 13 of arduino as output
	*/
	DDRB |= ((1 << DDB5));
	
	PORTB = ((1 <<  PB5));
	_delay_ms(2000);
	PORTB = ((0 <<  PB5));
	_delay_ms(2000);
	
	int a = 24;
	int b = 92;

	while (a > 1 && b > 1 && a != b){
		if (a > b){
			a = a-b;
		}
		else{
			b = b-a;
		}
		// printf("a = %d, b = %d\n", a, b);
		
		PORTB = ((1 <<  PB5));
		_delay_ms(500);
		PORTB = ((0 <<  PB5));
		_delay_ms(500);
	}
	

	// GCD is a or b
	if (a == b){
		// printf("gcd = %d\n", a);

		PORTB = ((1 <<  PB5));
		_delay_ms(5000);
		PORTB = ((0 <<  PB5));
		_delay_ms(5000);
	}

	// GCD is b
	if (a == 1 && b != 1){
		// printf("gcd = %d\n", b);
		
		PORTB = ((1 <<  PB5));
		_delay_ms(10000);
		PORTB = ((0 <<  PB5));
		_delay_ms(10000);
	}

	// GCD is a
	if (a != 1 && b == 1){
		// printf("gcd = %d\n", a);
		
		PORTB = ((1 <<  PB5));
		_delay_ms(15000);
		PORTB = ((0 <<  PB5));
		_delay_ms(15000);
	}
	PORTB = ((1 <<  PB5));

	return 0;
}
