const photoFiles = ["Am Stadtgraben 4/20240722_125312.jpg", "Am Stadtgraben 4/20240722_125320.jpg", "Am Stadtgraben 4/IMG_20240722_125230_939.jpg", "Am Stadtgraben 4/IMG_20240722_125232_991.jpg", "Grabenweg 4/IMG_20240722_135232_919.jpg", "Grabenweg 4/IMG_20240722_135236_909.jpg", "Hachtorstra\u00dfe 1/IMG-20240722-WA0024.jpg", "Hachtorstra\u00dfe 1/IMG-20240722-WA0028.jpg", "Hachtorstra\u00dfe 1/IMG_20240723_104341_978.jpg", "Hachtorstra\u00dfe 1/IMG_20240729_131528_860.jpg", "Hachtorstra\u00dfe 1/IMG_20240729_131536_036.jpg", "Hachtorstra\u00dfe 1/IMG_20240729_154704_975.jpg", "Hachtorstra\u00dfe 14/IMG_20240722_100949_802.jpg", "Hachtorstra\u00dfe 323/IMG-20240726-WA0011.jpg", "Hachtorstra\u00dfe 5/20240730_131345.jpg", "Hachtorstra\u00dfe 5/20240730_131358.jpg", "Hachtorstra\u00dfe 6/IMG-20240726-WA0005.jpg", "Hachtorstra\u00dfe 6/IMG-20240726-WA0006.jpg", "Hachtorstra\u00dfe 6/IMG-20240726-WA0007.jpg", "Hachtorstra\u00dfe 6/IMG-20240726-WA0008.jpg", "Hachtorstra\u00dfe 6/IMG_20240723_123416_410.jpg", "Hachtorstra\u00dfe 6/IMG_7453.JPG_2.png", "Hachtorstra\u00dfe 7/20240730_111728.jpg", "Hachtorstra\u00dfe 7/20240730_111731.jpg", "Hachtorstra\u00dfe 7/20240730_111735.jpg", "Hachtorstra\u00dfe 7/20240730_111741.jpg", "Hachtorstra\u00dfe 7/IMG_7501.JPG_1.png", "Hachtorstra\u00dfe 8/20240730_101009.jpg", "Hachtorstra\u00dfe 8/20240730_101018.jpg", "Hachtorstra\u00dfe 8/20240730_101026.jpg", "Hachtorstra\u00dfe 8/20240730_101034.jpg", "Hachtorstra\u00dfe 8/20240730_101046.jpg", "Hachtorstra\u00dfe 8/20240730_101059.jpg", "Hachtorstra\u00dfe 8/20240730_101101.jpg", "Hachtorstra\u00dfe 8/20240730_101132.jpg", "Hachtorstra\u00dfe 8/20240730_101435.jpg", "Hachtorstra\u00dfe 8/20240730_101451.jpg", "Hachtorstra\u00dfe 8/20240730_114016.jpg", "Hachtorstra\u00dfe 8/20240730_114024.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_121823_442.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_121830_984.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_121920_974.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_121925_834.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_131227_797.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_131234_919.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_131551_386.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_144855_175.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_154557_927.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_154623_783.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_160731_346.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_160736_418.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_160745_897.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_160758_504.jpg", "Hachtorstra\u00dfe 8/IMG_20240729_160803_735.jpg", "Mildestra\u00dfe 1/20240723_100953.jpg", "Mildestra\u00dfe 1/20240723_100957.jpg", "Mildestra\u00dfe 1/20240723_104146.jpg", "Mildestra\u00dfe 1/20240723_104148.jpg", "Mildestra\u00dfe 1/IMG-20240722-WA0025.jpg", "Mildestra\u00dfe 1/IMG-20240722-WA0026.jpg", "Mildestra\u00dfe 1/IMG-20240722-WA0027.jpg", "Mildestra\u00dfe 1/IMG-20240722-WA0029.jpg", "Mildestra\u00dfe 1/IMG-20240726-WA0009.jpg", "Mildestra\u00dfe 1/IMG-20240726-WA0010.jpg", "Mildestra\u00dfe 1/IMG-20240726-WA0014.jpg", "Mildestra\u00dfe 1/IMG-20240726-WA0015.jpg", "Mildestra\u00dfe 1/IMG-20240726-WA0016.jpg", "Mildestra\u00dfe 1/IMG_20240722_135255_992.jpg", "Mildestra\u00dfe 1/IMG_20240723_103759_867.jpg", "Mildestra\u00dfe 1/IMG_20240723_123406_221.jpg", "Mildestra\u00dfe 3/IMG-20240722-WA0023.jpg", "Mildestra\u00dfe 4/IMG_20240722_151337_755.jpg", "Ritterstra\u00dfe 2/20240730_101814.jpg", "Ritterstra\u00dfe 2/20240801_081809.jpg", "Ritterstra\u00dfe 2/20240801_081845.jpg", "Ritterstra\u00dfe 2/20240801_081848.jpg", "Ritterstra\u00dfe 2/20240801_081851.jpg", "Ritterstra\u00dfe 2/20240801_081857.jpg", "Ritterstra\u00dfe 2/20240801_081905.jpg", "Ritterstra\u00dfe 2/20240801_081918.jpg", "Ritterstra\u00dfe 2/20240801_081937.jpg", "Ritterstra\u00dfe 2/20240801_090254.jpg", "Ritterstra\u00dfe 2/20240801_090258.jpg", "Ritterstra\u00dfe 2/20240801_090319.jpg", "Ritterstra\u00dfe 2/20240801_090821.jpg", "Ritterstra\u00dfe 2/20240801_090825.jpg", "Ritterstra\u00dfe 2/20240801_090832.jpg", "Ritterstra\u00dfe 2/20240801_090904.jpg", "Ritterstra\u00dfe 2/20240801_105330.jpg", "Ritterstra\u00dfe 2/20240801_105332.jpg", "Ritterstra\u00dfe 2/20240801_105337.jpg", "Ritterstra\u00dfe 2/20240801_124123.jpg", "Ritterstra\u00dfe 2/20240801_124124.jpg", "Ritterstra\u00dfe 2/20240801_124132.jpg", "Ritterstra\u00dfe 2/20240801_124133.jpg", "Ritterstra\u00dfe 2/20240801_124136.jpg", "Ritterstra\u00dfe 2/20240801_124139.jpg", "Schlangenpfad 25/20240722_100556.jpg", "Schulstra\u00dfe 4/IMG_7502.JPG_0.png"];