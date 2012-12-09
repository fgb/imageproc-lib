/*
 * Signatures for interrupt handlers
 *
 * Created on 2009-4-8 by AMH, fgb
 */

#ifndef __INTERRUPTS_H
#define __INTERRUPTS_H

void __attribute__((__interrupt__, no_auto_psv)) _AddressError(void);

#endif // __INTERRUPTS_H
