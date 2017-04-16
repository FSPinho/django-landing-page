# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    ColorPrimary = apps.get_model("api", "ColorPrimary")
    db_alias = schema_editor.connection.alias
    ColorPrimary.objects.using(db_alias).bulk_create([
        ColorPrimary(name='red50', value='#ffebee'),
        ColorPrimary(name='red100', value='#ffcdd2'),
        ColorPrimary(name='red200', value='#ef9a9a'),
        ColorPrimary(name='red300', value='#e57373'),
        ColorPrimary(name='red400', value='#ef5350'),
        ColorPrimary(name='red500', value='#f44336'),
        ColorPrimary(name='red600', value='#e53935'),
        ColorPrimary(name='red700', value='#d32f2f'),
        ColorPrimary(name='red800', value='#c62828'),
        ColorPrimary(name='red900', value='#b71c1c'),

        ColorPrimary(name='pink50', value='#fce4ec'),
        ColorPrimary(name='pink100', value='#f8bbd0'),
        ColorPrimary(name='pink200', value='#f48fb1'),
        ColorPrimary(name='pink300', value='#f06292'),
        ColorPrimary(name='pink400', value='#ec407a'),
        ColorPrimary(name='pink500', value='#e91e63'),
        ColorPrimary(name='pink600', value='#d81b60'),
        ColorPrimary(name='pink700', value='#c2185b'),
        ColorPrimary(name='pink800', value='#ad1457'),
        ColorPrimary(name='pink900', value='#880e4f'),

        ColorPrimary(name='purple50', value='#f3e5f5'),
        ColorPrimary(name='purple100', value='#e1bee7'),
        ColorPrimary(name='purple200', value='#ce93d8'),
        ColorPrimary(name='purple300', value='#ba68c8'),
        ColorPrimary(name='purple400', value='#ab47bc'),
        ColorPrimary(name='purple500', value='#9c27b0'),
        ColorPrimary(name='purple600', value='#8e24aa'),
        ColorPrimary(name='purple700', value='#7b1fa2'),
        ColorPrimary(name='purple800', value='#6a1b9a'),
        ColorPrimary(name='purple900', value='#4a148c'),

        ColorPrimary(name='deepPurple50', value='#ede7f6'),
        ColorPrimary(name='deepPurple100', value='#d1c4e9'),
        ColorPrimary(name='deepPurple200', value='#b39ddb'),
        ColorPrimary(name='deepPurple300', value='#9575cd'),
        ColorPrimary(name='deepPurple400', value='#7e57c2'),
        ColorPrimary(name='deepPurple500', value='#673ab7'),
        ColorPrimary(name='deepPurple600', value='#5e35b1'),
        ColorPrimary(name='deepPurple700', value='#512da8'),
        ColorPrimary(name='deepPurple800', value='#4527a0'),
        ColorPrimary(name='deepPurple900', value='#311b92'),

        ColorPrimary(name='indigo50', value='#e8eaf6'),
        ColorPrimary(name='indigo100', value='#c5cae9'),
        ColorPrimary(name='indigo200', value='#9fa8da'),
        ColorPrimary(name='indigo300', value='#7986cb'),
        ColorPrimary(name='indigo400', value='#5c6bc0'),
        ColorPrimary(name='indigo500', value='#3f51b5'),
        ColorPrimary(name='indigo600', value='#3949ab'),
        ColorPrimary(name='indigo700', value='#303f9f'),
        ColorPrimary(name='indigo800', value='#283593'),
        ColorPrimary(name='indigo900', value='#1a237e'),

        ColorPrimary(name='blue50', value='#e3f2fd'),
        ColorPrimary(name='blue100', value='#bbdefb'),
        ColorPrimary(name='blue200', value='#90caf9'),
        ColorPrimary(name='blue300', value='#64b5f6'),
        ColorPrimary(name='blue400', value='#42a5f5'),
        ColorPrimary(name='blue500', value='#2196f3'),
        ColorPrimary(name='blue600', value='#1e88e5'),
        ColorPrimary(name='blue700', value='#1976d2'),
        ColorPrimary(name='blue800', value='#1565c0'),
        ColorPrimary(name='blue900', value='#0d47a1'),

        ColorPrimary(name='lightBlue50', value='#e1f5fe'),
        ColorPrimary(name='lightBlue100', value='#b3e5fc'),
        ColorPrimary(name='lightBlue200', value='#81d4fa'),
        ColorPrimary(name='lightBlue300', value='#4fc3f7'),
        ColorPrimary(name='lightBlue400', value='#29b6f6'),
        ColorPrimary(name='lightBlue500', value='#03a9f4'),
        ColorPrimary(name='lightBlue600', value='#039be5'),
        ColorPrimary(name='lightBlue700', value='#0288d1'),
        ColorPrimary(name='lightBlue800', value='#0277bd'),
        ColorPrimary(name='lightBlue900', value='#01579b'),

        ColorPrimary(name='cyan50', value='#e0f7fa'),
        ColorPrimary(name='cyan100', value='#b2ebf2'),
        ColorPrimary(name='cyan200', value='#80deea'),
        ColorPrimary(name='cyan300', value='#4dd0e1'),
        ColorPrimary(name='cyan400', value='#26c6da'),
        ColorPrimary(name='cyan500', value='#00bcd4'),
        ColorPrimary(name='cyan600', value='#00acc1'),
        ColorPrimary(name='cyan700', value='#0097a7'),
        ColorPrimary(name='cyan800', value='#00838f'),
        ColorPrimary(name='cyan900', value='#006064'),

        ColorPrimary(name='teal50', value='#e0f2f1'),
        ColorPrimary(name='teal100', value='#b2dfdb'),
        ColorPrimary(name='teal200', value='#80cbc4'),
        ColorPrimary(name='teal300', value='#4db6ac'),
        ColorPrimary(name='teal400', value='#26a69a'),
        ColorPrimary(name='teal500', value='#009688'),
        ColorPrimary(name='teal600', value='#00897b'),
        ColorPrimary(name='teal700', value='#00796b'),
        ColorPrimary(name='teal800', value='#00695c'),
        ColorPrimary(name='teal900', value='#004d40'),

        ColorPrimary(name='green50', value='#e8f5e9'),
        ColorPrimary(name='green100', value='#c8e6c9'),
        ColorPrimary(name='green200', value='#a5d6a7'),
        ColorPrimary(name='green300', value='#81c784'),
        ColorPrimary(name='green400', value='#66bb6a'),
        ColorPrimary(name='green500', value='#4caf50'),
        ColorPrimary(name='green600', value='#43a047'),
        ColorPrimary(name='green700', value='#388e3c'),
        ColorPrimary(name='green800', value='#2e7d32'),
        ColorPrimary(name='green900', value='#1b5e20'),

        ColorPrimary(name='lightGreen50', value='#f1f8e9'),
        ColorPrimary(name='lightGreen100', value='#dcedc8'),
        ColorPrimary(name='lightGreen200', value='#c5e1a5'),
        ColorPrimary(name='lightGreen300', value='#aed581'),
        ColorPrimary(name='lightGreen400', value='#9ccc65'),
        ColorPrimary(name='lightGreen500', value='#8bc34a'),
        ColorPrimary(name='lightGreen600', value='#7cb342'),
        ColorPrimary(name='lightGreen700', value='#689f38'),
        ColorPrimary(name='lightGreen800', value='#558b2f'),
        ColorPrimary(name='lightGreen900', value='#33691e'),

        ColorPrimary(name='lime50', value='#f9fbe7'),
        ColorPrimary(name='lime100', value='#f0f4c3'),
        ColorPrimary(name='lime200', value='#e6ee9c'),
        ColorPrimary(name='lime300', value='#dce775'),
        ColorPrimary(name='lime400', value='#d4e157'),
        ColorPrimary(name='lime500', value='#cddc39'),
        ColorPrimary(name='lime600', value='#c0ca33'),
        ColorPrimary(name='lime700', value='#afb42b'),
        ColorPrimary(name='lime800', value='#9e9d24'),
        ColorPrimary(name='lime900', value='#827717'),

        ColorPrimary(name='yellow50', value='#fffde7'),
        ColorPrimary(name='yellow100', value='#fff9c4'),
        ColorPrimary(name='yellow200', value='#fff59d'),
        ColorPrimary(name='yellow300', value='#fff176'),
        ColorPrimary(name='yellow400', value='#ffee58'),
        ColorPrimary(name='yellow500', value='#ffeb3b'),
        ColorPrimary(name='yellow600', value='#fdd835'),
        ColorPrimary(name='yellow700', value='#fbc02d'),
        ColorPrimary(name='yellow800', value='#f9a825'),
        ColorPrimary(name='yellow900', value='#f57f17'),

        ColorPrimary(name='amber50', value='#fff8e1'),
        ColorPrimary(name='amber100', value='#ffecb3'),
        ColorPrimary(name='amber200', value='#ffe082'),
        ColorPrimary(name='amber300', value='#ffd54f'),
        ColorPrimary(name='amber400', value='#ffca28'),
        ColorPrimary(name='amber500', value='#ffc107'),
        ColorPrimary(name='amber600', value='#ffb300'),
        ColorPrimary(name='amber700', value='#ffa000'),
        ColorPrimary(name='amber800', value='#ff8f00'),
        ColorPrimary(name='amber900', value='#ff6f00'),

        ColorPrimary(name='orange50', value='#fff3e0'),
        ColorPrimary(name='orange100', value='#ffe0b2'),
        ColorPrimary(name='orange200', value='#ffcc80'),
        ColorPrimary(name='orange300', value='#ffb74d'),
        ColorPrimary(name='orange400', value='#ffa726'),
        ColorPrimary(name='orange500', value='#ff9800'),
        ColorPrimary(name='orange600', value='#fb8c00'),
        ColorPrimary(name='orange700', value='#f57c00'),
        ColorPrimary(name='orange800', value='#ef6c00'),
        ColorPrimary(name='orange900', value='#e65100'),

        ColorPrimary(name='deepOrange50', value='#fbe9e7'),
        ColorPrimary(name='deepOrange100', value='#ffccbc'),
        ColorPrimary(name='deepOrange200', value='#ffab91'),
        ColorPrimary(name='deepOrange300', value='#ff8a65'),
        ColorPrimary(name='deepOrange400', value='#ff7043'),
        ColorPrimary(name='deepOrange500', value='#ff5722'),
        ColorPrimary(name='deepOrange600', value='#f4511e'),
        ColorPrimary(name='deepOrange700', value='#e64a19'),
        ColorPrimary(name='deepOrange800', value='#d84315'),
        ColorPrimary(name='deepOrange900', value='#bf360c'),

        ColorPrimary(name='brown50', value='#efebe9'),
        ColorPrimary(name='brown100', value='#d7ccc8'),
        ColorPrimary(name='brown200', value='#bcaaa4'),
        ColorPrimary(name='brown300', value='#a1887f'),
        ColorPrimary(name='brown400', value='#8d6e63'),
        ColorPrimary(name='brown500', value='#795548'),
        ColorPrimary(name='brown600', value='#6d4c41'),
        ColorPrimary(name='brown700', value='#5d4037'),
        ColorPrimary(name='brown800', value='#4e342e'),
        ColorPrimary(name='brown900', value='#3e2723'),

        ColorPrimary(name='blueGrey50', value='#eceff1'),
        ColorPrimary(name='blueGrey100', value='#cfd8dc'),
        ColorPrimary(name='blueGrey200', value='#b0bec5'),
        ColorPrimary(name='blueGrey300', value='#90a4ae'),
        ColorPrimary(name='blueGrey400', value='#78909c'),
        ColorPrimary(name='blueGrey500', value='#607d8b'),
        ColorPrimary(name='blueGrey600', value='#546e7a'),
        ColorPrimary(name='blueGrey700', value='#455a64'),
        ColorPrimary(name='blueGrey800', value='#37474f'),
        ColorPrimary(name='blueGrey900', value='#263238'),

        ColorPrimary(name='grey50', value='#fafafa'),
        ColorPrimary(name='grey100', value='#f5f5f5'),
        ColorPrimary(name='grey200', value='#eeeeee'),
        ColorPrimary(name='grey300', value='#e0e0e0'),
        ColorPrimary(name='grey400', value='#bdbdbd'),
        ColorPrimary(name='grey500', value='#9e9e9e'),
        ColorPrimary(name='grey600', value='#757575'),
        ColorPrimary(name='grey700', value='#616161'),
        ColorPrimary(name='grey800', value='#424242'),
        ColorPrimary(name='grey900', value='#212121'),

        ColorPrimary(name='black', value='#000000'),
        ColorPrimary(name='white', value='#ffffff'),
    ])
    
    ColorAccent = apps.get_model("api", "ColorAccent")
    db_alias = schema_editor.connection.alias
    ColorAccent.objects.using(db_alias).bulk_create([
        # Accent colors
        ColorAccent(name='redA100', value='#ff8a80'),
        ColorAccent(name='redA200', value='#ff5252'),
        ColorAccent(name='redA400', value='#ff1744'),
        ColorAccent(name='redA700', value='#d50000'),

        ColorAccent(name='pinkA100', value='#ff80ab'),
        ColorAccent(name='pinkA200', value='#ff4081'),
        ColorAccent(name='pinkA400', value='#f50057'),
        ColorAccent(name='pinkA700', value='#c51162'),

        ColorAccent(name='purpleA100', value='#ea80fc'),
        ColorAccent(name='purpleA200', value='#e040fb'),
        ColorAccent(name='purpleA400', value='#d500f9'),
        ColorAccent(name='purpleA700', value='#aa00ff'),

        ColorAccent(name='deepPurpleA100', value='#b388ff'),
        ColorAccent(name='deepPurpleA200', value='#7c4dff'),
        ColorAccent(name='deepPurpleA400', value='#651fff'),
        ColorAccent(name='deepPurpleA700', value='#6200ea'),

        ColorAccent(name='indigoA100', value='#8c9eff'),
        ColorAccent(name='indigoA200', value='#536dfe'),
        ColorAccent(name='indigoA400', value='#3d5afe'),
        ColorAccent(name='indigoA700', value='#304ffe'),

        ColorAccent(name='blueA100', value='#82b1ff'),
        ColorAccent(name='blueA200', value='#448aff'),
        ColorAccent(name='blueA400', value='#2979ff'),
        ColorAccent(name='blueA700', value='#2962ff'),

        ColorAccent(name='lightBlueA100', value='#80d8ff'),
        ColorAccent(name='lightBlueA200', value='#40c4ff'),
        ColorAccent(name='lightBlueA400', value='#00b0ff'),
        ColorAccent(name='lightBlueA700', value='#0091ea'),

        ColorAccent(name='cyanA100', value='#84ffff'),
        ColorAccent(name='cyanA200', value='#18ffff'),
        ColorAccent(name='cyanA400', value='#00e5ff'),
        ColorAccent(name='cyanA700', value='#00b8d4'),

        ColorAccent(name='tealA100', value='#a7ffeb'),
        ColorAccent(name='tealA200', value='#64ffda'),
        ColorAccent(name='tealA400', value='#1de9b6'),
        ColorAccent(name='tealA700', value='#00bfa5'),

        ColorAccent(name='greenA100', value='#b9f6ca'),
        ColorAccent(name='greenA200', value='#69f0ae'),
        ColorAccent(name='greenA400', value='#00e676'),
        ColorAccent(name='greenA700', value='#00c853'),

        ColorAccent(name='lightGreenA100', value='#ccff90'),
        ColorAccent(name='lightGreenA200', value='#b2ff59'),
        ColorAccent(name='lightGreenA400', value='#76ff03'),
        ColorAccent(name='lightGreenA700', value='#64dd17'),

        ColorAccent(name='limeA100', value='#f4ff81'),
        ColorAccent(name='limeA200', value='#eeff41'),
        ColorAccent(name='limeA400', value='#c6ff00'),
        ColorAccent(name='limeA700', value='#aeea00'),

        ColorAccent(name='yellowA100', value='#ffff8d'),
        ColorAccent(name='yellowA200', value='#ffff00'),
        ColorAccent(name='yellowA400', value='#ffea00'),
        ColorAccent(name='yellowA700', value='#ffd600'),

        ColorAccent(name='amberA100', value='#ffe57f'),
        ColorAccent(name='amberA200', value='#ffd740'),
        ColorAccent(name='amberA400', value='#ffc400'),
        ColorAccent(name='amberA700', value='#ffab00'),

        ColorAccent(name='orangeA100', value='#ffd180'),
        ColorAccent(name='orangeA200', value='#ffab40'),
        ColorAccent(name='orangeA400', value='#ff9100'),
        ColorAccent(name='orangeA700', value='#ff6d00'),

        ColorAccent(name='deepOrangeA100', value='#ff9e80'),
        ColorAccent(name='deepOrangeA200', value='#ff6e40'),
        ColorAccent(name='deepOrangeA400', value='#ff3d00'),
        ColorAccent(name='deepOrangeA700', value='#dd2c00'),
    ])


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial')
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
