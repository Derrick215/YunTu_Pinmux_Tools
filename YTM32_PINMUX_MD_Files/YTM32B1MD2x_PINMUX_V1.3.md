# YTM32B1MD2x_PINMUX_V1.3

## IOMUX

| 100LQFP | 64LQFP | 48LQFP | NAME | Default Function | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 | ALT6 | ALT7 | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | PTE_16 |  |  | PTE_16 | UART1_RTS | SPI2_SIN | MPWM0_CH7 |  |  | TMU_OUT7 |  |
| 2 |  |  | PTE_15 |  |  | PTE_15 | UART1_CTS | SPI2_SCK | MPWM0_CH6 |  |  | TMU_OUT6 |  |
| 3 | 1 | 1 | VDD15 | VDD15 | VDD15 |  |  |  |  |  |  |  | Typical Voltage:1.62V, 1uF LDO CAP needed |
| 4 | 2 | 2 | PTD_0 |  |  | PTD_0 | eTMR0_CH2 | SPI1_SCK | MPWM0_CH0 | I2C1_SDA |  | TMU_OUT1 |  |
| 5 | 3 |  | PTE_11 |  |  | PTE_11 | SPI2_PCS0 | LPTMR0_ALT1 | MPWM0_CH5 |  |  | TMU_OUT5 |  |
| 6 | 4 |  | PTE_10 |  |  | PTE_10 | CFMU_CLKOUT | SPI2_PCS1 | MPWM0_CH4 |  |  | TMU_OUT4 |  |
| 7 |  |  | PTE_13 |  |  | PTE_13 |  | SPI2_PCS2 | eTMR0_FLT0 |  |  |  |  |
| 8 | 5 | 3 | PTE_5 |  |  | PTE_5 | TCLK_IN2 | eTMR0_QD_PHA | MPWM0_CH3 | CAN0_TX | I2C0_SCL | EWDG_IN |  |
| 9 | 6 | 4 | PTE_4 |  |  | PTE_4 | eTMR0_FLT0 | eTMR0_QD_PHB | MPWM0_CH2 | CAN0_RX | I2C0_SDA | EWDG_OUT_b |  |
| 10 | 7 | 5 | VDD | VDD | VDD |  |  |  |  |  |  |  |  |
| 11 | 8 | 6 | VDDA | VDDA | VDDA |  |  |  |  |  |  |  |  |
| 12 | 9 |  | VREFH | VREFH | VREFH |  |  |  |  |  |  |  |  |
| 13 |  |  | VREFL | VREFL | VREFL |  |  |  |  |  |  |  |  |
| 14 | 10 | 7 | VSS | VSS | VSS |  |  |  |  |  |  |  |  |
| 15 | 11 | 8 | PTB_7 | EXTAL | EXTAL | PTB_7 | I2C0_SCL |  | SPI0_SCK | UART2_TX |  | TMU_OUT2 |  |
| 16 | 12 | 9 | PTB_6 | XTAL | XTAL | PTB_6 | I2C0_SDA |  | SPI0_SIN | UART2_RX |  | TMU_OUT1 |  |
| 17 |  |  | PTE_14 |  |  | PTE_14 | eTMR0_FLT1 |  | eTMR1_FLT1 |  |  |  |  |
| 18 | 13 |  | PTE_3 |  |  | PTE_3 | eTMR0_FLT0 | UART2_RTS | eTMR1_FLT0 | SPI0_SOUT | TMU_IN6 | ACMP0_OUT |  |
| 19 |  |  | PTE_12 |  |  | PTE_12 | eTMR0_FLT3 | UART2_TX |  | SPI0_PCS0 |  |  |  |
| 20 |  |  | PTD_17 |  |  | PTD_17 | eTMR0_FLT2 | UART2_RX | SPI0_PCS_COM |  |  |  |  |
| 21 | 14 | 10 | PTD_16 |  |  | PTD_16 | eTMR0_CH1 |  | SPI0_SIN | ACMP0_ACTIVE |  |  |  |
| 22 | 15 | 11 | PTD_15 |  |  | PTD_15 | eTMR0_CH0 |  | SPI0_SCK | RTC_CLKIN |  |  |  |
| 23 | 16 | 12 | PTE_9 |  |  | PTE_9 | eTMR0_CH7 | UART2_CTS | SPI0_PCS_COM |  |  |  |  |
| 24 |  |  | PTD_14 |  |  | PTD_14 | MPWM0_CH5 | UART1_TX | SPI1_PCS_COM |  |  | CFMU_CLKOUT |  |
| 25 |  |  | PTD_13 |  |  | PTD_13 | MPWM0_CH4 | UART1_RX | SPI1_PCS_COM |  |  | RTC_CLKOUT |  |
| 26 | 17 | 13 | PTE_8 | ACMP0_IN3 | ACMP0_IN3 | PTE_8 | eTMR0_CH6 |  |  | SPI0_PCS1 |  |  |  |
| 27 | 18 | 14 | PTB_5 |  |  | PTB_5 | eTMR0_CH5 | SPI0_PCS1 | SPI0_PCS0 | CFMU_CLKOUT | TMU_IN0 |  |  |
| 28 | 19 | 15 | PTB_4 |  |  | PTB_4 | eTMR0_CH4 | SPI0_SOUT |  |  | TMU_IN1 |  |  |
| 29 | 20 | 16 | PTC_3 | ADC0_SE11/ACMP0_IN4 | ADC0_SE11/ACMP0_IN4 | PTC_3 | eTMR0_CH3 | CAN0_TX | UART0_TX |  |  |  |  |
| 30 | 21 | 17 | PTC_2 | ADC0_SE10/ACMP0_IN5 | ADC0_SE10/ACMP0_IN5 | PTC_2 | eTMR0_CH2 | CAN0_RX | UART0_RX |  |  |  |  |
| 31 | 22 |  | PTD_7 | ACMP0_IN6 | ACMP0_IN6 | PTD_7 | UART2_TX | eTMR0_CH3 | eTMR0_FLT3 |  |  |  |  |
| 32 | 23 |  | PTD_6 | ACMP0_IN7 | ACMP0_IN7 | PTD_6 | UART2_RX | eTMR0_CH2 | eTMR0_FLT2 |  |  | SPI0_PCS3 |  |
| 33 | 24 | 18 | PTD_5 |  |  | PTD_5 | MPWM0_CH3 | LPTMR0_ALT2 | eTMR0_FLT1 | CFMU_CLKOUT | TMU_IN7 | SPI0_PCS1 |  |
| 34 |  |  | PTD_12 |  |  | PTD_12 | MPWM0_CH2 |  |  |  | UART2_RTS |  |  |
| 35 |  |  | PTD_11 |  |  | PTD_11 | MPWM0_CH1 | eTMR0_QD_PHA |  |  | UART2_CTS |  |  |
| 36 |  |  | PTD_10 |  |  | PTD_10 | MPWM0_CH0 | eTMR0_QD_PHB |  |  | CFMU_CLKOUT |  |  |
| 37 |  |  | VSS | VSS | VSS |  |  |  |  |  |  |  |  |
| 38 |  |  | VDD | VDD | VDD |  |  |  |  |  |  |  |  |
| 39 | 25 | 19 | PTC_1 | ADC0_SE9 | ADC0_SE9 | PTC_1 | eTMR0_CH1 | SPI2_SOUT |  |  | eTMR1_CH7 |  |  |
| 40 | 26 |  | PTC_0 | ADC0_SE8 | ADC0_SE8 | PTC_0 | eTMR0_CH0 | SPI2_SIN |  |  | eTMR1_CH6 |  |  |
| 41 |  |  | PTD_9 |  |  | PTD_9 |  |  | eTMR0_FLT3 |  | eTMR1_CH5 |  |  |
| 42 |  |  | PTD_8 |  |  | PTD_8 |  |  | eTMR0_FLT2 |  | eTMR1_CH4 |  |  |
| 43 | 27 |  | PTC_17 | ADC0_SE15 | ADC0_SE15 | PTC_17 | eTMR1_FLT3 | CAN2_TX |  | MPWM0_CH1 |  |  |  |
| 44 | 28 | 20 | PTC_16 | ADC0_SE14 | ADC0_SE14 | PTC_16 | eTMR1_FLT2 | CAN2_RX |  | MPWM0_CH0 |  |  |  |
| 45 | 29 | 21 | PTC_15 | ADC0_SE13 | ADC0_SE13 | PTC_15 | eTMR1_CH3 | SPI2_SCK |  |  | TMU_IN8 |  |  |
| 46 | 30 | 22 | PTC_14 | ADC0_SE12 | ADC0_SE12 | PTC_14 | eTMR1_CH2 | SPI2_PCS0 |  |  | TMU_IN9 |  |  |
| 47 | 31 | 23 | PTB_3 | ADC0_SE7 | ADC0_SE7 | PTB_3 | eTMR1_CH1 | SPI0_SIN | eTMR1_QD_PHA |  | TMU_IN2 |  |  |
| 48 | 32 | 24 | PTB_2 | ADC0_SE6 | ADC0_SE6 | PTB_2 | eTMR1_CH0 | SPI0_SCK | eTMR1_QD_PHB | RTC_CLKIN | TMU_IN3 |  |  |
| 49 |  |  | PTC_13 |  |  | PTC_13 | MPWM0_CH15 | MPWM0_CH7 | UART2_RTS |  |  |  |  |
| 50 |  |  | PTC_12 |  |  | PTC_12 | MPWM0_CH14 | MPWM0_CH6 | UART2_CTS |  |  |  |  |
| 51 |  |  | PTC_11 |  |  | PTC_11 | MPWM0_CH13 |  | SPI2_PCS_COM |  | TMU_IN10 |  |  |
| 52 |  |  | PTC_10 |  |  | PTC_10 | MPWM0_CH12 |  | SPI2_PCS_COM |  | TMU_IN11 |  |  |
| 53 | 33 | 25 | PTB_1 | ADC0_SE5 | ADC0_SE5 | PTB_1 | UART0_TX | SPI0_SOUT | TCLK_IN0 | CAN0_TX | LPTMR0_ALT1 |  |  |
| 54 | 34 | 26 | PTB_0 | ADC0_SE4 | ADC0_SE4 | PTB_0 | UART0_RX | SPI0_PCS0 | LPTMR0_ALT3 | CAN0_RX |  |  |  |
| 55 | 35 | 27 | PTC_9 |  |  | PTC_9 | UART1_TX | eTMR1_FLT1 | eTMR0_FLT1 |  | UART0_RTS |  |  |
| 56 | 36 | 28 | PTC_8 | DAC0_OUT | DAC0_OUT | PTC_8 | UART1_RX | eTMR1_FLT0 |  |  | UART0_CTS |  |  |
| 57 | 37 | 29 | PTA_7 | ADC0_SE3 | ADC0_SE3 | PTA_7 | eTMR0_FLT2 | SPI1_PCS3 | RTC_CLKIN |  | UART1_RTS |  |  |
| 58 | 38 |  | PTA_6 | ADC0_SE2 | ADC0_SE2 | PTA_6 | eTMR0_FLT1 | SPI1_PCS1 |  |  | UART1_CTS |  |  |
| 59 | 39 |  | PTE_7 |  |  | PTE_7 | eTMR0_CH7 | eTMR1_FLT0 |  |  |  |  |  |
| 60 | 40 | 30 | VSS | VSS | VSS |  |  |  |  |  |  |  |  |
| 61 | 41 | 31 | VDD | VDD | VDD |  |  |  |  |  |  |  |  |
| 62 |  |  | PTA_17 |  |  | PTA_17 | eTMR0_CH6 | eTMR1_FLT0 | EWDG_OUT_b |  |  |  |  |
| 63 |  |  | PTB_17 |  |  | PTB_17 | eTMR0_CH5 | SPI1_PCS3 |  |  |  |  |  |
| 64 |  |  | PTB_16 | ADC0_SE31 | ADC0_SE31 | PTB_16 | eTMR0_CH4 | SPI1_SOUT |  |  |  |  |  |
| 65 |  |  | PTB_15 | ADC0_SE30 | ADC0_SE30 | PTB_15 | eTMR0_CH3 | SPI1_SIN |  |  |  |  |  |
| 66 |  |  | PTB_14 | ADC0_SE25 | ADC0_SE25 | PTB_14 | eTMR0_CH2 | SPI1_SCK |  |  |  |  |  |
| 67 | 42 | 32 | PTB_13 | ADC0_SE24 | ADC0_SE24 | PTB_13 | eTMR0_CH1 | eTMR1_FLT1 | CAN2_TX | SPI0_PCS2 |  |  |  |
| 68 | 43 |  | PTB_12 | ADC0_SE23 | ADC0_SE23 | PTB_12 | eTMR0_CH0 | eTMR1_FLT2 | CAN2_RX | SPI0_PCS3 |  |  |  |
| 69 | 44 |  | PTD_4 | ADC0_SE22 | ADC0_SE22 | PTD_4 | eTMR0_FLT3 | eTMR1_FLT3 |  |  |  |  |  |
| 70 | 45 | 33 | PTD_3 | ADC0_SE19 | ADC0_SE19 | PTD_3 | MPWM0_CH13 | SPI1_PCS0 | I2C1_SCL | UART1_TX | TMU_IN4 | CM33_NMI_b |  |
| 71 | 46 | 34 | PTD_2 | ADC0_SE18 | ADC0_SE18 | PTD_2 | MPWM0_CH12 | SPI1_SOUT | I2C1_SDA | UART1_RX | TMU_IN5 |  |  |
| 72 | 47 | 35 | PTA_3 | ADC0_SE17 | ADC0_SE17 | PTA_3 | MPWM0_CH9 | I2C0_SCL | EWDG_IN | SPI2_SCK | UART0_TX |  |  |
| 73 | 48 | 36 | PTA_2 | ADC0_SE16 | ADC0_SE16 | PTA_2 | MPWM0_CH8 | I2C0_SDA | EWDG_OUT_b | SPI2_SIN | UART0_RX |  |  |
| 74 |  |  | PTB_11 |  |  | PTB_11 | MPWM0_CH11 |  |  |  |  |  |  |
| 75 |  |  | PTB_10 |  |  | PTB_10 | MPWM0_CH10 |  |  |  |  |  |  |
| 76 |  |  | PTB_9 |  |  | PTB_9 | MPWM0_CH9 |  |  |  |  |  |  |
| 77 |  |  | PTB_8 |  |  | PTB_8 | MPWM0_CH8 |  |  |  |  |  |  |
| 78 | 49 | 37 | PTA_1 | ADC0_SE1/ACMP0_IN1 | ADC0_SE1/ACMP0_IN1 | PTA_1 | eTMR1_CH1 | SPI2_SOUT |  | eTMR1_QD_PHA | UART0_RTS | TMU_OUT0 |  |
| 79 | 50 | 38 | PTA_0 | ADC0_SE0/ACMP0_IN0 | ADC0_SE0/ACMP0_IN0 | PTA_0 | MPWM0_CH1 | SPI2_PCS0 |  | eTMR0_QD_PHA | UART0_CTS | TMU_OUT3 |  |
| 80 | 51 | 39 | PTC_7 | ADC0_SE21 | ADC0_SE21 | PTC_7 | UART1_TX | CAN1_TX | MPWM0_CH11 | SPI2_PCS2 | eTMR1_QD_PHA |  |  |
| 81 | 52 | 40 | PTC_6 | ADC0_SE20 | ADC0_SE20 | PTC_6 | UART1_RX | CAN1_RX | MPWM0_CH10 | SPI2_PCS3 | eTMR1_QD_PHB |  |  |
| 82 |  |  | PTA_16 | ADC0_SE29 | ADC0_SE29 | PTA_16 | eTMR1_CH3 | SPI1_PCS2 |  |  |  |  |  |
| 83 |  |  | PTA_15 | ADC0_SE28 | ADC0_SE28 | PTA_15 | eTMR1_CH2 | SPI0_PCS3 | SPI2_PCS3 |  |  |  |  |
| 84 | 53 |  | PTE_6 | ADC0_SE27 | ADC0_SE27 | PTE_6 | SPI0_PCS2 |  | MPWM0_CH15 |  | UART1_RTS |  |  |
| 85 | 54 |  | PTE_2 | ADC0_SE26 | ADC0_SE26 | PTE_2 | SPI0_SOUT | LPTMR0_ALT3 | MPWM0_CH14 |  | UART1_CTS |  |  |
| 86 |  |  | VSS | VSS | VSS |  |  |  |  |  |  |  |  |
| 87 |  |  | VDD | VDD | VDD |  |  |  |  |  |  |  |  |
| 88 |  |  | PTA_14 |  |  | PTA_14 | eTMR0_FLT0 | eTMR1_FLT1 | EWDG_IN |  | eTMR1_FLT0 |  |  |
| 89 | 55 | 41 | PTA_13 |  |  | PTA_13 | eTMR1_CH7 | CAN1_TX | SPI0_PCS0 | UART2_TX | eTMR0_QD_PHA |  |  |
| 90 | 56 | 42 | PTA_12 |  |  | PTA_12 | eTMR1_CH6 | CAN1_RX | SPI0_SCK | UART2_RX | eTMR0_QD_PHB |  |  |
| 91 | 57 | 43 | PTA_11 |  |  | PTA_11 | eTMR1_CH5 |  | SPI0_SIN | ACMP0_ACTIVE | I2C1_SCL |  |  |
| 92 | 58 | 44 | PTA_10 | JTAG_TDO_SWD_SWO |  | PTA_10 | eTMR1_CH4 |  | SPI0_SOUT | RTC_CLKIN | I2C1_SDA | JTAG_TDO_SWD_SWO | Digital Input |
| 93 | 59 |  | PTE_1 |  |  | PTE_1 | SPI0_SIN |  | I2C1_SCL | SPI1_PCS0 | eTMR1_FLT1 |  |  |
| 94 | 60 |  | PTE_0 |  |  | PTE_0 | SPI0_SCK | TCLK_IN1 | I2C1_SDA | SPI1_SOUT | eTMR1_FLT2 |  |  |
| 95 | 61 | 45 | PTC_5 | JTAG_TDI |  | PTC_5 | MPWM0_CH0 | RTC_CLKOUT | SPI0_PCS1 |  | eTMR0_QD_PHB | JTAG_TDI | Pull Up Input |
| 96 | 62 | 46 | PTC_4 | JTAG_TCK_SWD_CLK | ACMP0_IN2 | PTC_4 | eTMR1_CH0 | RTC_CLKOUT |  | EWDG_IN | eTMR1_QD_PHB | JTAG_TCK_SWD_CLK | Pull Down Input |
| 97 | 63 | 47 | PTA_5 | RCU_RESET_b |  | PTA_5 |  | TCLK_IN1 |  |  | eTMR1_QD_PHB | RCU_RESET_b | Pull Up Input |
| 98 | 64 | 48 | PTA_4 | JTAG_TMS_SWD_IO |  | PTA_4 |  |  | ACMP0_OUT | EWDG_OUT_b |  | JTAG_TMS_SWD_IO | Pull Up Input |
| 99 |  |  | PTA_9 |  |  | PTA_9 | UART2_TX | SPI2_PCS0 |  | eTMR1_FLT2 | eTMR1_FLT3 |  |  |
| 100 |  |  | PTA_8 |  |  | PTA_8 | UART2_RX | SPI2_SOUT |  | eTMR1_FLT3 |  |  |  |

## Version

| Version | Author | Description |
| --- | --- | --- |
| V1.0 | Major Lin | Initial version. |
| V1.1 | Major Lin | Update VDD15 pad |
| V1.2 | Major Lin | Update PIN3 function in LQFP100 |
| V1.3 | Major Lin | Update VDD15 PIN for LQFP100 |
