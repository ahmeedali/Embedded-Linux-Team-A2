/**********************************************
 * 				DIO_INTERFACE.h
 *
 * 		 Created on: Feb 22, 2023
 *      Author: Muhammad Abdel Aziz
 ********************************************/


#ifndef MCAL_DIO_INTERFACE_H_
#define MCAL_DIO_INTERFACE_H_
#include "DIO_REG.h"
#include "../../LIB/calcBit.h"

#define PORTA 	0
#define PORTB 	1
#define PORTC 	2
#define PORTD 	3

#define PIN0	0
#define PIN1	1
#define PIN2	2
#define PIN3	3
#define PIN4	4
#define PIN5	5
#define PIN6	6
#define PIN7	7


//enum {PORTA,PORTB,PORTC,PORTD}; //PORTS
//enum {PIN0,PIN1,PIN2,PIN3,PIN4,PIN5,PIN6,PIN7}; //PINS 0->7
enum {LOW,HIGH}; // DIGITAL VALUES
enum {IN,OUT}; //PINS DIRECTIONS

void DIO_vSetPinDirection(uint8 Copy_u8PORT, uint8 Copy_u8PinNumber, uint8 copy_u8state);
void DIO_vSetPortDirection(uint8 Copy_u8PORT,uint8 copy_u8state);
void DIO_vWritePin(uint8 Copy_u8PORT,uint8 Copy_u8PinNumber, uint8 Copy_u8value);
void DIO_vWritePort(uint8 Copy_u8PORT,uint8 Copy_u8value);
void DIO_vTogglePin(uint8 Copy_u8PORT, uint8 Copy_u8PinNumber);
void DIO_vTogglePort(uint8 Copy_u8PORT);
void DIO_vWritePortValue(uint8 Copy_u8PORT,uint8 Copy_u8value);
uint8 DIO_u8GetPinValue(uint8 Copy_u8PORT,uint8 Copy_u8PinNumber);

#endif
