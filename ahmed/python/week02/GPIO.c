#include "avr/io.h"
        void Init_PORTA_GPIO(void)
        {
            DDRA = 0b11110011;
        }