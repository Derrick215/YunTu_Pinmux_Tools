# YTM32B1ME0x_PINMUX_V1.0

## IOMUX

| 144LQFP | 100LQFP | 64LQFP | NAME | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 | ALT6 | ALT7 | WKU | SORTNAME |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 |  | PTE_16 |  | PTE_16 |  | SPI2_SIN | eTMR2_CH7 | eTMR4_FLT0 |  | TMU_OUT7 |  | PTE_16 |
| 2 | 2 |  | PTE_15 |  | PTE_15 |  | SPI2_SCK | eTMR2_CH6 | eTMR4_FLT1 |  | TMU_OUT6 |  | PTE_15 |
| 3 | 3 | 1 | VDD11 | VDD11 |  |  |  |  |  |  |  |  | VDD11 |
| 4 | 4 | 2 | VDD25 | VDD25 |  |  |  |  |  |  |  |  | VDD25 |
| 5 | 5 | 3 | PTE_11 |  | PTE_11 | SPI2_PCS0 | LPTMR0_ALT1 | eTMR2_CH5 | LINFlexD3_TX | ETM_TRACE_D0 | TMU_OUT5 | WKU[0] | PTE_11 |
| 6 | 6 | 4 | PTE_10 |  | PTE_10 | SCU_CLKOUT | SPI2_PCS1 | eTMR2_CH4 | LINFlexD3_RX |  | TMU_OUT4 | WKU[1] | PTE_10 |
| 7 | 7 |  | PTE_13 |  | PTE_13 | eTMR4_CH5 | SPI2_PCS2 | eTMR2_FLT0 |  |  |  |  | PTE_13 |
| 8 | 8 | 5 | PTE_5 |  | PTE_5 | TCLK_IN2 | eTMR2_QD_PHA | eTMR2_CH3 | CAN0_TX |  | EWDG_IN | WKU[2] | PTE_05 |
| 9 | 9 | 6 | PTE_4 |  | PTE_4 | ETM_TRACE_D1 | eTMR2_QD_PHB | eTMR2_CH2 | CAN0_RX |  | EWDG_OUT_b | WKU[3] | PTE_04 |
| 10 |  |  | PTA_25 |  | PTA_25 | eTMR5_CH0 |  |  |  |  |  |  | PTA_25 |
| 11 | 10 | 7 | VDD | VDD |  |  |  |  |  |  |  |  | VDD |
| 12 |  |  | VSS | VSS |  |  |  |  |  |  |  |  | VSS |
| 13 | 11 | 8 | VDDA | VDDA |  |  |  |  |  |  |  |  | VDDA |
| 14 | 12 | 9 | VREFH | VREFH |  |  |  |  |  |  |  |  | VREFH |
| 15 | 13 |  | VREFL | VREFL |  |  |  |  |  |  |  |  | VREFL |
| 16 | 14 | 10 | VSS | VSS |  |  |  |  |  |  |  |  | VSS |
| 17 | 15 | 11 | PTB_7 | EXTAL | PTB_7 | I2C0_SCL |  | SPI3_SCK | eTMR4_FLT3 |  | TMU_OUT2 |  | PTB_07 |
| 18 | 16 | 12 | PTB_6 | XTAL | PTB_6 | I2C0_SDA |  | SPI3_SIN | eTMR4_FLT2 |  | TMU_OUT1 |  | PTB_06 |
| 19 |  |  | PTA_26 |  | PTA_26 | eTMR5_CH1 | SPI1_PCS0 | SPI0_PCS0 |  |  |  |  | PTA_26 |
| 20 | 17 |  | PTE_14 |  | PTE_14 | eTMR0_FLT1 |  | eTMR2_FLT1 |  |  |  |  | PTE_14 |
| 21 | 18 | 13 | PTE_3 |  | PTE_3 | eTMR0_FLT0 | SPI1_SIN | eTMR2_FLT0 | SPI3_SOUT | TMU_IN6 | ACMP0_OUT | WKU[4] | PTE_03 |
| 22 |  |  | PTA_27 |  | PTA_27 | eTMR5_CH2 | SPI1_SOUT | LINFlexD0_TX | CAN0_TX |  |  |  | PTA_27 |
| 23 | 19 |  | PTE_12 |  | PTE_12 | eTMR0_FLT3 | LINFlexD2_TX | eTMR5_FLT0 | SPI3_PCS0 |  |  |  | PTE_12 |
| 24 |  |  | PTA_28 |  | PTA_28 | eTMR5_CH3 | SPI1_SCK | LINFlexD0_RX | CAN0_RX |  |  |  | PTA_28 |
| 25 | 20 |  | PTD_17 |  | PTD_17 | eTMR0_FLT2 | LINFlexD2_RX | eTMR5_FLT1 |  |  |  |  | PTD_17 |
| 26 |  |  | PTA_29 |  | PTA_29 | eTMR5_CH4 |  | LINFlexD2_TX | SPI1_SIN |  |  |  | PTA_29 |
| 27 |  |  | PTA_30 |  | PTA_30 | eTMR5_CH5 | LINFlexD2_RX | SPI0_SOUT |  |  |  |  | PTA_30 |
| 28 | 21 | 14 | PTD_16 | EXTAL32 | PTD_16 | eTMR0_CH1 | CAN4_TX | SPI0_SIN | ACMP0_ACTIVE | ETM_TRACE_D2 | ETM_TRACE_CLKOUT |  | PTD_16 |
| 29 | 22 | 15 | PTD_15 | XTAL32 | PTD_15 | eTMR0_CH0 | CAN4_RX | SPI0_SCK |  | ETM_TRACE_D3 |  |  | PTD_15 |
| 30 | 23 | 16 | PTE_9 |  | PTE_9 | eTMR0_CH7 | SPI1_SCK | I2C2_SDA |  |  |  | WKU[7] | PTE_09 |
| 31 |  |  | VSS | VSS |  |  |  |  |  |  |  |  | VSS |
| 32 |  |  | VDD | VDD |  |  |  |  |  |  |  |  | VDD |
| 33 |  |  | PTA_31 |  | PTA_31 | eTMR5_CH6 |  | SPI0_PCS1 |  |  |  |  | PTA_31 |
| 34 | 24 |  | PTD_14 |  | PTD_14 | eTMR2_CH5 | LINFlexD1_TX |  | SPI5_PCS3 |  | SCU_CLKOUT |  | PTD_14 |
| 35 | 25 |  | PTD_13 |  | PTD_13 | eTMR2_CH4 | LINFlexD1_RX |  | SPI5_PCS2 |  | RTC_CLKOUT |  | PTD_13 |
| 36 |  |  | PTB_18 | ADC0_SE16 | PTB_18 | eTMR5_CH7 |  | SPI1_PCS1 |  |  |  |  | PTB_18 |
| 37 |  |  | PTB_20 | ADC0_SE17 | PTB_20 | LINFlexD3_TX |  |  | I2C1_SDA |  |  |  | PTB_20 |
| 38 |  |  | PTB_21 | ADC0_SE18 | PTB_21 | LINFlexD3_RX |  |  | I2C1_SCL |  |  |  | PTB_21 |
| 39 | 26 | 17 | PTE_8 | ACMP0_IN3 | PTE_8 | eTMR0_CH6 |  | I2C2_SCL | SPI3_PCS1 |  |  | WKU[8] | PTE_08 |
| 40 | 27 | 18 | PTB_5 |  | PTB_5 | eTMR0_CH5 | SPI0_PCS1 | SPI0_PCS0 | SCU_CLKOUT | TMU_IN0 |  |  | PTB_05 |
| 41 | 28 | 19 | PTB_4 |  | PTB_4 | eTMR0_CH4 | SPI0_SOUT |  |  | TMU_IN1 |  |  | PTB_04 |
| 42 | 29 | 20 | PTC_3 | ADC0_SE11/ACMP0_IN4 | PTC_3 | eTMR0_CH3 | CAN0_TX | LINFlexD0_TX | SPI4_PCS0 |  |  | WKU[9] | PTC_03 |
| 43 | 30 | 21 | PTC_2 | ADC0_SE10/ACMP0_IN5 | PTC_2 | eTMR0_CH2 | CAN0_RX | LINFlexD0_RX | SPI4_SCK | ETM_TRACE_CLKOUT |  | WKU[10] | PTC_02 |
| 44 | 31 | 22 | PTD_7 | ACMP0_IN6 | PTD_7 | LINFlexD2_TX | eTMR0_CH3 | eTMR2_FLT3 | SPI4_SIN | ETM_TRACE_D0 |  |  | PTD_07 |
| 45 | 32 | 23 | PTD_6 | ACMP0_IN7 | PTD_6 | LINFlexD2_RX | eTMR0_CH2 | eTMR2_FLT2 | SPI4_SOUT |  |  |  | PTD_06 |
| 46 | 33 | 24 | PTD_5 |  | PTD_5 | eTMR2_CH3 | LPTMR0_ALT2 | eTMR2_FLT1 | SPI4_PCS1 | TMU_IN7 |  | WKU[11] | PTD_05 |
| 47 | 34 |  | PTD_12 |  | PTD_12 | eTMR2_CH2 |  | ETM_TRACE_D1 | SPI5_SIN |  |  |  | PTD_12 |
| 48 | 35 |  | PTD_11 |  | PTD_11 | eTMR2_CH1 | eTMR2_QD_PHA | ETM_TRACE_D2 | SPI5_SOUT |  |  |  | PTD_11 |
| 49 | 36 |  | PTD_10 |  | PTD_10 | eTMR2_CH0 | eTMR2_QD_PHB | ETM_TRACE_D3 | SPI5_SCK | SCU_CLKOUT |  |  | PTD_10 |
| 50 | 37 |  | VSS | VSS |  |  |  |  |  |  |  |  | VSS |
| 51 | 38 |  | VDD | VDD |  |  |  |  |  |  |  |  | VDD |
| 52 | 39 | 25 | PTC_1 | ADC0_SE9 | PTC_1 | eTMR0_CH1 | SPI2_SOUT | CAN3_TX |  | eTMR1_CH7 |  | WKU[12] | PTC_01 |
| 53 | 40 | 26 | PTC_0 | ADC0_SE8 | PTC_0 | eTMR0_CH0 | SPI2_SIN | CAN3_RX |  | eTMR1_CH6 |  | WKU[13] | PTC_00 |
| 54 | 41 |  | PTD_9 |  | PTD_9 | LINFlexD4_TX |  | eTMR2_FLT3 |  | eTMR1_CH5 |  |  | PTD_09 |
| 55 | 42 |  | PTD_8 |  | PTD_8 | LINFlexD4_RX |  | eTMR2_FLT2 |  | eTMR1_CH4 |  |  | PTD_08 |
| 56 | 43 | 27 | PTC_17 | ADC0_SE15 | PTC_17 | eTMR1_FLT3 | CAN2_TX | SPI4_PCS0 | eTMR2_CH1 |  |  |  | PTC_17 |
| 57 | 44 | 28 | PTC_16 | ADC0_SE14 | PTC_16 | eTMR1_FLT2 | CAN2_RX | SPI4_SCK | eTMR2_CH0 |  |  |  | PTC_16 |
| 58 |  |  | PTB_22 | ADC0_SE19 | PTB_22 |  |  |  | LINFlexD1_TX |  |  |  | PTB_22 |
| 59 | 45 | 29 | PTC_15 | ADC0_SE13 | PTC_15 | eTMR1_CH3 | SPI2_SCK | SPI4_SIN | LINFlexD4_TX | TMU_IN8 |  | WKU[14] | PTC_15 |
| 60 |  |  | PTB_23 | ADC0_SE20 | PTB_23 |  | LINFlexD1_RX |  |  |  |  |  | PTB_23 |
| 61 | 46 | 30 | PTC_14 | ADC0_SE12 | PTC_14 | eTMR1_CH2 | SPI2_PCS0 | SPI4_SOUT | LINFlexD4_RX | TMU_IN9 |  | WKU[15] | PTC_14 |
| 62 |  |  | PTB_25 | ADC0_SE21 | PTB_25 |  |  | SPI4_PCS1 | SPI2_PCS0 |  |  |  | PTB_25 |
| 63 | 47 | 31 | PTB_3 | ADC0_SE7 | PTB_3 | eTMR1_CH1 | SPI0_SIN | eTMR1_QD_PHA |  | TMU_IN2 |  |  | PTB_03 |
| 64 |  |  | PTB_27 | ADC0_SE22 | PTB_27 | eTMR5_FLT2 |  |  | SPI2_SOUT |  |  |  | PTB_27 |
| 65 |  |  | PTB_28 | ADC0_SE23 | PTB_28 | eTMR5_FLT3 |  |  | SPI2_SIN |  |  |  | PTB_28 |
| 66 |  |  | VSS | VSS |  |  |  |  |  |  |  |  | VSS |
| 67 |  |  | VDD | VDD |  |  |  |  |  |  |  |  | VDD |
| 68 | 48 | 32 | PTB_2 | ADC0_SE6 | PTB_2 | eTMR1_CH0 | SPI0_SCK | eTMR1_QD_PHB |  | TMU_IN3 |  |  | PTB_02 |
| 69 |  |  | PTB_29 |  | PTB_29 |  |  |  | SPI2_SCK |  |  |  | PTB_29 |
| 70 | 49 |  | PTC_13 |  | PTC_13 | eTMR3_CH7 | eTMR2_CH7 |  |  |  |  |  | PTC_13 |
| 71 | 50 |  | PTC_12 |  | PTC_12 | eTMR3_CH6 | eTMR2_CH6 |  |  |  |  |  | PTC_12 |
| 72 |  |  | PTC_19 |  | PTC_19 |  |  |  | SPI2_PCS1 |  |  |  | PTC_19 |
| 73 |  |  | PTC_23 |  | PTC_23 | SPI0_SCK |  |  |  |  |  |  | PTC_23 |
| 74 | 51 |  | PTC_11 |  | PTC_11 | eTMR3_CH5 | eTMR4_CH2 | CAN5_TX |  | TMU_IN10 |  |  | PTC_11 |
| 75 | 52 |  | PTC_10 |  | PTC_10 | eTMR3_CH4 |  | CAN5_RX |  | TMU_IN11 |  |  | PTC_10 |
| 76 |  |  | PTC_27 |  | PTC_27 | eTMR4_CH4 |  |  |  |  |  |  | PTC_27 |
| 77 | 53 | 33 | PTB_1 | ADC0_SE5 | PTB_1 | LINFlexD0_TX | SPI0_SOUT | TCLK_IN0 | CAN0_TX | eTMR4_CH5 |  | WKU[16] | PTB_01 |
| 78 | 54 | 34 | PTB_0 | ADC0_SE4 | PTB_0 | LINFlexD0_RX | SPI0_PCS0 | LPTMR0_ALT3 | CAN0_RX | eTMR4_CH6 |  | WKU[17] | PTB_00 |
| 79 |  |  | PTC_28 |  | PTC_28 | eTMR4_CH7 |  |  |  |  |  |  | PTC_28 |
| 80 | 55 | 35 | PTC_9 |  | PTC_9 | LINFlexD1_TX | eTMR1_FLT1 | eTMR5_CH0 | CAN4_TX | SPI5_PCS1 |  |  | PTC_09 |
| 81 | 56 | 36 | PTC_8 |  | PTC_8 | LINFlexD1_RX | eTMR1_FLT0 | eTMR5_CH1 | CAN4_RX | SPI5_PCS0 |  |  | PTC_08 |
| 82 |  |  | PTC_29 |  | PTC_29 | eTMR5_CH2 |  |  |  |  |  |  | PTC_29 |
| 83 | 57 | 37 | PTA_7 | ADC0_SE3 | PTA_7 | eTMR0_FLT2 | eTMR5_CH3 | RTC_CLKIN | I2C2_SCL | SPI5_SCK |  | WKU[18] | PTA_07 |
| 84 |  |  | PTC_30 |  | PTC_30 | eTMR5_CH4 |  |  |  |  |  |  | PTC_30 |
| 85 | 58 | 38 | PTA_6 | ADC0_SE2 | PTA_6 | eTMR0_FLT1 | SPI1_PCS1 | eTMR5_CH5 | I2C2_SDA | SPI5_SIN |  | WKU[19] | PTA_06 |
| 86 |  |  | PTC_31 |  | PTC_31 | eTMR5_CH6 |  |  |  |  |  |  | PTC_31 |
| 87 | 59 | 39 | PTE_7 |  | PTE_7 | eTMR0_CH7 | eTMR3_FLT0 |  |  | SPI5_SOUT |  |  | PTE_07 |
| 88 |  |  | PTD_18 | ADC1_SE16 | PTD_18 | eTMR5_CH7 |  | CAN5_TX |  |  |  |  | PTD_18 |
| 89 |  |  | PTD_19 | ADC1_SE17 | PTD_19 |  |  | CAN5_RX |  |  |  |  | PTD_19 |
| 90 | 60 | 40 | VSS | VSS |  |  |  |  |  |  |  |  | VSS |
| 91 | 61 | 41 | VDD | VDD |  |  |  |  |  |  |  |  | VDD |
| 92 | 62 |  | PTA_17 |  | PTA_17 | eTMR0_CH6 | eTMR3_FLT0 | EWDG_OUT_b | eTMR5_FLT0 |  |  |  | PTA_17 |
| 93 | 63 |  | PTB_17 |  | PTB_17 | eTMR0_CH5 | SPI1_PCS3 | eTMR5_FLT1 |  |  |  |  | PTB_17 |
| 94 | 64 |  | PTB_16 | ADC1_SE15 | PTB_16 | eTMR0_CH4 | SPI1_SOUT |  |  |  |  |  | PTB_16 |
| 95 | 65 |  | PTB_15 | ADC1_SE14 | PTB_15 | eTMR0_CH3 | SPI1_SIN |  |  |  |  |  | PTB_15 |
| 96 | 66 |  | PTB_14 | ADC1_SE9 | PTB_14 | eTMR0_CH2 | SPI1_SCK |  |  |  |  |  | PTB_14 |
| 97 | 67 | 42 | PTB_13 | ADC1_SE8 | PTB_13 | eTMR0_CH1 | eTMR3_FLT1 | CAN2_TX |  |  |  | WKU[20] | PTB_13 |
| 98 | 68 | 43 | PTB_12 | ADC1_SE7 | PTB_12 | eTMR0_CH0 | eTMR3_FLT2 | CAN2_RX |  |  |  | WKU[21] | PTB_12 |
| 99 |  |  | PTD_22 | ADC1_SE18 | PTD_22 | eTMR4_FLT2 |  |  |  |  |  |  | PTD_22 |
| 100 | 69 | 44 | PTD_4 | ADC1_SE6 | PTD_4 | eTMR0_FLT3 | eTMR3_FLT3 |  |  | SPI5_PCS2 |  |  | PTD_04 |
| 101 | 70 | 45 | PTD_3 | ADC1_SE3 | PTD_3 | eTMR3_CH5 | SPI1_PCS0 | I2C1_SCL | CAN5_TX | TMU_IN4 | NMI_b | WKU[22] | PTD_03 |
| 102 | 71 | 46 | PTD_2 | ADC1_SE2 | PTD_2 | eTMR3_CH4 | SPI1_SOUT | I2C1_SDA | CAN5_RX | TMU_IN5 |  | WKU[23] | PTD_02 |
| 103 |  |  | PTD_23 | ADC1_SE19 | PTD_23 | eTMR4_FLT3 |  |  |  |  |  |  | PTD_23 |
| 104 | 72 | 47 | PTA_3 | ADC1_SE1 | PTA_3 | eTMR3_CH1 | I2C0_SCL | EWDG_IN |  | LINFlexD0_TX |  | WKU[24] | PTA_03 |
| 105 | 73 | 48 | PTA_2 | ADC1_SE0 | PTA_2 | eTMR3_CH0 | I2C0_SDA | EWDG_OUT_b |  | LINFlexD0_RX |  | WKU[25] | PTA_02 |
| 106 |  |  | PTD_24 | ADC1_SE20 | PTD_24 |  |  |  |  |  |  |  | PTD_24 |
| 107 | 74 |  | PTB_11 |  | PTB_11 | eTMR3_CH3 | LINFlexD5_TX |  |  |  |  |  | PTB_11 |
| 108 | 75 |  | PTB_10 |  | PTB_10 | eTMR3_CH2 | LINFlexD5_RX |  |  |  |  |  | PTB_10 |
| 109 | 76 |  | PTB_9 |  | PTB_9 | eTMR3_CH1 |  |  |  |  |  |  | PTB_09 |
| 110 |  |  | PTD_27 | ADC1_SE21 | PTD_27 | eTMR5_FLT2 |  |  |  |  |  |  | PTD_27 |
| 111 | 77 |  | PTB_8 |  | PTB_8 | eTMR3_CH0 |  |  |  |  |  |  | PTB_08 |
| 112 |  |  | PTD_28 | ADC1_SE22 | PTD_28 | eTMR5_FLT3 |  |  |  |  |  |  | PTD_28 |
| 113 | 78 | 49 | PTA_1 | ADC0_SE1/ACMP0_IN1 | PTA_1 | eTMR1_CH1 | LINFlexD5_TX |  | eTMR1_QD_PHA |  | TMU_OUT0 |  | PTA_01 |
| 114 |  |  | PTD_29 | ADC1_SE23 | PTD_29 |  |  |  |  |  |  |  | PTD_29 |
| 115 | 79 | 50 | PTA_0 | ADC0_SE0/ACMP0_IN0 | PTA_0 | eTMR2_CH1 | LINFlexD5_RX |  | eTMR2_QD_PHA |  | TMU_OUT3 |  | PTA_00 |
| 116 |  |  | PTD_30 |  | PTD_30 |  |  |  |  |  |  |  | PTD_30 |
| 117 | 80 | 51 | PTC_7 | ADC1_SE5 | PTC_7 | LINFlexD1_TX | CAN1_TX | eTMR3_CH3 |  | eTMR1_QD_PHA |  | WKU[26] | PTC_07 |
| 118 | 81 | 52 | PTC_6 | ADC1_SE4 | PTC_6 | LINFlexD1_RX | CAN1_RX | eTMR3_CH2 |  | eTMR1_QD_PHB |  | WKU[27] | PTC_06 |
| 119 | 82 |  | PTA_16 | ADC1_SE13 | PTA_16 | eTMR1_CH3 | SPI1_PCS2 |  |  |  |  |  | PTA_16 |
| 120 | 83 |  | PTA_15 | ADC1_SE12 | PTA_15 | eTMR1_CH2 | SPI0_PCS3 | SPI2_PCS3 |  |  |  |  | PTA_15 |
| 121 | 84 | 53 | PTE_6 | ADC1_SE11 | PTE_6 | SPI0_PCS2 |  | eTMR3_CH7 |  | ETM_TRACE_D2 | ETM_TRACE_CLKOUT | WKU[28] | PTE_06 |
| 122 | 85 | 54 | PTE_2 | ADC1_SE10 | PTE_2 | SPI0_SOUT | LPTMR0_ALT3 | eTMR3_CH6 |  | ETM_TRACE_D3 |  | WKU[29] | PTE_02 |
| 123 | 86 |  | VSS | VSS |  |  |  |  |  |  |  |  | VSS |
| 124 | 87 |  | VDD | VDD |  |  |  |  |  |  |  |  | VDD |
| 125 |  |  | PTE_19 |  | PTE_19 |  |  |  |  |  |  |  | PTE_19 |
| 126 |  |  | PTE_20 |  | PTE_20 | eTMR4_CH0 |  |  |  |  |  |  | PTE_20 |
| 127 | 88 |  | PTA_14 |  | PTA_14 | eTMR0_FLT0 | eTMR3_FLT1 | EWDG_IN |  | eTMR1_FLT0 |  |  | PTA_14 |
| 128 |  |  | PTE_21 |  | PTE_21 | eTMR4_CH1 |  |  |  |  |  |  | PTE_21 |
| 129 |  |  | PTE_22 |  | PTE_22 | eTMR4_CH2 |  |  |  |  |  |  | PTE_22 |
| 130 | 89 | 55 | PTA_13 |  | PTA_13 | eTMR1_CH7 | CAN1_TX | SPI3_PCS0 |  | eTMR2_QD_PHA |  | WKU[30] | PTA_13 |
| 131 |  |  | PTE_23 |  | PTE_23 | eTMR4_CH3 |  |  |  |  |  |  | PTE_23 |
| 132 |  |  | PTE_24 |  | PTE_24 | eTMR4_CH4 | CAN2_TX |  |  |  |  |  | PTE_24 |
| 133 |  |  | PTE_25 |  | PTE_25 | eTMR4_CH5 | CAN2_RX |  |  |  |  |  | PTE_25 |
| 134 | 90 | 56 | PTA_12 |  | PTA_12 | eTMR1_CH6 | CAN1_RX | SPI3_SCK |  | eTMR2_QD_PHB |  | WKU[31] | PTA_12 |
| 135 | 91 | 57 | PTA_11 |  | PTA_11 | eTMR1_CH5 |  | SPI3_SIN | ACMP0_ACTIVE |  |  |  | PTA_11 |
| 136 | 92 | 58 | PTA_10 |  | PTA_10 | eTMR1_CH4 |  | SPI3_SOUT |  |  | JTAG_TDO_SWD_SWO |  | PTA_10 |
| 137 | 93 | 59 | PTE_1 |  | PTE_1 | SPI0_SIN |  |  | SPI1_PCS0 | eTMR1_FLT1 |  | WKU[5] | PTE_01 |
| 138 | 94 | 60 | PTE_0 |  | PTE_0 | SPI0_SCK | TCLK_IN1 |  | SPI1_SOUT | eTMR1_FLT2 |  | WKU[6] | PTE_00 |
| 139 | 95 | 61 | PTC_5 |  | PTC_5 | eTMR2_CH0 | RTC_CLKOUT | SPI3_PCS1 |  | eTMR2_QD_PHB | JTAG_TDI |  | PTC_05 |
| 140 | 96 | 62 | PTC_4 | ACMP0_IN2 | PTC_4 | eTMR1_CH0 | RTC_CLKOUT |  | EWDG_IN | eTMR1_QD_PHB | JTAG_TCK_SWD_CLK |  | PTC_04 |
| 141 | 97 | 63 | PTA_5 |  | PTA_5 | CAN3_TX | TCLK_IN1 |  |  |  | RESET_b |  | PTA_05 |
| 142 | 98 | 64 | PTA_4 |  | PTA_4 | CAN3_RX |  | ACMP0_OUT | EWDG_OUT_b |  | JTAG_TMS_SWD_IO |  | PTA_04 |
| 143 | 99 |  | PTA_9 |  | PTA_9 | LINFlexD2_TX | SPI2_PCS0 |  | eTMR3_FLT2 | eTMR1_FLT3 | eTMR4_FLT0 |  | PTA_09 |
| 144 | 100 |  | PTA_8 |  | PTA_8 | LINFlexD2_RX | SPI2_SOUT |  | eTMR3_FLT3 | eTMR4_FLT1 |  |  | PTA_08 |
