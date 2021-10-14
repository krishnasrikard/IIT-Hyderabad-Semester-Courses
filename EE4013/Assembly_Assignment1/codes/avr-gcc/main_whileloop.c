//Turns LED on and off
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include "sevenseg.h"
#include "lcd.h"

int main (void) {
	
	/* 
	- Arduino boards have a LED at PB5
	- Set PB5, pin 13 of arduino as output
	
	DDRB |= ((1 << DDB5));
	PORTB = ((1 <<  PB5));
	_delay_ms(2000);
	PORTB = ((0 <<  PB5));
	_delay_ms(2000);
	*/

	// Using PortB for LCD interface
	DDRB = 0xFF; // 1111.1111; set PB0-PB7 as outputs	 
	LCD_Init(); // Initializing LCD controller
	
	int a = 24;
	int b = 92;

	while (a > 1 && b > 1 && a != b){
		if (a > b){
			a = a-b;
		}
		else{
			b = b-a;
		}
		
		/*
		// Observing the process using just blink
		PORTB = ((1 <<  PB5));
		_delay_ms(500);
		PORTB = ((0 <<  PB5));
		_delay_ms(500);
		*/
	}
	

	// GCD is a or b
	if (a == b){
		// For using LCD
		LCD_Clear();
		LCD_Integer(a);
		
		/* 
		// For using 7-Segment Display
		while(a){
			c = a%10;
			a = a/10;
			sevenseg(c);
			_delay_ms(500);
		}		
		*/

		/*
		// Observing results using just blink
		PORTB = ((1 <<  PB5));
		_delay_ms(5000);
		PORTB = ((0 <<  PB5));
		_delay_ms(5000);
		*/
	}

	// GCD is b
	if (a == 1 && b != 1){
		// For using LCD
		LCD_Clear();
		LCD_Integer(b);
		
		/*
		// For using 7-Segment Display
		while(b){
			c = b%10;
			b = b/10;
			sevenseg(c);
			_delay_ms(500);
		}
		*/
		
		/*
		// Observing results using just blink
		PORTB = ((1 <<  PB5));
		_delay_ms(10000);
		PORTB = ((0 <<  PB5));
		_delay_ms(10000);
		*/
	}

	// GCD is a
	if (a != 1 && b == 1){
		// For using LCD
		LCD_Clear();
		LCD_Integer(a);

		/*
		// For using 7-Segment Display
		while(a){
			c = a%10;
			a = a/10;
			sevenseg(c);
			_delay_ms(500);
		}
		*/
		
		/*
		// Observing results using just blink
		PORTB = ((1 <<  PB5));
		_delay_ms(15000);
		PORTB = ((0 <<  PB5));
		_delay_ms(15000);
		*/
	}
	
	return 0;
}
