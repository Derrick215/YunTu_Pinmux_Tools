# YTM32B1LE1x_PINMUX_V1.0

## IOMUX

| 48LQFP | 48QFN | 32QFN | TSSOP20 | NAME | Default Function | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 | ALT6 | ALT7 | Default State |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 |  |  | PTD_1 |  |  | PTD_1 | MPWM0_CH3 | SPI1_SIN |  | I2C0_SCL |  | TMU_OUT2 | Tri-State Input |
| 2 | 2 |  |  | PTD_0 |  |  | PTD_0 | MPWM0_CH2 | SPI1_SCK |  | I2C0_SDA |  | TMU_OUT1 | Tri-State Input |
| 3 | 3 | 1 | 3 | PTE_5 |  |  | PTE_5 | TCLK_IN2 |  | eTMR0_CH1 | CAN0_TX |  |  | Tri-State Input |
| 4 | 4 | 2 | 4 | PTE_4 |  |  | PTE_4 | CLKOUT |  | eTMR0_CH0 | CAN0_RX |  |  | Tri-State Input |
| 5 | 5 | 3 | 5 | VDD | VDD | VDD |  |  |  |  |  |  |  | VDD |
| 6 | 6 |  |  | VDDA | VDDA | VDDA |  |  |  |  |  |  |  | VDDA |
| 7 | 7 | 4 | 6 | VSS | VSS | VSS |  |  |  |  |  |  |  | VSS |
| 8 | 8 | 5 | 7 | PTB_7 | EXTAL | EXTAL | PTB_7 | I2C0_SCL |  | UART0_TX | SPI1_PCS3 |  | TMU_OUT2 | Tri-State Input |
| 9 | 9 | 6 | 8 | PTB_6 | XTAL | XTAL | PTB_6 | I2C0_SDA |  | UART0_RX | SPI1_PCS2 |  | TMU_OUT1 | Tri-State Input |
| 10 | 10 | 7 |  | PTD_16 |  |  | PTD_16 | MPWM0_CH1 |  | SPI0_SIN | ACMP0_ACTIVE |  |  | Tri-State Input |
| 11 | 11 | 8 |  | PTD_15 |  |  | PTD_15 | MPWM0_CH0 |  | SPI0_SCK |  |  |  | Tri-State Input |
| 12 | 12 |  |  | PTE_9 |  |  | PTE_9 | MPWM0_CH7 | SPI1_SCK |  |  |  |  | Tri-State Input |
| 13 | 13 | 9 |  | PTE_8 | ACMP0_IN3 | ACMP0_IN3 | PTE_8 | MPWM0_CH6 |  |  |  |  |  | Tri-State Input |
| 14 | 14 | 10 |  | PTB_5 |  |  | PTB_5 | MPWM0_CH5 | SPI0_PCS1 | SPI0_PCS0 | CLKOUT | TMU_IN0 | SPI1_PCS3 | Tri-State Input |
| 15 | 15 | 11 | 9 | PTB_4 |  |  | PTB_4 | MPWM0_CH4 | SPI0_SOUT |  |  | TMU_IN1 | SPI1_PCS2 | Tri-State Input |
| 16 | 16 | 12 |  | PTC_3 | ADC0_SE11/ACMP0_IN4 | ADC0_SE11/ACMP0_IN4 | PTC_3 | MPWM0_CH3 | CAN0_TX | UART0_TX |  |  |  | Tri-State Input |
| 17 | 17 | 13 |  | PTC_2 | ADC0_SE10/ACMP0_IN5 | ADC0_SE10/ACMP0_IN5 | PTC_2 | MPWM0_CH2 | CAN0_RX | UART0_RX |  |  |  | Tri-State Input |
| 18 | 18 | 14 |  | PTD_5 | ADC0_SE15 | ADC0_SE15 | PTD_5 |  | LPTMR0_ALT2 |  |  | TMU_IN7 |  | Tri-State Input |
| 19 | 19 |  |  | PTC_1 | ADC0_SE9 | ADC0_SE9 | PTC_1 | MPWM0_CH1 | SPI0_SOUT | SPI0_SIN |  | eTMR0_CH7 |  | Tri-State Input |
| 20 | 20 |  |  | PTC_16 | ADC0_SE14 | ADC0_SE14 | PTC_16 | eTMR0_FLT2 |  | SPI0_SCK |  |  |  | Tri-State Input |
| 21 | 21 |  |  | PTC_15 | ADC0_SE13 | ADC0_SE13 | PTC_15 | eTMR0_CH3 | SPI0_SCK | SPI0_SOUT |  | TMU_IN8 |  | Tri-State Input |
| 22 | 22 |  |  | PTC_14 | ADC0_SE12 | ADC0_SE12 | PTC_14 | eTMR0_CH2 |  | SPI0_PCS0 |  | TMU_IN9 |  | Tri-State Input |
| 23 | 23 | 15 | 10 | PTB_3 | ADC0_SE7 | ADC0_SE7 | PTB_3 | eTMR0_CH1 | SPI0_SIN | eTMR0_QD_PHA |  | TMU_IN2 |  | Tri-State Input |
| 24 | 24 | 16 | 11 | PTB_2 | ADC0_SE6 | ADC0_SE6 | PTB_2 | eTMR0_CH0 | SPI0_SCK | eTMR0_QD_PHB |  | TMU_IN3 |  | Tri-State Input |
| 25 | 25 | 17 | 12 | PTB_1 | ADC0_SE5 | ADC0_SE5 | PTB_1 | UART0_TX | SPI0_SOUT | TCLK_IN0 | CAN0_TX |  |  | Tri-State Input |
| 26 | 26 | 18 | 13 | PTB_0 | ADC0_SE4 | ADC0_SE4 | PTB_0 | UART0_RX | SPI0_PCS0 | LPTMR0_ALT3 | CAN0_RX |  |  | Tri-State Input |
| 27 | 27 |  |  | PTC_9 |  |  | PTC_9 | UART1_TX | eTMR0_FLT1 |  |  | UART0_RTS |  | Tri-State Input |
| 28 | 28 |  | 14 | PTC_8 | DAC0_OUT | DAC0_OUT | PTC_8 | UART1_RX | eTMR0_FLT0 |  |  | UART0_CTS |  | Tri-State Input |
| 29 | 29 | 19 |  | PTA_7 | ADC0_SE3 | ADC0_SE3 | PTA_7 |  |  |  |  | UART0_RTS |  | Tri-State Input |
| 30 | 30 | 20 |  | VSS | VSS | VSS |  |  |  |  |  |  |  | VSS |
| 31 | 31 | 21 |  | VDD | VDD | VDD |  |  |  |  |  |  |  | VDD |
| 32 | 32 |  |  | PTB_13 |  |  | PTB_13 | MPWM0_CH1 |  |  |  | UART0_CTS |  | Tri-State Input |
| 33 | 33 | 22 | 15 | PTD_3 | ADC0_SE2 | ADC0_SE2 | PTD_3 |  | SPI1_PCS0 | I2C0_SCL | MPWM0_CH0 | TMU_IN4 | CORE_NMI_b | Tri-State Input |
| 34 | 34 |  |  | PTD_2 | ACMP0_IN6 | ACMP0_IN6 | PTD_2 |  | SPI1_SOUT | I2C0_SDA | MPWM0_CH1 | TMU_IN5 |  | Tri-State Input |
| 35 | 35 | 23 | 16 | PTA_3 | ADC0_SE8/ACMP0_IN7 | ADC0_SE8/ACMP0_IN7 | PTA_3 | MPWM0_CH0 | I2C0_SCL | SPI1_SCK |  | UART0_TX |  | Tri-State Input |
| 36 | 36 | 24 | 17 | PTA_2 |  |  | PTA_2 | MPWM0_CH1 | I2C0_SDA | SPI1_SIN |  | UART0_RX |  | Tri-State Input |
| 37 | 37 | 25 | 18 | PTA_1 | ADC0_SE1/ACMP0_IN1 | ADC0_SE1/ACMP0_IN1 | PTA_1 | eTMR0_CH1 |  | SPI1_SOUT | eTMR0_QD_PHA | UART0_RTS | TMU_OUT0 | Tri-State Input |
| 38 | 38 | 26 | 19 | PTA_0 | ADC0_SE0/ACMP0_IN0 | ADC0_SE0/ACMP0_IN0 | PTA_0 | eTMR0_CH0 |  | SPI1_PCS0 |  | UART0_CTS | TMU_OUT3 | Tri-State Input |
| 39 | 39 |  |  | PTC_7 |  |  | PTC_7 | UART1_TX |  | SPI1_PCS1 | CAN0_TX | eTMR0_QD_PHA |  | Tri-State Input |
| 40 | 40 |  |  | PTC_6 |  |  | PTC_6 | UART1_RX |  |  | CAN0_RX | eTMR0_QD_PHB |  | Tri-State Input |
| 41 | 41 |  |  | PTA_13 |  |  | PTA_13 | eTMR0_CH7 |  | SPI0_PCS3 | UART1_TX |  |  | Tri-State Input |
| 42 | 42 |  |  | PTA_12 |  |  | PTA_12 | eTMR0_CH6 |  | SPI0_PCS2 | UART1_RX |  |  | Tri-State Input |
| 43 | 43 | 27 |  | PTA_11 |  |  | PTA_11 | eTMR0_CH5 | SPI0_PCS3 | I2C0_SCL | ACMP0_ACTIVE |  |  | Tri-State Input |
| 44 | 44 | 28 |  | PTA_10 |  |  | PTA_10 | eTMR0_CH4 | SPI0_PCS2 | I2C0_SDA |  |  |  | Tri-State Input |
| 45 | 45 | 29 |  | PTC_5 |  |  | PTC_5 | MPWM0_CH0 |  | eTMR0_CH1 |  |  |  | Tri-State Input |
| 46 | 46 | 30 | 20 | PTC_4 | SWD_CLK | ACMP0_IN2 | PTC_4 | eTMR0_CH0 |  |  |  | eTMR0_QD_PHB | SWD_CLK | Pull Down Input |
| 47 | 47 | 31 | 1 | PTA_5 | RCU_RESET_b |  | PTA_5 |  | TCLK_IN1 |  |  |  | RCU_RESET_b | Pull Up Input |
| 48 | 48 | 32 | 2 | PTA_4 | SWD_IO |  | PTA_4 |  |  | ACMP0_OUT |  |  | SWD_IO | Pull Up Input |

## Version

| Version | Author | Description |
| --- | --- | --- |
| V1.0 | Major Lin | Initial version. |
