/*
 * Interrupt service routines
 *
 * Created on 2009-4-2 by fgb, AMH
 */

#include "utils.h"


/******************************************************************************
 * Interrupt handlers for useful traps
 *
 * Note: Adapted from Microchip's traps.c
 */

void __attribute__((__interrupt__, no_auto_psv)) _AddressError(void)
{
        INTCON1bits.ADDRERR = 0;        //Clear the trap flags
        while(1) {
            LED_2 = ~LED_2;
            delay_ms(50);
        };
}
