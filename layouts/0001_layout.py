(DATPenSet()
    .append(DATPen()
        .tag("parameter-edges")
        .moveTo((0.0, 648.0))
        .lineTo((240.0, 648.0))
        .endPath()
        .moveTo((120.0, 390.0))
        .lineTo((120.0, 648.0))
        .endPath()
        .moveTo((0.0, 318.0))
        .lineTo((240.0, 318.0))
        .endPath()
        .moveTo((120.0, 60.0))
        .lineTo((120.0, 318.0))
        .endPath()
        .moveTo((740.0, 660.0))
        .lineTo((916.0, 660.0))
        .endPath()
        .moveTo((740.0, 600.0))
        .lineTo((916.0, 600.0))
        .endPath()
        .moveTo((740.0, 540.0))
        .lineTo((916.0, 540.0))
        .endPath()
        .moveTo((740.0, 180.0))
        .lineTo((916.0, 180.0))
        .endPath()
        .moveTo((1040.0, 596.0))
        .lineTo((1472.0, 596.0))
        .endPath()
        .moveTo((1256.0, 472.0))
        .lineTo((1256.0, 596.0))
        .endPath()
        .moveTo((1040.0, 472.0))
        .lineTo((1472.0, 472.0))
        .endPath()
        .moveTo((1040.0, 348.0))
        .lineTo((1472.0, 348.0))
        .endPath()
        .moveTo((1040.0, 224.0))
        .lineTo((1472.0, 224.0))
        .endPath()
        .moveTo((1256.0, 100.0))
        .lineTo((1256.0, 224.0))
        .endPath()
        .moveTo((1040.0, 100.0))
        .lineTo((1472.0, 100.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.5))
        .sw(3))
    .append(DATPen()
        .tag("clump-edges")
        .moveTo((0, 60))
        .lineTo((916, 60))
        .endPath()
        .moveTo((0.0, 390.0))
        .lineTo((240.0, 390.0))
        .endPath()
        .moveTo((240.0, 220.0))
        .lineTo((740.0, 220.0))
        .endPath()
        .moveTo((740.0, 480.0))
        .lineTo((916.0, 480.0))
        .endPath()
        .moveTo((240.0, 60.0))
        .lineTo((240.0, 720.0))
        .endPath()
        .moveTo((740.0, 60.0))
        .lineTo((740.0, 720.0))
        .endPath()
        .f(bw(0.0, 0.0))
        .s(bw(0.25))
        .sw(5))
    .append(DATPen()
        .tag("sidebar")
        .moveTo((916, 0))
        .lineTo((1040, 0))
        .lineTo((1040, 720))
        .lineTo((916, 720))
        .closePath()
        .f(bw(0.5)))
    .append(DATPen()
        .tag("advbar")
        .moveTo((1040, 0))
        .lineTo((1472, 0))
        .lineTo((1472, 60))
        .lineTo((1040, 60))
        .closePath()
        .f(bw(0.75)))
    .append(DATPenSet()
        .tag("labels")
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Amount', None]})
            .moveTo((6.0, 402.0))
            .lineTo((114.0, 402.0))
            .lineTo((114.0, 466.0))
            .lineTo((6.0, 466.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Angle', None]})
            .moveTo((126.0, 402.0))
            .lineTo((234.0, 402.0))
            .lineTo((234.0, 466.0))
            .lineTo((126.0, 466.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Bass', None]})
            .moveTo((6, 72))
            .lineTo((114.0, 72.0))
            .lineTo((114.0, 136.0))
            .lineTo((6, 136))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Treble', None]})
            .moveTo((126.0, 72.0))
            .lineTo((234.0, 72.0))
            .lineTo((234.0, 136.0))
            .lineTo((126.0, 136.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'L/R Balance', None]})
            .moveTo((246.0, 72.0))
            .lineTo((734.0, 72.0))
            .lineTo((734.0, 136.0))
            .lineTo((246.0, 136.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Output', None]})
            .moveTo((746.0, 192.0))
            .lineTo((910.0, 192.0))
            .lineTo((910.0, 256.0))
            .lineTo((746.0, 256.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Compensation', None]})
            .moveTo((746.0, 72.0))
            .lineTo((910.0, 72.0))
            .lineTo((910.0, 136.0))
            .lineTo((746.0, 136.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Crossfeed Realism', None]})
            .moveTo((1046.0, 608.0))
            .lineTo((1466.0, 608.0))
            .lineTo((1466.0, 672.0))
            .lineTo((1046.0, 672.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Bass Frequency', None]})
            .moveTo((1046.0, 484.0))
            .lineTo((1250.0, 484.0))
            .lineTo((1250.0, 548.0))
            .lineTo((1046.0, 548.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Treble Frequency', None]})
            .moveTo((1262.0, 484.0))
            .lineTo((1466.0, 484.0))
            .lineTo((1466.0, 548.0))
            .lineTo((1262.0, 548.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Soft Start Time', None]})
            .moveTo((1046.0, 360.0))
            .lineTo((1466.0, 360.0))
            .lineTo((1466.0, 424.0))
            .lineTo((1046.0, 424.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Dim Level', None]})
            .moveTo((1046.0, 236.0))
            .lineTo((1466.0, 236.0))
            .lineTo((1466.0, 300.0))
            .lineTo((1046.0, 300.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Safe Gain', None]})
            .moveTo((1046.0, 112.0))
            .lineTo((1250.0, 112.0))
            .lineTo((1250.0, 176.0))
            .lineTo((1046.0, 176.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ParamLabel/text', 'Dither', None]})
            .moveTo((1262.0, 112.0))
            .lineTo((1466.0, 112.0))
            .lineTo((1466.0, 176.0))
            .lineTo((1262.0, 176.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'CROSSFEED', None]})
            .moveTo((14.0, 648.0))
            .lineTo((226.0, 648.0))
            .lineTo((226.0, 720.0))
            .lineTo((14.0, 720.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPen()
            .add_data({'ts': ['ClumpLabel/text', 'EQUALIZATION', None]})
            .moveTo((14.0, 318.0))
            .lineTo((226.0, 318.0))
            .lineTo((226.0, 390.0))
            .lineTo((14.0, 390.0))
            .closePath()
            .f(bw(0.0, 0.05)))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Mono', None], 'value': 0})
                .moveTo((746.0, 666.0))
                .lineTo((910.0, 666.0))
                .lineTo((910.0, 714.0))
                .lineTo((746.0, 714.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Mono', None], 'value': 1})
                .moveTo((746.0, 666.0))
                .lineTo((910.0, 666.0))
                .lineTo((910.0, 714.0))
                .lineTo((746.0, 714.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Flip L/R', None], 'value': 0})
                .moveTo((746.0, 606.0))
                .lineTo((910.0, 606.0))
                .lineTo((910.0, 654.0))
                .lineTo((746.0, 654.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Flip L/R', None], 'value': 1})
                .moveTo((746.0, 606.0))
                .lineTo((910.0, 606.0))
                .lineTo((910.0, 654.0))
                .lineTo((746.0, 654.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Polarity', None], 'value': 0})
                .moveTo((746.0, 546.0))
                .lineTo((910.0, 546.0))
                .lineTo((910.0, 594.0))
                .lineTo((746.0, 594.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Polarity', None], 'value': 1})
                .moveTo((746.0, 546.0))
                .lineTo((910.0, 546.0))
                .lineTo((910.0, 594.0))
                .lineTo((746.0, 594.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Dim', None], 'value': 0})
                .moveTo((746.0, 486.0))
                .lineTo((910.0, 486.0))
                .lineTo((910.0, 534.0))
                .lineTo((746.0, 534.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Dim', None], 'value': 1})
                .moveTo((746.0, 486.0))
                .lineTo((910.0, 486.0))
                .lineTo((910.0, 534.0))
                .lineTo((746.0, 534.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': False})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Hyperrealistic', 'CrossfeedRealism'], 'value': 0})
                .moveTo((1074.0, 644.0))
                .lineTo((1438.0, 644.0))
                .lineTo((1438.0, 696.0))
                .lineTo((1074.0, 696.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Realistic', 'CrossfeedRealism'], 'value': 1})
                .moveTo((1074.0, 644.0))
                .lineTo((1438.0, 644.0))
                .lineTo((1438.0, 696.0))
                .lineTo((1074.0, 696.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Standard', 'CrossfeedRealism'], 'value': 2})
                .moveTo((1074.0, 644.0))
                .lineTo((1438.0, 644.0))
                .lineTo((1438.0, 696.0))
                .lineTo((1074.0, 696.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': True})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Off', None], 'value': 0})
                .moveTo((1076.0, 152.0))
                .lineTo((1142.0, 152.0))
                .lineTo((1142.0, 196.0))
                .lineTo((1076.0, 196.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'On', None], 'value': 1})
                .moveTo((1154.0, 152.0))
                .lineTo((1220.0, 152.0))
                .lineTo((1220.0, 196.0))
                .lineTo((1154.0, 196.0))
                .closePath()
                .f(bw(0.0, 0.05))))
        .append(DATPenSet()
            .add_data({'initialValue': 0, 'shows_all_strings': True})
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'Off', None], 'value': 0})
                .moveTo((1292.0, 152.0))
                .lineTo((1358.0, 152.0))
                .lineTo((1358.0, 196.0))
                .lineTo((1292.0, 196.0))
                .closePath()
                .f(bw(0.0, 0.05)))
            .append(DATPen()
                .add_data({'ts': ['Parameter/option', 'On', None], 'value': 1})
                .moveTo((1370.0, 152.0))
                .lineTo((1436.0, 152.0))
                .lineTo((1436.0, 196.0))
                .lineTo((1370.0, 196.0))
                .closePath()
                .f(bw(0.0, 0.05))))))