(DATPenSet()
    .append(DATPen()
        .tag("parameter-edges")
        .moveTo((0.0, 688.0))
        .lineTo((790.0, 688.0))
        .endPath()
        .moveTo((914.0, 688.0))
        .lineTo((1138.0, 688.0))
        .endPath()
        .moveTo((1026.0, 436.0))
        .lineTo((1026.0, 688.0))
        .endPath()
        .moveTo((914.0, 436.0))
        .lineTo((1138.0, 436.0))
        .endPath()
        .moveTo((1138.0, 436.0))
        .lineTo((1362.0, 436.0))
        .endPath()
        .moveTo((1362.0, 436.0))
        .lineTo((1362.0, 688.0))
        .endPath()
        .moveTo((1138.0, 688.0))
        .lineTo((1362.0, 688.0))
        .endPath()
        .moveTo((1250.0, 436.0))
        .lineTo((1250.0, 688.0))
        .endPath()
        .moveTo((1138.0, 436.0))
        .lineTo((1362.0, 436.0))
        .endPath()
        .moveTo((1362.0, 688.0))
        .lineTo((1586.0, 688.0))
        .endPath()
        .moveTo((1474.0, 436.0))
        .lineTo((1474.0, 688.0))
        .endPath()
        .moveTo((1362.0, 436.0))
        .lineTo((1586.0, 436.0))
        .endPath()
        .moveTo((1346.0, 188.0))
        .lineTo((1346.0, 316.0))
        .endPath()
        .moveTo((1346.0, 188.0))
        .lineTo((1346.0, 316.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.5))
        .sw(3))
    .append(DATPen()
        .tag("clump-edges")
        .moveTo((0, 60))
        .lineTo((790, 60))
        .endPath()
        .moveTo((158.0, 688.0))
        .lineTo((158.0, 760.0))
        .endPath()
        .moveTo((316.0, 688.0))
        .lineTo((316.0, 760.0))
        .endPath()
        .moveTo((474.0, 688.0))
        .lineTo((474.0, 760.0))
        .endPath()
        .moveTo((632.0, 688.0))
        .lineTo((632.0, 760.0))
        .endPath()
        .moveTo((158.0, 180.0))
        .lineTo((158.0, 688.0))
        .endPath()
        .moveTo((316.0, 180.0))
        .lineTo((316.0, 688.0))
        .endPath()
        .moveTo((474.0, 180.0))
        .lineTo((474.0, 688.0))
        .endPath()
        .moveTo((632.0, 180.0))
        .lineTo((632.0, 688.0))
        .endPath()
        .moveTo((0.0, 180.0))
        .lineTo((790.0, 180.0))
        .endPath()
        .moveTo((1138.0, 316.0))
        .lineTo((1138.0, 760.0))
        .endPath()
        .moveTo((1362.0, 316.0))
        .lineTo((1362.0, 760.0))
        .endPath()
        .moveTo((914.0, 316.0))
        .lineTo((1586.0, 316.0))
        .endPath()
        .moveTo((914.0, 188.0))
        .lineTo((1586.0, 188.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.25))
        .sw(5))
    .append(DATPen()
        .tag("sidebar")
        .moveTo((790, 0))
        .lineTo((914, 0))
        .lineTo((914, 760))
        .lineTo((790, 760))
        .closePath()
        .f(bw(0.5)))
    .append(DATPen()
        .tag("advbar")
        .moveTo((914, 0))
        .lineTo((1586, 0))
        .lineTo((1586, 60))
        .lineTo((914, 60))
        .closePath()
        .f(bw(0.75)))
    .append(DATPenSet()
        .tag("labels")
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'dry', None]})
            .moveTo((14, 60))
            .lineTo((144.0, 60.0))
            .lineTo((144.0, 180.0))
            .lineTo((14.0, 180.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'us': 'vulf'})
            .moveTo((646.0, 60.0))
            .lineTo((776.0, 60.0))
            .lineTo((776.0, 180.0))
            .lineTo((646.0, 180.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Attack', None]})
            .moveTo((920.0, 448.0))
            .lineTo((1020.0, 448.0))
            .lineTo((1020.0, 512.0))
            .lineTo((920.0, 512.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Release', None]})
            .moveTo((1032.0, 448.0))
            .lineTo((1132.0, 448.0))
            .lineTo((1132.0, 512.0))
            .lineTo((1032.0, 512.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Stereo Link', None]})
            .moveTo((920.0, 328.0))
            .lineTo((1132.0, 328.0))
            .lineTo((1132.0, 392.0))
            .lineTo((920.0, 392.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Mix', None]})
            .moveTo((1144.0, 448.0))
            .lineTo((1244.0, 448.0))
            .lineTo((1244.0, 512.0))
            .lineTo((1144.0, 512.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Phase', None]})
            .moveTo((1256.0, 448.0))
            .lineTo((1356.0, 448.0))
            .lineTo((1356.0, 512.0))
            .lineTo((1256.0, 512.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Speed', None]})
            .moveTo((1144.0, 328.0))
            .lineTo((1356.0, 328.0))
            .lineTo((1356.0, 392.0))
            .lineTo((1144.0, 392.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Noise', None]})
            .moveTo((1368.0, 448.0))
            .lineTo((1468.0, 448.0))
            .lineTo((1468.0, 512.0))
            .lineTo((1368.0, 512.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Crunch', None]})
            .moveTo((1480.0, 448.0))
            .lineTo((1580.0, 448.0))
            .lineTo((1580.0, 512.0))
            .lineTo((1480.0, 512.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Type', None]})
            .moveTo((1368.0, 328.0))
            .lineTo((1580.0, 328.0))
            .lineTo((1580.0, 392.0))
            .lineTo((1368.0, 392.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'External Sidechain', None]})
            .moveTo((1088.0, 200.0))
            .lineTo((1340.0, 200.0))
            .lineTo((1340.0, 264.0))
            .lineTo((1088.0, 264.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Sidechain Tilt', None]})
            .moveTo((1352.0, 200.0))
            .lineTo((1580.0, 200.0))
            .lineTo((1580.0, 264.0))
            .lineTo((1352.0, 264.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Digital Ref Level', None]})
            .moveTo((920, 72))
            .lineTo((1580, 72))
            .lineTo((1580, 136))
            .lineTo((920, 136))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'IN', None]})
            .moveTo((14.0, 688.0))
            .lineTo((144.0, 688.0))
            .lineTo((144.0, 760.0))
            .lineTo((14.0, 760.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'COMP', None]})
            .moveTo((172.0, 688.0))
            .lineTo((302.0, 688.0))
            .lineTo((302.0, 760.0))
            .lineTo((172.0, 760.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'WOW', None]})
            .moveTo((330.0, 688.0))
            .lineTo((460.0, 688.0))
            .lineTo((460.0, 760.0))
            .lineTo((330.0, 760.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'LOFI', None]})
            .moveTo((488.0, 688.0))
            .lineTo((618.0, 688.0))
            .lineTo((618.0, 760.0))
            .lineTo((488.0, 760.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'OUT', None]})
            .moveTo((646.0, 688.0))
            .lineTo((776.0, 688.0))
            .lineTo((776.0, 760.0))
            .lineTo((646.0, 760.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'COMP ADV', None]})
            .moveTo((928.0, 688.0))
            .lineTo((1124.0, 688.0))
            .lineTo((1124.0, 760.0))
            .lineTo((928.0, 760.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'WOW ADV', None]})
            .moveTo((1152.0, 688.0))
            .lineTo((1348.0, 688.0))
            .lineTo((1348.0, 760.0))
            .lineTo((1152.0, 760.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'LOFI ADV', None]})
            .moveTo((1376.0, 688.0))
            .lineTo((1572.0, 688.0))
            .lineTo((1572.0, 760.0))
            .lineTo((1376.0, 760.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'SIDE\nCHAIN', None]})
            .moveTo((914.0, 204.0))
            .lineTo((1022.0, 204.0))
            .lineTo((1022.0, 300.0))
            .lineTo((914.0, 300.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPenSet()
            .add_data({'initialValue': 1, 'shows_all_strings': True})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Off', None], 'value': 0})
                .moveTo((950.0, 366.0))
                .lineTo((1020.0, 366.0))
                .lineTo((1020.0, 410.0))
                .lineTo((950.0, 410.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'On', None], 'value': 1})
                .moveTo((1032.0, 366.0))
                .lineTo((1102.0, 366.0))
                .lineTo((1102.0, 410.0))
                .lineTo((1032.0, 410.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'us': '33.3 RPM', 'value': 0})
                .moveTo((1172.0, 362.0))
                .lineTo((1328.0, 362.0))
                .lineTo((1328.0, 414.0))
                .lineTo((1172.0, 414.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'us': '45 RPM', 'value': 1})
                .moveTo((1172.0, 362.0))
                .lineTo((1328.0, 362.0))
                .lineTo((1328.0, 414.0))
                .lineTo((1172.0, 414.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'us': '78 RPM', 'value': 2})
                .moveTo((1172.0, 362.0))
                .lineTo((1328.0, 362.0))
                .lineTo((1328.0, 414.0))
                .lineTo((1172.0, 414.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Analog', 'LoFiType'], 'value': 0})
                .moveTo((1396.0, 362.0))
                .lineTo((1552.0, 362.0))
                .lineTo((1552.0, 414.0))
                .lineTo((1396.0, 414.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', "1990's Digital", 'LoFiType'], 'value': 1})
                .moveTo((1396.0, 362.0))
                .lineTo((1552.0, 362.0))
                .lineTo((1552.0, 414.0))
                .lineTo((1396.0, 414.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', "1980's Digital", 'LoFiType'], 'value': 2})
                .moveTo((1396.0, 362.0))
                .lineTo((1552.0, 362.0))
                .lineTo((1552.0, 414.0))
                .lineTo((1396.0, 414.0))
                .closePath()
                .f(bw(0.0, 0.05))))))