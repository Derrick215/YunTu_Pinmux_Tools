# YTM32B1ME1x_PINMUX_V1.2

## IOMUX

| 144LQFP | 100LQFP | 64LQFP | NAME | Default | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 | ALT6 | ALT7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 |  | PTE_16 |  |  | PTE_16 | UART1_RTS | SPI2_SIN | eTMR2_CH7 |  |  | TMU_OUT7 |
| 2 | 2 |  | PTE_15 |  |  | PTE_15 | UART1_CTS | SPI2_SCK | eTMR2_CH6 |  |  | TMU_OUT6 |
| 3 | 3 | 1 | VDD12 | VDD12 | VDD12 |  |  |  |  |  |  |  |
| 4 | 4 | 2 | PTD_0 |  |  | PTD_0 | eTMR0_CH2 | SPI1_SCK | eTMR2_CH0 | ETM_TRACE_D0 |  | TMU_OUT1 |
| 5 | 5 | 3 | PTE_11 |  |  | PTE_11 | SPI2_PCS0 | LPTMR0_ALT1 | eTMR2_CH5 | UART3_TX | ETM_TRACE_D0 | TMU_OUT5 |
| 6 | 6 | 4 | PTE_10 |  |  | PTE_10 | SCU_CLKOUT | SPI2_PCS1 | eTMR2_CH4 | UART3_RX |  | TMU_OUT4 |
| 7 | 7 |  | PTE_13 |  |  | PTE_13 | MPWM0_CH5 | SPI2_PCS2 | eTMR2_FLT0 | MPWM0_CH10 |  |  |
| 8 | 8 | 5 | PTE_5 |  |  | PTE_5 | TCLK_IN2 | eTMR2_QD_PHA | eTMR2_CH3 | CAN0_TX |  | EWDG_IN |
| 9 | 9 | 6 | PTE_4 |  |  | PTE_4 | ETM_TRACE_D1 | eTMR2_QD_PHB | eTMR2_CH2 | CAN0_RX |  | EWDG_OUT_b |
| 10 |  |  | PTA_25 |  |  | PTA_25 | MPWM0_CH8 |  |  |  |  |  |
| 11 | 10 | 7 | VDD | VDD | VDD |  |  |  |  |  |  |  |
| 12 |  |  | VSS | VSS | VSS |  |  |  |  |  |  |  |
| 13 | 11 | 8 | VDDA | VDDA | VDDA |  |  |  |  |  |  |  |
| 14 | 12 | 9 | VREFH | VREFH | VREFH |  |  |  |  |  |  |  |
| 15 | 13 |  | VREFL | VREFL | VREFL |  |  |  |  |  |  |  |
| 16 | 14 | 10 | VSS | VSS | VSS |  |  |  |  |  |  |  |
| 17 | 15 | 11 | PTB_7 | EXTAL | EXTAL | PTB_7 | I2C0_SCL |  | SPI3_SCK |  |  | TMU_OUT2 |
| 18 | 16 | 12 | PTB_6 | XTAL | XTAL | PTB_6 | I2C0_SDA |  | SPI3_SIN |  |  | TMU_OUT1 |
| 19 |  |  | PTA_26 |  |  | PTA_26 | MPWM0_CH9 | SPI1_PCS0 | SPI0_PCS0 |  |  |  |
| 20 | 17 |  | PTE_14 |  |  | PTE_14 | eTMR0_FLT1 |  | eTMR2_FLT1 | SCU_CLKOUT |  |  |
| 21 | 18 | 13 | PTE_3 |  |  | PTE_3 | eTMR0_FLT0 | SPI1_SIN | eTMR2_FLT0 | SPI3_SOUT | TMU_IN6 | CMP0_OUT |
| 22 |  |  | PTA_27 |  |  | PTA_27 | MPWM0_CH10 | SPI1_SOUT | UART0_TX | CAN0_TX |  |  |
| 23 | 19 |  | PTE_12 |  |  | PTE_12 | eTMR0_FLT3 | UART2_TX |  | SPI3_PCS0 | eTMR3_CH5 | UART2_RTS |
| 24 |  |  | PTA_28 |  |  | PTA_28 | MPWM0_CH11 | SPI1_SCK | UART0_RX | CAN0_RX |  |  |
| 25 | 20 |  | PTD_17 |  |  | PTD_17 | eTMR0_FLT2 | UART2_RX |  | SPI3_PCS0 |  | eTMR2_CH2 |
| 26 |  |  | PTA_29 |  |  | PTA_29 | MPWM0_CH12 |  | UART2_TX | SPI1_SIN |  |  |
| 27 |  |  | PTA_30 |  |  | PTA_30 | MPWM0_CH13 | UART2_RX | SPI0_SOUT |  |  |  |
| 28 | 21 | 14 | PTD_16 | EXTAL32 | EXTAL32 | PTD_16 | eTMR0_CH1 |  | SPI0_SIN | CMP0_ACTIVE | ETM_TRACE_D2 | ETM_TRACE_CLKOUT |
| 29 | 22 | 15 | PTD_15 | XTAL32 | XTAL32 | PTD_15 | eTMR0_CH0 |  | SPI0_SCK |  | ETM_TRACE_D3 |  |
| 30 | 23 | 16 | PTE_9 |  |  | PTE_9 | eTMR0_CH7 | SPI1_SCK | I2C2_SDA | UART2_CTS |  | SCU_CLKOUT |
| 31 |  |  | VSS | VSS | VSS |  |  |  |  |  |  |  |
| 32 |  |  | VDD | VDD | VDD |  |  |  |  |  |  |  |
| 33 |  |  | PTA_31 |  |  | PTA_31 | MPWM0_CH14 |  | SPI0_PCS1 |  | MPWM0_CH4 |  |
| 34 | 24 |  | PTD_14 |  |  | PTD_14 | eTMR2_CH5 | UART1_TX | I2C0_SCL | CMP0_ACTIVE | SPI5_PCS3 | SCU_CLKOUT |
| 35 | 25 |  | PTD_13 |  |  | PTD_13 | eTMR2_CH4 | UART1_RX | I2C0_SDA | SPI5_PCS2 | MPWM0_CH5 | RTC_CLKOUT |
| 36 |  |  | PTB_18 | ADC0_S16 | ADC0_S16 | PTB_18 | MPWM0_CH15 |  | SPI1_PCS1 |  | MPWM0_CH6 |  |
| 37 |  |  | PTB_20 | ADC0_S17 | ADC0_S17 | PTB_20 | UART3_TX |  |  | I2C1_SDA |  |  |
| 38 |  |  | PTB_21 | ADC0_S18 | ADC0_S18 | PTB_21 | UART3_RX |  |  | I2C1_SCL |  |  |
| 39 | 26 | 17 | PTE_8 | CMP0_IN3 | CMP0_IN3 | PTE_8 | eTMR0_CH6 |  | I2C2_SCL | SPI3_PCS1 | MPWM0_CH9 | SENT0_RX_IN0 |
| 40 | 27 | 18 | PTB_5 |  |  | PTB_5 | eTMR0_CH5 | SPI0_PCS1 | SPI0_PCS0 | SCU_CLKOUT | TMU_IN0 | SENT0_RX_IN1 |
| 41 | 28 | 19 | PTB_4 |  |  | PTB_4 | eTMR0_CH4 | SPI0_SOUT |  |  | TMU_IN1 |  |
| 42 | 29 | 20 | PTC_3 | ADC0_S11/CMP0_IN4 | ADC0_S11/CMP0_IN4 | PTC_3 | eTMR0_CH3 | CAN0_TX | UART0_TX | SPI4_PCS0 |  |  |
| 43 | 30 | 21 | PTC_2 | ADC0_S10/CMP0_IN5/DPDWK_IN1 | ADC0_S10/CMP0_IN5/DPDWK_IN1 | PTC_2 | eTMR0_CH2 | CAN0_RX | UART0_RX | SPI4_SCK | ETM_TRACE_CLKOUT |  |
| 44 | 31 | 22 | PTD_7 | CMP0_IN6 | CMP0_IN6 | PTD_7 | UART2_TX | eTMR0_CH3 | eTMR2_FLT3 | SPI4_SIN | ETM_TRACE_D0 |  |
| 45 | 32 | 23 | PTD_6 | CMP0_IN7 | CMP0_IN7 | PTD_6 | UART2_RX | eTMR0_CH2 | eTMR2_FLT2 | SPI4_SOUT |  | SPI0_PCS0 |
| 46 | 33 | 24 | PTD_5 |  |  | PTD_5 | eTMR2_CH3 | LPTMR0_ALT2 | eTMR2_FLT1 | SPI4_PCS1 | TMU_IN7 | SPI0_PCS1 |
| 47 | 34 |  | PTD_12 |  |  | PTD_12 | eTMR2_CH2 |  | ETM_TRACE_D1 | UART2_RTS | SPI0_SOUT | SPI5_SIN |
| 48 | 35 |  | PTD_11 |  |  | PTD_11 | eTMR2_CH1 | eTMR2_QD_PHA | ETM_TRACE_D2 | UART2_CTS | SPI0_SCK | SPI5_SOUT |
| 49 | 36 |  | PTD_10 |  |  | PTD_10 | eTMR2_CH0 | eTMR2_QD_PHB | ETM_TRACE_D3 | SPI0_SIN | SCU_CLKOUT | SPI5_SCK |
| 50 | 37 |  | VSS | VSS | VSS |  |  |  |  |  |  |  |
| 51 | 38 |  | VDD | VDD | VDD |  |  |  |  |  |  |  |
| 52 | 39 | 25 | PTC_1 | ADC0_S9 | ADC0_S9 | PTC_1 | eTMR0_CH1 | SPI2_SOUT | CAN3_TX | UART5_TX | eTMR1_CH7 |  |
| 53 | 40 | 26 | PTC_0 | ADC0_S8/DPDWK_IN0 | ADC0_S8/DPDWK_IN0 | PTC_0 | eTMR0_CH0 | SPI2_SIN | CAN3_RX | UART5_RX | eTMR1_CH6 |  |
| 54 | 41 |  | PTD_9 |  |  | PTD_9 | UART4_TX |  | eTMR2_FLT3 | I2C1_SCL | eTMR1_CH5 |  |
| 55 | 42 |  | PTD_8 |  |  | PTD_8 | UART4_RX |  | eTMR2_FLT2 | I2C1_SDA | eTMR1_CH4 | SPI3_SOUT |
| 56 | 43 | 27 | PTC_17 | ADC0_S15 | ADC0_S15 | PTC_17 | eTMR1_FLT3 | CAN2_TX | SPI4_PCS0 | eTMR2_CH1 |  | SPI3_SCK |
| 57 | 44 | 28 | PTC_16 | ADC0_S14 | ADC0_S14 | PTC_16 | eTMR1_FLT2 | CAN2_RX | SPI4_SCK | eTMR2_CH0 | SPI3_SIN | I2C1_SDA |
| 58 |  |  | PTB_22 | ADC0_S19 | ADC0_S19 | PTB_22 |  | SPI3_PCS1 |  | UART1_TX |  |  |
| 59 | 45 | 29 | PTC_15 | ADC0_S13 | ADC0_S13 | PTC_15 | eTMR1_CH3 | SPI2_SCK | SPI4_SIN | UART4_TX | TMU_IN8 | I2C1_SCL |
| 60 |  |  | PTB_23 | ADC0_S20 | ADC0_S20 | PTB_23 |  | UART1_RX |  |  |  |  |
| 61 | 46 | 30 | PTC_14 | ADC0_S12 | ADC0_S12 | PTC_14 | eTMR1_CH2 | SPI2_PCS0 | SPI4_SOUT | UART4_RX | TMU_IN9 | eTMR3_CH4 |
| 62 |  |  | PTB_25 | ADC0_S21 | ADC0_S21 | PTB_25 |  |  | SPI4_PCS1 | SPI2_PCS0 |  |  |
| 63 | 47 | 31 | PTB_3 | ADC0_S7 | ADC0_S7 | PTB_3 | eTMR1_CH1 | SPI0_SIN | eTMR1_QD_PHA |  | TMU_IN2 |  |
| 64 |  |  | PTB_27 | ADC0_S22 | ADC0_S22 | PTB_27 |  |  |  | SPI2_SOUT | MPWM0_CH0 |  |
| 65 |  |  | PTB_28 | ADC0_S23 | ADC0_S23 | PTB_28 |  |  |  | SPI2_SIN | MPWM0_CH1 |  |
| 66 |  |  | VSS | VSS | VSS |  |  |  |  |  |  |  |
| 67 |  |  | VDD | VDD | VDD |  |  |  |  |  |  |  |
| 68 | 48 | 32 | PTB_2 | ADC0_S6 | ADC0_S6 | PTB_2 | eTMR1_CH0 | SPI0_SCK | eTMR1_QD_PHB | MPWM0_CH2 | TMU_IN3 |  |
| 69 |  |  | PTB_29 |  |  | PTB_29 |  |  |  | SPI2_SCK | MPWM0_CH3 |  |
| 70 | 49 |  | PTC_13 |  |  | PTC_13 | eTMR3_CH7 | eTMR2_CH7 |  | UART2_RTS | eTMR3_CH3 |  |
| 71 | 50 |  | PTC_12 |  |  | PTC_12 | eTMR3_CH6 | eTMR2_CH6 | SPI2_PCS1 | UART2_CTS | eTMR3_CH2 |  |
| 72 |  |  | PTC_19 |  |  | PTC_19 |  |  |  | SPI2_PCS1 | MPWM0_CH7 |  |
| 73 |  |  | PTC_23 |  |  | PTC_23 | SPI0_SCK |  |  |  | MPWM0_CH11 |  |
| 74 | 51 |  | PTC_11 |  |  | PTC_11 | eTMR3_CH5 | MPWM0_CH2 |  |  | TMU_IN10 |  |
| 75 | 52 |  | PTC_10 |  |  | PTC_10 | eTMR3_CH4 | eTMR0_CH6 | SPI2_PCS1 | SPI4_PCS0 | TMU_IN11 | eTMR3_CH0 |
| 76 |  |  | PTC_27 |  |  | PTC_27 | MPWM0_CH4 |  |  |  | MPWM0_CH15 | SPI4_SCK |
| 77 | 53 | 33 | PTB_1 | ADC1_S25/ADC0_S5 | ADC1_S25/ADC0_S5 | PTB_1 | UART0_TX | SPI0_SOUT | TCLK_IN0 | CAN0_TX | MPWM0_CH5 |  |
| 78 | 54 | 34 | PTB_0 | ADC1_S24/ADC0_S4 | ADC1_S24/ADC0_S4 | PTB_0 | UART0_RX | SPI0_PCS0 | LPTMR0_ALT3 | CAN0_RX | MPWM0_CH6 |  |
| 79 |  |  | PTC_28 |  |  | PTC_28 | MPWM0_CH7 | eTMR3_CH7 |  | I2C1_SCL |  | CAN3_TX |
| 80 | 55 | 35 | PTC_9 |  |  | PTC_9 | UART1_TX | eTMR1_FLT1 | SPI5_PCS1 | MPWM0_CH8 | SPI0_SIN | I2C0_SDA |
| 81 | 56 | 36 | PTC_8 | DAC0_OUT | DAC0_OUT | PTC_8 | UART1_RX | eTMR1_FLT0 | SPI5_PCS0 | MPWM0_CH9 | SPI0_SCK | I2C0_SCL |
| 82 |  |  | PTC_29 |  |  | PTC_29 | MPWM0_CH10 |  |  | I2C1_SDA |  | CAN3_RX |
| 83 | 57 | 37 | PTA_7 | ADC0_S3 | ADC0_S3 | PTA_7 | eTMR0_FLT2 | MPWM0_CH11 | RTC_CLKIN | I2C2_SCL | SPI5_SCK | UART1_RTS |
| 84 |  |  | PTC_30 |  |  | PTC_30 | MPWM0_CH12 |  |  |  |  |  |
| 85 | 58 | 38 | PTA_6 | ADC0_S2 | ADC0_S2 | PTA_6 | eTMR0_FLT1 | SPI1_PCS1 | SPI5_SIN | I2C2_SDA | MPWM0_CH13 | UART1_CTS |
| 86 |  |  | PTC_31 |  |  | PTC_31 | MPWM0_CH14 |  | I2C1_SDA |  |  |  |
| 87 | 59 | 39 | PTE_7 |  |  | PTE_7 | eTMR0_CH7 | eTMR3_FLT0 | SPI5_SOUT |  | SPI3_SCK |  |
| 88 |  |  | PTD_18 | ADC1_S16 | ADC1_S16 | PTD_18 | MPWM0_CH15 |  | I2C1_SCL | I2C1_SDA |  |  |
| 89 |  |  | PTD_19 | ADC1_S17 | ADC1_S17 | PTD_19 |  |  |  | I2C1_SCL |  |  |
| 90 | 60 | 40 | VSS | VSS | VSS |  |  |  |  |  |  |  |
| 91 | 61 | 41 | VDD | VDD | VDD |  |  |  |  |  |  |  |
| 92 | 62 |  | PTA_17 |  |  | PTA_17 | eTMR0_CH6 | eTMR3_FLT0 | EWDG_OUT_b |  | SPI3_SOUT |  |
| 93 | 63 |  | PTB_17 |  |  | PTB_17 | eTMR0_CH5 | SPI1_PCS3 |  |  | SPI3_PCS0 |  |
| 94 | 64 |  | PTB_16 | ADC1_S15 | ADC1_S15 | PTB_16 | eTMR0_CH4 | SPI1_SOUT |  |  |  |  |
| 95 | 65 |  | PTB_15 | ADC1_S14 | ADC1_S14 | PTB_15 | eTMR0_CH3 | SPI1_SIN |  |  |  |  |
| 96 | 66 |  | PTB_14 | ADC1_S9/ADC0_S25 | ADC1_S9/ADC0_S25 | PTB_14 | eTMR0_CH2 | SPI1_SCK |  |  |  |  |
| 97 | 67 | 42 | PTB_13 | ADC1_S8/ADC0_S24 | ADC1_S8/ADC0_S24 | PTB_13 | eTMR0_CH1 | eTMR3_FLT1 | CAN2_TX |  | SPI3_PCS2 |  |
| 98 | 68 | 43 | PTB_12 | ADC1_S7 | ADC1_S7 | PTB_12 | eTMR0_CH0 | eTMR3_FLT2 | CAN2_RX |  | SPI3_PCS3 |  |
| 99 |  |  | PTD_22 | ADC1_S18 | ADC1_S18 | PTD_22 |  |  |  | MPWM0_CH12 |  |  |
| 100 | 69 | 44 | PTD_4 | ADC1_S6 | ADC1_S6 | PTD_4 | eTMR0_FLT3 | eTMR3_FLT3 |  | MPWM0_CH13 | SPI5_PCS2 | SPI1_PCS1 |
| 101 | 70 | 45 | PTD_3 | ADC1_S3 | ADC1_S3 | PTD_3 | eTMR3_CH5 | SPI1_PCS0 | I2C1_SCL | UART3_RX | TMU_IN4 | CORE_NMI_b |
| 102 | 71 | 46 | PTD_2 | ADC1_S2 | ADC1_S2 | PTD_2 | eTMR3_CH4 | SPI1_SOUT | I2C1_SDA | UART3_TX | TMU_IN5 |  |
| 103 |  |  | PTD_23 | ADC1_S19 | ADC1_S19 | PTD_23 |  | SPI3_PCS0 |  | MPWM0_CH14 |  |  |
| 104 | 72 | 47 | PTA_3 | ADC1_S1 | ADC1_S1 | PTA_3 | eTMR3_CH1 | I2C0_SCL | EWDG_IN |  | UART0_TX | SPI1_SCK |
| 105 | 73 | 48 | PTA_2 | ADC1_S0 | ADC1_S0 | PTA_2 | eTMR3_CH0 | I2C0_SDA | EWDG_OUT_b |  | UART0_RX | SPI1_SIN |
| 106 |  |  | PTD_24 | ADC1_S20 | ADC1_S20 | PTD_24 |  |  |  |  |  |  |
| 107 | 74 |  | PTB_11 |  |  | PTB_11 | eTMR3_CH3 | UART5_TX |  |  |  | SPI4_SIN |
| 108 | 75 |  | PTB_10 |  |  | PTB_10 | eTMR3_CH2 | UART5_RX |  |  | I2C0_SDA | SPI4_SCK |
| 109 | 76 |  | PTB_9 |  |  | PTB_9 | eTMR3_CH1 |  |  |  | I2C0_SCL | SPI4_SOUT |
| 110 |  |  | PTD_27 | ADC1_S21 | ADC1_S21 | PTD_27 |  |  |  |  |  |  |
| 111 | 77 |  | PTB_8 |  |  | PTB_8 | eTMR3_CH0 |  |  |  | SPI0_PCS5 | SPI4_PCS0 |
| 112 |  |  | PTD_28 | ADC1_S22 | ADC1_S22 | PTD_28 |  |  |  |  |  |  |
| 113 | 78 | 49 | PTA_1 | ADC0_S1/CMP0_IN1 | ADC0_S1/CMP0_IN1 | PTA_1 | eTMR1_CH1 | UART0_RTS | I2C0_SDA | eTMR1_QD_PHA | SPI0_PCS6 | TMU_OUT0 |
| 114 |  |  | PTD_29 | ADC1_S23 | ADC1_S23 | PTD_29 |  |  |  | SPI4_PCS1 |  |  |
| 115 | 79 | 50 | PTA_0 | ADC0_S0/CMP0_IN0 | ADC0_S0/CMP0_IN0 | PTA_0 | eTMR2_CH1 | UART0_CTS | I2C0_SCL | eTMR2_QD_PHA | SPI0_PCS7 | TMU_OUT3 |
| 116 |  |  | PTD_30 |  |  | PTD_30 |  |  |  |  |  |  |
| 117 | 80 | 51 | PTC_7 | ADC1_S5 | ADC1_S5 | PTC_7 | UART1_TX | CAN1_TX | eTMR3_CH3 | eTMR3_CH7 | eTMR1_QD_PHA |  |
| 118 | 81 | 52 | PTC_6 | ADC1_S4/DPDWK_IN2 | ADC1_S4/DPDWK_IN2 | PTC_6 | UART1_RX | CAN1_RX | eTMR3_CH2 | eTMR3_CH6 | eTMR1_QD_PHB |  |
| 119 | 82 |  | PTA_16 | ADC1_S13 | ADC1_S13 | PTA_16 | eTMR1_CH3 | SPI1_PCS2 | SPI0_PCS4 |  |  |  |
| 120 | 83 |  | PTA_15 | ADC1_S12 | ADC1_S12 | PTA_15 | eTMR1_CH2 | SPI0_PCS3 | SPI2_PCS3 |  |  |  |
| 121 | 84 | 53 | PTE_6 | ADC1_S11 | ADC1_S11 | PTE_6 | SPI0_PCS2 |  | eTMR3_CH7 | UART1_RTS | ETM_TRACE_D2 | ETM_TRACE_CLKOUT |
| 122 | 85 | 54 | PTE_2 | ADC1_S10 | ADC1_S10 | PTE_2 | SPI0_SOUT | LPTMR0_ALT3 | eTMR3_CH6 | UART1_CTS |  | ETM_TRACE_D3 |
| 123 | 86 |  | VSS | VSS | VSS |  |  |  |  |  |  |  |
| 124 | 87 |  | VDD | VDD | VDD |  |  |  |  |  |  |  |
| 125 |  |  | PTE_19 |  |  | PTE_19 | eTMR2_CH6 |  | SPI1_PCS4 | SPI0_SCK |  |  |
| 126 |  |  | PTE_20 |  |  | PTE_20 | MPWM0_CH0 | eTMR3_CH0 | SPI1_PCS3 | SPI0_SIN |  |  |
| 127 | 88 |  | PTA_14 |  |  | PTA_14 | eTMR0_FLT0 | eTMR3_FLT1 | EWDG_IN | eTMR3_CH4 | eTMR1_FLT0 |  |
| 128 |  |  | PTE_21 |  |  | PTE_21 | MPWM0_CH1 |  |  | eTMR3_CH1 | SPI4_SIN |  |
| 129 |  |  | PTE_22 |  |  | PTE_22 | MPWM0_CH2 |  |  | eTMR3_CH2 | SPI4_SCK |  |
| 130 | 89 | 55 | PTA_13 |  |  | PTA_13 | eTMR1_CH7 | CAN1_TX | SPI3_PCS0 | eTMR3_CH3 | eTMR2_QD_PHA |  |
| 131 |  |  | PTE_23 |  |  | PTE_23 | MPWM0_CH3 | CAN1_RX |  | eTMR3_CH3 | SPI4_PCS0 |  |
| 132 |  |  | PTE_24 |  |  | PTE_24 | MPWM0_CH4 | CAN2_TX |  | eTMR3_CH4 | SPI4_PCS1 |  |
| 133 |  |  | PTE_25 |  |  | PTE_25 | MPWM0_CH5 | CAN2_RX |  | eTMR3_CH5 | SPI4_SOUT |  |
| 134 | 90 | 56 | PTA_12 |  |  | PTA_12 | eTMR1_CH6 | CAN1_RX | SPI3_SCK |  | eTMR2_QD_PHB | SENT0_RX_IN0 |
| 135 | 91 | 57 | PTA_11 |  |  | PTA_11 | eTMR1_CH5 | CAN1_TX | SPI3_SIN | CMP0_ACTIVE | SPI1_PCS0 | SENT0_RX_IN1 |
| 136 | 92 | 58 | PTA_10 | JTAG_TDO_SWD_SWO |  | PTA_10 | eTMR1_CH4 |  | SPI3_SOUT |  |  | JTAG_TDO_SWD_SWO |
| 137 | 93 | 59 | PTE_1 |  |  | PTE_1 | SPI0_SIN |  | I2C1_SCL | SPI1_PCS0 | eTMR1_FLT1 |  |
| 138 | 94 | 60 | PTE_0 |  |  | PTE_0 | SPI0_SCK | TCLK_IN1 | I2C1_SDA | SPI1_SOUT | eTMR1_FLT2 |  |
| 139 | 95 | 61 | PTC_5 | JTAG_TDI |  | PTC_5 | eTMR2_CH0 | RTC_CLKOUT | SPI3_PCS1 |  | eTMR2_QD_PHB | JTAG_TDI |
| 140 | 96 | 62 | PTC_4 | JTAG_TCK_SWD_CLK | CMP0_IN2 | PTC_4 | eTMR1_CH0 | RTC_CLKOUT |  | EWDG_IN | eTMR1_QD_PHB | JTAG_TCK_SWD_CLK |
| 141 | 97 | 63 | PTA_5 | RCU_RESET_b |  | PTA_5 | CAN3_TX | TCLK_IN1 |  |  |  | RCU_RESET_b |
| 142 | 98 | 64 | PTA_4 | JTAG_TMS_SWD_IO |  | PTA_4 | CAN3_RX |  | CMP0_OUT | EWDG_OUT_b |  | JTAG_TMS_SWD_IO |
| 143 | 99 |  | PTA_9 |  |  | PTA_9 | UART2_TX | SPI2_PCS0 | SPI1_SIN | eTMR3_FLT2 | eTMR1_FLT3 |  |
| 144 | 100 |  | PTA_8 |  |  | PTA_8 | UART2_RX | SPI2_SOUT | SPI1_SCK | eTMR3_FLT3 |  |  |