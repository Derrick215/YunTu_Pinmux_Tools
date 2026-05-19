# YTM32B1LE0x_PINMUX_V1.0

## IOMUX

| NAME | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 | ALT6 | ALT7 | 48LQFP | 32QFN | 32LQFP | 64LQFP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PTD_1 |  | PTD_1 | eTMR0_CH3 | SPI1_SIN |  | I2C1_SCL |  | TMU_OUT2 | 1 |  | 1 | 1 |
| PTD_0 |  | PTD_0 | eTMR0_CH2 | SPI1_SCK |  | I2C1_SDA |  | TMU_OUT1 | 2 |  | 2 | 2 |
| PTE_11 |  | PTE_11 | SPI2_PCS0 | lpTMR0_ALT1 |  |  |  | TMU_OUT5 |  |  |  | 3 |
| PTE_10 |  | PTE_10 | CLKOUT | SPI2_PCS1 |  |  |  | TMU_OUT4 |  |  |  | 4 |
| PTE_5 |  | PTE_5 | TCLK_IN2 |  | eTMR1_CH1 | CAN0_TX |  |  | 3 | 1 |  | 5 |
| PTE_4 |  | PTE_4 | CLKOUT |  | eTMR1_CH0 | CAN0_RX |  |  | 4 | 2 |  | 6 |
| VDD | VDD |  |  |  |  |  |  |  | 5 | 3 | 3 | 7 |
| VDDA | VDDA |  |  |  |  |  |  |  | 6 |  | 4 | 8 |
| VREFH | VREFH |  |  |  |  |  |  |  |  |  |  | 9 |
| VREFL | VREFL |  |  |  |  |  |  |  |  |  | 5 |  |
| VSS | VSS |  |  |  |  |  |  |  | 7 | 4 | 6 | 10 |
| PTB_7 | EXTAL | PTB_7 | I2C0_SCL |  | UART2_TX |  |  | TMU_OUT2 | 8 | 5 | 7 | 11 |
| PTB_6 | XTAL | PTB_6 | I2C0_SDA |  | UART2_RX |  |  | TMU_OUT1 | 9 | 6 | 8 | 12 |
| PTE_3 |  | PTE_3 | eTMR0_FLT0 | SPI1_SIN |  |  | TMU_IN6 | ACMP0_OUT |  |  |  | 13 |
| PTD_16 | EXTAL32K | PTD_16 | eTMR0_CH1 |  | SPI0_SIN | ACMP0_ACTIVE |  |  | 10 | 7 |  | 14 |
| PTD_15 | XTAL32K | PTD_15 | eTMR0_CH0 |  | SPI0_SCK |  |  |  | 11 | 8 |  | 15 |
| PTE_9 |  | PTE_9 | eTMR0_CH7 | SPI1_SCK |  |  |  |  | 12 |  |  | 16 |
| PTE_8 | ACMP0_IN3 | PTE_8 | eTMR0_CH6 |  |  |  |  |  | 13 | 9 |  | 17 |
| PTB_5 |  | PTB_5 | eTMR0_CH5 | SPI0_PCS1 | SPI0_PCS0 | CLKOUT | TMU_IN0 |  | 14 | 10 | 9 | 18 |
| PTB_4 |  | PTB_4 | eTMR0_CH4 | SPI0_SOUT |  |  | TMU_IN1 |  | 15 | 11 | 10 | 19 |
| PTC_3 | ADC0_SE11/ACMP0_IN4 | PTC_3 | eTMR0_CH3 | CAN0_TX | UART0_TX |  |  |  | 16 | 12 | 11 | 20 |
| PTC_2 | ADC0_SE10/ACMP0_IN5 | PTC_2 | eTMR0_CH2 | CAN0_RX | UART0_RX |  |  |  | 17 | 13 | 12 | 21 |
| PTD_7 | ACMP0_IN6 | PTD_7 | UART2_TX | eTMR0_CH3 |  |  |  |  |  |  |  | 22 |
| PTD_6 | ACMP0_IN7 | PTD_6 | UART2_RX | eTMR0_CH2 |  |  |  |  |  |  |  | 23 |
| PTD_5 |  | PTD_5 |  | lpTMR0_ALT2 |  |  | TMU_IN7 |  | 18 | 14 |  | 24 |
| PTC_1 | ADC0_SE9 | PTC_1 | eTMR0_CH1 | SPI2_SOUT | SPI2_SIN |  | eTMR1_CH7 |  | 19 |  | 13 | 25 |
| PTC_0 | ADC0_SE8 | PTC_0 | eTMR0_CH0 | SPI2_SIN | SPI2_PCS1 |  | eTMR1_CH6 |  |  |  | 14 | 26 |
| PTC_17 | ADC0_SE15 | PTC_17 | eTMR1_FLT3 |  | SPI2_PCS2 |  |  |  |  |  |  | 27 |
| PTC_16 | ADC0_SE14 | PTC_16 | eTMR1_FLT2 |  | SPI2_SCK |  |  |  | 20 |  |  | 28 |
| PTC_15 | ADC0_SE13 | PTC_15 | eTMR1_CH3 | SPI2_SCK | SPI2_SOUT |  | TMU_IN8 |  | 21 |  |  | 29 |
| PTC_14 | ADC0_SE12 | PTC_14 | eTMR1_CH2 |  | SPI2_PCS0 |  | TMU_IN9 |  | 22 |  |  | 30 |
| PTB_3 | ADC0_SE7 | PTB_3 | eTMR1_CH1 | SPI0_SIN | eTMR1_QD_PHA |  | TMU_IN2 |  | 23 | 15 | 15 | 31 |
| PTB_2 | ADC0_SE6 | PTB_2 | eTMR1_CH0 | SPI0_SCK | eTMR1_QD_PHB |  | TMU_IN3 |  | 24 | 16 | 16 | 32 |
| PTB_1 | ADC0_SE5 | PTB_1 | UART0_TX | SPI0_SOUT | TCLK_IN0 | CAN0_TX |  |  | 25 | 17 | 17 | 33 |
| PTB_0 | ADC0_SE4 | PTB_0 | UART0_RX | SPI0_PCS0 | lpTMR0_ALT3 | CAN0_RX |  |  | 26 | 18 | 18 | 34 |
| PTC_9 |  | PTC_9 | UART1_TX | eTMR1_FLT1 |  |  | UART0_RTS |  | 27 |  |  | 35 |
| PTC_8 |  | PTC_8 | UART1_RX | eTMR1_FLT0 |  |  | UART0_CTS |  | 28 |  |  | 36 |
| PTA_7 | ADC0_SE3 | PTA_7 | eTMR0_FLT2 |  | RTC_CLKIN |  | UART1_RTS |  | 29 | 19 | 19 | 37 |
| PTA_6 | ADC0_SE2 | PTA_6 | eTMR0_FLT1 | SPI1_PCS1 |  |  | UART1_CTS |  |  |  | 20 | 38 |
| PTE_7 |  | PTE_7 | eTMR0_CH7 | SPI1_PCS2 |  |  |  |  |  |  |  | 39 |
| VSS | VSS |  |  |  |  |  |  |  | 30 | 20 |  | 40 |
| VDD | VDD |  |  |  |  |  |  |  | 31 | 21 |  | 41 |
| PTB_13 |  | PTB_13 | eTMR0_CH1 |  |  |  |  |  | 32 |  |  | 42 |
| PTB_12 |  | PTB_12 | eTMR0_CH0 |  |  |  |  |  |  |  |  | 43 |
| PTD_4 |  | PTD_4 | eTMR0_FLT3 |  |  |  |  |  |  |  |  | 44 |
| PTD_3 |  | PTD_3 |  | SPI1_PCS0 | I2C1_SCL | eTMR2_CH0 | TMU_IN4 | CORE_NMI_b | 33 | 22 | 21 | 45 |
| PTD_2 |  | PTD_2 |  | SPI1_SOUT | I2C1_SDA | eTMR2_CH1 | TMU_IN5 |  | 34 |  | 22 | 46 |
| PTA_3 |  | PTA_3 | eTMR2_CH0 | I2C0_SCL | SPI2_SCK |  | UART0_TX |  | 35 | 23 | 23 | 47 |
| PTA_2 |  | PTA_2 | eTMR2_CH1 | I2C0_SDA | SPI2_SIN |  | UART0_RX |  | 36 | 24 | 24 | 48 |
| PTA_1 | ADC0_SE1/ACMP0_IN1 | PTA_1 | eTMR1_CH1 |  | SPI2_SOUT | eTMR1_QD_PHA | UART0_RTS | TMU_OUT0 | 37 | 25 | 25 | 49 |
| PTA_0 | ADC0_SE0/ACMP0_IN0 | PTA_0 | eTMR1_CH0 |  | SPI2_PCS0 |  | UART0_CTS | TMU_OUT3 | 38 | 26 | 26 | 50 |
| PTC_7 |  | PTC_7 | UART1_TX |  | SPI2_PCS1 | CAN0_TX | eTMR1_QD_PHA |  | 39 |  | 27 | 51 |
| PTC_6 |  | PTC_6 | UART1_RX |  |  | CAN0_RX | eTMR1_QD_PHB |  | 40 |  | 28 | 52 |
| PTE_6 |  | PTE_6 | SPI0_PCS2 |  |  |  | UART1_RTS |  |  |  |  | 53 |
| PTE_2 |  | PTE_2 | SPI0_SOUT | lpTMR0_ALT3 |  |  | UART1_CTS |  |  |  |  | 54 |
| PTA_13 |  | PTA_13 | eTMR1_CH7 |  |  | UART2_TX |  |  | 41 |  |  | 55 |
| PTA_12 |  | PTA_12 | eTMR1_CH6 |  |  | UART2_RX |  |  | 42 |  |  | 56 |
| PTA_11 |  | PTA_11 | eTMR1_CH5 |  | I2C1_SCL | ACMP0_ACTIVE |  |  | 43 | 27 |  | 57 |
| PTA_10 |  | PTA_10 | eTMR1_CH4 |  | I2C1_SDA |  |  |  | 44 | 28 |  | 58 |
| PTE_1 |  | PTE_1 | SPI0_SIN |  | I2C1_SCL | SPI1_PCS0 | eTMR1_FLT1 |  |  |  |  | 59 |
| PTE_0 |  | PTE_0 | SPI0_SCK | TCLK_IN1 | I2C1_SDA | SPI1_SOUT | eTMR1_FLT2 |  |  |  |  | 60 |
| PTC_5 |  | PTC_5 | eTMR2_CH0 | RTC_CLKOUT | eTMR1_CH1 |  |  |  | 45 | 29 | 29 | 61 |
| PTC_4 | ACMP0_IN2 | PTC_4 | eTMR1_CH0 | RTC_CLKOUT |  |  | eTMR1_QD_PHB | SWD_CLK | 46 | 30 | 30 | 62 |
| PTA_5 |  | PTA_5 |  | TCLK_IN1 |  |  |  | RCU_RESET_b | 47 | 31 | 31 | 63 |
| PTA_4 |  | PTA_4 |  |  | ACMP0_OUT |  |  | SWD_IO | 48 | 32 | 32 | 64 |
