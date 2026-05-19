# YTM32B1HA0x_PINMUX_V1.1

## IOMUX

| 100LQFP | 144LQFP | 176LQFP | NAME | Drive Strength | Default Function | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 | ALT6 | ALT7 | ALT8 | ALT9 | ALT10 | ALT11 | ALT12 | ALT13 | ALT14 | ALT15 | WKU | Default State |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 1 | PTA_18 | NORMAL |  |  | PTA_18 | eTMR4_CH0 | LINFlexD1_TX | SPI1_SOUT | eTMR5_CH0 |  |  |  | SPI6_SOUT |  |  |  |  | MPWM2_CH0 |  |  | Tri-State Input |
|  |  | 2 | PTA_19 | NORMAL |  |  | PTA_19 | eTMR4_CH1 | LINFlexD1_RX | SPI1_SCK |  |  |  |  | SPI6_SCK |  |  |  |  | MPWM2_CH1 |  |  | Tri-State Input |
|  |  | 3 | PTA_20 | NORMAL |  |  | PTA_20 | eTMR4_CH2 |  | SPI1_SIN |  |  |  |  | SPI6_SIN |  |  |  |  | MPWM2_CH2 |  |  | Tri-State Input |
| 1 | 1 | 4 | PTE_16 | NORMAL | ADC0_S28 | ADC0_S28 | PTE_16 | LINFlexD3_TX | SPI2_SIN | eTMR2_CH7 | eTMR4_FLT0 |  | TMU_OUT7 | FMU_ERR_OUT1 | SPI6_PCS0 |  |  |  |  | MPWM2_CH3 | FMU_ERR_IN1 | wku_ind[32] | Tri-State Input |
| 2 | 2 | 5 | PTE_15 | NORMAL | ADC0_S27 | ADC0_S27 | PTE_15 | LINFlexD3_RX | SPI2_SCK | eTMR2_CH6 | eTMR4_FLT1 |  | TMU_OUT6 | FMU_ERR_OUT0 | SPI6_PCS1 | ACMP1_ACTIVE |  |  |  | MPWM2_CH4 | FMU_ERR_IN0 | wku_ind[33] | Tri-State Input |
|  |  | 6 | PTA_21 | NORMAL |  |  | PTA_21 | eTMR4_CH3 |  | SPI1_PCS0 |  |  |  | SPI2_PCS2 | SPI6_PCS2 |  |  |  |  | MPWM2_CH5 |  |  | Tri-State Input |
| 3 | 3 | 7 | VDD11 | NORMAL | VDD11 | VDD11 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD11 |
| 4 | 4 | 8 | VDD25 | NORMAL | VDD25 | VDD25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD25 |
|  |  | 9 | PTA_22 | NORMAL |  |  | PTA_22 | eTMR4_CH4 |  | SPI1_PCS1 |  |  |  |  | SPI6_PCS3 |  |  |  |  | MPWM2_CH7 |  | wku_ind[34] | Tri-State Input |
| 5 | 5 | 10 | PTE_11 | NORMAL | ADC0_S30 | ADC0_S30 | PTE_11 | SPI2_PCS0 | LPTMR0_ALT1 | eTMR2_CH5 | LINFlexD3_TX | ETM_TRACE_D0 | TMU_OUT5 | LINFlexD4_TX |  |  |  |  | SENT1_RX_IN0 | MPWM2_CH8 |  | wku_ind[0] | Tri-State Input |
| 6 | 6 | 11 | PTE_10 | NORMAL | ADC0_S29 | ADC0_S29 | PTE_10 | SCU_CLKOUT | SPI2_PCS1 | eTMR2_CH4 | LINFlexD3_RX | CLKOUT_STANDBY | TMU_OUT4 | LINFlexD4_RX |  | SPI3_SIN |  |  | SENT1_RX_IN1 | MPWM2_CH9 |  | wku_ind[1] | Tri-State Input |
| 7 | 7 | 12 | PTE_13 | NORMAL |  |  | PTE_13 | eTMR4_CH5 | SPI2_PCS2 | eTMR2_FLT0 | SPI2_PCS0 |  |  | FMU_ERR_IN3 |  |  |  | eTMR3_CH5 | SENT1_RX_IN2 | MPWM2_CH10 |  |  | Tri-State Input |
|  |  | 13 | PTA_23 | NORMAL |  |  | PTA_23 | eTMR4_CH6 |  |  |  |  |  |  |  |  |  |  |  | MPWM2_CH11 |  |  | Tri-State Input |
| 8 | 8 | 14 | PTE_5 | NORMAL |  |  | PTE_5 | TCLK_IN2 | eTMR2_QD_PHA | eTMR2_CH3 | CAN0_TX | eTMR3_CH5 |  | FMU_ERR_IN2 |  |  |  |  | SENT1_RX_IN3 | MPWM2_CH12 |  | wku_ind[2] | Tri-State Input |
| 9 | 9 | 15 | PTE_4 | NORMAL |  |  | PTE_4 | ETM_TRACE_D1 | eTMR2_QD_PHB | eTMR2_CH2 | CAN0_RX | eTMR3_CH4 |  | SPI0_PCS0 | eTMR3_CH7 |  | SPI1_PCS1 |  |  | MPWM2_CH13 |  | wku_ind[3] | Tri-State Input |
|  |  | 16 | PTA_24 | NORMAL |  |  | PTA_24 | eTMR4_CH7 |  |  |  |  |  |  |  | eTMR4_CH0 |  |  |  | MPWM2_CH14 |  |  | Tri-State Input |
|  | 10 | 17 | PTA_25 | NORMAL |  |  | PTA_25 | eTMR5_CH0 |  |  |  |  |  |  |  |  |  |  |  | MPWM2_CH15 |  | wku_ind[57] | Tri-State Input |
| 10 | 11 | 18 | VDD | NORMAL | VDD | VDD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD |
|  | 12 | 19 | VSS | NORMAL | VSS | VSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VSS |
| 11 | 13 | 20 | VDDA | NORMAL | VDDA | VDDA |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDDA |
| 12 | 14 | 21 | VREFH | NORMAL | VREFH | VREFH |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VREFH |
| 13 | 15 | 22 | VREFL | NORMAL | VREFL | VREFL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VREFL |
| 14 | 16 | 23 | VSSA | NORMAL | VSSA | VSSA |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VSSA |
| 15 | 17 | 24 | PTB_7 | NORMAL | EXTAL | EXTAL | PTB_7 | I2C0_SCL |  | SPI3_SCK | eTMR4_FLT3 |  | TMU_OUT2 |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 16 | 18 | 25 | PTB_6 | NORMAL | XTAL | XTAL | PTB_6 | I2C0_SDA |  | SPI3_SIN | eTMR4_FLT2 |  | TMU_OUT1 |  |  |  |  |  |  |  |  |  | Tri-State Input |
|  | 19 | 26 | PTA_26 | NORMAL |  |  | PTA_26 | eTMR5_CH1 | SPI1_PCS0 | SPI0_PCS0 |  |  | ENET_PPS0 |  |  | eTMR4_CH1 |  |  |  |  |  | wku_ind[61] | Tri-State Input |
| 17 | 20 | 27 | PTE_14 | NORMAL |  |  | PTE_14 | eTMR0_FLT1 |  | eTMR2_FLT1 | SCU_CLKOUT |  | ENET_PPS1 | CAN4_RX |  |  | eTMR2_CH3 | LINFlexD5_TX |  |  |  | wku_ind[35] | Tri-State Input |
| 18 | 21 | 28 | PTE_3 | NORMAL |  |  | PTE_3 | eTMR0_FLT0 | SPI1_SIN | eTMR2_FLT0 | SPI3_SOUT | TMU_IN6 | ACMP0_OUT | CAN4_TX | eTMR2_CH3 |  | ENET_PPS0 | LINFlexD5_RX |  |  |  | wku_ind[4] | Tri-State Input |
|  | 22 | 29 | PTA_27 | NORMAL |  |  | PTA_27 | eTMR5_CH2 | SPI1_SOUT | LINFlexD0_TX | CAN0_TX |  |  |  | ENET_PPS1 |  | eTMR4_CH2 |  |  |  |  |  | Tri-State Input |
| 19 | 23 | 30 | PTE_12 | NORMAL | DAC1_OUT | DAC1_OUT | PTE_12 | eTMR0_FLT3 | LINFlexD2_TX | eTMR5_FLT0 | SPI3_PCS0 |  |  |  | eTMR3_CH5 | ENET_PPS3 |  | CAN5_TX |  |  |  |  | Tri-State Input |
|  | 24 | 31 | PTA_28 | NORMAL | ACMP1_IN5 | ACMP1_IN5 | PTA_28 | eTMR5_CH3 | SPI1_SCK | LINFlexD0_RX | CAN0_RX |  |  |  |  | eTMR4_CH3 |  |  |  |  |  |  | Tri-State Input |
| 20 | 25 | 32 | PTD_17 | NORMAL |  |  | PTD_17 | eTMR0_FLT2 | LINFlexD2_RX | eTMR5_FLT1 | SPI3_PCS0 |  | ENET_PPS2 | SPI5_PCS0 |  |  | CAN5_RX | eTMR2_CH2 | ENET_MII_RMII_MDC |  |  |  | Tri-State Input |
|  | 26 | 33 | PTA_29 | NORMAL |  |  | PTA_29 | eTMR5_CH4 |  | LINFlexD2_TX | SPI1_SIN |  |  |  | ENET_PPS2 | eTMR4_CH4 |  |  |  |  |  |  | Tri-State Input |
|  | 27 | 34 | PTA_30 | NORMAL |  |  | PTA_30 | eTMR5_CH5 | LINFlexD2_RX | SPI0_SOUT |  |  |  |  |  | eTMR4_CH5 | SPI1_SOUT |  |  |  |  | wku_ind[58] | Tri-State Input |
| 21 | 28 | 35 | PTD_16 | NORMAL | EXTAL32 | EXTAL32 | PTD_16 | eTMR0_CH1 | CAN4_TX | SPI0_SIN | ACMP0_ACTIVE | ETM_TRACE_D2 | ETM_TRACE_CLKOUT |  | eTMR4_CH7 |  | LINFlexD8_TX |  | ENET_MII_RMII_MDIO |  |  |  | Tri-State Input |
| 22 | 29 | 36 | PTD_15 | NORMAL | XTAL32 | XTAL32 | PTD_15 | eTMR0_CH0 | CAN4_RX | SPI0_SCK | SPI3_PCS1 | ETM_TRACE_D3 | LINFlexD8_RX | SAI1_SYNC | ENET_PPS2 |  | CAN3_RX | eTMR4_CH6 |  |  |  | wku_ind[36] | Tri-State Input |
| 23 | 30 | 37 | PTE_9 | NORMAL |  |  | PTE_9 | eTMR0_CH7 | SPI1_SCK | I2C2_SDA | ENET_PPS3 | ENET_MII_RMII_TX_EN |  | SPI5_SOUT |  |  | CAN3_TX | eTMR4_CH5 |  |  |  | wku_ind[7] | Tri-State Input |
|  | 31 | 38 | VSS | NORMAL | VSS | VSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VSS |
|  | 32 | 39 | VDD | NORMAL | VDD | VDD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD |
|  | 33 | 40 | PTA_31 | NORMAL |  |  | PTA_31 | eTMR5_CH6 |  | SPI0_PCS1 |  |  | TMU_OUT8 |  |  | eTMR4_CH6 |  |  |  | MPWM0_CH4 |  |  | Tri-State Input |
| 24 | 34 | 41 | PTD_14 | NORMAL |  |  | PTD_14 | eTMR2_CH5 | LINFlexD1_TX | I2C0_SCL | ENET_PPS0 | SAI1_MCLK | CLKOUT_RUN | SPI5_SCK | SPI5_PCS3 | SCU_CLKOUT | ACMP0_ACTIVE |  |  | MPWM2_CH6 |  |  | Tri-State Input |
| 25 | 35 | 42 | PTD_13 | NORMAL |  |  | PTD_13 | eTMR2_CH4 | LINFlexD1_RX | I2C0_SDA | ENET_PPS1 | SAI1_DATA0 | RTC_CLKOUT | SPI5_SIN | SPI5_PCS2 |  |  |  |  | MPWM0_CH5 |  | wku_ind[37] | Tri-State Input |
|  | 36 | 43 | PTB_18 | NORMAL | ADC0_S16 | ADC0_S16 | PTB_18 | eTMR5_CH7 |  | SPI1_PCS1 |  |  | TMU_OUT9 | LINFlexD2_TX |  | eTMR4_CH7 |  |  |  | MPWM0_CH6 |  |  | Tri-State Input |
|  |  | 44 | PTB_19 | NORMAL |  |  | PTB_19 | eTMR4_CH7 |  |  |  | eTMR5_CH7 | TMU_OUT10 | LINFlexD2_RX |  |  |  |  | QSPI_DQSA |  |  |  | Tri-State Input |
|  | 37 | 45 | PTB_20 | NORMAL | ADC0_S17 | ADC0_S17 | PTB_20 | LINFlexD3_TX |  |  | I2C1_SDA |  |  |  |  |  | eTMR5_CH0 |  | QSPI_IOFA[4] |  |  |  | Tri-State Input |
|  | 38 | 46 | PTB_21 | NORMAL | ADC0_S18 | ADC0_S18 | PTB_21 | LINFlexD3_RX |  |  | I2C1_SCL |  |  |  |  |  | eTMR5_CH1 |  | QSPI_IOFA[5] |  |  | wku_ind[38] | Tri-State Input |
| 26 | 39 | 47 | PTE_8 | NORMAL | ACMP0_IN3 | ACMP0_IN3 | PTE_8 | eTMR0_CH6 | SPI5_PCS1 | I2C2_SCL | ENET_MII_RMII_MDC | SAI1_BCLK |  | SPI3_PCS1 |  |  |  | SENT0_RX_IN0 | QSPI_IOFA[6] |  |  | wku_ind[8] | Tri-State Input |
| 27 | 40 | 48 | PTB_5 | HD |  |  | PTB_5 | eTMR0_CH5 | SPI0_PCS1 | SPI0_PCS0 | CLKOUT_RUN | TMU_IN0 | ENET_MII_RMII_MDC | ENET_MII_RMII_TXD[0] | eTMR4_CH3 | I2C2_SCL |  | SENT0_RX_IN1 | QSPI_IOFA[7] |  |  |  | Tri-State Input |
| 28 | 41 | 49 | PTB_4 | HD | ACMP1_IN4 | ACMP1_IN4 | PTB_4 | eTMR0_CH4 | SPI0_SOUT |  |  | TMU_IN1 | ENET_MII_RMII_MDIO | ENET_MII_RMII_TXD[1] | eTMR4_CH2 | SCU_CLKOUT |  | SENT0_RX_IN2 |  |  | QSPI_IOFB[0] |  | Tri-State Input |
| 29 | 42 | 50 | PTC_3 | NORMAL | ADC0_S11/ACMP0_IN4 | ADC0_S11/ACMP0_IN4 | PTC_3 | eTMR0_CH3 | CAN0_TX | LINFlexD0_TX | SPI4_PCS0 | QSPI_PCSFA |  |  |  |  |  | SENT0_RX_IN3 |  |  | QSPI_IOFB[3] | wku_ind[9] | Tri-State Input |
| 30 | 43 | 51 | PTC_2 | HD | ADC0_S10/ACMP0_IN5 | ADC0_S10/ACMP0_IN5 | PTC_2 | eTMR0_CH2 | CAN0_RX | LINFlexD0_RX | SPI4_SCK | ETM_TRACE_CLKOUT | QSPI_IOFA[3] | ENET_MII_RMII_TXD[1] | SPI0_PCS2 | SPI3_PCS2 | ENET_MII_RMII_TXD[0] |  |  |  |  |  | Tri-State Input |
| 31 | 44 | 52 | PTD_7 | HD | ACMP0_IN6 | ACMP0_IN6 | PTD_7 | LINFlexD2_TX | eTMR0_CH3 | eTMR2_FLT3 | SPI4_SIN | ETM_TRACE_D0 | QSPI_IOFA[1] | ENET_MII_RMII_TXD[0] |  |  | SPI3_PCS3 | SPI0_PCS3 | ENET_MII_RMII_TXD[1] |  |  |  | Tri-State Input |
| 32 | 45 | 53 | PTD_6 | NORMAL | ACMP_IN7 | ACMP_IN7 | PTD_6 | LINFlexD2_RX | eTMR0_CH2 | eTMR2_FLT2 | SPI4_SOUT |  | SPI0_PCS0 | ENET_MII_TXD3 | ENET_MII_RMII_TX_CLK |  | eTMR4_CH4 | ENET_MII_TXD2 |  |  | QSPI_IOFB[1] |  | Tri-State Input |
| 33 | 46 | 54 | PTD_5 | NORMAL |  |  | PTD_5 | eTMR2_CH3 | LPTMR0_ALT2 | eTMR2_FLT1 | SPI4_PCS1 | TMU_IN7 | SPI0_PCS1 | ENET_MII_TXD2 | ENET_MII_RX_CLK |  | eTMR0_CH2 | ENET_MII_TXD3 |  |  | QSPI_IOFB[2] | wku_ind[11] | Tri-State Input |
| 34 | 47 | 55 | PTD_12 | HD |  |  | PTD_12 | eTMR2_CH2 |  | ETM_TRACE_D1 | ENET_MII_RMII_TX_EN | SPI0_SOUT | QSPI_IOFA[2] |  | ENET_MII_RMII_TX_CLK |  |  | SPI5_SIN |  |  |  |  | Tri-State Input |
| 35 | 48 | 56 | PTD_11 | HD |  |  | PTD_11 | eTMR2_CH1 | eTMR2_QD_PHA | ETM_TRACE_D2 |  | SPI0_SCK | QSPI_IOFA[0] | ENET_MII_TXD2 | ENET_MII_RMII_TX_CLK |  | ENET_MII_RMII_TX_EN |  | SPI5_SOUT |  |  |  | Tri-State Input |
| 36 | 49 | 57 | PTD_10 | HD |  |  | PTD_10 | eTMR2_CH0 | eTMR2_QD_PHB | ETM_TRACE_D3 | SPI0_SIN | CLKOUT_RUN | QSPI_SCKFA | ENET_MII_TXD3 | ENET_MII_RX_CLK |  | eTMR4_CH2 |  | SPI5_SCK | SCU_CLKOUT |  |  | Tri-State Input |
| 37 | 50 | 58 | VSS | NORMAL | VSS | VSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VSS |
| 38 | 51 | 59 | VDD | NORMAL | VDD | VDD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD |
| 39 | 52 | 60 | PTC_1 | NORMAL | ADC0_S9 | ADC0_S9 | PTC_1 | eTMR0_CH1 | SPI2_SOUT | CAN3_TX |  | eTMR1_CH7 |  | CAN3_RX | ENET_MII_RMII_RXD[0] | ENET_MII_RX_CLK |  |  | ENET_MII_RMII_RXD[1] |  | QSPI_SCKFB | wku_ind[12] | Tri-State Input |
| 40 | 53 | 61 | PTC_0 | NORMAL | ADC0_S8 | ADC0_S8 | PTC_0 | eTMR0_CH0 | SPI2_SIN | CAN3_RX |  | eTMR1_CH6 | ENET_MII_RMII_TX_CLK | CAN3_TX | ENET_MII_RMII_RXD[1] |  |  |  | ENET_MII_RMII_RXD[0] |  | QSPI_DQSB | wku_ind[13] | Tri-State Input |
| 41 | 54 | 62 | PTD_9 | NORMAL |  |  | PTD_9 | LINFlexD4_TX |  | eTMR2_FLT3 |  | eTMR1_CH5 |  |  | ENET_MII_RXD2 | I2C1_SCL | LINFlexD6_TX | FMU_ERR_IN2 | ENET_MII_RMII_RXD[0] |  | QSPI_IOFB[4] |  | Tri-State Input |
| 42 | 55 | 63 | PTD_8 | NORMAL |  |  | PTD_8 | LINFlexD4_RX |  | eTMR2_FLT2 |  | eTMR1_CH4 |  | SPI3_SOUT | ENET_MII_RXD3 | I2C1_SDA | LINFlexD6_RX | FMU_ERR_IN3 | ENET_MII_RMII_RXD[1] |  | QSPI_IOFB[5] |  | Tri-State Input |
| 43 | 56 | 64 | PTC_17 | HD | ADC0_S15 | ADC0_S15 | PTC_17 | eTMR1_FLT3 | CAN2_TX | SPI4_PCS0 | eTMR2_CH1 |  |  | SPI3_SCK |  |  |  |  | ENET_MII_RMII_RX_DV |  | QSPI_IOFB[6] |  | Tri-State Input |
| 44 | 57 | 65 | PTC_16 | HD | ADC0_S14 | ADC0_S14 | PTC_16 | eTMR1_FLT2 | CAN2_RX | SPI4_SCK | eTMR2_CH0 |  | I2C1_SDA | SPI3_SIN | eTMR4_CH1 |  |  | LINFlexD2_RX | ENET_MII_RMII_RX_ER |  | QSPI_IOFB[7] |  | Tri-State Input |
|  | 58 | 66 | PTB_22 | NORMAL | ADC0_S19 | ADC0_S19 | PTB_22 | eTMR5_CH2 | SPI3_PCS1 |  | LINFlexD1_TX |  |  | CAN2_RX | ENET_MII_CRS | CAN1_TX |  |  |  |  | QSPI_IOFB[3] |  | Tri-State Input |
| 45 | 59 | 67 | PTC_15 | NORMAL | ADC0_S13 | ADC0_S13 | PTC_15 | eTMR1_CH3 | SPI2_SCK | SPI4_SIN | LINFlexD4_TX | TMU_IN8 | I2C1_SCL | CAN2_TX | ENET_MII_CRS | CAN1_RX | LINFlexD2_TX |  | ENET_MII_RMII_RX_DV | ENET_MII_RXD2 | QSPI_PCSFB | wku_ind[14] | Tri-State Input |
|  | 60 | 68 | PTB_23 | NORMAL | ADC0_S20 | ADC0_S20 | PTB_23 |  | LINFlexD1_RX |  |  |  | CAN1_RX |  | ENET_MII_COL | eTMR5_CH3 |  |  |  |  |  | wku_ind[39] | Tri-State Input |
|  |  | 69 | PTB_24 | NORMAL |  |  | PTB_24 | eTMR5_CH4 |  |  |  |  | CAN1_TX |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 46 | 61 | 70 | PTC_14 | NORMAL | ADC0_S12 | ADC0_S12 | PTC_14 | eTMR1_CH2 | SPI2_PCS0 | SPI4_SOUT | LINFlexD4_RX | TMU_IN9 | eTMR3_CH4 |  | ENET_MII_COL | CAN2_RX |  |  | ENET_MII_RMII_RX_ER | ENET_MII_RXD3 |  | wku_ind[15] | Tri-State Input |
|  | 62 | 71 | PTB_25 | NORMAL | ADC0_S21 | ADC0_S21 | PTB_25 |  |  | SPI4_PCS1 | SPI2_PCS0 |  |  |  | eTMR5_CH5 | CAN2_TX |  |  |  |  |  |  | Tri-State Input |
|  |  | 72 | PTB_26 | NORMAL |  |  | PTB_26 | eTMR5_CH6 |  |  |  |  |  |  |  |  |  |  |  |  |  | wku_ind[10] | Tri-State Input |
| 47 | 63 | 73 | PTB_3 | NORMAL | ADC0_S7 | ADC0_S7 | PTB_3 | eTMR1_CH1 | SPI0_SIN | eTMR1_QD_PHA | CAN4_TX | TMU_IN2 |  |  |  |  | SPI2_SOUT | SAI0_MCLK |  |  |  |  | Tri-State Input |
|  | 64 | 74 | PTB_27 | NORMAL | ADC0_S22 | ADC0_S22 | PTB_27 | eTMR5_FLT2 |  |  | SPI2_SOUT |  |  | LINFlexD5_TX | eTMR5_CH7 |  |  |  |  | MPWM0_CH0 |  |  | Tri-State Input |
|  | 65 | 75 | PTB_28 | NORMAL | ADC0_S23 | ADC0_S23 | PTB_28 | eTMR5_FLT3 |  |  | SPI2_SIN |  | ENET_PPS3 |  | LINFlexD5_RX |  |  |  |  | MPWM0_CH1 |  | wku_ind[59] | Tri-State Input |
|  | 66 | 76 | VSS | NORMAL | VSS | VSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VSS |
|  | 67 | 77 | VDD | NORMAL | VDD | VDD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD |
| 48 | 68 | 78 | PTB_2 | NORMAL | ADC0_S6 | ADC0_S6 | PTB_2 | eTMR1_CH0 | SPI0_SCK | eTMR1_QD_PHB |  | TMU_IN3 | SAI0_DATA0 |  | CAN4_RX | LINFlexD9_RX |  | SPI2_SIN |  | MPWM0_CH2 |  | wku_ind[40] | Tri-State Input |
|  | 69 | 79 | PTB_29 | NORMAL |  |  | PTB_29 |  |  |  | SPI2_SCK |  | SAI0_DATA1 | LINFlexD6_TX |  | LINFlexD9_TX |  |  |  | MPWM0_CH3 |  |  | Tri-State Input |
|  |  | 80 | PTB_30 | NORMAL |  |  | PTB_30 |  |  |  |  |  |  |  |  |  |  |  |  | MPWM0_CH4 |  |  | Tri-State Input |
| 49 | 70 | 81 | PTC_13 | NORMAL |  |  | PTC_13 | eTMR3_CH7 | eTMR2_CH7 |  |  |  | SAI0_SYNC |  |  |  | eTMR3_CH3 |  |  |  |  |  | Tri-State Input |
|  |  | 82 | PTB_31 | NORMAL |  |  | PTB_31 |  |  |  |  |  |  |  | CAN7_TX |  |  |  |  | MPWM0_CH5 |  |  | Tri-State Input |
|  |  | 83 | PTC_18 | NORMAL |  |  | PTC_18 |  |  |  |  |  | SAI0_DATA2 | LINFlexD6_RX | CAN7_RX |  |  |  |  | MPWM0_CH6 |  | wku_ind[60] | Tri-State Input |
| 50 | 71 | 84 | PTC_12 | NORMAL |  |  | PTC_12 | eTMR3_CH6 | eTMR2_CH6 | SPI2_PCS1 |  |  | SAI0_BCLK |  | CAN6_TX |  | eTMR3_CH2 |  |  |  |  |  | Tri-State Input |
|  | 72 | 85 | PTC_19 | NORMAL |  |  | PTC_19 |  |  |  | SPI2_PCS1 |  | SAI0_DATA3 | LINFlexD7_TX | CAN6_RX |  |  |  |  | MPWM0_CH7 |  |  | Tri-State Input |
|  |  | 86 | PTC_20 | NORMAL |  |  | PTC_20 |  |  |  |  |  |  | LINFlexD7_RX |  |  |  |  |  | MPWM0_CH8 |  |  | Tri-State Input |
|  |  | 87 | PTC_21 | NORMAL |  |  | PTC_21 |  |  |  |  |  |  |  |  |  |  |  |  | MPWM0_CH9 |  |  | Tri-State Input |
|  |  | 88 | PTC_22 | NORMAL |  |  | PTC_22 |  |  |  |  |  |  | eTMR1_CH0 |  |  |  |  |  | MPWM0_CH10 |  |  | Tri-State Input |
|  | 73 | 89 | PTC_23 | NORMAL |  |  | PTC_23 | SPI0_SCK |  |  |  |  |  |  |  |  |  |  |  | MPWM0_CH11 |  | wku_ind[62] | Tri-State Input |
|  |  | 90 | PTC_24 | NORMAL |  |  | PTC_24 | eTMR4_CH0 | eTMR3_CH0 |  |  |  |  |  | CAN6_TX |  |  |  |  | MPWM0_CH12 |  |  | Tri-State Input |
|  |  | 91 | PTC_25 | NORMAL |  |  | PTC_25 | eTMR4_CH1 | eTMR3_CH1 |  | SPI4_PCS1 |  |  |  | CAN6_RX |  |  |  |  | MPWM0_CH13 |  | wku_ind[41] | Tri-State Input |
| 51 | 74 | 92 | PTC_11 | NORMAL |  |  | PTC_11 | eTMR3_CH5 | eTMR4_CH2 | CAN5_TX |  | TMU_IN10 |  |  | CAN5_RX |  | eTMR3_CH1 | SPI4_SOUT |  |  |  | wku_ind[42] | Tri-State Input |
|  |  | 93 | PTC_26 | NORMAL |  |  | PTC_26 | eTMR4_CH3 | eTMR3_CH3 |  |  |  | SPI4_SIN |  | CAN5_RX |  |  |  |  | MPWM0_CH14 |  |  | Tri-State Input |
| 52 | 75 | 94 | PTC_10 | NORMAL | ADC1_S27 | ADC1_S27 | PTC_10 | eTMR3_CH4 |  | CAN5_RX | SPI4_PCS0 | TMU_IN11 | eTMR3_CH0 | eTMR0_CH6 |  | CAN5_TX |  | SPI2_PCS1 |  |  |  |  | Tri-State Input |
|  | 76 | 95 | PTC_27 | NORMAL |  |  | PTC_27 | eTMR4_CH4 |  |  |  |  | SPI4_SCK | CAN5_TX |  |  | eTMR3_CH4 |  |  | MPWM0_CH15 |  |  | Tri-State Input |
| 53 | 77 | 96 | PTB_1 | NORMAL | ADC0_S5 | ADC0_S5 | PTB_1 | LINFlexD0_TX | SPI0_SOUT | TCLK_IN0 | CAN0_TX | eTMR4_CH5 |  |  |  | eTMR3_CH5 |  | eTMR0_CH7 |  | MPWM0_CH0 |  | wku_ind[16] | Tri-State Input |
| 54 | 78 | 97 | PTB_0 | NORMAL | ADC0_S4 | ADC0_S4 | PTB_0 | LINFlexD0_RX | SPI0_PCS0 | LPTMR0_ALT3 | CAN0_RX | eTMR4_CH6 |  |  |  | eTMR3_CH6 |  | eTMR0_CH3 |  | MPWM0_CH1 |  | wku_ind[17] | Tri-State Input |
|  | 79 | 98 | PTC_28 | NORMAL |  |  | PTC_28 | eTMR4_CH7 |  |  | I2C1_SCL |  |  | CAN3_TX |  |  | eTMR3_CH7 |  |  |  |  |  | Tri-State Input |
| 55 | 80 | 99 | PTC_9 | HD | ACMP1_IN6 | ACMP1_IN6 | PTC_9 | LINFlexD1_TX | eTMR1_FLT1 | eTMR5_CH0 | CAN4_TX | SPI0_SIN | I2C0_SDA |  | CAN1_RX | eTMR4_CH0 |  |  | SPI5_PCS1 | MPWM0_CH2 |  | wku_ind[43] | Tri-State Input |
| 56 | 81 | 100 | PTC_8 | HD | DAC0_OUT | DAC0_OUT | PTC_8 | LINFlexD1_RX | eTMR1_FLT0 | eTMR5_CH1 | CAN4_RX | SPI0_SCK | I2C0_SCL |  | CAN1_TX | eTMR4_CH1 |  |  | SPI5_PCS0 | MPWM0_CH3 |  |  | Tri-State Input |
|  | 82 | 101 | PTC_29 | NORMAL |  |  | PTC_29 | eTMR5_CH2 |  |  | I2C1_SDA |  |  | CAN3_RX | eTMR4_CH2 |  |  |  |  |  |  |  | Tri-State Input |
| 57 | 83 | 102 | PTA_7 | NORMAL | ADC0_S3 | ADC0_S3 | PTA_7 | eTMR0_FLT2 | eTMR5_CH3 | RTC_CLKIN | I2C2_SCL |  |  | LINFlexD3_TX | SPI0_PCS1 | eTMR4_CH3 | CAN0_TX |  |  | SPI5_SCK |  | wku_ind[18] | Tri-State Input |
|  | 84 | 103 | PTC_30 | NORMAL |  |  | PTC_30 | eTMR5_CH4 |  |  |  |  |  | CAN4_TX | eTMR4_CH4 |  |  |  |  |  |  |  | Tri-State Input |
| 58 | 85 | 104 | PTA_6 | NORMAL | ADC0_S2 | ADC0_S2 | PTA_6 | eTMR0_FLT1 | SPI1_PCS1 | eTMR5_CH5 | I2C2_SDA | SPI3_PCS1 |  | LINFlexD3_RX | CAN0_RX | eTMR4_CH5 |  |  | SPI5_SIN |  |  | wku_ind[19] | Tri-State Input |
|  | 86 | 105 | PTC_31 | NORMAL |  |  | PTC_31 | eTMR5_CH6 |  | I2C1_SDA |  |  |  |  | CAN4_RX |  | eTMR4_CH6 |  |  |  |  |  | Tri-State Input |
| 59 | 87 | 106 | PTE_7 | NORMAL |  |  | PTE_7 | eTMR0_CH7 | eTMR3_FLT0 |  |  | SPI3_SCK |  |  | LINFlexD4_RX |  | SPI5_SOUT |  |  |  |  |  | Tri-State Input |
|  | 88 | 107 | PTD_18 | NORMAL | ADC1_S16 | ADC1_S16 | PTD_18 | eTMR5_CH7 | CAN5_TX | I2C1_SCL | I2C1_SDA |  |  |  | CAN7_TX |  |  |  |  |  |  |  | Tri-State Input |
|  | 89 | 108 | PTD_19 | NORMAL | ADC1_S17 | ADC1_S17 | PTD_19 |  | CAN5_RX |  | I2C1_SCL |  |  |  | CAN7_RX |  |  |  |  |  |  |  | Tri-State Input |
| 60 | 90 | 109 | VSS | NORMAL | VSS | VSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VSS |
| 61 | 91 | 110 | VDD | NORMAL | VDD | VDD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD |
| 62 | 92 | 111 | PTA_17 | NORMAL |  |  | PTA_17 | eTMR0_CH6 | eTMR3_FLT0 |  | eTMR5_FLT0 | SPI3_SOUT |  | LINFlexD4_TX |  |  |  |  |  | MPWM2_CH0 |  |  | Tri-State Input |
| 63 | 93 | 112 | PTB_17 | NORMAL | ADC1_S26 | ADC1_S26 | PTB_17 | eTMR0_CH5 | SPI1_PCS3 | eTMR5_FLT1 |  | SPI3_PCS0 |  | LINFlexD4_RX |  | eTMR3_CH7 |  |  |  | MPWM2_CH1 |  | wku_ind[44] | Tri-State Input |
|  |  | 113 | PTD_20 | NORMAL | ADC1_S31 | ADC1_S31 | PTD_20 | eTMR5_CH1 |  |  | SPI1_PCS2 | SPI3_SIN |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 64 | 94 | 114 | PTB_16 | NORMAL | ADC1_S15 | ADC1_S15 | PTB_16 | eTMR0_CH4 | SPI1_SOUT | LINFlexD4_TX |  |  |  |  | SENT1_RX_IN0 |  |  |  |  |  |  | wku_ind[53] | Tri-State Input |
| 65 | 95 | 115 | PTB_15 | NORMAL | ADC1_S14 | ADC1_S14 | PTB_15 | eTMR0_CH3 | SPI1_SIN |  |  | LINFlexD7_TX |  |  | SENT1_RX_IN1 |  |  |  |  | MPWM2_CH2 |  | wku_ind[54] | Tri-State Input |
| 66 | 96 | 116 | PTB_14 | NORMAL | ADC1_S9 | ADC1_S9 | PTB_14 | eTMR0_CH2 | SPI1_SCK |  |  | LINFlexD7_RX |  |  | SENT1_RX_IN2 |  |  |  |  | MPWM2_CH3 |  |  | Tri-State Input |
|  |  | 117 | PTD_21 | NORMAL |  |  | PTD_21 | eTMR5_CH2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 67 | 97 | 118 | PTB_13 | NORMAL | ADC1_S8 | ADC1_S8 | PTB_13 | eTMR0_CH1 | eTMR3_FLT1 | CAN2_TX |  |  | LINFlexD8_TX | SPI3_PCS2 | SENT1_RX_IN3 |  |  |  |  |  |  | wku_ind[20] | Tri-State Input |
| 68 | 98 | 119 | PTB_12 | NORMAL | ADC1_S7 | ADC1_S7 | PTB_12 | eTMR0_CH0 | eTMR3_FLT2 | CAN2_RX |  |  | LINFlexD8_RX | SPI3_PCS3 |  |  |  |  |  |  |  | wku_ind[21] | Tri-State Input |
|  | 99 | 120 | PTD_22 | NORMAL | ADC1_S18 | ADC1_S18 | PTD_22 | eTMR4_FLT2 |  |  |  |  |  |  | eTMR5_CH3 |  |  |  |  |  |  |  | Tri-State Input |
| 69 | 100 | 121 | PTD_4 | NORMAL | ADC1_S6 | ADC1_S6 | PTD_4 | eTMR0_FLT3 | eTMR3_FLT3 |  |  |  | SPI5_PCS0 |  | eTMR5_CH7 | SPI1_PCS1 |  | SPI5_PCS2 |  |  |  | wku_ind[45] | Tri-State Input |
| 70 | 101 | 122 | PTD_3 | NORMAL | ADC1_S3 | ADC1_S3 | PTD_3 | eTMR3_CH5 | SPI1_PCS0 | I2C1_SCL | CAN5_TX | TMU_IN4 | CORE_NMI_b |  | eTMR5_CH6 | LINFlexD3_RX |  |  |  |  |  | wku_ind[22] | Tri-State Input |
| 71 | 102 | 123 | PTD_2 | NORMAL | ADC1_S2 | ADC1_S2 | PTD_2 | eTMR3_CH4 | SPI1_SOUT | I2C1_SDA | CAN5_RX | TMU_IN5 | SPI5_SOUT |  | eTMR5_CH5 | LINFlexD3_TX |  |  |  |  |  | wku_ind[23] | Tri-State Input |
|  | 103 | 124 | PTD_23 | NORMAL | ADC1_S19 | ADC1_S19 | PTD_23 | eTMR4_FLT3 |  |  |  |  |  |  | eTMR5_CH4 |  |  |  |  |  |  |  | Tri-State Input |
| 72 | 104 | 125 | PTA_3 | NORMAL | ADC1_S1 | ADC1_S1 | PTA_3 | eTMR3_CH1 | I2C0_SCL |  |  | LINFlexD0_TX | SPI5_SCK | FMU_ERR_OUT1 | eTMR5_CH4 | SPI1_SCK |  |  |  |  | FMU_ERR_IN1 | wku_ind[24] | Tri-State Input |
| 73 | 105 | 126 | PTA_2 | NORMAL | ADC1_S0/ACMP1_IN2 | ADC1_S0/ACMP1_IN2 | PTA_2 | eTMR3_CH0 | I2C0_SDA |  |  | LINFlexD0_RX | SPI5_SIN | FMU_ERR_OUT0 | eTMR5_CH3 |  |  |  | SPI1_SIN |  | FMU_ERR_IN0 | wku_ind[25] | Tri-State Input |
|  | 106 | 127 | PTD_24 | NORMAL | ADC1_S20 | ADC1_S20 | PTD_24 |  |  |  |  |  |  |  | eTMR5_CH5 |  |  |  |  |  |  |  | Tri-State Input |
| 74 | 107 | 128 | PTB_11 | NORMAL | ADC1_S30 | ADC1_S30 | PTB_11 | eTMR3_CH3 | LINFlexD5_TX |  |  |  |  | SPI4_SIN | eTMR5_CH2 |  |  |  |  |  |  | wku_ind[63] | Tri-State Input |
|  |  | 129 | VDD | NORMAL | VDD | VDD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD |
|  |  | 130 | VSS | NORMAL | VSS | VSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VSS |
| 75 | 108 | 131 | PTB_10 | NORMAL | ADC1_S29 | ADC1_S29 | PTB_10 | eTMR3_CH2 | LINFlexD5_RX | SAI1_MCLK | LINFlexD9_TX |  |  | SPI4_SCK | eTMR5_CH1 |  |  |  |  |  |  |  | Tri-State Input |
|  |  | 132 | PTD_25 | NORMAL |  |  | PTD_25 | eTMR5_CH6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 76 | 109 | 133 | PTB_9 | NORMAL | ADC0_S25 | ADC0_S25 | PTB_9 | eTMR5_CH0 | eTMR3_CH1 | SAI1_DATA0 | LINFlexD9_RX |  |  | SPI4_SOUT |  |  |  |  |  |  |  | wku_ind[46] | Tri-State Input |
|  |  | 134 | PTD_26 | NORMAL |  |  | PTD_26 | eTMR5_CH7 |  |  |  | SPI5_SCK |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
|  | 110 | 135 | PTD_27 | NORMAL | ADC1_S21 | ADC1_S21 | PTD_27 | eTMR5_FLT2 |  |  |  | SPI5_SOUT |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 77 | 111 | 136 | PTB_8 | NORMAL | ADC0_S24 | ADC0_S24 | PTB_8 | eTMR3_CH0 |  | SAI1_BCLK |  | SPI0_PCS5 |  | SPI4_PCS0 | eTMR4_CH7 |  |  |  |  |  |  | wku_ind[47] | Tri-State Input |
|  | 112 | 137 | PTD_28 | NORMAL | ADC1_S22 | ADC1_S22 | PTD_28 | eTMR5_FLT3 |  |  |  | SPI5_SIN |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 78 | 113 | 138 | PTA_1 | NORMAL | ADC0_S1/ACMP_IN1 | ADC0_S1/ACMP_IN1 | PTA_1 | eTMR1_CH1 | LINFlexD5_TX |  | eTMR1_QD_PHA | SPI0_PCS6 | TMU_OUT0 | SPI4_PCS1 |  |  |  |  |  |  |  | wku_ind[55] | Tri-State Input |
|  | 114 | 139 | PTD_29 | NORMAL | ADC1_S23 | ADC1_S23 | PTD_29 |  |  |  |  | SPI5_PCS2 |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 79 | 115 | 140 | PTA_0 | NORMAL | ADC0_S0/ACMP_IN0 | ADC0_S0/ACMP_IN0 | PTA_0 | eTMR2_CH1 | LINFlexD5_RX |  | eTMR2_QD_PHA | SPI0_PCS7 | TMU_OUT3 | SPI4_PCS2 |  | eTMR3_CH0 |  |  |  |  | FMU_ERR_IN2 |  | Tri-State Input |
|  | 116 | 141 | PTD_30 | NORMAL |  |  | PTD_30 |  |  |  |  | SPI5_PCS3 |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
|  |  | 142 | PTD_31 | NORMAL |  |  | PTD_31 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 80 | 117 | 143 | PTC_7 | NORMAL | ADC1_S5 | ADC1_S5 | PTC_7 | LINFlexD1_TX | CAN1_TX | eTMR3_CH3 | eTMR3_CH7 | eTMR1_QD_PHA |  | I2C1_SCL |  | SPI0_PCS0 |  | CAN2_TX |  |  | FMU_ERR_IN3 | wku_ind[26] | Tri-State Input |
| 81 | 118 | 144 | PTC_6 | NORMAL | ADC1_S4 | ADC1_S4 | PTC_6 | LINFlexD1_RX | CAN1_RX | eTMR3_CH2 | eTMR3_CH6 | eTMR1_QD_PHB |  | I2C1_SDA |  | SPI0_PCS1 |  | CAN2_RX | SPI1_PCS1 | MPWM1_CH9 |  | wku_ind[27] | Tri-State Input |
|  |  | 145 | PTE_17 | NORMAL |  |  | PTE_17 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 82 | 119 | 146 | PTA_16 | NORMAL | ADC1_S13 | ADC1_S13 | PTA_16 | eTMR1_CH3 | SPI1_PCS2 | SPI0_PCS4 | LINFlexD6_TX |  |  | SPI4_PCS3 |  |  |  |  |  | MPWM1_CH0 |  | wku_ind[56] | Tri-State Input |
|  |  | 147 | PTE_18 | NORMAL |  |  | PTE_18 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
| 83 | 120 | 148 | PTA_15 | NORMAL | ADC1_S12 | ADC1_S12 | PTA_15 | eTMR1_CH2 | SPI0_PCS3 | SPI2_PCS3 | LINFlexD6_RX | SPI5_PCS0 | SAI0_SYNC |  |  |  |  |  |  | MPWM1_CH1 |  | wku_ind[48] | Tri-State Input |
| 84 | 121 | 149 | PTE_6 | NORMAL | ADC1_S11 | ADC1_S11 | PTE_6 | SPI0_PCS2 |  | eTMR3_CH7 |  | SAI0_DATA1 |  | eTMR4_CH6 |  | ETM_TRACE_D2 | ETM_TRACE_CLKOUT |  |  | MPWM1_CH2 |  | wku_ind[28] | Tri-State Input |
| 85 | 122 | 150 | PTE_2 | NORMAL | ADC1_S10 | ADC1_S10 | PTE_2 | SPI0_SOUT | LPTMR0_ALT3 | eTMR3_CH6 |  | SAI0_DATA2 |  | eTMR0_CH3 | eTMR4_CH0 |  | ETM_TRACE_D3 |  |  | MPWM1_CH3 |  | wku_ind[29] | Tri-State Input |
| 86 | 123 | 151 | VSS | NORMAL | VSS | VSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VSS |
| 87 | 124 | 152 | VDD | NORMAL | VDD | VDD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD |
|  | 125 | 153 | PTE_19 | NORMAL |  |  | PTE_19 | eTMR2_CH6 |  |  | I2C4_SDA |  |  |  |  |  |  |  |  |  |  |  | Tri-State Input |
|  | 126 | 154 | PTE_20 | NORMAL |  |  | PTE_20 | eTMR4_CH0 |  |  | I2C4_SCL |  |  |  | eTMR3_CH0 |  |  |  |  |  |  |  | Tri-State Input |
| 88 | 127 | 155 | PTA_14 | NORMAL | ADC1_S28 | ADC1_S28 | PTA_14 | eTMR0_FLT0 | eTMR3_FLT1 |  |  | eTMR1_FLT0 | SAI0_DATA3 |  | eTMR3_CH4 | SPI1_PCS3 | SPI5_PCS1 |  |  | MPWM1_CH0 |  |  | Tri-State Input |
|  | 128 | 156 | PTE_21 | NORMAL |  |  | PTE_21 | eTMR4_CH1 |  |  |  | SPI4_SIN |  |  | eTMR3_CH1 |  |  |  |  | MPWM1_CH1 |  |  | Tri-State Input |
|  | 129 | 157 | PTE_22 | NORMAL |  |  | PTE_22 | eTMR4_CH2 |  |  |  | SPI4_SCK |  |  | eTMR3_CH2 |  |  |  |  | MPWM1_CH2 |  |  | Tri-State Input |
| 89 | 130 | 158 | PTA_13 | NORMAL | ADC1_S25 | ADC1_S25 | PTA_13 | eTMR1_CH7 | CAN1_TX | SPI3_PCS0 |  | eTMR2_QD_PHA | SAI0_DATA0 | SPI1_PCS4 | eTMR3_CH3 |  |  |  |  | MPWM1_CH3 |  | wku_ind[30] | Tri-State Input |
|  | 131 | 159 | PTE_23 | NORMAL |  |  | PTE_23 | eTMR4_CH3 | CAN1_RX |  |  | SPI4_PCS0 |  |  | eTMR3_CH3 |  |  |  |  | MPWM1_CH4 |  | wku_ind[49] | Tri-State Input |
|  | 132 | 160 | PTE_24 | NORMAL |  |  | PTE_24 | eTMR4_CH4 | CAN2_TX |  |  | SPI4_PCS1 |  |  | eTMR3_CH4 |  |  |  |  | MPWM1_CH5 |  |  | Tri-State Input |
|  | 133 | 161 | PTE_25 | NORMAL |  |  | PTE_25 | eTMR4_CH5 | CAN2_RX |  |  | SPI4_SOUT |  |  | eTMR3_CH5 |  |  |  |  | MPWM1_CH6 |  | wku_ind[50] | Tri-State Input |
| 90 | 134 | 162 | PTA_12 | NORMAL | ADC1_S24 | ADC1_S24 | PTA_12 | eTMR1_CH6 | CAN1_RX | SPI3_SCK |  | eTMR2_QD_PHB | SAI0_BCLK | ACMP1_OUT | SPI1_PCS5 | eTMR3_CH2 |  | CLKOUT_STANDBY | SENT0_RX_IN0 | MPWM1_CH7 |  | wku_ind[31] | Tri-State Input |
| 91 | 135 | 163 | PTA_11 | HD |  |  | PTA_11 | eTMR1_CH5 | CAN1_TX | SPI3_SIN | ACMP0_ACTIVE | SPI1_PCS0 | TMU_OUT8 |  | eTMR3_CH1 | SPI7_PCS0 |  |  | SENT0_RX_IN1 | MPWM1_CH8 |  |  | Tri-State Input |
| 92 | 136 | 164 | PTA_10 | HD | JTAG_TDO_SWD_SWO |  | PTA_10 | eTMR1_CH4 |  | SPI3_SOUT |  |  | TMU_OUT9 |  |  |  |  |  | SENT0_RX_IN2 |  | JTAG_TDO_SWD_SWO |  | Tri-State Input |
| 93 | 137 | 165 | PTE_1 | HD |  |  | PTE_1 | SPI0_SIN |  | I2C1_SCL | SPI1_PCS0 | eTMR1_FLT1 | TMU_OUT10 |  | SPI0_SCK | SPI7_SIN | LINFlexD7_TX |  | SENT0_RX_IN3 | MPWM1_CH10 |  | wku_ind[5] | Tri-State Input |
| 94 | 138 | 166 | PTE_0 | HD |  |  | PTE_0 | SPI0_SCK | TCLK_IN1 | I2C1_SDA | SPI1_SOUT | eTMR1_FLT2 | TMU_OUT11 |  | SPI0_SIN | SPI7_SOUT | LINFlexD7_RX |  |  | MPWM1_CH11 |  | wku_ind[6] | Tri-State Input |
|  |  | 167 | PTE_26 | NORMAL |  |  | PTE_26 | eTMR3_CH6 | eTMR4_CH6 |  |  |  |  |  |  |  |  |  |  | MPWM1_CH12 |  |  | Tri-State Input |
| 95 | 139 | 168 | PTC_5 | NORMAL | JTAG_TDI |  | PTC_5 | eTMR2_CH0 | RTC_CLKOUT | SPI3_PCS1 | I2C3_SDA | eTMR2_QD_PHB | SAI0_MCLK |  |  | SPI7_SCK |  |  |  | MPWM1_CH13 | JTAG_TDI |  | Pull Down Input |
| 96 | 140 | 169 | PTC_4 | NORMAL | JTAG_TCK_SWD_CLK | ACMP0_IN2/ACMP1_IN3 | PTC_4 | eTMR1_CH0 | RTC_CLKOUT |  | I2C3_SCL | eTMR1_QD_PHB |  |  |  |  |  |  |  |  | JTAG_TCK_SWD_CLK |  | Pull Up Input |
| 97 | 141 | 170 | PTA_5 | NORMAL | RCU_RESET_b |  | PTA_5 | CAN3_TX | TCLK_IN1 |  |  |  |  | FMU_ERR_IN3 |  |  |  |  |  |  | RCU_RESET_b |  | Pull Up Input |
|  |  | 171 | VSS | NORMAL | VSS | VSS |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VSS |
|  |  | 172 | VDD | NORMAL | VDD | VDD |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | VDD |
| 98 | 142 | 173 | PTA_4 | NORMAL | JTAG_TMS_SWD_IO |  | PTA_4 | CAN3_RX |  | ACMP0_OUT |  |  |  | FMU_ERR_IN2 |  | SPI7_PCS1 |  |  |  |  | JTAG_TMS_SWD_IO |  | Pull Up Input |
|  |  | 174 | PTE_27 | NORMAL |  |  | PTE_27 | eTMR3_CH7 | eTMR4_CH7 |  |  |  |  |  |  | SPI7_PCS3 |  |  |  |  |  |  | Tri-State Input |
| 99 | 143 | 175 | PTA_9 | NORMAL | ADC0_S31 | ADC0_S31 | PTA_9 | LINFlexD2_TX | SPI2_PCS0 | SPI1_SIN | eTMR3_FLT2 | eTMR1_FLT3 | eTMR4_FLT0 |  | SPI3_PCS0 | SPI7_PCS2 |  | FMU_ERR_IN2 |  | MPWM1_CH14 |  | wku_ind[51] | Tri-State Input |
| 100 | 144 | 176 | PTA_8 | NORMAL | ADC0_S26 | ADC0_S26 | PTA_8 | LINFlexD2_RX | SPI2_SOUT | SPI1_SCK | eTMR3_FLT3 | eTMR4_FLT1 |  |  | eTMR4_CH4 |  |  | FMU_ERR_IN3 |  | MPWM1_CH15 |  | wku_ind[52] | Tri-State Input |

## Version

| Version | Author | Description |
| --- | --- | --- |
| V1.0 | Major Lin | Initial version. |
| V1.1 | Major Lin | Update power pads |
