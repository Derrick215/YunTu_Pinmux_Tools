# YTM32B1MD1x_PINMUX_V1.0

## PINMUX

| NAME | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 | ALT6 | ALT7 | WKU | HD | 100LQFP | 64LQFP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PTE_16 |  | PTE_16 |  | SPI2_SIN | eTMR2_CH7 |  |  | TMU_OUT7 |  |  | 1 |  |
| PTE_15 |  | PTE_15 |  | SPI2_SCK | eTMR2_CH6 |  |  | TMU_OUT6 |  |  | 2 |  |
| VDD11 | VDD11 |  |  |  |  |  |  |  |  |  | 3 | 1 |
| VDD25 | VDD25 |  |  |  |  |  |  |  |  |  | 4 | 2 |
| PTE_11 |  | PTE_11 | SPI2_PCS0 | lpTMR0_ALT1 | eTMR2_CH5 | SENT_RX_IN1 | ETM_TRACE_D0 | TMU_OUT5 | wku_ind[0] |  | 5 | 3 |
| PTE_10 |  | PTE_10 | SCU_CLKOUT | SPI2_PCS1 | eTMR2_CH4 |  |  | TMU_OUT4 |  |  | 6 | 4 |
| PTE_13 |  | PTE_13 |  | SPI2_PCS2 | eTMR2_FLT0 |  |  |  |  |  | 7 |  |
| PTE_5 |  | PTE_5 | TCLK_IN2 | eTMR2_QD_PHA | eTMR2_CH3 | CAN0_TX |  | EWDG_IN |  |  | 8 | 5 |
| PTE_4 |  | PTE_4 | ETM_TRACE_D1 | eTMR2_QD_PHB | eTMR2_CH2 | CAN0_RX |  | EWDG_OUT_b | wku_ind[1] |  | 9 | 6 |
| VDD | VDD |  |  |  |  |  |  |  |  |  | 10 | 7 |
| VDDA | VDDA |  |  |  |  |  |  |  |  |  | 11 | 8 |
| VREFH | VREFH |  |  |  |  |  |  |  |  |  | 12 | 9 |
| VREFL | VREFL |  |  |  |  |  |  |  |  |  | 13 |  |
| VSS | VSS |  |  |  |  |  |  |  |  |  | 14 | 10 |
| PTB_7 | EXTAL | PTB_7 | I2C0_SCL |  | SPI3_SCK |  |  | TMU_OUT2 |  |  | 15 | 11 |
| PTB_6 | XTAL | PTB_6 | I2C0_SDA |  | SPI3_SIN |  |  | TMU_OUT1 |  |  | 16 | 12 |
| PTE_14 |  | PTE_14 | eTMR0_FLT1 |  | eTMR2_FLT1 |  |  |  |  |  | 17 |  |
| PTE_3 |  | PTE_3 | eTMR0_FLT0 | SPI1_SIN | eTMR2_FLT0 | SPI3_SOUT | TMU_IN6 | ACMP0_OUT | wku_ind[2] |  | 18 | 13 |
| PTE_12 |  | PTE_12 | eTMR0_FLT3 | LINFlexD2_TX |  | SPI3_PCS0 |  |  |  |  | 19 |  |
| PTD_17 |  | PTD_17 | eTMR0_FLT2 | LINFlexD2_RX |  |  |  |  |  |  | 20 |  |
| PTD_16 |  | PTD_16 | eTMR0_CH1 |  | SPI0_SIN | ACMP0_ACTIVE | ETM_TRACE_D2 | ETM_TRACE_CLKOUT |  |  | 21 | 14 |
| PTD_15 |  | PTD_15 | eTMR0_CH0 |  | SPI0_SCK |  | ETM_TRACE_D3 |  |  |  | 22 | 15 |
| PTE_9 |  | PTE_9 | eTMR0_CH7 | SPI1_SCK |  |  |  |  |  |  | 23 | 16 |
| PTD_14 |  | PTD_14 | eTMR2_CH5 | LINFlexD1_TX |  |  |  | SCU_CLKOUT |  |  | 24 |  |
| PTD_13 |  | PTD_13 | eTMR2_CH4 | LINFlexD1_RX |  |  |  | RTC_CLKOUT |  |  | 25 |  |
| PTE_8 | ACMP0_IN3 | PTE_8 | eTMR0_CH6 |  |  | SPI3_PCS1 |  |  | wku_ind[4] |  | 26 | 17 |
| PTB_5 |  | PTB_5 | eTMR0_CH5 | SPI0_PCS1 | SPI0_PCS0 | SCU_CLKOUT | TMU_IN0 |  |  | Y | 27 | 18 |
| PTB_4 |  | PTB_4 | eTMR0_CH4 | SPI0_SOUT |  |  | TMU_IN1 |  |  | Y | 28 | 19 |
| PTC_3 | ADC0_SE11/ACMP0_IN4 | PTC_3 | eTMR0_CH3 | CAN0_TX | LINFlexD0_TX |  |  |  |  |  | 29 | 20 |
| PTC_2 | ADC0_SE10/ACMP0_IN5 | PTC_2 | eTMR0_CH2 | CAN0_RX | LINFlexD0_RX |  | ETM_TRACE_CLKOUT |  | wku_ind[5] |  | 30 | 21 |
| PTD_7 | ACMP0_IN6 | PTD_7 | LINFlexD2_TX | eTMR0_CH3 | eTMR2_FLT3 |  | ETM_TRACE_D0 |  |  |  | 31 | 22 |
| PTD_6 | ACMP0_IN7 | PTD_6 | LINFlexD2_RX | eTMR0_CH2 | eTMR2_FLT2 |  |  |  |  |  | 32 | 23 |
| PTD_5 |  | PTD_5 | eTMR2_CH3 | lpTMR0_ALT2 | eTMR2_FLT1 |  | TMU_IN7 |  |  |  | 33 | 24 |
| PTD_12 |  | PTD_12 | eTMR2_CH2 |  | ETM_TRACE_D1 |  | SPI3_PCS2 |  |  |  | 34 |  |
| PTD_11 |  | PTD_11 | eTMR2_CH1 | eTMR2_QD_PHA | ETM_TRACE_D2 |  | SPI3_PCS3 |  |  |  | 35 |  |
| PTD_10 |  | PTD_10 | eTMR2_CH0 | eTMR2_QD_PHB | ETM_TRACE_D3 |  | SCU_CLKOUT |  |  |  | 36 |  |
| VSS | VSS |  |  |  |  |  |  |  |  |  | 37 |  |
| VDD | VDD |  |  |  |  |  |  |  |  |  | 38 |  |
| PTC_1 | ADC0_SE9 | PTC_1 | eTMR0_CH1 | SPI2_SOUT |  |  | eTMR1_CH7 |  | wku_ind[6] |  | 39 | 25 |
| PTC_0 | ADC0_SE8 | PTC_0 | eTMR0_CH0 | SPI2_SIN |  |  | eTMR1_CH6 |  |  |  | 40 | 26 |
| PTD_9 |  | PTD_9 |  |  | eTMR2_FLT3 |  | eTMR1_CH5 |  |  |  | 41 |  |
| PTD_8 |  | PTD_8 |  |  | eTMR2_FLT2 |  | eTMR1_CH4 |  |  |  | 42 |  |
| PTC_17 | ADC0_SE15 | PTC_17 | eTMR1_FLT3 | CAN2_TX |  | eTMR2_CH1 |  |  |  | Y | 43 | 27 |
| PTC_16 | ADC0_SE14 | PTC_16 | eTMR1_FLT2 | CAN2_RX |  | eTMR2_CH0 |  |  |  | Y | 44 | 28 |
| PTC_15 | ADC0_SE13 | PTC_15 | eTMR1_CH3 | SPI2_SCK |  |  | TMU_IN8 |  | wku_ind[7] |  | 45 | 29 |
| PTC_14 | ADC0_SE12 | PTC_14 | eTMR1_CH2 | SPI2_PCS0 |  |  | TMU_IN9 |  |  |  | 46 | 30 |
| PTB_3 | ADC0_SE7 | PTB_3 | eTMR1_CH1 | SPI0_SIN | eTMR1_QD_PHA |  | TMU_IN2 |  |  |  | 47 | 31 |
| PTB_2 | ADC0_SE6 | PTB_2 | eTMR1_CH0 | SPI0_SCK | eTMR1_QD_PHB |  | TMU_IN3 |  |  |  | 48 | 32 |
| PTC_13 |  | PTC_13 | eTMR3_CH7 | eTMR2_CH7 |  |  |  |  |  |  | 49 |  |
| PTC_12 |  | PTC_12 | eTMR3_CH6 | eTMR2_CH6 |  |  |  |  |  |  | 50 |  |
| PTC_11 |  | PTC_11 | eTMR3_CH5 |  |  |  | TMU_IN10 |  |  |  | 51 |  |
| PTC_10 |  | PTC_10 | eTMR3_CH4 |  |  |  | TMU_IN11 |  |  |  | 52 |  |
| PTB_1 | ADC0_SE5 | PTB_1 | LINFlexD0_TX | SPI0_SOUT | TCLK_IN0 | CAN0_TX |  |  | wku_ind[8] |  | 53 | 33 |
| PTB_0 | ADC0_SE4 | PTB_0 | LINFlexD0_RX | SPI0_PCS0 | lpTMR0_ALT3 | CAN0_RX |  |  |  |  | 54 | 34 |
| PTC_9 |  | PTC_9 | LINFlexD1_TX | eTMR1_FLT1 |  |  |  |  |  | Y | 55 | 35 |
| PTC_8 |  | PTC_8 | LINFlexD1_RX | eTMR1_FLT0 |  |  |  |  |  | Y | 56 | 36 |
| PTA_7 | ADC0_SE3 | PTA_7 | eTMR0_FLT2 |  | RTC_CLKIN | SENT_RX_IN0 |  |  | wku_ind[9] |  | 57 | 37 |
| PTA_6 | ADC0_SE2 | PTA_6 | eTMR0_FLT1 | SPI1_PCS1 |  | SENT_RX_IN1 |  |  |  |  | 58 | 38 |
| PTE_7 |  | PTE_7 | eTMR0_CH7 | eTMR3_FLT0 |  |  |  |  |  |  | 59 | 39 |
| VSS | VSS |  |  |  |  |  |  |  |  |  | 60 | 40 |
| VDD | VDD |  |  |  |  |  |  |  |  |  | 61 | 41 |
| PTA_17 |  | PTA_17 | eTMR0_CH6 | eTMR3_FLT0 | EWDG_OUT_b |  |  |  |  |  | 62 |  |
| PTB_17 |  | PTB_17 | eTMR0_CH5 | SPI1_PCS3 |  |  |  |  |  |  | 63 |  |
| PTB_16 | ADC0_SE31 | PTB_16 | eTMR0_CH4 | SPI1_SOUT |  |  |  |  |  |  | 64 |  |
| PTB_15 | ADC0_SE30 | PTB_15 | eTMR0_CH3 | SPI1_SIN |  |  |  |  |  |  | 65 |  |
| PTB_14 | ADC0_SE25 | PTB_14 | eTMR0_CH2 | SPI1_SCK |  |  |  |  |  |  | 66 |  |
| PTB_13 | ADC0_SE24 | PTB_13 | eTMR0_CH1 | eTMR3_FLT1 | CAN2_TX | SPI3_PCS2 |  |  |  |  | 67 | 42 |
| PTB_12 | ADC0_SE23 | PTB_12 | eTMR0_CH0 | eTMR3_FLT2 | CAN2_RX | SPI3_PCS3 |  |  | wku_ind[10] |  | 68 | 43 |
| PTD_4 | ADC0_SE22 | PTD_4 | eTMR0_FLT3 | eTMR3_FLT3 |  |  |  |  |  |  | 69 | 44 |
| PTD_3 | ADC0_SE19 | PTD_3 | eTMR3_CH5 | SPI1_PCS0 | I2C1_SCL |  | TMU_IN4 | NMI_b | wku_ind[11] |  | 70 | 45 |
| PTD_2 | ADC0_SE18 | PTD_2 | eTMR3_CH4 | SPI1_SOUT | I2C1_SDA |  | TMU_IN5 |  |  |  | 71 | 46 |
| PTA_3 | ADC0_SE17 | PTA_3 | eTMR3_CH1 | I2C0_SCL | EWDG_IN | SENT_RX_IN0 | LINFlexD0_TX |  |  |  | 72 | 47 |
| PTA_2 | ADC0_SE16 | PTA_2 | eTMR3_CH0 | I2C0_SDA | EWDG_OUT_b | SENT_RX_IN1 | LINFlexD0_RX |  | wku_ind[12] |  | 73 | 48 |
| PTB_11 |  | PTB_11 | eTMR3_CH3 |  |  |  |  |  |  |  | 74 |  |
| PTB_10 |  | PTB_10 | eTMR3_CH2 |  |  |  |  |  |  |  | 75 |  |
| PTB_9 |  | PTB_9 | eTMR3_CH1 |  |  |  |  |  |  |  | 76 |  |
| PTB_8 |  | PTB_8 | eTMR3_CH0 |  |  |  |  |  |  |  | 77 |  |
| PTA_1 | ADC0_SE1/ACMP0_IN1 | PTA_1 | eTMR1_CH1 |  |  | eTMR1_QD_PHA |  | TMU_OUT0 |  |  | 78 | 49 |
| PTA_0 | ADC0_SE0/ACMP0_IN0 | PTA_0 | eTMR2_CH1 |  |  | eTMR2_QD_PHA |  | TMU_OUT3 |  |  | 79 | 50 |
| PTC_7 | ADC0_SE21 | PTC_7 | LINFlexD1_TX | CAN1_TX | eTMR3_CH3 |  | eTMR1_QD_PHA |  |  |  | 80 | 51 |
| PTC_6 | ADC0_SE20 | PTC_6 | LINFlexD1_RX | CAN1_RX | eTMR3_CH2 |  | eTMR1_QD_PHB |  | wku_ind[13] |  | 81 | 52 |
| PTA_16 | ADC0_SE29 | PTA_16 | eTMR1_CH3 | SPI1_PCS2 |  |  |  |  |  |  | 82 |  |
| PTA_15 | ADC0_SE28 | PTA_15 | eTMR1_CH2 | SPI0_PCS3 | SPI2_PCS3 |  |  |  |  |  | 83 |  |
| PTE_6 | ADC0_SE27 | PTE_6 | SPI0_PCS2 |  | eTMR3_CH7 | SENT_RX_IN1 | ETM_TRACE_D2 | ETM_TRACE_CLKOUT | wku_ind[14] |  | 84 | 53 |
| PTE_2 | ADC0_SE26 | PTE_2 | SPI0_SOUT | lpTMR0_ALT3 | eTMR3_CH6 |  | ETM_TRACE_D3 |  |  |  | 85 | 54 |
| VSS | VSS |  |  |  |  |  |  |  |  |  | 86 |  |
| VDD | VDD |  |  |  |  |  |  |  |  |  | 87 |  |
| PTA_14 |  | PTA_14 | eTMR0_FLT0 | eTMR3_FLT1 | EWDG_IN |  | eTMR1_FLT0 |  |  |  | 88 |  |
| PTA_13 |  | PTA_13 | eTMR1_CH7 | CAN1_TX | SPI3_PCS0 |  | eTMR2_QD_PHA |  |  |  | 89 | 55 |
| PTA_12 |  | PTA_12 | eTMR1_CH6 | CAN1_RX | SPI3_SCK |  | eTMR2_QD_PHB |  | wku_ind[15] |  | 90 | 56 |
| PTA_11 |  | PTA_11 | eTMR1_CH5 |  | SPI3_SIN | ACMP0_ACTIVE |  |  |  | Y | 91 | 57 |
| PTA_10 |  | PTA_10 | eTMR1_CH4 |  | SPI3_SOUT |  |  | JTAG_TDO/SWD_SWO |  | Y | 92 | 58 |
| PTE_1 |  | PTE_1 | SPI0_SIN |  | SENT_RX_IN0 | SPI1_PCS0 | eTMR1_FLT1 |  |  | Y | 93 | 59 |
| PTE_0 |  | PTE_0 | SPI0_SCK | TCLK_IN1 |  | SPI1_SOUT | eTMR1_FLT2 |  | wku_ind[3] | Y | 94 | 60 |
| PTC_5 |  | PTC_5 | eTMR2_CH0 | RTC_CLKOUT | SPI3_PCS1 |  | eTMR2_QD_PHB | JTAG_TDI |  |  | 95 | 61 |
| PTC_4 | ACMP0_IN2 | PTC_4 | eTMR1_CH0 | RTC_CLKOUT |  | EWDG_IN | eTMR1_QD_PHB | JTAG_TCK/SWD_CLK |  |  | 96 | 62 |
| PTA_5 |  | PTA_5 |  | TCLK_IN1 |  |  |  | RESET_b |  |  | 97 | 63 |
| PTA_4 |  | PTA_4 |  |  | ACMP0_OUT | EWDG_OUT_b |  | JTAG_TMS/SWD_IO |  |  | 98 | 64 |
| PTA_9 |  | PTA_9 | LINFlexD2_TX | SPI2_PCS0 |  | eTMR3_FLT2 | eTMR1_FLT3 |  |  |  | 99 |  |
| PTA_8 |  | PTA_8 | LINFlexD2_RX | SPI2_SOUT |  | eTMR3_FLT3 |  |  |  |  | 100 |  |

## Version

| Version | Date | Comment |
| --- | --- | --- |
| 1.0 | 2022-10-17 | Initial version |
