//Turns LED on and off
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include "sevenseg.h"
#include "lcd.h"

int GCD_Subtraction(int x, int y){
	if ((x == 1) || (y == 1)) return 1;
	if (x == y) return x;
	if (x > y) return GCD_Subtraction(x-y, y);
	if (x < y) return GCD_Subtraction(x, y-x);
}

int main (void) {
	
	// Using PortB for LCD interface
	DDRB = 0xFF; // 1111.1111; set PB0-PB7 as outputs	 
	LCD_Init(); // Initializing LCD controller
	
	int o = GCD_Subtraction(15,255);
	LCD_Clear();
	LCD_Integer(o);

	return 0;
}
